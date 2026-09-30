# -*- coding: utf-8 -*-
# freeAudio - Radio Player
# BASS (subprocess) is the sole playback backend.
# Initial player structure and state accessors based on work by Gary Mp (GaryMp/freeradio).

import ctypes
import json
import logging
import os
import subprocess
import sys
import threading
import time
import re
import random
import urllib.request
import atexit
import tempfile

from . import timeshift as _timeshift_mod

log = logging.getLogger()

# Dedicated log for audio mirror attempts (start_mirror()) - separate
# from NVDA's own log (which log.warning()/log.error() calls elsewhere in
# this file go to) because that one depends on NVDA's log level and
# requires knowing where/how to search it. This file is a single, small,
# plain-text log a non-technical user can just attach to a bug report.
# Off by default, matching bass_host.py's own _DEBUG_ENABLED for the
# time-shift debug log - flip to True (or expose a setting) when actively
# chasing a mirror report; leaving it on unconditionally would mean every
# user's mirror use quietly grows a file in their temp folder for a
# diagnostic almost nobody needs day to day.
_MIRROR_DEBUG_ENABLED = False
_MIRROR_DEBUG_LOG_PATH = os.path.join(tempfile.gettempdir(), "freeAudio_mirror_debug.log")


def _mirror_debug_log(msg):
	if not _MIRROR_DEBUG_ENABLED:
		return
	try:
		with open(_MIRROR_DEBUG_LOG_PATH, "a", encoding="utf-8") as f:
			f.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg))
	except Exception:
		pass


_WATCHDOG_INTERVAL = 5
_WATCHDOG_BACKOFF = [5, 10, 20, 30, 30, 30]

_ICY_INTERVAL = 30
_ICY_TIMEOUT = 10

_BASS_ATTRIB_VOL = 2
_BASS_TAG_META = 5
_BASS_CONFIG_NET_TIMEOUT = 11
_BASS_CONFIG_NET_HTTPS_FLAG = 71
_BASS_CONFIG_NET_SSL = 73
_BASS_CONFIG_NET_SSL_VERIFY = 74
_BASS_CONFIG_NET_PLAYLIST = 21
_BASS_CONFIG_NET_PREBUF = 15
_BASS_CONFIG_NET_READTIMEOUT = 37

# Device / output routing
_BASS_DEVICE_DEFAULT  = -1   # system default output

# Seconds of rolling capture kept when the user has NOT enabled the
# user-facing rewind feature. The time-shift buffer's capture connection is
# now kept running at all times (not just when rewind is enabled) because
# music recognition and recording both tail it instead of opening their own
# fresh connection - some stations serve a new ad to every brand-new
# connection, and reusing this already-open one avoids re-triggering that.
# When rewind IS enabled, TimeShiftBuffer.CAPACITY_SECONDS (10 min) is used
# instead so the existing rewind window is unaffected.
_LIGHT_BUFFER_SECONDS = 45

# Station tuning transition effect — plays a short local sound effect
# (tuner.mp3, bundled alongside this file) while connecting to a new
# station, instead of a numeric crossfade. BASS backend only; see
# RadioPlayer.set_tuning_effect_enabled().
_TUNER_MP3_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tuner.mp3")
_TUNER_POLL_INTERVAL = 0.25  # seconds between end-of-clip checks while looping

# Cached duration of tuner.mp3, in seconds, discovered the first time it is
# played (via timeshift_status() right after opening). Used on subsequent
# tuning transitions to start playback from a random position instead of
# always from the beginning. None until first discovered.
_TUNER_LENGTH_SECONDS = None

# Podcast/audio book resume-wait effect — plays a short local sound effect
# (casette.mp3, bundled alongside this file) on a small separate engine
# while the real episode/chapter stream connects and seeks back to its
# saved position, instead of letting the episode's own audio play
# audibly from 0:00 in the meantime. See RadioPlayer._launch_bass().
_CASETTE_MP3_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "casette.mp3")

# Cached duration of casette.mp3, in seconds - same purpose as
# _TUNER_LENGTH_SECONDS above, just for the resume-wait clip.
_CASETTE_LENGTH_SECONDS = None

_BASS_ERROR_SSL	  = 41
_BASS_ERROR_FILEFORM = 40
_BASS_ERROR_TIMEOUT  = 38
_BASS_ERROR_NOTAVAIL = 37
_BASS_ERROR_ALREADY  = 8


def _is_seekable_media(station):
	"""True if *station* is a podcast episode or audio-book chapter
	(GETEM/LibriVox) - i.e. locally-seekable media that should get the
	podcast-style resume/seek/speed/finish-detection treatment throughout
	this file.

	Deliberately keyed off the dedicated "media_kind" field (set only by
	podcast.PodcastEpisode.to_dict(), getem.GetemBook.to_dict() and
	librivox.LibriVoxBook.to_dict()) rather than substring-matching the
	free-text "tags" field. A real Radio Browser station can legitimately
	carry "podcast" as a community-assigned genre tag on an ordinary live
	stream (e.g. talk-radio mirrors of podcast-hosting platforms like
	Zeno.fm or Qingting.fm) - matching against "tags" used to make
	freeAudio treat such a station as an actual downloadable podcast
	episode: opened seekable, resumed to a saved position that can never
	apply to a live/infinite stream, and left stuck (muted) behind the
	casette.mp3 resume-wait effect while the seek retry loop spent up to
	15 seconds failing over and over. "media_kind" is never derived from
	external data, so it can't collide with a real station's own tags."""
	return bool(station) and station.get("media_kind") in ("podcast", "audiobook", "jukebox")


def _read_icy_title(url):
	try:
		req = urllib.request.Request(
			url,
			headers={"User-Agent": "freeAudio-NVDA/1.0", "Icy-MetaData": "1"},
		)
		with urllib.request.urlopen(req, timeout=_ICY_TIMEOUT) as resp:
			metaint_str = resp.headers.get("icy-metaint", "")
			if not metaint_str:
				return None
			metaint = int(metaint_str)
			resp.read(metaint)
			meta_len_byte = resp.read(1)
			if not meta_len_byte:
				return None
			meta_len = meta_len_byte[0] * 16
			if meta_len == 0:
				return None
			meta_raw = resp.read(meta_len).decode("utf-8", errors="ignore")
			# NOTE: match up to the closing "';" (not just the next "'"),
			# since the title itself may contain an apostrophe (e.g.
			# "Don't Stop Believin'"). ICY metadata always terminates each
			# key='value' pair with "';", so this is a safe delimiter.
			m = re.search(r"StreamTitle='(.*?)';", meta_raw)
			if m:
				title = m.group(1).strip()
				return title if title else None
	except Exception:
		pass
	return None




def _resolve_playlist_url(url, timeout=8, _hops=3):
	# Only http(s) URLs are fetched here. urllib transparently supports
	# file://, which would let a station entry (which anyone can submit
	# to Radio Browser without an account) read an arbitrary local file,
	# so non-http(s) schemes are passed through unresolved rather than
	# fetched.
	if not url or not url.lower().startswith(("http://", "https://")):
		return url
	try:
		import urllib.request as _req
		req = _req.Request(
			url,
			headers={"User-Agent": "freeAudio-NVDA/1.0",
					 "Icy-MetaData": "1"},
		)
		with _req.urlopen(req, timeout=timeout) as resp:
			final_url = resp.url if hasattr(resp, "url") else url
			ct = (resp.headers.get("content-type") or "").lower().split(";")[0].strip()
			data = resp.read(8192).decode("utf-8", "ignore")

		audio_types = ("audio/", "application/ogg", "video/")
		# A content-type that already says "this is audio" is trusted
		# outright - but only when it isn't one of the playlist-ish
		# audio/* types below (audio/x-mpegurl, audio/x-scpls, ...),
		# which also start with "audio/" yet are playlists, not streams.
		playlist_audio_types = (
			"audio/x-mpegurl", "audio/mpegurl", "audio/x-scpls",
			"audio/x-ms-wax",
		)
		if ct.startswith(audio_types) and ct not in playlist_audio_types:
			return final_url if final_url != url else url

		from urllib.parse import urljoin as _urljoin
		base_url = final_url
		stripped = data.lstrip()
		next_url = None

		is_pls = (
			ct == "audio/x-scpls" or url.lower().endswith(".pls")
			or stripped[:9].lower().startswith("[playlist")
		)
		is_m3u = (
			not is_pls and (
				ct in ("audio/x-mpegurl", "application/x-mpegurl",
					   "audio/mpegurl", "application/vnd.apple.mpegurl")
				or url.lower().endswith((".m3u", ".m3u8"))
				or stripped.startswith("#EXTM3U")
			)
		)
		is_asx = (
			not is_pls and not is_m3u and (
				ct in ("video/x-ms-asf", "audio/x-ms-wax", "audio/x-ms-wmx")
				or any(url.lower().endswith(e) for e in (".asx", ".wmx", ".wax"))
				or stripped[:5].lower().startswith("<asx")
			)
		)

		if is_pls:
			for line in data.splitlines():
				if line.lower().startswith("file1="):
					next_url = _urljoin(base_url, line.split("=", 1)[1].strip())
					break

		elif is_m3u:
			for line in data.splitlines():
				line = line.strip()
				if line and not line.startswith("#"):
					next_url = _urljoin(base_url, line)
					break

		elif is_asx:
			import re as _re
			m = _re.search(r"href\s*=\s*[\"']([^\"']+)[\"']", data, _re.IGNORECASE)
			if m:
				next_url = _urljoin(base_url, m.group(1))

		if next_url is None:
			# Last resort: some tuning endpoints - TuneIn's Tune.ashx among
			# them - return neither a "[playlist]" nor a "#EXTM3U" header,
			# just a bare newline-separated list of candidate stream URLs.
			# If the first non-empty line is itself a URL, take it.
			for line in data.splitlines():
				line = line.strip()
				if line:
					if line.lower().startswith(("http://", "https://")):
						next_url = _urljoin(base_url, line)
					break

		if next_url and next_url != url:
			if _hops > 0:
				# The link inside might itself be another playlist
				# (e.g. a tuning endpoint pointing at a second .pls).
				return _resolve_playlist_url(next_url, timeout=timeout, _hops=_hops - 1)
			return next_url

	except Exception:
		pass

	return url


# Segments at/below this go through _HlsStreamMerger (juyun.tv-style
# feeds run 1-2s, ordinary broadcaster HLS runs 6-8s).
_HLS_SHORT_SEGMENT_THRESHOLD = 4

# How long a _should_hls_merge() decision is cached, so a stall/
# reconnect never re-fetches the playlist mid-struggle.
_HLS_MERGE_DECISION_TTL = 1800  # seconds


def _get_hls_target_duration(url, timeout=4):
	"""Return the #EXT-X-TARGETDURATION (seconds) of an HLS playlist, or
	None if it can't be determined. Follows one hop of master-playlist
	indirection (variants of one rendition share a segment duration, so
	one hop is enough). Used by _should_hls_merge().
	"""
	# http(s) only - same SSRF guard as _resolve_playlist_url (a station
	# URL can come from an unauthenticated source).
	if not url or not url.lower().startswith(("http://", "https://")):
		return None
	try:
		import urllib.request as _req
		from urllib.parse import urljoin as _urljoin

		def _fetch(u):
			req = _req.Request(u, headers={"User-Agent": "freeAudio-NVDA/1.0"})
			with _req.urlopen(req, timeout=timeout) as resp:
				# The tag we need is always near the top of a well-formed
				# playlist; capping the read keeps this cheap even against
				# a media playlist listing thousands of old segments.
				return resp.read(65536).decode("utf-8", "ignore")

		def _target_duration(playlist_text):
			for line in playlist_text.splitlines():
				line = line.strip()
				if line.startswith("#EXT-X-TARGETDURATION:"):
					try:
						return float(line.split(":", 1)[1])
					except ValueError:
						return None
			return None

		data = _fetch(url)
		duration = _target_duration(data)
		if duration is not None:
			return duration

		if "#EXT-X-STREAM-INF" in data:
			lines = data.splitlines()
			variant = None
			for i, line in enumerate(lines):
				if line.strip().startswith("#EXT-X-STREAM-INF"):
					for candidate in lines[i + 1:]:
						candidate = candidate.strip()
						if candidate and not candidate.startswith("#"):
							variant = _urljoin(url, candidate)
							break
					if variant:
						break
			if variant and variant != url:
				return _target_duration(_fetch(variant))
	except Exception:
		pass
	return None


def _find_system_ffmpeg():
	"""Return the path to a usable ffmpeg.exe, or None.

	Search order:
	  1. ffmpeg.exe next to this file (the add-on's own directory) -
	     this is where the recorder and music recognizer expect to
	     find it by default, so the merger must look here too or it
	     will report "no ffmpeg_path configured" even though the
	     recorder happily uses that same copy.
	  2. Any ffmpeg.exe on PATH (shutil.which).
	  3. A handful of common Windows install locations - the
	     chocolatey shim directory, winget/scoop links, and the
	     conventional unzipped-folder locations.

	Used by _HlsStreamMerger.start() as a fallback when the user
	hasn't set config.conf["freeAudio"]["ffmpeg_path"] explicitly,
	so short-segment HLS smoothing works out of the box whenever
	ffmpeg is already available to the rest of the add-on."""
	import shutil as _shutil

	# 1. Next to this module - matches the recorder/recognizer default.
	try:
		_local_ffmpeg = os.path.join(
			os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe"
		)
		if os.path.isfile(_local_ffmpeg):
			return _local_ffmpeg
	except Exception:
		pass

	# 2. PATH.
	try:
		found = _shutil.which("ffmpeg")
		if found and os.path.isfile(found):
			return found
	except Exception:
		pass

	# 3. Common install locations.
	_local = os.environ.get("LOCALAPPDATA") or ""
	_programdata = os.environ.get("ProgramData") or ""
	_programfiles = os.environ.get("ProgramFiles") or ""
	_programfiles_x86 = os.environ.get("ProgramFiles(x86)") or ""

	candidates = [
		os.path.join(_programdata, "chocolatey", "bin", "ffmpeg.exe"),
		os.path.join(_local, "Microsoft", "WinGet", "Links", "ffmpeg.exe"),
		os.path.join(_local, "Programs", "ffmpeg", "bin", "ffmpeg.exe"),
		os.path.join(_programfiles, "ffmpeg", "bin", "ffmpeg.exe"),
		os.path.join(_programfiles_x86, "ffmpeg", "bin", "ffmpeg.exe"),
		r"C:\ffmpeg\bin\ffmpeg.exe",
	]
	for path in candidates:
		if path and os.path.isfile(path):
			return path
	return None


def _read_icy_title_via_playlist(url, timeout=_ICY_TIMEOUT):
	"""Like _read_icy_title(), but first unwraps *url* through
	_resolve_playlist_url() if it points at a playlist/tuning wrapper
	(.pls/.m3u/.asx, or a source's own tuning endpoint such as TuneIn's
	Tune.ashx) rather than a raw audio stream.

	_read_icy_title() alone only works when the given URL is already a
	direct stream connection that echoes back an "icy-metaint" header -
	true for Radio Browser's pre-resolved url_resolved, but not for
	sources like TuneIn whose station "url"/"url_resolved" is a tuning
	URL that returns a small playlist file instead of audio (see
	externalSources.search_tunein()). BASS itself unwraps that playlist
	natively when actually playing the stream, but the plain urllib
	request _read_icy_title() makes does not - so every "what's playing"
	fallback call site in trackInfoMixin.py should go through this
	wrapper instead of calling _read_icy_title() directly.

	Cheap for the common case: _resolve_playlist_url() returns audio URLs
	unchanged (content-type check) without downloading anything beyond
	the initial response headers/first chunk.
	"""
	resolved = _resolve_playlist_url(url, timeout=timeout)
	return _read_icy_title(resolved)


class _BassSubprocessEngine:
	"""
	Runs bass_host.py as a child process so that BASS audio appears as a
	separate entry in the Windows volume mixer — independent from nvda.exe.

	Communication: newline-delimited JSON on stdin/stdout.
	"""

	def __init__(self, dll_dir, device_index=-1):
		self._dll_dir  = dll_dir
		self._device_index = device_index  # -1 = system default
		self._proc	 = None
		self._lock	 = threading.RLock()
		self._ready	= False
		self._icy_title = None
		# The outer layer can assign a connect notification callback.
		self.on_slow_connect = None
		self.on_meta	   = None
		# Called if there is no response within 5 seconds; UI may show 'connecting'.
		self.on_connecting = None
		# Called when bass_host sends a stall event.
		self.on_stall	  = None
		self._reader_thread = None
		self._stop_reader   = threading.Event()
		self._play_seq	 = 0
		self._pending_play = None   # (seq, event, [result, error])
		self._current_play_seq = None  # Track currently active play request
		# The "error" string bass_host.py sends alongside {"ok": false} for
		# a failed play (see bass_host.py's _send({"ok": ok, "error": ...})
		# for the "play" command) - e.g. "StreamCreateURL failed (err=41)".
		# Set by _read_loop()/play() on every play attempt (cleared to None
		# on success) so callers that get False back from play() can look
		# here for *why*, instead of that detail being read off the wire
		# and then silently discarded the way it used to be.
		self.last_play_error = None
		# Last few lines the bass_host.py subprocess wrote to stderr (e.g.
		# an uncaught traceback if it crashed on startup) - drained
		# continuously by a background thread once the process starts (see
		# load()) rather than read on demand, so a subprocess that does
		# write to stderr during normal operation never blocks trying to
		# fill an unread pipe. Bounded so a chatty/crash-looping process
		# can't grow this unboundedly.
		self._stderr_tail = []
		self._stderr_tail_lock = threading.Lock()
		atexit.register(self._cleanup)

	def _drain_stderr(self, proc):
		try:
			for raw_line in proc.stderr:
				line = raw_line.rstrip("\r\n")
				with self._stderr_tail_lock:
					self._stderr_tail.append(line)
					if len(self._stderr_tail) > 50:
						del self._stderr_tail[: len(self._stderr_tail) - 50]
		except Exception:
			pass

	def get_stderr_tail(self):
		"""Return the last lines the subprocess wrote to stderr, for
		diagnosing a load()/play() failure - e.g. an uncaught traceback if
		bass_host.py crashed on startup."""
		with self._stderr_tail_lock:
			return list(self._stderr_tail)

	def _find_python(self):
		"""
		Find a non-elevated pythonw.exe to run bass_host.py as a normal
		(non-admin) subprocess so Windows does not trigger UAC elevation.

		Search order:
		1. Bundled embed Python (python/ folder of the plugin) — matching the architecture
		2. pythonw.exe / python.exe next to bass_host.py
		3. pythonw.exe / python.exe next to sys.executable
		4. sys.executable itself if it is literally python/pythonw
		5. PATH fallback
		"""
		candidates = []

		# 1. Embed Python embedded in the plugin — folder matching the architecture
		is64 = ctypes.sizeof(ctypes.c_voidp) == 8
		arch_dir = "x64" if is64 else "x86"
		bundled_dir = os.path.join(self._dll_dir, "python", arch_dir)
		for name in ("pythonw.exe", "python.exe"):
			candidates.append(os.path.join(bundled_dir, name))

		# 2. Alongside the script itself
		for name in ("pythonw.exe", "python.exe"):
			candidates.append(os.path.join(self._dll_dir, name))

		# 3. Alongside whatever interpreter is running NVDA
		exe_dir = os.path.dirname(sys.executable)
		for name in ("pythonw.exe", "python.exe"):
			candidates.append(os.path.join(exe_dir, name))

		# 4. sys.executable itself if it is literally python/pythonw
		base = os.path.basename(sys.executable).lower()
		if base in ("python.exe", "pythonw.exe"):
			candidates.append(sys.executable)

		for path in candidates:
			if os.path.isfile(path):
				return path

		# 5. PATH fallback
		for name in ("pythonw", "python"):
			try:
				result = subprocess.run(
					["where", name],
					capture_output=True, text=True,
					creationflags=subprocess.CREATE_NO_WINDOW,
				)
				if result.returncode == 0:
					first = result.stdout.strip().splitlines()[0].strip()
					if os.path.isfile(first):
						return first
			except Exception:
				pass

		return None

	def load(self):
		host_script = os.path.join(self._dll_dir, "bass_host.py")
		if not os.path.isfile(host_script):
			return False

		python = self._find_python()
		if not python:
			return False

		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		si.wShowWindow = 0

		try:
			cmd = [python, host_script]
			if self._device_index != -1:
				cmd += ["--device", str(self._device_index)]
			proc = subprocess.Popen(
				cmd,
				stdin=subprocess.PIPE,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				startupinfo=si,
				creationflags=subprocess.CREATE_NO_WINDOW,
				encoding="utf-8",
				bufsize=1,
			)
		except Exception:
			return False

		with self._lock:
			self._proc = proc

		# Drain stderr continuously in the background from here on - see
		# _drain_stderr()'s docstring for why this can't just be read on
		# demand after a failure.
		threading.Thread(
			target=self._drain_stderr, args=(proc,), daemon=True, name="freeAudio-BassStderr").start()

		try:
			line = proc.stdout.readline()
			resp = json.loads(line)
			if not resp.get("ok"):
				self._kill()
				return False
		except Exception:
			self._kill()
			return False

		self._ready = True
		self._stop_reader.clear()
		self._reader_thread = threading.Thread(
			target=self._read_loop, daemon=True, name="freeAudio-BassReader")
		self._reader_thread.start()

		return True

	def ready(self):
		return self._ready and self._proc is not None and self._proc.poll() is None

	def unload(self):
		self._stop_reader.set()
		self._send({"cmd": "quit"})
		time.sleep(0.3)
		self._kill()
		self._ready = False

	def _kill(self):
		with self._lock:
			proc = self._proc
			self._proc = None
		if proc:
			try:
				proc.terminate()
				proc.wait(timeout=2)
			except Exception:
				try:
					proc.kill()
				except Exception:
					pass

	def _cleanup(self):
		self.unload()

	def _send(self, obj):
		with self._lock:
			proc = self._proc
		if proc and proc.poll() is None:
			try:
				proc.stdin.write(json.dumps(obj) + "\n")
				proc.stdin.flush()
			except Exception:
				pass

	def list_devices(self, timeout=5.0):
		"""Return list of (index, name) tuples for all BASS output devices.
		Sends list_devices command to the host process and waits for reply.
		Returns [] on failure.
		"""
		if not self.ready():
			return []
		evt	= threading.Event()
		result = [None]

		def _wait_for_reply():
			# Temporarily hook the read loop result via a one-shot flag
			deadline = time.time() + timeout
			self._send({"cmd": "list_devices"})
			while time.time() < deadline:
				time.sleep(0.05)
				if result[0] is not None:
					break

		# We piggyback on the existing _read_loop; add a side-channel listener
		old_on_devices = getattr(self, "_on_devices_reply", None)

		def _on_reply(devices):
			result[0] = devices
			evt.set()

		self._on_devices_reply = _on_reply
		self._send({"cmd": "list_devices"})
		evt.wait(timeout=timeout)
		self._on_devices_reply = old_on_devices
		return result[0] if result[0] is not None else []

	def _cancel_current_play(self):
		"""Cancel any ongoing play request and send stop to host."""
		with self._lock:
			if self._current_play_seq is not None:
				# Send stop to host to ensure any pending stream is cancelled
				self._send({"cmd": "stop"})
				self._current_play_seq = None

			# Also clear any pending response
			if self._pending_play:
				seq, evt, result_slot = self._pending_play
				result_slot[0] = False
				result_slot[1] = "cancelled"
				evt.set()
				self._pending_play = None

	def play(self, url, volume_0_1=1.0, seekable=False, rate=None, transpose=None):
		"""Send play command and block until the host confirms success/failure.

		If a previous play is still pending, it is cancelled first.
		seekable=True asks the host to open the URL without BASS_STREAM_BLOCK
		so seek_relative() actually works (podcasts); live radio should
		leave this False.

		rate/transpose (optional) are applied by bass_host.py atomically as
		part of this same play() call, before the new stream opens - see
		BassHost.play()'s docstring. Pass the exact value this track should
		start at (e.g. 1.0/0.0 to reset a jukebox track with no saved
		profile) rather than relying on a separate, earlier
		set_playback_rate()/set_transpose() call having already landed.
		Leave as None to keep whatever rate/transpose the host already has
		(the normal case for a live station, which doesn't need either).

		On failure, the reason bass_host.py gave (e.g. "StreamCreateURL
		failed (err=41)") is left on self.last_play_error for the caller
		to read - see its declaration in __init__() for why this exists.
		"""
		self.last_play_error = None
		if not self.ready():
			self.last_play_error = "BASS not loaded"
			return False

		# Cancel any ongoing play request
		self._cancel_current_play()

		# Assign a sequence number so _read_loop can route the reply back.
		with self._lock:
			self._play_seq += 1
			seq = self._play_seq
			self._current_play_seq = seq
			evt = threading.Event()
			self._pending_play = (seq, evt, [None, None])   # [ok, error]
			result_slot = self._pending_play[2]

		payload = {"cmd": "play", "url": url, "volume": volume_0_1, "seq": seq, "seekable": seekable}
		if rate is not None:
			payload["rate"] = float(rate)
		if transpose is not None:
			payload["transpose"] = float(transpose)
		self._send(payload)

		# If there is no response in the first 5 seconds, give the "connecting" signal, then wait another 25 seconds.
		got_reply = evt.wait(timeout=5)
		if not got_reply:
			if self.on_connecting:
				try:
					self.on_connecting(url)
				except Exception:
					pass
			got_reply = evt.wait(timeout=25)

		with self._lock:
			# Clear pending regardless
			if self._pending_play and self._pending_play[0] == seq:
				self._pending_play = None
			if self._current_play_seq == seq:
				self._current_play_seq = None

		if not got_reply:
			# The host may still be in BASS_StreamCreateURL.
			# If we do not send stop, it will start sound when completed.
			self._send({"cmd": "stop"})
			self.last_play_error = "timed out waiting for a response from the BASS host"
			return False

		success = result_slot[0]
		if not success:
			self.last_play_error = result_slot[1] or "unknown error"
		return bool(success)

	def stop(self):
		self._cancel_current_play()
		self._send({"cmd": "stop"})

	def pause(self):
		self._send({"cmd": "pause"})

	def resume(self):
		self._send({"cmd": "resume"})

	def set_volume(self, volume_0_1):
		# 2.0 upper limit matches bass_host.py; negative values are not allowed.
		self._send({"cmd": "volume", "value": max(0.0, min(2.0, volume_0_1))})

	# -- Time-shift (local buffer file) playback -------------------------

	def play_timeshift_file(self, path, volume_0_1=1.0, start_seconds=0.0, timeout=5.0):
		"""Open a local time-shift buffer file for seekable playback.
		Blocks until the host confirms success/failure. Returns True/False.
		"""
		if not self.ready():
			return False
		evt	= threading.Event()
		result = [False]

		old_on_reply = getattr(self, "_on_generic_reply", None)

		def _on_reply(ok):
			result[0] = ok
			evt.set()

		self._on_generic_reply = _on_reply
		self._send({
			"cmd": "timeshift_play",
			"path": path,
			"volume": volume_0_1,
			"start_seconds": start_seconds,
		})
		evt.wait(timeout=timeout)
		self._on_generic_reply = old_on_reply
		return result[0]

	def timeshift_seek(self, delta_seconds, timeout=3.0):
		"""Seek relative to the current position in the open time-shift
		file stream. Returns (ok, position_seconds, length_seconds)."""
		if not self.ready():
			return False, 0.0, 0.0
		evt	= threading.Event()
		result = [(False, 0.0, 0.0)]

		old_on_reply = getattr(self, "_on_timeshift_reply", None)

		def _on_reply(ok, position_seconds, length_seconds):
			result[0] = (ok, position_seconds, length_seconds)
			evt.set()

		self._on_timeshift_reply = _on_reply
		self._send({"cmd": "timeshift_seek", "delta_seconds": delta_seconds})
		evt.wait(timeout=timeout)
		self._on_timeshift_reply = old_on_reply
		return result[0]

	def timeshift_status(self, timeout=3.0):
		"""Return (position_seconds, length_seconds) for the currently open
		time-shift file stream, or (0.0, 0.0) on timeout/failure."""
		if not self.ready():
			return 0.0, 0.0
		evt	= threading.Event()
		result = [(0.0, 0.0)]

		old_on_reply = getattr(self, "_on_timeshift_status_reply", None)

		def _on_reply(position_seconds, length_seconds):
			result[0] = (position_seconds, length_seconds)
			evt.set()

		self._on_timeshift_status_reply = _on_reply
		self._send({"cmd": "timeshift_status"})
		evt.wait(timeout=timeout)
		self._on_timeshift_status_reply = old_on_reply
		return result[0]

	def set_bass_boost(self, boost_0_1):
		"""Adjust the bass boost level (0.0 = off, 1.0 = max +12 dB)."""
		self._send({"cmd": "bass_boost", "value": max(0.0, min(1.0, float(boost_0_1)))})

	def set_playback_rate(self, rate, timeout=3.0):
		"""Set pitch-preserving playback speed (podcasts only).

		rate: 1.0 = normal, 1.1 = 10% faster, 0.9 = 10% slower (clamped to
		0.5-3.0 on the host side). Returns (applied, actual_rate, reason) —
		applied is False when bass_fx.dll isn't available or the current
		stream can't be tempo-adjusted; the rate is still remembered on the
		host for the next tempo-capable stream either way.
		"""
		if not self.ready():
			return False, rate, "not_ready"
		evt = threading.Event()
		result = [(False, rate, "timeout")]

		old_on_reply = getattr(self, "_on_playback_rate_reply", None)

		def _on_reply(applied, actual_rate, reason):
			result[0] = (applied, actual_rate, reason)
			evt.set()

		self._on_playback_rate_reply = _on_reply
		self._send({"cmd": "set_playback_rate", "rate": float(rate)})
		evt.wait(timeout=timeout)
		self._on_playback_rate_reply = old_on_reply
		return result[0]

	def set_transpose(self, semitones, timeout=3.0):
		"""Set pitch transpose, independent of playback speed (podcasts,
		audio books and jukebox tracks). semitones: 0.0 = no shift; positive
		shifts up, negative shifts down (clamped to -12.0..12.0 on the host
		side). Persists across tracks (like playback rate) so it re-applies
		automatically the next time a tempo-capable stream is opened.

		Returns (applied, actual_semitones, reason) - applied is False when
		bass_fx.dll isn't available or the current stream can't be
		tempo-adjusted; the value is still remembered on the host for the
		next tempo-capable stream either way.
		"""
		if not self.ready():
			return False, semitones, "not_ready"
		evt = threading.Event()
		result = [(False, semitones, "timeout")]

		old_on_reply = getattr(self, "_on_transpose_reply", None)

		def _on_reply(applied, actual_semitones, reason):
			result[0] = (applied, actual_semitones, reason)
			evt.set()

		self._on_transpose_reply = _on_reply
		self._send({"cmd": "set_transpose", "semitones": float(semitones)})
		evt.wait(timeout=timeout)
		self._on_transpose_reply = old_on_reply
		return result[0]

	def adjust_transpose(self, delta, timeout=3.0):
		"""Nudge transpose by *delta* semitones relative to the last value
		sent (tracked in self._transpose, mirroring self._playback_rate).
		Returns (applied, actual_semitones, reason): see set_transpose()."""
		return self.set_transpose(getattr(self, "_transpose", 0.0) + delta, timeout=timeout)

	def get_transpose(self):
		return getattr(self, "_transpose", 0.0)

	def set_fx(self, fx_name):
		"""Adjust DirectX 8 effect.

		fx_name: "none" | "chorus" | "compressor" | "distortion" |
				 "echo" | "flanger" | "gargle" | "reverb" |
				 "eq_bass" | "eq_treble" | "eq_vocal"
		It is applied instantly on the active stream.
		"""
		self._send({"cmd": "set_fx", "fx": fx_name or "none"})

	def set_eq_gain(self, band, gain_db):
		"""Set the ParamEQ gain for one EQ band in dB (-15..+15).

		band:	"eq_bass" | "eq_treble" | "eq_vocal"
		gain_db: dB value; applied immediately if the band effect is active.
		"""
		self._send({"cmd": "set_eq_gain", "band": band,
					"gain_db": max(-15.0, min(15.0, float(gain_db)))})

	def get_icy_title(self):
		return self._icy_title

	def _read_loop(self):
		with self._lock:
			proc = self._proc
		if not proc:
			return
		try:
			for raw in proc.stdout:
				if self._stop_reader.is_set():
					break
				raw = raw.strip()
				if not raw:
					continue
				try:
					msg = json.loads(raw)
				except Exception:
					continue

				# ICY metadata event
				if msg.get("event") and msg.get("type") == "meta":
					title = msg.get("title", "")
					if title:
						self._icy_title = title
						if self.on_meta:
							try:
								self.on_meta(title)
							except Exception:
								pass
					continue

				# Stall event — BASS stream interrupted, reconnect
				if msg.get("event") and msg.get("type") == "stall":
					cb = getattr(self, "on_stall", None)
					if cb:
						try:
							cb()
						except Exception:
							pass
					continue

				# list_devices reply
				if msg.get("ok") and "devices" in msg:
					cb = getattr(self, "_on_devices_reply", None)
					if cb:
						try:
							cb(msg["devices"])
						except Exception:
							pass
					continue

				# Time-shift replies — routed unambiguously via the "cmd" echo
				# field the host attaches to these specific responses.
				reply_cmd = msg.get("cmd")
				if reply_cmd == "timeshift_play":
					cb = getattr(self, "_on_generic_reply", None)
					if cb:
						try:
							cb(bool(msg.get("ok")))
						except Exception:
							pass
					continue
				if reply_cmd == "timeshift_seek":
					cb = getattr(self, "_on_timeshift_reply", None)
					if cb:
						try:
							cb(msg.get("seeked", False),
							   msg.get("position_seconds", 0.0),
							   msg.get("length_seconds", 0.0))
						except Exception:
							pass
					continue
				if reply_cmd == "timeshift_status":
					cb = getattr(self, "_on_timeshift_status_reply", None)
					if cb:
						try:
							cb(msg.get("position_seconds", 0.0), msg.get("length_seconds", 0.0))
						except Exception:
							pass
					continue
				if reply_cmd == "set_playback_rate":
					cb = getattr(self, "_on_playback_rate_reply", None)
					if cb:
						try:
							cb(bool(msg.get("rate_applied", False)),
							   msg.get("rate", 1.0), msg.get("reason", ""))
						except Exception:
							pass
					continue
				if reply_cmd == "set_transpose":
					cb = getattr(self, "_on_transpose_reply", None)
					if cb:
						try:
							cb(bool(msg.get("transpose_applied", False)),
							   msg.get("semitones", 0.0), msg.get("reason", ""))
						except Exception:
							pass
					continue

				# Play result — route to waiting play() call
				seq = msg.get("seq")
				if seq is not None:
					with self._lock:
						pending = self._pending_play
						current_seq = self._current_play_seq
					# Only accept response if it matches the current active play
					if pending and pending[0] == seq and current_seq == seq:
						pending[2][0] = msg.get("ok", False)
						pending[2][1] = msg.get("error")
						pending[1].set()
					continue

		except Exception:
			pass
		finally:
			# Unblock any waiting play() call if the process died
			with self._lock:
				pending = self._pending_play
				self._pending_play = None
				self._current_play_seq = None
			if pending:
				pending[1].set()


# _BassEngine is the old in-process class — we keep the name but now it
# delegates to the subprocess engine.  RadioPlayer only uses the public API
# (load, ready, play, stop, pause, resume, set_volume, get_icy_title, unload,
# on_meta), which _BassSubprocessEngine fully satisfies.
class _BassEngine(_BassSubprocessEngine):
	"""Subprocess-based BASS engine (previously in-process)."""

	def __init__(self, dll_dir, output_device=_BASS_DEVICE_DEFAULT):
		# output_device: -1 = system default, positive int = specific device index
		super().__init__(dll_dir, device_index=output_device)


class _HlsStreamMerger:
	"""Streams an HLS (.m3u8) source to BASS through a local HTTP server
	whose body is ffmpeg's remuxed output, instead of handing BASS the
	original playlist URL.

	Why this exists: BASS (via basshls.dll) plays each HLS segment as
	its own stream. On very-short-segment sources (juyun.tv camera
	feeds, ~1-2s segments), that drains the playback buffer at every
	boundary - heard as a repeated ~1-2s stutter. VLC and browsers avoid
	this by remuxing segments into one continuous stream before
	decoding; ffmpeg does the same here, and this class pipes its stdout
	to whatever BASS connects to on the local server.

	Uses "-c:a copy" (pure remux, no re-encoding, minimal CPU). A plain
	concatenation of raw segment bytes isn't enough - each segment
	has its own MPEG-TS PCR/continuity counters, so the result has
	timestamp discontinuities BASS won't tolerate; ffmpeg's remux fixes
	that without touching the codec. An earlier version re-encoded to
	MP3 instead, because some long-segment sources (TRT2 among them)
	weren't copy-compatible - but the merger now only runs for confirmed
	short-segment sources (_should_hls_merge()), which those never are,
	so it's back to a plain copy. If a short-segment source ever turns
	out to have the same problem, re-encode just that one rather than
	bringing MP3 back as the default.

	The ffmpeg executable is resolved in this order:
	  1. config.conf["freeAudio"]["ffmpeg_path"], if set and valid.
	  2. _find_system_ffmpeg(), which looks next to this module (where
	     the recorder and recognizer already expect to find it), then
	     on PATH, then in a handful of common Windows install locations.

	If neither resolves, start() returns None and the caller falls back
	to the original (un-merged) URL - which means the original segment-
	boundary stutter, but at least the stream still plays.
	"""

	def __init__(self):
		self._server = None
		self._thread = None
		self._port = 0
		self._source_url = None
		self._ffmpeg_path = None
		self._stop_event = threading.Event()

	def start(self, source_url):
		"""Start the merger for *source_url*. Returns the local URL BASS
		should play, or None if the merger could not be started (most
		commonly because no ffmpeg executable could be found)."""
		import http.server
		import socketserver
		import config as _config

		self.stop()
		self._source_url = source_url
		self._stop_event.clear()

		# Resolve an ffmpeg executable. Prefer the user's configured
		# path (the same one the recorder uses for format conversion);
		# if that's empty or invalid, fall back to auto-detection -
		# which includes the add-on's own directory, since that's where
		# the recorder/recognizer expect ffmpeg.exe to live by default.
		# If neither works, return None so the caller falls back to the
		# original URL.
		ffmpeg_path = (_config.conf["freeAudio"].get("ffmpeg_path") or "").strip()
		if not ffmpeg_path or not os.path.isfile(ffmpeg_path):
			ffmpeg_path = _find_system_ffmpeg()
		if not ffmpeg_path:
			log.warning(
				"freeAudio: HLS merger not started - no ffmpeg found. "
				"Place ffmpeg.exe next to radioPlayer.py, set 'ffmpeg_path' "
				"in freeAudio settings, or install ffmpeg on PATH."
			)
			return None
		self._ffmpeg_path = ffmpeg_path

		merger = self

		class _Handler(http.server.BaseHTTPRequestHandler):
			def do_GET(self):
				merger._serve_stream(self)

			def log_message(self, *args):
				pass  # silence the default stderr logging

		class _Server(socketserver.ThreadingTCPServer):
			allow_reuse_address = True
			daemon_threads = True

		try:
			self._server = _Server(("127.0.0.1", 0), _Handler)
			self._port = self._server.server_address[1]
		except Exception:
			self._server = None
			return None

		self._thread = threading.Thread(
			target=self._server.serve_forever, daemon=True,
			name="freeAudio-hls-merger")
		self._thread.start()
		return "http://127.0.0.1:%d/stream" % self._port

	def local_url(self):
		"""Return the local URL BASS should be playing, or None if the
		merger isn't currently running. Used by the BASS stall-reconnect
		path so it reconnects to the same merged stream instead of
		bypassing the merger and going straight back to the original
		.m3u8 (which would immediately re-enter the segment-boundary
		stutter that caused the stall in the first place)."""
		if self._server is None or self._port == 0:
			return None
		return "http://127.0.0.1:%d/stream" % self._port

	def stop(self):
		"""Stop the local server and clean up.

		Deliberately does NOT close any in-flight client socket. The
		handler thread started by ThreadingTCPServer owns that socket,
		and it is the only thing allowed to close it - it exits its own
		loop as soon as self._stop_event is set, and http.server closes
		the socket for it when the handler returns. Closing the socket
		from here would race with the handler thread's own writes and
		produce "ValueError: I/O operation on closed file" tracebacks on
		every station switch."""
		self._stop_event.set()
		if self._server:
			try:
				self._server.shutdown()
				self._server.server_close()
			except Exception:
				pass
			self._server = None
		if self._thread:
			try:
				self._thread.join(timeout=2)
			except Exception:
				pass
			self._thread = None

	def _serve_stream(self, handler):
		"""Handle one BASS connection: launch ffmpeg on the source URL,
		pipe its stdout straight to the client socket. When BASS closes
		the connection (seek, station switch, stop - all normal), ffmpeg
		is terminated too, so the merger never leaks a subprocess."""
		ffmpeg_path = getattr(self, "_ffmpeg_path", None)
		if not ffmpeg_path:
			# Shouldn't be reachable - start() already refused to start
			# without a path - but keep this as a defensive belt.
			try:
				handler.send_response(500)
				handler.end_headers()
			except Exception:
				pass
			return

		try:
			handler.send_response(200)
			# MPEG-TS is what HLS segments carry for both audio-only and
			# audio+video live streams; BASS (via basshls/bass_aac) sniffs
			# the actual container from the bytes themselves, so the exact
			# Content-Type value is only cosmetic here.
			handler.send_header("Content-Type", "video/mp2t")
			handler.send_header("Cache-Control", "no-cache")
			handler.send_header("Connection", "close")
			handler.end_headers()
		except Exception:
			return

		try:
			handler.connection.settimeout(30.0)
		except Exception:
			pass

		cmd = [
			ffmpeg_path,
			"-hide_banner",
			"-loglevel", "error",
			# Present a browser-like UA to the CDN - some HLS origins
			# refuse connections from unknown clients.
			"-user_agent", "freeAudio-NVDA/1.0",
			# Let ffmpeg itself reconnect the input on transient network
			# failures. This is the main reason the pipeline survives
			# brief CDN hiccups without BASS ever seeing a stalled stream.
			"-reconnect", "1",
			"-reconnect_streamed", "1",
			"-reconnect_delay_max", "5",
			# Some HLS origins serve very small segments; ask ffmpeg to
			# buffer a reasonable amount before starting to output, so
			# the initial burst of segments doesn't cause an early stall
			# on BASS's side.
			"-probesize", "1M",
			"-analyzeduration", "1M",
			"-i", self._source_url,
			# Pure remux (no re-encode) - see _HlsStreamMerger's
			# docstring. No -ac/-ar here: those imply a filter pass,
			# which ffmpeg refuses to combine with "-c:a copy".
			"-map", "0:a:0",
			"-vn",
			"-c:a", "copy",
			# Output format: MPEG-TS.
			"-f", "mpegts",
			# Write to stdout.
			"-",
		]

		proc = None
		try:
			proc = subprocess.Popen(
				cmd,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
				bufsize=0,
			)
		except Exception as e:
			log.warning("freeAudio: HLS merger could not start ffmpeg: %s", e)
			try:
				handler.send_response(500)
			except Exception:
				pass
			return

		# Drain ffmpeg's stderr in a background thread so a chatty
		# decode warning can never fill the pipe and block ffmpeg. The
		# last few lines are kept around for diagnosing a stream that
		# never produced any output.
		stderr_tail = []

		def _drain_stderr(p, tail):
			try:
				for line in p.stderr:
					tail.append(line)
					if len(tail) > 20:
						del tail[: len(tail) - 20]
			except Exception:
				pass

		threading.Thread(
			target=_drain_stderr, args=(proc, stderr_tail),
			daemon=True, name="freeAudio-hls-ffmpeg-err"
		).start()

		bytes_written = 0
		try:
			while not self._stop_event.is_set():
				try:
					chunk = proc.stdout.read(32768)
				except Exception:
					break
				if not chunk:
					break
				bytes_written += len(chunk)
				try:
					handler.wfile.write(chunk)
					handler.wfile.flush()
				except (ValueError, OSError, BrokenPipeError):
					# BASS closed the connection (seek, switch, stop) -
					# normal, just end this handler quietly.
					break
		except Exception:
			pass
		finally:
			try:
				proc.terminate()
				proc.wait(timeout=2)
			except Exception:
				try:
					proc.kill()
				except Exception:
					pass
			if bytes_written == 0 and stderr_tail:
				log.warning(
					"freeAudio: HLS merger ffmpeg produced no output for %s; "
					"last stderr: %s",
					self._source_url, b"".join(stderr_tail[-5:]).decode("utf-8", "replace")
				)


class RadioPlayer:
	"""
	Unified radio player.
	BASS (in-process ctypes) is the sole playback backend.
	"""

	BACKEND_BASS	  = "bass"
	BACKEND_NONE	  = "none"

	def __init__(self, output_device=_BASS_DEVICE_DEFAULT, config_path=None):
		self._current_url = None
		self._current_url_resolved = None
		self._current_name = ""
		self._current_station = {}
		self._is_playing = False
		self._volume = 100
		self._bass_boost = 0.0   # bass boost level: 0.0–1.0
		self._playback_rate = 1.0  # pitch-preserving speed for podcasts: 1.0 = normal
		self._transpose = 0.0  # pitch shift in semitones, independent of speed: 0.0 = no shift
		self._audio_fx   = "none"  # active DirectX 8 effect name
		self._intentional_stop = False
		self._play_lock = threading.RLock()  # Prevent concurrent play operations
		self._play_gen  = 0		  # Incremented on every play(); bg threads check this

		self._backend = self.BACKEND_NONE

		self._audio_device_refresh_mode = "reliable"

		# Local HLS stream merger - created lazily for the first
		# short-segment HLS station played (_should_hls_merge()). See
		# _HlsStreamMerger's docstring.
		self._hls_merger = None
		# url -> (should_merge, decided_at) - see _should_hls_merge().
		self._hls_merge_decision_cache = {}

		dll_dir = os.path.dirname(os.path.abspath(__file__))
		self._bass_engine = _BassEngine(dll_dir, output_device=output_device)
		self._bass_engine.load()
		if self._bass_engine.ready():
			self._bass_engine.on_meta = self._on_bass_meta
			self._bass_engine.on_connecting = self._on_bass_connecting
			self._bass_engine.on_stall = self._on_bass_stall

		self._icy_title = None
		self._icy_stop = threading.Event()
		self._icy_thread = None

		self._output_device_index = output_device  # User-selected device index
		self.on_device_lost = None  # Callback: called when the device is lost (device_index)
		# Callback: called with (url) right after a podcast's position is
		# saved due to a pause or the episode finishing - NOT the periodic
		# 15s autosave. Lets the UI refresh that one episode row's
		# [Listened]/duration display without a continuously-ticking timer.
		# May run on a background thread (called from _on_bass_stall).
		self.on_podcast_progress_saved = None
		# Callback: called with (station) only when a podcast/GETEM item
		# actually reaches its end (never on a plain pause) - see the
		# is_podcast branch of _on_bass_stall(). Lets the UI auto-advance to
		# the next episode/chapter. Deliberately separate from
		# on_podcast_progress_saved, which also fires on pause and only
		# gets a bare url, not enough to tell "finished" from "paused".
		# May run on a background thread (called from _on_bass_stall); the
		# handler is responsible for marshalling onto the UI thread.
		self.on_podcast_finished = None
		# Callback: called with (station, url, reason) when a live-radio
		# launch's BASS connection attempt fails outright (BASS_StreamCreateURL/
		# ChannelPlay never succeeded for this URL through any resolve
		# step) - see _bg_launch()'s post-_launch() backend check below.
		# reason is whatever string bass_host.py sent back with its
		# {"ok": false, "error": ...} reply for the "play" command (e.g.
		# "StreamCreateURL failed (err=41)"), forwarded via
		# _BassSubprocessEngine.last_play_error - or "unknown reason" if
		# that wasn't available for some reason.
		#
		# Without this, a failed _launch_bass() used to be swallowed
		# silently: _is_playing was already set True back in play()
		# (optimistically, before the connection was confirmed) and
		# nothing ever set it back to False or told the user anything -
		# _launch() doesn't raise on a failed connection, it just quietly
		# returns without setting self._backend to BACKEND_BASS. The UI
		# kept showing the station as "playing" indefinitely with no
		# audio and no error, and time-shift/rewind would only ever
		# report the generic "not available for the current playback
		# backend" message, with no indication *why* BASS never actually
		# started. May run on a background thread - the handler is
		# responsible for marshalling onto the UI thread.
		self.on_play_failed = None

		# Crossfade
		self._crossfade_duration = 0.0   # seconds; 0.0 = disabled
		self._crossfade_engine   = None  # old _BassEngine being faded out

		# Station tuning transition effect (alternative to numeric crossfade,
		# mutually exclusive with it — see set_tuning_effect_enabled()).
		self._tuning_effect_enabled = False
		self._tuning_engine = None  # old _BassEngine currently playing tuner.mp3
		self._tuning_stop   = None  # threading.Event signalling the loop-watcher to stop

		self._watchdog_stop = threading.Event()
		self._watchdog_thread = threading.Thread(target=self._watchdog_loop, daemon=True)
		self._watchdog_thread.start()

		# Podcast resume positions: {url: {"position": secs, "name": str,
		# "updated": iso timestamp}}, persisted to disk so an episode
		# picks up where it left off next time it's played (podcasts are
		# always seekable - see the "seekable" play() flag - so resuming
		# is just a seek after playback starts).
		# Stored under the NVDA user config directory rather than next to
		# this file - the addon folder gets wiped and replaced on every
		# update, which would silently lose all saved positions.
		self._podcast_positions_path = self._get_podcast_positions_path()
		self._podcast_positions_lock = threading.Lock()
		self._podcast_positions = self._load_podcast_positions()

		# Jukebox folder resume positions: {folder_path: {"track_index": int,
		# "track_path": str, "updated": iso timestamp}}, persisted the same
		# way as podcast positions above, so replaying a folder picks up
		# from the last track played in it instead of always track 1. The
		# track's own within-track position comes for free from
		# _podcast_positions above (jukebox tracks are seekable media too -
		# see _is_seekable_media()), so this only needs to remember *which*
		# track.
		self._jukebox_folder_positions_path = self._get_jukebox_folder_positions_path()
		self._jukebox_folder_positions_lock = threading.Lock()
		self._jukebox_folder_positions = self._load_jukebox_folder_positions()
		self._podcast_autosave_stop = threading.Event()
		self._podcast_autosave_thread = threading.Thread(
			target=self._podcast_autosave_loop, daemon=True,
			name="freeAudio-podcast-autosave")
		self._podcast_autosave_thread.start()

		# Time-shift buffer (rewind/fast-forward for live radio). Disabled by
		# default — the caller enables it via set_timeshift_enabled(True)
		# once the user opts in from the settings panel. Only supported on
		# the BASS backend.
		self._timeshift_enabled = False
		self._timeshift_active  = False   # True while time-shifted (buffered) playback is active
		self._timeshift_suspended_for_mirror = False  # True while suspend_timeshift_for_mirror() has stopped capture to free a connection slot for the mirror
		# User-configurable rewind buffer capacity in seconds (default 10
		# min; up to 5 hours via Settings). Only applies once the
		# time-shift feature itself is enabled — the always-on lightweight
		# buffer stays fixed at _LIGHT_BUFFER_SECONDS regardless.
		self._timeshift_capacity_seconds = 600
		self._timeshift_buffer  = _timeshift_mod.TimeShiftBuffer()
		# _play_gen value for which _timeshift_buffer currently holds the
		# right station's capture session. _timeshift_active is reset to
		# False as soon as _bg_launch starts (see below), well before the
		# buffer itself is actually stopped/restarted for the new stream -
		# so without this, a rewind press landing in that gap would treat
		# the *previous* station's still-live buffer file as "ready" and
		# start time-shift playback from it instead of correctly reporting
		# "not buffered yet". None until the first station has ever fully
		# swapped the buffer over.
		self._timeshift_buffer_gen = None
		# Serializes every "stop old capture / start new capture / assign
		# _timeshift_buffer_gen" sequence across the different code paths
		# that can trigger one (_bg_launch on station switch, the BASS
		# stall reconnect, and set_timeshift_enabled's _bg_start_capture).
		# Without this, two such sequences racing (e.g. a fast station
		# switch landing while set_timeshift_enabled's background thread is
		# still resolving the previous station's URL) could interleave
		# their stop()/start() calls and finish with the buffer capturing
		# one station while _timeshift_buffer_gen claims it belongs to a
		# different one - rewind_timeshift() would then refuse forever with
		# "no_buffer_yet" until something (station switch, feature toggle)
		# happened to reset it back into sync.
		self._timeshift_launch_lock = threading.Lock()

		self._device_monitor_thread = threading.Thread(target=self._device_monitor_loop, daemon=True)
		self._device_monitor_thread.start()



	def _podcast_position_key(self, station):
		"""Return the key used to store a podcast/audiobook chapter's
		resume position.

		Prefers an explicit "podcast_resume_key" field over the station's
		own "url". Some sources (GETEM) route playback through a local
		proxy whose URL path token is deliberately randomized per NVDA
		session (see getem.get_stream_url()), so keying resume positions
		on that URL would silently lose them on every restart. In that
		case the caller sets "podcast_resume_key" to the chapter's real
		(stable) upstream URL, and resume keeps working across restarts
		regardless of the session-random token."""
		if station and station.get("podcast_resume_key"):
			return station["podcast_resume_key"]
		return (station.get("url") if station else None) or self._current_url

	def _on_bass_meta(self, title):
		self._icy_title = title

	def _on_bass_connecting(self, url):
		"""Called if BASS connection could not be established within 5s."""
		if self.on_slow_connect:
			try:
				self.on_slow_connect(url)
			except Exception:
				pass

	def _should_hls_merge(self, url, timeout=4):
		"""Whether *url* (an HLS .m3u8) should route through
		_HlsStreamMerger - only short-segment sources need it (see
		_HlsStreamMerger's docstring). Cached per URL for
		_HLS_MERGE_DECISION_TTL so a stall/reconnect never re-fetches
		the playlist mid-struggle. Unknown (fetch failed/timed out/no
		TARGETDURATION) defaults to False - stay on the cheaper plain
		path unless the merger is positively confirmed needed.
		"""
		now = time.time()
		cached = self._hls_merge_decision_cache.get(url)
		if cached and now - cached[1] < _HLS_MERGE_DECISION_TTL:
			return cached[0]
		duration = _get_hls_target_duration(url, timeout=timeout)
		decision = duration is not None and duration <= _HLS_SHORT_SEGMENT_THRESHOLD
		self._hls_merge_decision_cache[url] = (decision, now)
		if duration is not None:
			log.info(
				"freeAudio: HLS target duration for %s = %.0fs (%s merger)",
				url, duration, "using" if decision else "skipping",
			)
		else:
			log.info("freeAudio: could not determine HLS target duration for "
					 "%s, leaving merger off", url)
		return decision

	def _on_bass_stall(self):
		"""Called when bass_host.py sends a stall event."""
		if not self._is_playing or self._intentional_stop:
			return

		station = self._current_station
		is_podcast = _is_seekable_media(station)

		# If it's a podcast, reaching stall means the episode has ended.
		# Mark as listened and stop player instead of reconnecting/restarting.
		if is_podcast:
			log.info("freeAudio: Podcast episode finished playing.")
			self._save_podcast_position_now(station, -1.0, -1.0)
			cb = self.on_podcast_progress_saved
			if cb:
				try:
					cb(station.get("url") or self._current_url)
				except Exception:
					pass
			finished_cb = self.on_podcast_finished
			if finished_cb:
				try:
					finished_cb(station)
				except Exception:
					pass
			# Deliberately keep_mirror=True here - see stop()'s docstring
			# for why an unconditional stop_mirror() in this specific
			# "track finished on its own" path breaks Audio Mirror on
			# every jukebox/audio-book auto-advance.
			self.stop(keep_mirror=True)
			return

		# bass_host's stall watcher monitors whatever is on the single BASS
		# channel, live URL or the local time-shift .buf file alike, and
		# can't tell us which one stalled. A still-growing .buf file is
		# especially prone to tripping its buffer-empty/position-stuck
		# checks spuriously. If we're currently time-shifted, treat this
		# as that (not a dead live connection) and just fall back to live
		# the same clean way exit_timeshift_to_live() always does -
		# running the live-URL reconnect/backoff loop below instead would
		# silently tear down time-shift mode via _bg_launch's own reset,
		# then immediately race back into a fresh, still-too-small buffer
		# on the next rewind press, repeating indefinitely.
		if self._timeshift_active:
			log.warning("freeAudio: BASS stall detected during time-shifted "
						"playback, returning to live")
			self.exit_timeshift_to_live()
			return

		url = self._current_url
		vol = self._volume
		if not url:
			return
		log.warning("freeAudio: BASS stall detected, reconnecting: %s", url)

		# If this is a merged HLS station, reconnect to the merger's
		# local URL, not the original .m3u8, or we'd re-enter the same
		# stutter that caused the stall. _should_hls_merge() hits cache
		# here (decided at launch), so no playlist re-fetch mid-struggle.
		_is_hls = url.lower().split("?")[0].endswith(".m3u8")
		_use_merger = _is_hls and self._should_hls_merge(url)

		# Capture generation at the moment of stall so reconnect thread
		# can detect if a newer play() has already taken over.
		stall_gen = self._play_gen

		def _reconnect(captured_gen=stall_gen):
			if not self._is_playing or self._intentional_stop:
				return
			# First attempt is immediate — Icecast dropouts should reconnect
			# without delay. Subsequent retries back off progressively.
			for wait in (0, 5, 10, 20, 30):
				if not self._is_playing or self._intentional_stop:
					return
				# Abort if a newer play() already started
				if self._play_gen != captured_gen:
					return
				time.sleep(wait)
				if not self._is_playing or self._intentional_stop:
					return
				if self._play_gen != captured_gen:
					return  # User selected a different station
				if self._current_url != url:
					return

				# Decide which URL this reconnect attempt should use.
				# For HLS, prefer the merger's current local URL; if the
				# merger isn't running any more (rare - it's only stopped
				# by stop() or by switching to a non-HLS station), try to
				# restart it from the original source URL.
				reconnect_url = url
				if _use_merger:
					local = self._hls_merger.local_url() if self._hls_merger is not None else None
					if not local:
						try:
							if self._hls_merger is None:
								self._hls_merger = _HlsStreamMerger()
							local = self._hls_merger.start(url)
						except Exception:
							local = None
					if local:
						reconnect_url = local
					else:
						log.warning(
							"freeAudio: HLS merger unavailable on reconnect, "
							"falling back to original URL (stream may stutter)"
						)

				log.info("freeAudio: BASS stall reconnect attempt: %s", reconnect_url)
				with self._play_lock:
					# Double-check generation under lock before bumping
					if self._play_gen != captured_gen:
						return
					self._play_gen += 1
					captured_gen = self._play_gen
				try:
					if self._launch_bass(reconnect_url, vol):
						log.info("freeAudio: BASS stall reconnect OK")
						# The time-shift capture connection is independent of
						# BASS playback and was never interrupted by this
						# stall, so the buffer is still valid for the current
						# station - only _play_gen advanced here, not the
						# buffer's own generation. Sync them so rewind_timeshift()
						# doesn't mistake this still-good buffer for a stale
						# one and refuse to rewind (see its gen check).
						if self._backend == self.BACKEND_BASS:
							with self._timeshift_launch_lock:
								if self._play_gen == captured_gen:
									self._timeshift_buffer_gen = captured_gen
						return
				except Exception:
					pass
			log.warning("freeAudio: BASS stall reconnect exhausted")

			# BASS could not recover after repeated attempts. There is no
			# other backend to fall back to, so stop playback cleanly
			# instead of leaving _is_playing True with no audio actually
			# playing (and possibly stale ICY metadata still displayed).
			if not self._is_playing or self._intentional_stop:
				return
			if self._play_gen != captured_gen:
				return
			self.stop()

		threading.Thread(target=_reconnect, daemon=True,
						 name="freeAudio-BassReconnect").start()


	def _watchdog_loop(self):
		# The BASS backend is self-managing (its own stall/reconnect logic
		# in _on_bass_stall handles recovery), so with no other backend
		# left to babysit, this loop has nothing left to do. Kept as a
		# lightweight idle thread rather than removed outright to avoid
		# touching the start/stop wiring in __init__/terminate().
		while not self._watchdog_stop.is_set():
			for _ in range(_WATCHDOG_INTERVAL * 2):
				if self._watchdog_stop.is_set():
					return
				time.sleep(0.5)


	def _start_icy_thread(self, url):
		self._stop_icy_thread()
		self._icy_title = None
		self._icy_stop.clear()
		self._icy_thread = threading.Thread(target=self._icy_loop, args=(url,), daemon=True)
		self._icy_thread.start()

	def _stop_icy_thread(self):
		self._icy_stop.set()
		t = self._icy_thread
		self._icy_thread = None
		if t and t.is_alive():
			t.join(timeout=2)
		self._icy_stop.clear()

	def _icy_loop(self, url):
		while not self._icy_stop.is_set():
			title = _read_icy_title(url)
			if title and title != self._icy_title:
				self._icy_title = title
			for _ in range(_ICY_INTERVAL * 2):
				if self._icy_stop.is_set():
					return
				time.sleep(0.5)

	def get_icy_title(self):
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			return self._bass_engine.get_icy_title()
		return self._icy_title

	def set_audio_device_refresh_mode(self, mode):
		"""Ustaw tryb odświeżania listy urządzeń BASS."""
		self._audio_device_refresh_mode = "fast" if mode == "fast" else "reliable"

	def use_fresh_audio_device_probe(self):
		return getattr(self, "_audio_device_refresh_mode", "reliable") != "fast"

	def _stop_current(self):
		if self._bass_engine:
			self._bass_engine.stop()
		self._backend = self.BACKEND_NONE

	def _launch(self, url, volume, gen=None):
		"""Launch playback via BASS.
		Always called from a background thread.
		gen: the _play_gen value captured when this launch was requested.
			 If self._play_gen no longer matches, a newer play() has arrived
			 and we must stop immediately without starting any audio output.
		"""
		def _stale():
			return gen is not None and self._play_gen != gen

		self._stop_current()

		if _stale():
			return

		if self._bass_engine and self._bass_engine.ready():
			try:
				if self._launch_bass(url, volume):
					if _stale():
						self._bass_engine.stop()
						return
					return
			except Exception:
				pass

	def _launch_bass(self, url, volume):
		"""Start BASS playback — single attempt, no retry."""
		# Ensure any previously playing stream is stopped before starting a new one.
		if self._bass_engine:
			self._bass_engine.stop()
		station = self._current_station
		is_podcast = _is_seekable_media(station)
		saved_pos = 0.0
		if is_podcast:
			saved_pos = self.get_podcast_position(self._podcast_position_key(station))

		# If we're about to try resuming a podcast, open the real stream
		# muted and play casette.mp3 (looped) on a small separate engine
		# meanwhile, instead of letting the episode's own audio play
		# audibly from 0:00 while we wait for BASS to accept the seek back
		# to saved_pos. Uses the same loop-watcher as station tuning
		# transitions (_tuning_loop_watcher), just pointed at the
		# casette.mp3 clip instead of tuner.mp3 - see
		# set_tuning_effect_enabled() and _play_casette_clip().
		resume_wait_engine = None
		resume_wait_stop   = None
		if is_podcast and saved_pos > 1.0:
			try:
				dll_dir = os.path.dirname(os.path.abspath(__file__))
				candidate = _BassEngine(dll_dir, output_device=self._output_device_index)
				if candidate.load():
					self._play_casette_clip(candidate)
					resume_wait_engine = candidate
					resume_wait_stop   = threading.Event()
					threading.Thread(
						target=self._tuning_loop_watcher,
						args=(resume_wait_engine, resume_wait_stop, self._play_gen),
						kwargs={"clip_fn": self._play_casette_clip},
						daemon=True, name="freeAudio-podcast-resume-tuner"
					).start()
			except Exception:
				resume_wait_engine = None
				resume_wait_stop   = None

		play_volume = 0.0 if resume_wait_engine else (volume / 100.0)
		# Bake the current rate/transpose into this same play() call so the
		# new stream is guaranteed to start at exactly self._playback_rate/
		# self._transpose - see _BassSubprocessEngine.play()'s docstring
		# for why this matters more than it looks: playbackCoreMixin.
		# _play_station() already updates self._playback_rate/self._transpose
		# via set_playback_rate_value()/set_transpose_value() before this
		# runs (e.g. resetting a jukebox track with no saved profile back
		# to 1.0/0.0), but that update is a separate, earlier round-trip to
		# the same reused bass_host.py subprocess - passing the values
		# again here removes any dependency on that earlier command having
		# already been fully processed before this new stream opens.
		# None for a live station (not is_podcast): nothing to reset, and
		# rate/transpose don't apply to live streams anyway.
		launch_rate	  = self._playback_rate if is_podcast else None
		launch_transpose = self._transpose	  if is_podcast else None
		success = self._bass_engine.play(url, play_volume, seekable=is_podcast,
										  rate=launch_rate, transpose=launch_transpose)

		def _stop_resume_wait():
			if resume_wait_stop:
				resume_wait_stop.set()
			if resume_wait_engine:
				try:
					resume_wait_engine.stop()
					resume_wait_engine.unload()
				except Exception:
					pass

		if success:
			self._backend = self.BACKEND_BASS
			# Reapply bass boost setting (DSP resets when stream restarts)
			boost = getattr(self, "_bass_boost", 0.0)
			if boost > 0.0:
				try:
					self._bass_engine.set_bass_boost(boost)
				except Exception:
					pass
			# Reapply FX setting — _apply_fx() in bass_host already runs during
			# play(), but we send set_fx again as a safety net for edge cases
			# (e.g. subprocess state divergence after device switch).
			fx = getattr(self, "_audio_fx", "none")
			if fx and fx != "none":
				try:
					self._bass_engine.set_fx(fx)
				except Exception:
					pass
			# Reapply playback rate (podcasts only) — bass_host.py's Host
			# remembers the rate on its own and reapplies it automatically
			# the next time a tempo-capable stream is opened *within the
			# same subprocess* (see _try_create_url). But whenever a fresh
			# _BassEngine is created instead of reusing the existing one —
			# crossfade/tuning transitions (play()), or switch_output_device()
			# — the new subprocess's Host starts at the default rate (1.0)
			# and never learns about self._playback_rate, so the previously
			# chosen speed silently reverts to normal on the next episode or
			# resume. Resending it here (same safety-net pattern as bass
			# boost/FX above) keeps it in sync regardless of which engine
			# instance ended up serving this stream.
			if is_podcast and self._playback_rate != 1.0:
				try:
					self._bass_engine.set_playback_rate(self._playback_rate)
				except Exception:
					pass
			# Reapply pitch transpose the same way, for the same reason.
			if is_podcast and self._transpose != 0.0:
				try:
					self._bass_engine.set_transpose(self._transpose)
				except Exception:
					pass
			# Resume podcasts from where they were left off - podcasts are
			# always opened seekable (see the "seekable" flag above), so
			# this is just a relative seek from the fresh position (0).
			if is_podcast and saved_pos > 1.0:
				self._resume_podcast_position_on_engine(self._bass_engine, saved_pos)
			if resume_wait_engine:
				_stop_resume_wait()
				# Reveal the episode at its real volume now that it's
				# positioned correctly (or we gave up waiting for the seek).
				try:
					self._bass_engine.set_volume(volume / 100.0)
				except Exception:
					pass
			return True
		_stop_resume_wait()
		return False

	def _resume_podcast_position(self, saved_pos):
		"""Seek to saved_pos right after a podcast starts playing.

		A seek attempted in the first instant after play() returns can
		silently fail (or land at 0) - BASS may not have finished reading
		the stream's Content-Length yet, so the seek target gets clamped
		against a not-yet-populated length. The previous version fired a
		single seek and ignored its result entirely, so this failure was
		invisible and the episode just kept playing from the start. Retry
		briefly instead of giving up after one silent attempt.
		"""
		self._resume_podcast_position_on_engine(self._bass_engine, saved_pos)

	def _resume_podcast_position_on_engine(self, engine, saved_pos):
		"""Seek *engine* to saved_pos right after it starts playing a
		seekable (podcast) stream. Shared by the main playback path
		(_resume_podcast_position) and by start_mirror(), which needs the
		same retry behaviour to pick up the mirror output at the position
		the main output is already at.

		Podcasts are opened as progressive network streams, not fully
		pre-buffered (see _BassEngine.play()'s "seekable" docstring), so a
		seek attempted the instant play() reports success can legitimately
		fail: BASS may not yet have downloaded/parsed enough of the stream
		to know its length or accept a position change. The previous retry
		window here (6 attempts, 0.25s apart - under 2 seconds total) was
		too short on an ordinary connection, so a slow-to-buffer episode
		would consistently exhaust every attempt and silently keep playing
		from 0:00 with no visible error. Retry for up to ~15 seconds with
		a growing delay between attempts to give normal buffering time to
		catch up before giving up.
		"""
		deadline = time.time() + 15.0
		delay = 0.3
		attempt = 0
		while time.time() < deadline:
			attempt += 1
			try:
				ok, _pos, _length = engine.timeshift_seek(saved_pos)
			except Exception:
				ok = False
			if ok:
				return
			time.sleep(delay)
			delay = min(delay * 1.5, 1.5)
		log.info("freeAudio: could not resume podcast at %.1fs after %d attempts over ~15s",
				  saved_pos, attempt)

	def set_crossfade_duration(self, seconds):
		"""Set the crossfade duration in seconds when switching stations.

		seconds: 0.0 disables crossfade (instant cut); recommended range 1.0–4.0.
		Only effective with the BASS backend.
		"""
		self._crossfade_duration = max(0.0, float(seconds))

	def get_crossfade_duration(self):
		return self._crossfade_duration

	def _abort_crossfade(self):
		"""Immediately stop any in-progress fade-out engine.  Must be called
		from a context where it is safe to unload a _BassEngine."""
		engine = self._crossfade_engine
		self._crossfade_engine = None
		if engine:
			try:
				engine.stop()
				engine.unload()
			except Exception:
				pass

	def set_tuning_effect_enabled(self, enabled):
		"""Enable/disable the 'station tuning' transition effect.

		When enabled, switching stations plays tuner.mp3 (looped for as long
		as needed) while the new station connects in the background; as soon
		as the new stream is confirmed playing, the effect is cut over
		instantly. Only effective with the BASS backend. Mutually exclusive
		with a numeric crossfade — callers should set that duration to 0.0
		when enabling this.
		"""
		self._tuning_effect_enabled = bool(enabled)

	def get_tuning_effect_enabled(self):
		return self._tuning_effect_enabled

	def _play_tuner_clip(self, engine):
		"""Open tuner.mp3 on engine for the station tuning transition effect.

		Starts from a random position once the clip's duration is known, so
		each station switch (and each loop restart while waiting) sounds
		different instead of always starting from the same spot. The first
		time it's ever played, the duration isn't known yet, so it starts
		from 0.0 and the discovered length is cached in _TUNER_LENGTH_SECONDS
		for all later calls.
		"""
		global _TUNER_LENGTH_SECONDS
		start = 0.0
		if _TUNER_LENGTH_SECONDS and _TUNER_LENGTH_SECONDS > 1.0:
			start = random.uniform(0.0, max(0.0, _TUNER_LENGTH_SECONDS - 1.0))
		ok = engine.play_timeshift_file(_TUNER_MP3_PATH, self._volume / 100.0, start_seconds=start)
		if ok and not _TUNER_LENGTH_SECONDS:
			try:
				_pos, length = engine.timeshift_status()
				if length > 0:
					_TUNER_LENGTH_SECONDS = length
			except Exception:
				pass
		return ok

	def _play_casette_clip(self, engine):
		"""Open casette.mp3 on engine for the podcast/audio book
		resume-wait effect (see _launch_bass()).

		Mirrors _play_tuner_clip() exactly, just for the separate
		casette.mp3 clip and its own cached duration
		(_CASETTE_LENGTH_SECONDS), so the two effects don't share - or
		fight over - the same "discovered length" cache.
		"""
		global _CASETTE_LENGTH_SECONDS
		start = 0.0
		if _CASETTE_LENGTH_SECONDS and _CASETTE_LENGTH_SECONDS > 1.0:
			start = random.uniform(0.0, max(0.0, _CASETTE_LENGTH_SECONDS - 1.0))
		ok = engine.play_timeshift_file(_CASETTE_MP3_PATH, self._volume / 100.0, start_seconds=start)
		if ok and not _CASETTE_LENGTH_SECONDS:
			try:
				_pos, length = engine.timeshift_status()
				if length > 0:
					_CASETTE_LENGTH_SECONDS = length
			except Exception:
				pass
		return ok

	def _abort_tuning_transition(self):
		"""Immediately stop any in-progress tuning-effect engine and its
		loop-watcher thread. Must be called from a context where it is safe
		to unload a _BassEngine."""
		stop_evt = self._tuning_stop
		self._tuning_stop = None
		if stop_evt:
			stop_evt.set()
		engine = self._tuning_engine
		self._tuning_engine = None
		if engine:
			try:
				engine.stop()
				engine.unload()
			except Exception:
				pass

	def _tuning_loop_watcher(self, engine, stop_evt, gen, clip_fn=None):
		"""While a tuning/resume-wait effect is in progress, replay its clip
		from the start whenever it reaches its end, so the effect keeps
		playing for as long as the new station/episode takes to connect.

		*clip_fn* is a callable(engine) -> bool that (re)starts the clip;
		defaults to _play_tuner_clip() for the station tuning transition.
		The podcast/audio book resume-wait path (_launch_bass()) passes
		_play_casette_clip instead, so the same watcher loop is reused for
		both effects without either one hearing the other's clip."""
		if clip_fn is None:
			clip_fn = self._play_tuner_clip
		while not stop_evt.is_set() and self._play_gen == gen:
			time.sleep(_TUNER_POLL_INTERVAL)
			if stop_evt.is_set() or self._play_gen != gen:
				return
			try:
				pos, length = engine.timeshift_status()
			except Exception:
				return
			if length > 0 and pos >= length - 0.15:
				if stop_evt.is_set() or self._play_gen != gen:
					return
				try:
					clip_fn(engine)
				except Exception:
					return

	def play(self, url, name="", url_resolved=None, station=None):
		with self._play_lock:
			# Save the resume position of whatever podcast is currently
			# playing before we switch away from it - _current_station is
			# about to be overwritten below.
			if self._is_playing:
				try:
					self._save_current_podcast_position_if_playing()
				except Exception:
					pass

			# Bump generation — any in-flight _bg_launch with an older gen will
			# notice the mismatch and abort before starting audio output.
			self._play_gen += 1
			my_gen = self._play_gen

			# --- Crossfade logic (BASS backend only) ---
			# If a stream is currently playing on BASS and crossfade is enabled,
			# keep the old engine alive as a temporary fade-out engine and spin up
			# a brand-new _BassEngine for the new station.  The old engine will
			# continue playing until the new stream is confirmed started, then it
			# is gradually faded to silence in a background thread.
			xfade_engine = None
			tuner_engine = None
			do_crossfade = (
				self._crossfade_duration > 0.0
				and not self._tuning_effect_enabled
				and self._backend == self.BACKEND_BASS
				and self._bass_engine is not None
				and self._bass_engine.ready()
				and self._is_playing
			)
			do_tuning = (
				not do_crossfade
				and self._tuning_effect_enabled
				and self._backend == self.BACKEND_BASS
				and self._bass_engine is not None
				and self._bass_engine.ready()
				and self._is_playing
			)

			if do_crossfade:
				# Abort any previous (still running) fade-out/tuning first.
				self._abort_crossfade()
				self._abort_tuning_transition()

				# Save old engine — it keeps playing untouched.
				xfade_engine = self._bass_engine

				# Create a fresh engine for the new station.
				# load() is called in the background thread (blocking I/O outside lock).
				dll_dir = os.path.dirname(os.path.abspath(__file__))
				self._bass_engine = _BassEngine(dll_dir, output_device=self._output_device_index)
				# backend is NONE until _launch_bass() succeeds below.
				self._backend = self.BACKEND_NONE
			elif do_tuning:
				# Abort any previous (still running) fade-out/tuning first.
				self._abort_crossfade()
				self._abort_tuning_transition()

				# Old engine switches over to the tuning sound effect right
				# away, instead of continuing to play the old station. If
				# we're switching INTO a podcast/audio book (Enter on an
				# episode/chapter, not the pause/resume path - that one
				# skips do_tuning entirely because _is_playing is already
				# False by then), use the casette.mp3 resume-wait clip here
				# too instead of the station-tuning tuner.mp3, so Enter and
				# pause/resume sound consistent. See _play_casette_clip()
				# and the matching resume-wait logic in _launch_bass().
				target_is_podcast = _is_seekable_media(station)
				transition_clip_fn = self._play_casette_clip if target_is_podcast else self._play_tuner_clip

				tuner_engine = self._bass_engine
				try:
					transition_clip_fn(tuner_engine)
				except Exception:
					pass

				stop_evt = threading.Event()
				self._tuning_stop   = stop_evt
				self._tuning_engine = tuner_engine
				threading.Thread(
					target=self._tuning_loop_watcher,
					args=(tuner_engine, stop_evt, my_gen),
					kwargs={"clip_fn": transition_clip_fn},
					daemon=True, name="freeAudio-tuning-loop"
				).start()

				# Create a fresh engine for the new station — it connects in
				# the background while the tuning effect is heard.
				dll_dir = os.path.dirname(os.path.abspath(__file__))
				self._bass_engine = _BassEngine(dll_dir, output_device=self._output_device_index)
				self._backend = self.BACKEND_NONE
			else:
				# Normal path: stop whatever is currently playing.
				self._abort_crossfade()
				self._abort_tuning_transition()
				self._stop_current()

			self._stop_icy_thread()

			self._current_url		  = url
			self._current_url_resolved = url_resolved or url
			self._current_name		 = name
			self._current_station	  = station or {}
			self._intentional_stop	 = False
			self._is_playing		   = True

			vol		= self._volume
			stream_url = url_resolved or url

		def _bg_launch(gen=my_gen, xfade=xfade_engine, tuner=tuner_engine):
			# Each blocking step is guarded: if a newer play() arrived while we
			# were busy, our generation is stale — bail out immediately.
			if self._play_gen != gen:
				if xfade:
					try:
						xfade.stop()
						xfade.unload()
					except Exception:
						pass
				if tuner:
					self._abort_tuning_transition()
				return

			# A fresh launch (new station, reconnect, or crossfade) always
			# starts in live mode. Reset any stale time-shift state from a
			# previous station now, before anything else - otherwise a
			# leftover "active" flag would cause the next rewind/forward
			# press to try to seek within the (unseekable) live URL stream
			# instead of correctly starting a new time-shift session.
			if self._timeshift_active:
				self._timeshift_active = False
				try:
					self._timeshift_buffer.exit_playback()
				except Exception:
					pass

			# If crossfade or tuning mode: load the brand-new engine now (blocking).
			if xfade is not None or tuner is not None:
				loaded = self._bass_engine.load()
				if not loaded or not self._bass_engine.ready():
					# New engine failed to initialise — restore old engine and
					# fall back to a regular (non-crossfade/non-tuning) launch.
					log.warning("freeAudio: crossfade/tuning engine failed to load, falling back.")
					try:
						self._bass_engine.unload()
					except Exception:
						pass
					self._bass_engine = xfade if xfade is not None else tuner
					xfade = None
					if tuner is not None:
						# Reusing the tuner engine as the live engine now —
						# just stop its loop-watcher and clear tracking,
						# without stopping/unloading the engine itself (that
						# happens via self._bass_engine.stop() just below).
						stop_evt = self._tuning_stop
						self._tuning_stop = None
						if stop_evt:
							stop_evt.set()
						self._tuning_engine = None
						tuner = None
					try:
						self._bass_engine.stop()
					except Exception:
						pass
				else:
					self._bass_engine.on_meta	   = self._on_bass_meta
					self._bass_engine.on_connecting  = self._on_bass_connecting
					self._bass_engine.on_stall	   = self._on_bass_stall

				if self._play_gen != gen:
					if xfade:
						try:
							xfade.stop()
							xfade.unload()
						except Exception:
							pass
					if tuner:
						self._abort_tuning_transition()
					return

			# Route confirmed short-segment HLS (.m3u8) stations through
			# the merger so BASS gets one continuous stream instead of
			# draining its buffer at every segment boundary. See
			# _should_hls_merge()/_HlsStreamMerger's docstring.
			#
			# The mirror output deliberately keeps using the original
			# stream_url: the merger serves a single client, the mirror
			# is a second, independent subprocess.
			launch_url = stream_url
			if stream_url.lower().split("?")[0].endswith(".m3u8") and self._should_hls_merge(stream_url):
				try:
					if self._hls_merger is None:
						self._hls_merger = _HlsStreamMerger()
					merger_url = self._hls_merger.start(stream_url)
				except Exception:
					merger_url = None
				if merger_url:
					log.warning("freeAudio: routing HLS stream through built-in merger (short segments): %s",
								merger_url)
					launch_url = merger_url
				else:
					log.warning("freeAudio: HLS merger failed to start, using original URL")
			else:
				# Not merged (not HLS, or _should_hls_merge() said no) -
				# stop any merger left over from a previous station so it
				# doesn't keep running/downloading unused.
				if self._hls_merger is not None:
					try:
						self._hls_merger.stop()
					except Exception:
						pass

			# If a mirror output is active, kick off its (re)connect on a
			# separate thread at the same time as the main stream below,
			# instead of waiting for the main connect to finish first.
			# Each connect is a separate network round-trip through its own
			# bass_host subprocess, so starting them together — rather than
			# one after the other — keeps the two outputs much closer to
			# in sync instead of the mirror trailing behind by however long
			# the main connect took.
			mirror_thread = None
			mirror = getattr(self, "_mirror_engine", None)
			mirror_dev = getattr(self, "_mirror_device_index", None)
			if mirror is not None and mirror_dev is not None:
				station = self._current_station
				is_podcast = _is_seekable_media(station)
				saved_pos = 0.0
				if is_podcast:
					saved_pos = self.get_podcast_position(self._podcast_position_key(station))
				rate = self._playback_rate

				def _sync_mirror(m=mirror, u=stream_url, v=vol, g=gen,
								  podcast=is_podcast, pos=saved_pos, r=rate):
					if self._play_gen != g:
						return
					try:
						m.stop()
						# Podcasts/audio books must open seekable, same as
						# the main engine, or the resume-position and
						# rewind/forward seeks below silently no-op on
						# the mirror.
						m.play(u, v / 100.0, seekable=podcast)
					except Exception:
						return
					if self._play_gen != g:
						return
					if podcast and r != 1.0:
						try:
							m.set_playback_rate(r)
						except Exception:
							pass
					if podcast and pos > 1.0:
						self._resume_podcast_position_on_engine(m, pos)

				mirror_thread = threading.Thread(
					target=_sync_mirror, daemon=True,
					name="freeAudio-mirror-sync")
				mirror_thread.start()

			try:
				self._launch(launch_url, vol, gen=gen)
			except Exception:
				if self._play_gen == gen:
					self._is_playing = False
				if xfade:
					try:
						xfade.stop()
						xfade.unload()
					except Exception:
						pass
				if tuner:
					self._abort_tuning_transition()
				return

			if self._play_gen != gen:
				# A newer play() started while _launch was running; it has
				# already called _stop_current(), so just exit.
				if xfade:
					try:
						xfade.stop()
						xfade.unload()
					except Exception:
						pass
				if tuner:
					self._abort_tuning_transition()
				return

			# _launch() doesn't raise on a failed BASS connection - it just
			# returns quietly without ever setting self._backend to
			# BACKEND_BASS (see _launch()/_launch_bass()). Left unchecked,
			# self._is_playing (already set True back in play(), before
			# this background launch even started - see play()) would stay
			# True forever with nothing actually playing: no audio, no
			# error, and time-shift/rewind only ever reporting the generic
			# "not available for the current playback backend" message
			# with no indication why BASS never started in the first
			# place. Treat this exactly like the exception branch above.
			if self._backend != self.BACKEND_BASS:
				reason = getattr(self._bass_engine, "last_play_error", None) or "unknown reason"
				log.warning("freeAudio: BASS connection failed for %s, giving up (%s)", launch_url, reason)
				self._is_playing = False
				if xfade:
					try:
						xfade.stop()
						xfade.unload()
					except Exception:
						pass
				if tuner:
					self._abort_tuning_transition()
				cb = self.on_play_failed
				if cb:
					try:
						cb(self._current_station, launch_url, reason)
					except Exception:
						pass
				return

			# New stream is confirmed playing — for the tuning effect this is
			# an instant hard cut (not a fade): stop the tuner sound right away.
			if tuner:
				self._abort_tuning_transition()

			# New stream is confirmed playing — begin fade-out of the old engine.
			if xfade:
				self._crossfade_engine = xfade
				xfade_vol = vol / 100.0

				def _fade_out(engine=xfade, start_vol=xfade_vol):
					duration = self._crossfade_duration
					steps	= max(10, int(duration * 20))  # ~50 ms per step
					interval = duration / steps
					for i in range(steps):
						# Stop early if a newer crossfade has already taken over.
						if self._crossfade_engine is not engine:
							break
						frac = 1.0 - (i + 1) / steps
						try:
							engine.set_volume(frac * start_vol)
						except Exception:
							break
						time.sleep(interval)
					# Clean up — only if still ours.
					if self._crossfade_engine is engine:
						self._crossfade_engine = None
					try:
						engine.stop()
						engine.unload()
					except Exception:
						pass

				threading.Thread(
					target=_fade_out, daemon=True, name="freeAudio-fadeout"
				).start()

			if self._backend != self.BACKEND_BASS:
				self._start_icy_thread(stream_url)

			# Time-shift buffer: restart capture for the new station. Always
			# running on the BASS backend now (see _LIGHT_BUFFER_SECONDS above)
			# so recognition/recording have an already-open connection to tail
			# instead of opening their own; capacity is only smaller when the
			# user-facing rewind feature itself is off. Only supported on the
			# BASS backend.
			#
			# IMPORTANT: the previous station's capture session is always
			# torn down first, unconditionally - even if resolving/starting
			# the new one fails or the new stream is unsupported (HLS).
			# Otherwise a stale buffer from the *previous* station would
			# keep capturing in the background and could get played back
			# by rewind, even though a different station is now selected.
			if self._backend == self.BACKEND_BASS:
				with self._timeshift_launch_lock:
					# Re-check under the lock, not just before it: another
					# thread (e.g. set_timeshift_enabled's own capture-start,
					# or a stall reconnect) may have been holding the lock
					# for a newer generation while we were waiting for it.
					# If so, our station has already been superseded - bail
					# out without touching the buffer so we can't clobber
					# the newer, correct capture session.
					if self._play_gen == gen:
						is_podcast = _is_seekable_media(self._current_station)
						# HLS streams are excluded from capture for the same
						# two reasons podcast-like media is (see the comment
						# just below): (1) opening a second connection to
						# the same HLS origin from the always-on capture
						# buffer can make the origin throttle or briefly
						# stall one of the two, which BASS hears as a
						# dropout, and (2) the rewind feature can't usefully
						# seek in an HLS stream anyway (see
						# rewind_timeshift's "hls_unsupported" return), so
						# there is nothing this buffer would be providing.
						# The URL-shape check is intentionally identical to
						# the one used at launch time above, so the two can
						# never disagree about what counts as HLS.
						is_hls_stream = stream_url.lower().split("?")[0].endswith(".m3u8")
						if is_podcast or is_hls_stream:
							# Podcasts and GETEM audio books are on-demand,
							# already-seekable files (via seek_relative()/
							# timeshift_seek() directly on the BASS engine -
							# see script_timeshiftRewind's podcast branch),
							# not a live ad-inserted stream - none of the
							# reasons this buffer exists for live radio
							# (a rewind window, letting recognition/recording
							# tail an already-open connection past a
							# per-connection ad) apply to them. Capturing one
							# anyway was ballooning the .buf file far past
							# CAPACITY_SECONDS for file-based streams - just
							# stop whatever capture was left running from a
							# previous (live) station instead of starting or
							# keeping one for this one.
							try:
								self._timeshift_buffer.stop()
							except Exception:
								pass
							self._timeshift_buffer_gen = None
						else:
							self._timeshift_buffer.CAPACITY_SECONDS = (
								self._timeshift_capacity_seconds if self._timeshift_enabled else _LIGHT_BUFFER_SECONDS
							)
							# Only non-HLS reaches here now (see the
							# is_hls_stream check above), so the URL is
							# resolved the normal way. HLS master playlists
							# are not simple "one line = one audio URL"
							# playlists anyway - resolving them the way
							# _resolve_playlist_url() resolves .pls/.m3u
							# files could pick the wrong sub-stream.
							capture_url = _resolve_playlist_url(stream_url)

							# If the buffer is already actively capturing this exact
							# URL, this _bg_launch is a *reconnect* of the same
							# station - e.g. resume() falling back to a full relaunch
							# after a long pause, not the user picking a different
							# station. Tearing the capture down and restarting it
							# here would throw away a connection that has already
							# played past whatever per-connection ad the station
							# serves brand-new listeners; a fresh start() would just
							# get served that ad again, reintroducing the exact bug
							# this buffer exists to avoid for recognition/recording.
							# Only stop()+start() when the station actually changed.
							if self._timeshift_buffer.is_active() and self._timeshift_buffer.get_url() == capture_url:
								log.info("freeAudio TimeShift: reusing existing capture for %s (same station, "
										  "not a switch)", capture_url)
							else:
								try:
									self._timeshift_buffer.stop()
								except Exception:
									pass
								try:
									log.info("freeAudio TimeShift: starting capture for %s (resolved from %s)",
											  capture_url, stream_url)
									self._timeshift_buffer.start(capture_url)
								except Exception as e:
									log.info("freeAudio TimeShift: could not start capture: %s", e, exc_info=True)
							# Whether reused or freshly started, this buffer instance
							# now genuinely belongs to *this* launch's station.
							self._timeshift_buffer_gen = gen

			# The mirror (re)connect was already started concurrently above;
			# just make sure it has finished before this launch is done.
			if mirror_thread is not None:
				mirror_thread.join(timeout=30.0)

		threading.Thread(target=_bg_launch, daemon=True, name="freeAudio-launch").start()

	def pause(self):
		with self._play_lock:
			if not self._is_playing:
				return
			station = self._current_station
			try:
				self._save_current_podcast_position_if_playing()
			except Exception:
				pass
			self._play_gen += 1
			self._intentional_stop = True
			self._paused_at = time.time()
			if self._bass_engine:
				self._bass_engine.pause()
			self._is_playing = False
		# Also pause Mirror
		mirror = getattr(self, "_mirror_engine", None)
		if mirror and mirror.ready():
			try:
				mirror.pause()
			except Exception:
				pass
		if _is_seekable_media(station):
			cb = self.on_podcast_progress_saved
			if cb:
				try:
					cb(self._podcast_position_key(station))
				except Exception:
					pass

	def resume(self):
		_BASS_RESUME_THRESHOLD = 10  # seconds — reconnect if this time has passed

		with self._play_lock:
			if self._is_playing or not self._current_url:
				return
			self._play_gen += 1
			my_gen = self._play_gen
			self._intentional_stop = False
			self._is_playing = True

			paused_duration = time.time() - getattr(self, "_paused_at", 0)

			# Podcasts always take the reconnect-and-seek path below, never
			# the quick in-place BASS resume. The in-place resume trusts the
			# BASS host to keep its own position on a paused, still-
			# downloading network stream, which is not reliable for
			# podcasts in practice - it can come back at (or near) 0
			# instead of where playback was paused. The reconnect path is
			# the same one a fresh play() uses, seeking to the position
			# saved in podcast_positions.json (updated right before pause),
			# so it is the one path proven to land at the right spot.
			station = self._current_station
			is_podcast = _is_seekable_media(station)

			if (
				not is_podcast
				and self._backend == self.BACKEND_BASS
				and self._bass_engine
				and paused_duration <= _BASS_RESUME_THRESHOLD
			):
				self._bass_engine.resume()
				# Wake up Mirror with a short resume
				mirror = getattr(self, "_mirror_engine", None)
				if mirror and mirror.ready():
					try:
						mirror.resume()
					except Exception:
						pass
				# The time-shift capture connection was never touched by
				# pause() (it keeps recording the live edge the whole
				# time - see timeshift.py's design notes), so the buffer
				# itself is still valid for this station. Only _play_gen
				# advanced here (twice: once on pause(), once here) -
				# sync _timeshift_buffer_gen to match so rewind_timeshift()
				# doesn't mistake this still-good buffer for a stale one
				# left over from a station switch and refuse to rewind.
				self._timeshift_buffer_gen = my_gen
				return

			if self._backend == self.BACKEND_BASS and self._bass_engine:
				# Long pause (or a podcast, which always lands here) —
				# restart BASS. This always reconnects to the *live* URL
				# below (see _bg_resume), never back into time-shifted
				# playback, so any active time-shift session must be torn
				# down here - the same reset _bg_launch does on every fresh
				# launch. Skipping this (as before) left _timeshift_active
				# stuck True while BASS was actually playing the live
				# stream again: rewind/forward would then call
				# timeshift_seek() against a plain live stream that
				# was never opened via play_timeshift_file(), which does
				# nothing, making navigation silently stop working until
				# the buffer was toggled off/on or the station changed. It
				# also left _suspend_trim permanently incremented (its
				# matching exit_playback() was never called), which quietly
				# let the capture file grow past its capacity forever.
				if self._timeshift_active:
					self._timeshift_active = False
					try:
						self._timeshift_buffer.exit_playback()
					except Exception:
						pass
				self._bass_engine.stop()
				self._backend = self.BACKEND_NONE

			vol = self._volume
			stream_url = self._current_url_resolved or self._current_url

		def _bg_resume(gen=my_gen):
			if self._play_gen != gen:
				return

			# Restart the mirror concurrently with the main stream below,
			# instead of after it finishes, so both outputs reconnect at
			# roughly the same moment after a long pause.
			mirror_thread = None
			mirror = getattr(self, "_mirror_engine", None)
			if mirror and mirror.ready():
				station = self._current_station
				podcast = _is_seekable_media(station)
				pos = self.get_podcast_position(self._podcast_position_key(station)) if podcast else 0.0
				rate = self._playback_rate

				def _sync_mirror(m=mirror, u=stream_url, v=vol, g=gen,
								  podcast=podcast, pos=pos, r=rate):
					if self._play_gen != g:
						return
					try:
						m.stop()
						# Podcasts/audio books must reopen seekable, same
						# as the main engine, or the resume-position and
						# rewind/forward seeks below silently no-op on
						# the mirror.
						m.play(u, v / 100.0, seekable=podcast)
					except Exception:
						return
					if self._play_gen != g:
						return
					if podcast and r != 1.0:
						try:
							m.set_playback_rate(r)
						except Exception:
							pass
					if podcast and pos > 1.0:
						self._resume_podcast_position_on_engine(m, pos)

				mirror_thread = threading.Thread(
					target=_sync_mirror, daemon=True,
					name="freeAudio-mirror-sync")
				mirror_thread.start()

			try:
				self._launch(stream_url, vol, gen=gen)
			except Exception:
				if self._play_gen == gen:
					self._is_playing = False
				if mirror_thread is not None:
					mirror_thread.join(timeout=30.0)
				return
			if self._play_gen != gen:
				if mirror_thread is not None:
					mirror_thread.join(timeout=30.0)
				return
			if self._backend != self.BACKEND_BASS:
				self._start_icy_thread(stream_url)
			elif self._timeshift_buffer_gen is not None:
				# Same reasoning as the short-pause path above: this is a
				# reconnect of the SAME station after a long pause, not a
				# station switch, so the capture buffer was never stopped or
				# restarted and is still valid - only re-sync the generation
				# counter so rewind_timeshift() doesn't treat it as stale.
				self._timeshift_buffer_gen = gen
			if mirror_thread is not None:
				mirror_thread.join(timeout=30.0)

		threading.Thread(target=_bg_resume, daemon=True, name="freeAudio-resume").start()

	def stop(self, keep_mirror=False):
		"""Stop the current stream. *keep_mirror*, if True, leaves the
		Audio Mirror output (self._mirror_engine/_mirror_device_index)
		untouched instead of tearing it down - used only by
		_on_bass_stall()'s "track finished on its own" handling, never by
		a real user-requested stop.

		Why: for a jukebox folder track or audio-book chapter,
		self.on_podcast_finished (wired to
		GlobalPlugin._on_podcast_finished in __init__.py) only ever does
		wx.CallAfter(self._on_podcast_finished_ui, station) - it returns
		immediately, and the actual advance-to-the-next-track/chapter
		play() call happens later, once wx's event loop gets around to
		running that queued callback. So by the time _on_bass_stall()
		reaches this call, that next play() has *not* run yet - it's not
		a fuzzy race, this stop() is *guaranteed* to run first. With the
		old unconditional stop_mirror() here, self._mirror_engine was
		already None by the time the deferred play() finally ran, so its
		own mirror-resync (in _bg_launch - see start_mirror()'s
		docstring) had nothing to resync and Audio Mirror silently never
		came back on every jukebox/audio-book auto-advance, even though
		the main output kept playing fine (a fresh play() doesn't depend
		on anything this stop() clears).
		With keep_mirror=True, the mirror engine reference survives: if a
		next track *does* follow, that play()'s own resync logic picks it
		up exactly as it would for a manual track change. If nothing
		follows (last track in the sequence), the mirror's own stream was
		mirroring the exact same source that just ended, so it simply
		runs out of audio and goes quiet on its own - functionally
		silence either way, but correctly ready to resync the next time
		anything is played, without the user needing to manually toggle
		Audio Mirror off and back on."""
		with self._play_lock:
			if self._is_playing:
				try:
					self._save_current_podcast_position_if_playing()
				except Exception:
					pass
			self._play_gen += 1
			self._intentional_stop = True
			self._stop_icy_thread()
			self._abort_crossfade()
			self._abort_tuning_transition()

			if self._bass_engine:
				self._bass_engine.stop()

			self._current_url = None
			self._current_name = ""
			self._current_station = {}
			self._is_playing = False
			self._backend = self.BACKEND_NONE

		# Also stop Mirror (except lock - no risk of deadlock)
		if not keep_mirror:
			self.stop_mirror()

		# Stop time-shift capture (outside lock — no risk of deadlock).
		# This always runs now regardless of the rewind toggle - see
		# _LIGHT_BUFFER_SECONDS above.
		try:
			self._timeshift_buffer.stop()
		except Exception:
			pass
		self._timeshift_active = False

		# Stop the local HLS merger, if one was started for this stream.
		# A subsequent play() of an HLS URL will lazily recreate it. This
		# is deliberately done outside the lock and after everything else,
		# so a merger shutdown can never block or interfere with the
		# playback state changes above.
		if self._hls_merger is not None:
			try:
				self._hls_merger.stop()
			except Exception:
				pass

	def set_volume(self, volume):
		with self._play_lock:
			# Allow amplification beyond 100 % up to 200 % (maps to 0.0–2.0 in BASS).
			self._volume = max(0, min(200, int(volume)))
			# Sync mirror volume too
			mirror = getattr(self, "_mirror_engine", None)
			if mirror and mirror.ready():
				try:
					mirror.set_volume(self._volume / 100.0)
				except Exception:
					pass
			if not self._is_playing:
				return

			if self._backend == self.BACKEND_BASS and self._bass_engine:
				self._bass_engine.set_volume(self._volume / 100.0)
				return

	def set_bass_boost(self, boost_0_1):
		"""Adjust the bass boost level.

		boost_0_1: 0.0 = off, 1.0 = maximum (+12 dB low-shelf ~150 Hz).
		"""
		self._bass_boost = max(0.0, min(1.0, float(boost_0_1)))
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			try:
				self._bass_engine.set_bass_boost(self._bass_boost)
			except Exception:
				pass

	_PLAYBACK_RATE_STEP = 0.1
	_PLAYBACK_RATE_MIN  = 0.5
	_PLAYBACK_RATE_MAX  = 2.0

	def _step_playback_rate(self, delta):
		"""Increase/decrease the pitch-preserving podcast playback rate by
		*delta* (rounded to 1 decimal place so repeated steps land cleanly
		on 0.9/1.0/1.1 etc. instead of drifting from float addition).

		Returns (applied, actual_rate, reason): see set_playback_rate_value().
		"""
		return self.set_playback_rate_value(self._playback_rate + delta)

	def set_playback_rate_value(self, rate):
		"""Set the pitch-preserving podcast playback rate to an absolute
		value - the counterpart to _step_playback_rate()'s delta-based
		stepping, used to apply a saved per-feed/per-book playback speed
		(see PodcastFeed.audio_profile / GetemBook.audio_profile and
		playbackCoreMixin._play_station()) the moment an episode/chapter
		from it starts playing, rather than nudging up from whatever rate
		happened to be in effect already.

		Returns (applied, actual_rate, reason):
		- applied=True  -> the rate is actually in effect right now.
		- applied=False -> not currently possible (wrong backend, bass_fx.dll
		  not installed, or the current stream isn't tempo-wrapped e.g. a
		  live station or a podcast episode that fell back to a plain
		  stream) - the requested rate is still remembered and will apply
		  automatically to the next tempo-capable stream that opens.
		"""
		new_rate = round(float(rate), 1)
		new_rate = max(self._PLAYBACK_RATE_MIN, min(self._PLAYBACK_RATE_MAX, new_rate))
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			try:
				applied, actual_rate, reason = self._bass_engine.set_playback_rate(new_rate)
			except Exception:
				applied, actual_rate, reason = False, new_rate, "engine_error"
			self._playback_rate = actual_rate if applied else new_rate
			if applied:
				self._sync_mirror_playback_rate(self._playback_rate)
			return applied, self._playback_rate, reason
		self._playback_rate = new_rate
		return False, new_rate, "wrong_backend"

	def increase_playback_rate(self):
		return self._step_playback_rate(self._PLAYBACK_RATE_STEP)

	def decrease_playback_rate(self):
		return self._step_playback_rate(-self._PLAYBACK_RATE_STEP)

	def get_playback_rate(self):
		return self._playback_rate

	_TRANSPOSE_STEP = 0.25  # one eighth of a whole tone (a whole tone = 2 semitones)
	_TRANSPOSE_MIN  = -12.0
	_TRANSPOSE_MAX  = 12.0

	def _step_transpose(self, delta):
		"""Raise/lower the pitch transpose by *delta* semitones (rounded to
		2 decimal places so repeated 0.25 steps land cleanly instead of
		drifting from float addition). Returns (applied, actual_semitones,
		reason): see set_transpose_value()."""
		return self.set_transpose_value(self._transpose + delta)

	def set_transpose_value(self, semitones):
		"""Set the pitch transpose to an absolute value in semitones,
		independent of playback speed - the counterpart to
		_step_transpose()'s delta-based stepping, used to restore a saved
		per-feed/per-book transpose the moment a track starts playing.

		Returns (applied, actual_semitones, reason):
		- applied=True  -> the shift is actually in effect right now.
		- applied=False -> not currently possible (wrong backend, bass_fx.dll
		  not installed, or the current stream isn't tempo-wrapped, e.g. a
		  live station) - the requested value is still remembered and will
		  apply automatically to the next tempo-capable stream that opens.
		"""
		new_semitones = round(float(semitones), 2)
		new_semitones = max(self._TRANSPOSE_MIN, min(self._TRANSPOSE_MAX, new_semitones))
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			try:
				applied, actual, reason = self._bass_engine.set_transpose(new_semitones)
			except Exception:
				applied, actual, reason = False, new_semitones, "engine_error"
			self._transpose = actual if applied else new_semitones
			if applied:
				self._sync_mirror_transpose(self._transpose)
			return applied, self._transpose, reason
		self._transpose = new_semitones
		return False, new_semitones, "wrong_backend"

	def increase_transpose(self):
		return self._step_transpose(self._TRANSPOSE_STEP)

	def decrease_transpose(self):
		return self._step_transpose(-self._TRANSPOSE_STEP)

	def get_transpose(self):
		return self._transpose

	def get_bass_boost(self):
		return getattr(self, "_bass_boost", 0.0)

	def set_fx(self, fx_name):
		"""Adjust and save DirectX 8 effect.

		fx_name: "none" | "chorus" | "compressor" | "distortion" |
				 "echo" | "flanger" | "gargle" | "reverb" |
				 "eq_bass" | "eq_treble" | "eq_vocal"
		It only works on the BASS backend; is applied immediately to the active stream.
		"""
		self._audio_fx = fx_name or "none"
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			try:
				self._bass_engine.set_fx(self._audio_fx)
			except Exception:
				pass

	def set_eq_gain(self, band, gain_db):
		"""Set the ParamEQ gain for one EQ band in dB (-15..+15).

		band:	"eq_bass" | "eq_treble" | "eq_vocal"
		gain_db: dB value applied immediately; ignored unless BASS backend is active.
		"""
		# Store so it can be restored after reconnect / device switch
		if not hasattr(self, "_eq_gains"):
			self._eq_gains = {}
		self._eq_gains[band] = max(-15.0, min(15.0, float(gain_db)))
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			try:
				self._bass_engine.set_eq_gain(band, gain_db)
			except Exception:
				pass

	def get_eq_gain(self, band):
		"""Return the stored EQ gain for *band*, or the default if not set."""
		_defaults = {"eq_bass": 9.0, "eq_treble": 9.0, "eq_vocal": 6.0}
		return getattr(self, "_eq_gains", {}).get(band, _defaults.get(band, 9.0))

	def get_fx(self):
		return getattr(self, "_audio_fx", "none")

	def get_volume(self):
		return self._volume

	def seek_relative(self, seconds):
		"""Seek relative to current position (for file-based playback like podcasts).
		Only works with BASS backend. Returns (ok, new_position_seconds).
		"""
		if self._backend != self.BACKEND_BASS or not self._bass_engine:
			return False, 0.0
		try:
			ok, pos, length = self._bass_engine.timeshift_seek(seconds)
			if ok:
				station = self._current_station
				if _is_seekable_media(station):
					self._save_podcast_position_now(station, pos, length)
				self._sync_mirror_timeshift_seek(seconds)
			return ok, pos
		except Exception:
			return False, 0.0

	# -- Podcast resume position ---------------------------------------------

	def _get_podcast_positions_path(self):
		"""Path for podcast_positions.json directly under the NVDA user config directory."""
		try:
			import globalVars
			base_dir = globalVars.appArgs.configPath
		except Exception:
			# Fallback for standalone/test use outside NVDA.
			base_dir = os.path.dirname(os.path.abspath(__file__))

		return os.path.join(base_dir, "podcast_positions.json")

	def _load_podcast_positions(self):
		try:
			with open(self._podcast_positions_path, "r", encoding="utf-8") as fh:
				data = json.load(fh)
			if isinstance(data, dict):
				return data
		except FileNotFoundError:
			pass
		except Exception as e:
			log.error("freeAudio: failed to load podcast positions: %s", e)
		return {}

	def _write_podcast_positions(self):
		tmp_path = self._podcast_positions_path + ".tmp"
		try:
			with self._podcast_positions_lock:
				data = dict(self._podcast_positions)
			with open(tmp_path, "w", encoding="utf-8") as fh:
				json.dump(data, fh, ensure_ascii=False, indent=2)
			os.replace(tmp_path, self._podcast_positions_path)
		except Exception as e:
			log.error("freeAudio: failed to save podcast positions: %s", e)
			try:
				os.remove(tmp_path)
			except OSError:
				pass

	def get_podcast_position(self, url):
		"""Return the saved resume position (seconds) for *url*, or 0.0."""
		if not url:
			return 0.0
		with self._podcast_positions_lock:
			entry = self._podcast_positions.get(url)
		return float(entry.get("position", 0.0)) if entry else 0.0

	def clear_podcast_position(self, url):
		"""Remove the saved resume position for *url*, if any - used when
		the episode's podcast feed is unsubscribed
		(RadioDialog._on_podcast_remove()) or a GETEM audio book is removed
		from the library (RadioDialog._on_getem_remove_from_library()), so
		stale progress doesn't linger for content the user can no longer
		see or resume."""
		if not url:
			return
		with self._podcast_positions_lock:
			removed = self._podcast_positions.pop(url, None) is not None
		if removed:
			self._write_podcast_positions()

	def clear_podcast_positions(self, urls):
		"""Bulk version of clear_podcast_position() for a whole feed's worth
		of episode URLs, or a whole book's worth of chapter stream URLs, at
		once - a single disk write instead of one per URL."""
		if not urls:
			return
		changed = False
		with self._podcast_positions_lock:
			for url in urls:
				if url and self._podcast_positions.pop(url, None) is not None:
					changed = True
		if changed:
			self._write_podcast_positions()

	def _get_jukebox_folder_positions_path(self):
		"""Path for jukebox_folder_positions.json, next to podcast_positions.json
		under the NVDA user config directory."""
		try:
			import globalVars
			base_dir = globalVars.appArgs.configPath
		except Exception:
			base_dir = os.path.dirname(os.path.abspath(__file__))

		return os.path.join(base_dir, "jukebox_folder_positions.json")

	def _load_jukebox_folder_positions(self):
		try:
			with open(self._jukebox_folder_positions_path, "r", encoding="utf-8") as fh:
				data = json.load(fh)
			if isinstance(data, dict):
				return data
		except FileNotFoundError:
			pass
		except Exception as e:
			log.error("freeAudio: failed to load jukebox folder positions: %s", e)
		return {}

	def _write_jukebox_folder_positions(self):
		tmp_path = self._jukebox_folder_positions_path + ".tmp"
		try:
			with self._jukebox_folder_positions_lock:
				data = dict(self._jukebox_folder_positions)
			with open(tmp_path, "w", encoding="utf-8") as fh:
				json.dump(data, fh, ensure_ascii=False, indent=2)
			os.replace(tmp_path, self._jukebox_folder_positions_path)
		except Exception as e:
			log.error("freeAudio: failed to save jukebox folder positions: %s", e)
			try:
				os.remove(tmp_path)
			except OSError:
				pass

	def save_jukebox_folder_position(self, folder_path, track_index, track_path=""):
		"""Remember that *track_index* of *folder_path* was just played, so
		RadioDialog._on_jukebox_entry_play() can resume there next time
		instead of always starting the folder over from track 1. Called
		from playbackCoreMixin._play_station() for every track played as
		part of a folder sequence - both dialog-driven and the headless
		auto-advance in _advance_jukebox_folder_headless() - so the
		remembered track stays current even while the dialog is closed."""
		if not folder_path:
			return
		with self._jukebox_folder_positions_lock:
			self._jukebox_folder_positions[folder_path] = {
				"track_index": int(track_index),
				"track_path": track_path or "",
				"updated": time.strftime("%Y-%m-%dT%H:%M:%S"),
			}
		self._write_jukebox_folder_positions()

	def get_jukebox_folder_position(self, folder_path):
		"""Return (track_index, track_path) last saved for *folder_path*,
		or None if nothing's been played from it yet."""
		if not folder_path:
			return None
		with self._jukebox_folder_positions_lock:
			entry = self._jukebox_folder_positions.get(folder_path)
		if not entry:
			return None
		return int(entry.get("track_index", 0)), entry.get("track_path", "")

	def clear_jukebox_folder_position(self, folder_path):
		"""Remove the saved position for *folder_path* - used when the
		folder is played through to the end of its last track (so it
		starts over from track 1 next time rather than staying "stuck" on
		the last track forever), and when the folder is removed from the
		jukebox library (RadioDialog._on_jukebox_remove_entry())."""
		if not folder_path:
			return
		with self._jukebox_folder_positions_lock:
			removed = self._jukebox_folder_positions.pop(folder_path, None) is not None
		if removed:
			self._write_jukebox_folder_positions()

	def has_podcast_position_entry(self, url):
		"""Whether *url* has ever had a podcast resume position recorded.
		A reliable way to tell a podcast episode URL from a plain radio
		stream URL when tag info isn't available - e.g. resuming the last
		station on NVDA startup from a config saved before the
		"last_station_tags" field existed, where the reconstructed station
		dict has no "tags" to check."""
		if not url:
			return False
		with self._podcast_positions_lock:
			return url in self._podcast_positions

	def _save_current_podcast_position_if_playing(self):
		"""Query and persist the live playback position of the current
		station, if it's a podcast that's actually playing right now.
		Called before switching stations, on pause/stop, and on
		termination, so the resume point is never far behind."""
		station = self._current_station
		if not _is_seekable_media(station):
			return
		if self._backend != self.BACKEND_BASS or not self._bass_engine:
			return
		try:
			pos, length = self._bass_engine.timeshift_status()
		except Exception:
			return

		# If position returned 0.0 but stream was playing, check if it reached the end
		if pos <= 0.0 and length <= 0.0:
			return

		self._save_podcast_position_now(station, pos, length)

	def _save_podcast_position_now(self, station, position, length=0.0):
		"""Persist *position* for the given podcast station.
		If position is within 3 seconds of the end, mark as listened (position = -1)."""
		url = self._podcast_position_key(station)
		if not url:
			return

		is_finished = False
		if length > 0:
			if length - position <= 3.0:
				is_finished = True
		elif position == -1.0:
			is_finished = True

		with self._podcast_positions_lock:
			if is_finished:
				self._podcast_positions[url] = {
					"position": -1.0,
					"listened": True,
					"name": station.get("name", "").strip(),
					"updated": time.strftime("%Y-%m-%dT%H:%M:%S"),
				}
			else:
				self._podcast_positions[url] = {
					"position": round(float(position), 1),
					"listened": False,
					"name": station.get("name", "").strip(),
					"updated": time.strftime("%Y-%m-%dT%H:%M:%S"),
				}
		self._write_podcast_positions()

	def _podcast_autosave_loop(self):
		"""Periodically save the resume position of a playing podcast, so a
		crash or unexpected NVDA restart doesn't lose much progress.

		The dialog no longer shows a live-ticking elapsed/total duration on
		the episode list (that caused NVDA to re-announce the focused row
		every second), so this no longer refreshes the in-memory
		live-progress cache each tick - it only does the periodic disk save,
		every _AUTOSAVE_INTERVAL seconds."""
		_AUTOSAVE_INTERVAL = 15
		while not self._podcast_autosave_stop.is_set():
			if self._podcast_autosave_stop.wait(timeout=_AUTOSAVE_INTERVAL):
				return
			try:
				if self._is_playing:
					self._save_current_podcast_position_if_playing()
			except Exception:
				pass

	def get_playback_position(self):
		"""Return (ok, position_seconds, length_seconds) for whatever is
		currently open on the BASS backend (live station, timeshift buffer
		file, or a seekable podcast stream all share the same handle)."""
		if self._backend != self.BACKEND_BASS or not self._bass_engine:
			return False, 0.0, 0.0
		try:
			pos, length = self._bass_engine.timeshift_status()
		except Exception:
			return False, 0.0, 0.0
		if pos <= 0.0 and length <= 0.0:
			return False, 0.0, 0.0
		return True, pos, length

	def is_playing(self):
		return self._is_playing

	def has_media(self):
		return self._current_url is not None

	def get_current_name(self):
		return self._current_name

	def get_current_station(self):
		return self._current_station

	def get_backend(self):
		return self._backend

	# -- Time-shift (rewind / fast-forward live radio) -------------------
	#
	# Only supported on the BASS backend. The capture buffer (timeshift.py)
	# runs continuously in the background whenever the feature is enabled
	# and something is playing; entering/exiting time-shift mode only
	# switches which BASS stream (live URL vs. local buffer file) is
	# actually feeding the audio output - the capture itself is untouched,
	# so returning to live never loses buffered audio.

	def set_timeshift_capacity_seconds(self, seconds):
		"""Set how much rewind-buffer audio to retain once the time-shift
		feature is enabled (clamped to 10 minutes .. 5 hours). Takes effect
		immediately — including on a capture that's already running, no
		restart or reconnect needed — since the buffer just reads this
		value back on its next periodic trim check.
		"""
		try:
			seconds = int(seconds)
		except (TypeError, ValueError):
			seconds = 600
		seconds = max(600, min(seconds, 18000))
		self._timeshift_capacity_seconds = seconds
		if self._timeshift_enabled:
			self._timeshift_buffer.CAPACITY_SECONDS = seconds

	def set_timeshift_disk_full_callback(self, callback):
		"""Register a callback invoked (at most once per capture session)
		if the time-shift buffer can't keep writing because the disk is
		full. Purely informational — capture keeps running with whatever
		space is available, live playback is never affected."""
		self._timeshift_buffer._notify_disk_full = callback

	def set_timeshift_enabled(self, enabled):
		"""Enable or disable the time-shift buffer feature.

		Disabling immediately returns to live playback (if time-shifted)
		and stops capturing. Enabling while already playing starts
		capturing right away, without interrupting playback.
		"""
		self._timeshift_enabled = bool(enabled)
		if not self._timeshift_enabled:
			if self._timeshift_active:
				self.exit_timeshift_to_live()
			# NOTE: capture itself is deliberately NOT stopped here anymore -
			# recognition and recording tail this same connection to avoid
			# re-triggering per-session ad insertion on stations that serve
			# one to every brand-new connection. Just shrink the retention
			# window back down to the lightweight default; the existing
			# connection (and its "past the ad" position in the stream) is
			# left untouched.
			self._timeshift_buffer.CAPACITY_SECONDS = _LIGHT_BUFFER_SECONDS
		elif (
			self._is_playing
			and self._backend == self.BACKEND_BASS
			# Podcasts/GETEM audio books never get a capture started for
			# them in the first place (see _bg_launch above) - they're
			# already seekable files, so there's nothing here to widen the
			# retention window on.
			and not _is_seekable_media(self._current_station)
			# HLS live streams are also excluded - see the is_hls_stream
			# check in _bg_launch for the full rationale (two connections
			# to the same HLS origin, plus a buffer the rewind feature
			# can't seek in anyway).
			and not (
				(self._current_url_resolved or self._current_url or "")
				.lower().split("?")[0].endswith(".m3u8")
			)
		):
			self._timeshift_buffer.CAPACITY_SECONDS = self._timeshift_capacity_seconds
			stream_url = self._current_url_resolved or self._current_url
			captured_gen = self._play_gen
			if stream_url:
				def _bg_start_capture(url=stream_url, gen=captured_gen):
					# Share _timeshift_launch_lock with _bg_launch's own
					# stop/start/gen-assign sequence. Without this, a fast
					# station switch landing while this thread is still
					# resolving the *previous* station's URL could finish
					# its stop()/start() call after _bg_launch's, silently
					# overwriting the new (correct) capture session with a
					# stale one - after which the gen check below would
					# still (wrongly) look consistent from this thread's
					# point of view, leaving the buffer captured for the
					# wrong station indefinitely.
					with self._timeshift_launch_lock:
						if self._play_gen != gen:
							return
						resolved_for_capture = _resolve_playlist_url(url)
						# The light (45s) buffer is already running continuously
						# in the background for every playing station (see
						# _LIGHT_BUFFER_SECONDS above) - turning the rewind
						# feature on here just needs to widen its capacity to
						# 10 minutes, not open a brand-new connection. If it's
						# already capturing this exact URL, calling start()
						# anyway would (TimeShiftBuffer.start() always stops
						# itself first) throw away a connection that's already
						# past whatever per-connection ad the station serves
						# brand-new listeners, and get served a fresh one on
						# reconnect - the same bug _bg_launch's reuse guard
						# avoids for station switches/resumes.
						if self._timeshift_buffer.is_active() and self._timeshift_buffer.get_url() == resolved_for_capture:
							log.info("freeAudio TimeShift: reusing existing capture for %s (rewind enabled, "
									  "not a switch)", resolved_for_capture)
						else:
							try:
								log.info("freeAudio TimeShift: starting capture for %s (resolved from %s)",
										  resolved_for_capture, url)
								self._timeshift_buffer.start(resolved_for_capture)
							except Exception as e:
								log.info("freeAudio TimeShift: could not start capture: %s", e, exc_info=True)
						# Whether reused or freshly started, sync the buffer
						# generation the same way _bg_launch's own start()
						# does - otherwise a prior play_gen bump elsewhere (e.g. a
						# BASS stall reconnect) that never got mirrored into
						# _timeshift_buffer_gen would keep rewind_timeshift()
						# permanently refusing with "no_buffer_yet", and toggling
						# this setting off/on would never be able to fix it since
						# this was the one start-capture path that skipped the
						# sync. Only skip it if a newer play() has since
						# superseded this station.
						if self._play_gen == gen:
							self._timeshift_buffer_gen = gen
				threading.Thread(
					target=_bg_start_capture, daemon=True,
					name="freeAudio-TimeShiftResolve",
				).start()

	def is_timeshift_enabled(self):
		return self._timeshift_enabled

	def get_timeshift_buffer(self):
		"""Return the TimeShiftBuffer instance backing this player. Used by
		the recorder and music recognizer to tail the already-open capture
		connection instead of opening a fresh one."""
		return self._timeshift_buffer

	def get_timeshift_buffered_seconds(self):
		"""How many seconds of audio are currently available to rewind."""
		try:
			return self._timeshift_buffer.buffered_seconds()
		except Exception:
			return 0.0

	def is_timeshifted(self):
		"""True while time-shifted (buffered, seekable) playback is active,
		as opposed to normal live playback."""
		return self._timeshift_active

	def rewind_timeshift(self, seconds=15):
		"""Rewind by *seconds*.

		If not already time-shifted, this enters time-shift mode starting
		*seconds* before the live edge. Returns
		(ok, position_seconds, buffered_seconds, reason) where reason is a
		short code identifying why it failed ("ok" on success):
		"feature_disabled", "wrong_backend", "hls_unsupported",
		"no_buffer_yet", "no_buffer_file", "engine_error".
		"""
		if not self._timeshift_enabled:
			return False, 0.0, 0.0, "feature_disabled"
		if self._backend != self.BACKEND_BASS or not self._bass_engine:
			return False, 0.0, 0.0, "wrong_backend"
		if self._timeshift_buffer.is_hls_skipped():
			return False, 0.0, 0.0, "hls_unsupported"

		# The buffer object is reused across stations and only actually
		# torn down/restarted partway through _bg_launch - well after
		# _timeshift_active is reset for the new station. A rewind that
		# lands in that gap must not be allowed to treat the *previous*
		# station's still-open buffer file as ready.
		if self._timeshift_buffer_gen != self._play_gen:
			return False, 0.0, 0.0, "no_buffer_yet"

		buffered = self._timeshift_buffer.buffered_seconds()
		if buffered <= 0:
			return False, 0.0, 0.0, "no_buffer_yet"

		if not self._timeshift_active:
			path = self._timeshift_buffer.get_file_path()
			if not path:
				return False, 0.0, buffered, "no_buffer_file"
			start_pos = max(0.0, buffered - abs(seconds))
			vol = self._volume / 100.0
			self._timeshift_buffer.enter_playback()
			ok = self._bass_engine.play_timeshift_file(path, vol, start_pos)
			if not ok:
				self._timeshift_buffer.exit_playback()
				return False, 0.0, buffered, "engine_error"
			self._timeshift_active = True
			self._sync_mirror_timeshift_enter(path, start_pos)
			return True, start_pos, buffered, "ok"

		ok, position, _length = self._bass_engine.timeshift_seek(-abs(seconds))
		if ok:
			self._sync_mirror_timeshift_seek(-abs(seconds))
		return ok, position, buffered, ("ok" if ok else "engine_error")

	def forward_timeshift(self, seconds=15):
		"""Fast-forward by *seconds* while time-shifted.

		If this reaches the live edge, playback automatically returns to
		the live stream. Returns (ok, position_seconds_or_none, at_live_edge).
		"""
		if not self._timeshift_active or not self._bass_engine:
			return False, 0.0, False

		ok, position, length = self._bass_engine.timeshift_seek(abs(seconds))
		if not ok:
			# Once time-shifted, a forward seek can only fail because the
			# requested position is beyond what has actually been captured
			# so far - i.e. we're already at (or asking past) the live
			# edge. BASS_ChannelSetPosition usually errors out here rather
			# than landing close to the end, so the normal "within
			# _EDGE_MARGIN_SECONDS of length" check below never gets a
			# chance to fire. Treat the failure itself as having reached
			# live instead of surfacing a raw seek error to the user.
			self.exit_timeshift_to_live()
			return True, None, True

		self._sync_mirror_timeshift_seek(abs(seconds))

		_EDGE_MARGIN_SECONDS = 2.0
		if length - position <= _EDGE_MARGIN_SECONDS:
			self.exit_timeshift_to_live()
			return True, None, True

		return True, position, False

	def exit_timeshift_to_live(self):
		"""Return from time-shifted playback to the live stream immediately.
		Capture continues uninterrupted - only the playback source switches.
		"""
		if not self._timeshift_active:
			return
		self._timeshift_active = False
		self._timeshift_buffer.exit_playback()
		if self._backend == self.BACKEND_BASS and self._bass_engine:
			stream_url = self._current_url_resolved or self._current_url
			if stream_url:
				vol = self._volume / 100.0
				try:
					self._bass_engine.play(stream_url, vol)
				except Exception:
					pass
		self._sync_mirror_exit_to_live()

	# -- Mirror sync helpers for time-shift and playback rate ------------
	#
	# The mirror output is a second, independent bass_host subprocess (see
	# start_mirror()), so nothing that happens on the main engine reaches
	# it automatically. Without these, entering/seeking/exiting time-shift
	# or changing podcast playback speed would only ever affect the main
	# output, leaving the mirrored device stuck on live audio at normal
	# speed. Each helper is fire-and-forget on a background thread so a
	# slow mirror round-trip never delays the main output's response.

	def _get_ready_mirror(self):
		mirror = getattr(self, "_mirror_engine", None)
		if mirror is not None and mirror.ready():
			return mirror
		return None

	def _sync_mirror_timeshift_enter(self, path, start_pos):
		"""Open the same time-shift buffer file, at the same position, on
		the mirror engine right after the main engine enters time-shift."""
		mirror = self._get_ready_mirror()
		if mirror is None:
			return
		vol = self._volume / 100.0

		def _do(m=mirror, p=path, pos=start_pos, v=vol):
			try:
				m.play_timeshift_file(p, v, pos)
			except Exception:
				pass

		threading.Thread(target=_do, daemon=True, name="freeAudio-mirror-timeshift").start()

	def _sync_mirror_timeshift_seek(self, delta_seconds):
		"""Apply the same rewind/forward seek to the mirror engine's
		already-open time-shift file, so it tracks the main output."""
		mirror = self._get_ready_mirror()
		if mirror is None:
			return

		def _do(m=mirror, d=delta_seconds):
			try:
				m.timeshift_seek(d)
			except Exception:
				pass

		threading.Thread(target=_do, daemon=True, name="freeAudio-mirror-timeshift").start()

	def _sync_mirror_exit_to_live(self):
		"""Switch the mirror engine back to the live URL right after the
		main engine does, so it doesn't stay stuck on the time-shift file."""
		mirror = self._get_ready_mirror()
		if mirror is None:
			return
		stream_url = self._current_url_resolved or self._current_url
		if not stream_url:
			return
		vol = self._volume / 100.0

		def _do(m=mirror, u=stream_url, v=vol):
			try:
				m.play(u, v)
			except Exception:
				pass

		threading.Thread(target=_do, daemon=True, name="freeAudio-mirror-timeshift").start()

	def _sync_mirror_playback_rate(self, rate):
		"""Reapply a just-changed podcast playback rate on the mirror
		engine too, so both outputs stay at the same speed."""
		mirror = self._get_ready_mirror()
		if mirror is None:
			return

		def _do(m=mirror, r=rate):
			try:
				m.set_playback_rate(r)
			except Exception:
				pass

		threading.Thread(target=_do, daemon=True, name="freeAudio-mirror-rate").start()

	def _sync_mirror_transpose(self, semitones):
		"""Reapply a just-changed pitch transpose on the mirror engine too,
		so both outputs stay at the same pitch."""
		mirror = self._get_ready_mirror()
		if mirror is None:
			return

		def _do(m=mirror, s=semitones):
			try:
				m.set_transpose(s)
			except Exception:
				pass

		threading.Thread(target=_do, daemon=True, name="freeAudio-mirror-transpose").start()

	def get_audio_devices(self, fresh=None):
		"""Zwróć listę (indeks, nazwa) dostępnych urządzeń wyjściowych BASS.

		Gdy fresh=True, lista jest pobierana z krótkotrwałego procesu hosta
		BASS. To wymusza aktualne indeksy urządzeń po podłączeniu lub
		odłączeniu wyjścia audio bez restartu NVDA.
		"""
		if fresh is None:
			fresh = self.use_fresh_audio_device_probe()
		if fresh:
			dll_dir = os.path.dirname(os.path.abspath(__file__))
			probe_engine = _BassEngine(dll_dir, output_device=_BASS_DEVICE_DEFAULT)
			try:
				if probe_engine.load() and probe_engine.ready():
					devices = probe_engine.list_devices()
					if devices:
						return devices
			except Exception:
				pass
			finally:
				try:
					probe_engine.unload()
				except Exception:
					pass
		if self._bass_engine and self._bass_engine.ready():
			return self._bass_engine.list_devices()
		return []

	@staticmethod
	def _normalize_audio_device_name(name):
		return " ".join(str(name or "").split()).casefold()

	def resolve_audio_device(self, devices, saved_index=-1, saved_name=""):
		"""Dopasuj zapisane urządzenie do aktualnej listy BASS.

		Zwraca (indeks, nazwa, sposób), gdzie sposób to: "default",
		"name", "index" albo "missing".
		"""
		try:
			saved_index = int(saved_index)
		except Exception:
			saved_index = -1
		if saved_index == -1 and not saved_name:
			return -1, "", "default"

		wanted_name = self._normalize_audio_device_name(saved_name)
		if wanted_name:
			for idx, name in devices:
				if self._normalize_audio_device_name(name) == wanted_name:
					return idx, name, "name"

		for idx, name in devices:
			try:
				if int(idx) == saved_index:
					return idx, name, "index"
			except Exception:
				pass

		return saved_index, saved_name or "", "missing"

	def start_mirror(self, device_index, device_name=""):
		"""Start mirroring the current stream to an additional output device.
		Launches a second bass_host process on device_index and plays the
		same source the main output is already on, so switching on audio
		mirroring continues from where playback already was rather than
		starting over. Three cases:
		- Time-shifted live radio: the mirror opens the same time-shift
		  buffer file, seeked to the main output's current time-shift
		  position, instead of jumping to the live edge.
		- Podcasts: the mirror is opened seekable and seeked to the main
		  output's current position, same as before.
		- Live (non-time-shifted) radio: the mirror just opens the live URL.
		If a podcast playback-rate adjustment is active, it's reapplied on
		the mirror engine too - it's a brand-new subprocess (unlike the
		mirror-resync paths in _bg_launch/_bg_resume, which reuse the
		already-running mirror subprocess and so don't need this), so it
		would otherwise silently come up at normal speed. See the matching
		safety-net comment in _launch().
		*device_name*, if given, is used to re-resolve device_index against
		a freshly probed device list before opening it - BASS device
		indices can drift between when the picker dialog listed devices
		and when this runs, and unlike switch_output_device() (which goes
		through resolve_audio_device() for exactly this reason), a stale
		index here would silently open the wrong device rather than error,
		so mirroring would produce no audible sound with no obvious cause.
		Returns True on success, False otherwise.
		"""
		if not self._current_url:
			_mirror_debug_log(
				"start_mirror: no current_url, nothing to mirror (requested device=%r %r)"
				% (device_index, device_name)
			)
			return False
		self._teardown_mirror_engine()
		if device_name:
			try:
				fresh_devices = self.get_audio_devices(fresh=True)
				resolved_index, _resolved_name, match = self.resolve_audio_device(
					fresh_devices, device_index, device_name,
				)
				if match != "missing":
					device_index = resolved_index
			except Exception:
				pass
		_mirror_debug_log(
			"start_mirror: attempting device=%r (%r) resolved_from_name=%r url=%r station=%r"
			% (device_index, device_name, bool(device_name), self._current_url, self._current_station.get("name"))
		)
		dll_dir = os.path.dirname(os.path.abspath(__file__))
		mirror_engine = _BassEngine(dll_dir, output_device=device_index)
		if not mirror_engine.load():
			stderr_tail = mirror_engine.get_stderr_tail()
			log.warning(
				"freeAudio: mirror subprocess failed to load for device %r (%r): %s",
				device_index, device_name, stderr_tail,
			)
			_mirror_debug_log(
				"start_mirror: FAILED - mirror subprocess failed to load for device=%r (%r) stderr=%r"
				% (device_index, device_name, stderr_tail)
			)
			return False
		vol = self._volume / 100.0
		station = self._current_station
		is_podcast = _is_seekable_media(station)
		timeshifted = self._timeshift_active

		current_pos = 0.0
		if timeshifted:
			pos_ok, current_pos, _length = self.get_playback_position()
			if not pos_ok:
				current_pos = 0.0
			path = self._timeshift_buffer.get_file_path()
			ok = bool(path) and mirror_engine.play_timeshift_file(path, vol, current_pos)
		else:
			url = self._current_url_resolved or self._current_url
			if is_podcast:
				pos_ok, current_pos, _length = self.get_playback_position()
				if not pos_ok:
					current_pos = 0.0
			ok = mirror_engine.play(url, vol, seekable=is_podcast)

		time.sleep(1.0)
		if not ok:
			last_error = getattr(mirror_engine, "last_play_error", None)
			log.warning(
				"freeAudio: mirror play failed for device %r (%r): %s",
				device_index, device_name, last_error,
			)
			_mirror_debug_log(
				"start_mirror: FAILED - play() returned false for device=%r (%r) "
				"is_podcast=%r timeshifted=%r last_play_error=%r"
				% (device_index, device_name, is_podcast, timeshifted, last_error)
			)
			mirror_engine.unload()
			return False
		if is_podcast and self._playback_rate != 1.0:
			try:
				mirror_engine.set_playback_rate(self._playback_rate)
			except Exception:
				pass
		if is_podcast and self._transpose != 0.0:
			try:
				mirror_engine.set_transpose(self._transpose)
			except Exception:
				pass
		if not timeshifted and is_podcast and current_pos > 1.0:
			self._resume_podcast_position_on_engine(mirror_engine, current_pos)
		self._mirror_engine	   = mirror_engine
		self._mirror_device_index = device_index
		_mirror_debug_log(
			"start_mirror: SUCCESS - mirroring to device=%r (%r)" % (device_index, device_name)
		)
		return True

	def suspend_timeshift_for_mirror(self):
		"""Temporarily stop the time-shift buffer's capture connection to
		free up a connection slot for the mirror, for stations that reject
		more than N simultaneous connections from the same client - main
		playback + the always-on time-shift capture (see
		_LIGHT_BUFFER_SECONDS) is already 2, and some servers only allow
		2 total, so adding a 3rd for the mirror fails even though the
		mirror itself is otherwise fine. See
		audioDeviceMixin._do_mirror(), which calls this only as a retry
		after a first mirror attempt already failed, and only when
		nothing is recording - the capture connection is shared with
		recording (see get_timeshift_buffer()'s docstring), so stopping
		it here would cut off an in-progress recording too.
		Returns True if it stopped a running capture (so retrying the
		mirror is worth it), False if there was nothing to stop (the
		buffer wasn't active, so this wouldn't free anything and the
		mirror failure has some other cause).
		Call resume_timeshift_after_mirror() to restart it afterwards -
		stop_mirror() does this automatically.
		"""
		if not self._timeshift_buffer.is_active():
			_mirror_debug_log("suspend_timeshift_for_mirror: buffer wasn't active, nothing to free")
			return False
		self._timeshift_suspended_for_mirror = True
		self._timeshift_buffer.stop()
		_mirror_debug_log("suspend_timeshift_for_mirror: stopped active capture to free a connection slot")
		return True

	def resume_timeshift_after_mirror(self):
		"""Restart the time-shift buffer's capture, undoing
		suspend_timeshift_for_mirror() - called by stop_mirror() once the
		mirror that needed the freed-up connection is gone, and also by
		audioDeviceMixin._do_mirror() itself if the retried mirror attempt
		still failed (no point leaving the buffer suspended for nothing).
		A no-op if nothing was suspended, or if playback has since moved
		on to a different station (nothing sensible left to resume
		capturing for).
		"""
		if not getattr(self, "_timeshift_suspended_for_mirror", False):
			return
		self._timeshift_suspended_for_mirror = False
		if not self._is_playing or not self._current_url:
			return
		stream_url = self._current_url_resolved or self._current_url
		resolved_for_capture = _resolve_playlist_url(stream_url)
		try:
			self._timeshift_buffer.start(resolved_for_capture)
		except Exception:
			pass

	def _teardown_mirror_engine(self):
		"""Stop and unload the mirror engine, if any, without touching the
		time-shift buffer - the part of stop_mirror() safe to call from
		start_mirror() itself when clearing out a stale engine before
		opening a fresh one. Calling the full stop_mirror() there instead
		would resume_timeshift_after_mirror() before the new attempt even
		starts, undoing a suspend_timeshift_for_mirror() from a previous
		call and putting the connection count right back to what caused
		the failure this call might be retrying past."""
		engine = getattr(self, "_mirror_engine", None)
		if engine:
			try:
				engine.stop()
				engine.unload()
			except Exception:
				pass
		self._mirror_engine	   = None
		self._mirror_device_index = None

	def stop_mirror(self):
		"""Stop the mirror output if one is running."""
		self._teardown_mirror_engine()
		self.resume_timeshift_after_mirror()

	def log_mirror_debug(self, msg):
		"""Public wrapper around this module's _mirror_debug_log(), for
		callers outside radioPlayer.py (audioDeviceMixin.py's _do_mirror())
		that want to record their own part of a mirror attempt - e.g. why
		the connection-freeing retry was or wasn't attempted - in the same
		freeAudio_mirror_debug.log timeline."""
		_mirror_debug_log(msg)

	def get_mirror_device(self):
		"""Return the device index of the active mirror, or None."""
		return getattr(self, "_mirror_device_index", None)

	def switch_output_device(self, device_index):
		"""Przełącz wyjście BASS i zachowaj bieżące odtwarzanie.

		BASS przypina strumień do urządzenia użytego przez proces hosta, więc
		aktywny strumień jest uruchamiany ponownie na świeżo załadowanym hoście
		dla nowego urządzenia. Nazwa stacji, jej dane i głośność zostają
		zachowane.

		device_index: indeks urządzenia BASS; -1 = domyślne systemowe.
		Zwraca indeks urządzenia, które faktycznie zostało wybrane.
		"""
		requested_device_index = device_index
		with self._play_lock:
			was_playing = self._is_playing
			current_url = self._current_url
			current_url_resolved = self._current_url_resolved
			current_name = self._current_name
			current_station = dict(self._current_station or {})

			self._abort_crossfade()
			self._abort_tuning_transition()
			self._stop_icy_thread()

			if self._timeshift_active:
				self._timeshift_active = False
				try:
					self._timeshift_buffer.exit_playback()
				except Exception:
					pass

			if self._bass_engine:
				try:
					self._bass_engine.stop()
					self._bass_engine.unload()
				except Exception:
					pass

			dll_dir = os.path.dirname(os.path.abspath(__file__))
			self._bass_engine = _BassEngine(dll_dir, output_device=device_index)
			self._bass_engine.load()

			if not self._bass_engine.ready() and device_index != -1:
				log.warning(
					"freeAudio: Device %d unavailable, falling back to system default.",
					device_index,
				)
				try:
					self._bass_engine.unload()
				except Exception:
					pass
				device_index = -1
				self._bass_engine = _BassEngine(dll_dir, output_device=device_index)
				self._bass_engine.load()
				notify_lost = True
			else:
				notify_lost = False

			if self._bass_engine.ready():
				self._bass_engine.on_meta		= self._on_bass_meta
				self._bass_engine.on_connecting  = self._on_bass_connecting
				self._bass_engine.on_stall	   = self._on_bass_stall

			self._output_device_index = device_index
			self._backend			 = self.BACKEND_NONE
			self._is_playing		  = False
			self._intentional_stop	= False
			self._play_gen		   += 1

		if notify_lost:
			cb = self.on_device_lost
			if cb:
				try:
					cb(requested_device_index)
				except Exception:
					pass

		if was_playing and current_url:
			self.play(
				current_url,
				current_name,
				url_resolved=current_url_resolved,
				station=current_station,
			)
		return device_index

	def _device_monitor_loop(self):
		"""Periodically checks for the presence of the selected audio device.

		If it is not in the device list or is disabled, it will return to the system default.
		(index -1) automatically passes and triggers the on_device_lost callback.
		Since BASS can always access the system default (-1), the default
		There is no tracking for the device.
		"""
		_CHECK_INTERVAL = 10   # second
		_BASS_DEVICE_ENABLED = 1

		while not self._watchdog_stop.is_set():
			# 10-second hold — with cancellation control in 0.5s steps
			for _ in range(_CHECK_INTERVAL * 2):
				if self._watchdog_stop.is_set():
					return
				time.sleep(0.5)

			target = self._output_device_index
			if target == -1:
				# System default — no need to monitor
				continue

			try:
				devices = self.get_audio_devices()  # [(index, name), ...]
			except Exception:
				continue

			if not devices:
				# BASS not ready yet or list could not be retrieved — skip
				continue

			# Is the selected device still available?
			found = any(idx == target for idx, _name in devices)
			if found:
				continue

			# Device lost — switch to system default
			lost_index = target
			log.warning(
				"freeAudio: Audio device %d disappeared, falling back to system default.",
				lost_index,
			)
			try:
				self.switch_output_device(-1)
			except Exception:
				pass

			cb = self.on_device_lost
			if cb:
				try:
					cb(lost_index)
				except Exception:
					pass

	def terminate(self):
		self._watchdog_stop.set()
		self._podcast_autosave_stop.set()
		self.stop_mirror()
		self._abort_crossfade()
		self._abort_tuning_transition()
		self.stop()
		if self._hls_merger is not None:
			try:
				self._hls_merger.stop()
			except Exception:
				pass
		if self._bass_engine:
			self._bass_engine.unload()