# -*- coding: utf-8 -*-
# freeAudio - Saves the section between two bookmarks of a podcast episode,
# audio book part or jukebox track as an audio excerpt.
#
# The excerpt goes to <recordings folder>\<name of the playing media>\ and is
# cut with ffmpeg without re-encoding (-c copy), so it keeps the original
# format. Everything here is independent of wx / the dialog; the UI side
# (bookmarkUI.BookmarkList.save_excerpt_between_marked) hands in a "source"
# dict describing where the audio comes from:
#
#   folder     name of the sub-folder to create (the media's name)
#   prefix     optional text put in front of the file name (e.g. the part
#              title of an audio book)
#   local      path of an existing local file to cut from, or None
#   url        callable() -> URL ffmpeg can read directly, or None
#   download   callable(out_path) that downloads the whole item to out_path,
#              or None (used when the item can't be read by URL - e.g. GETEM
#              needs its login session - or when reading the URL fails)
#   prefer_download   True to skip the direct URL and download first
#   referer    optional Referer header for the direct URL
#   ext        file extension (".mp3" ...) of the source when it can't be
#              taken from the local path / URL

import logging
import os
import re
import shutil
import subprocess
import tempfile
import threading
from urllib.parse import urlparse

import config

log = logging.getLogger(__name__)

_CREATE_NO_WINDOW = 0x08000000
_KNOWN_EXTENSIONS = (
	".mp3", ".m4a", ".m4b", ".aac", ".ogg", ".oga", ".opus", ".wav", ".flac", ".mp4", ".wma",
)
_RESERVED_NAMES = {
	"con", "prn", "aux", "nul",
	*("com%d" % i for i in range(1, 10)),
	*("lpt%d" % i for i in range(1, 10)),
}

_active = set()
_active_lock = threading.Lock()


# -- helpers ---------------------------------------------------------------

def recordings_dir():
	"""Same folder the recordings go to (the 'recordings_dir' setting, or
	Documents\\freeAudio Recordings)."""
	custom_dir = config.conf["freeAudio"].get("recordings_dir", "").strip()
	if custom_dir and os.path.isabs(custom_dir):
		return custom_dir
	return os.path.join(os.path.expanduser("~"), "Documents", "freeAudio Recordings")


def find_ffmpeg():
	"""ffmpeg.exe: the 'ffmpeg_path' setting (file or folder), then the
	add-on's own folder (ffmpeg ships with it), then PATH. None if not found."""
	exe_names = ("ffmpeg.exe", "ffmpeg")
	configured = (config.conf["freeAudio"].get("ffmpeg_path", "") or "").strip()
	if configured:
		if os.path.isfile(configured):
			return configured
		if os.path.isdir(configured):
			for name in exe_names:
				candidate = os.path.join(configured, name)
				if os.path.isfile(candidate):
					return candidate
	base = os.path.dirname(os.path.abspath(__file__))
	for sub in ("", "ffmpeg", "bin", os.path.join("ffmpeg", "bin"), "lib", "tools"):
		for name in exe_names:
			candidate = os.path.join(base, sub, name)
			if os.path.isfile(candidate):
				return candidate
	# One level deeper, for layouts like <addon>\lib\ffmpeg-x.y\bin\ffmpeg.exe.
	try:
		for root, dirs, files in os.walk(base):
			depth = os.path.relpath(root, base).count(os.sep)
			if depth >= 3:
				dirs[:] = []
				continue
			for name in exe_names:
				if name in files:
					return os.path.join(root, name)
	except OSError:
		pass
	return shutil.which("ffmpeg")


def safe_name(text, fallback="Untitled", limit=80):
	"""*text* made usable as a Windows file / folder name."""
	text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", text or "")
	text = re.sub(r"\s+", " ", text).strip().strip(".").strip()
	if len(text) > limit:
		text = text[:limit].rstrip(" .")
	if not text:
		return fallback
	if text.split(".")[0].lower() in _RESERVED_NAMES:
		text = "_" + text
	return text


def _time_label(seconds):
	"""Position for use in a file name: 1.23 / 1.02.03 (no colons)."""
	seconds = max(0, int(round(seconds)))
	hours, rem = divmod(seconds, 3600)
	minutes, secs = divmod(rem, 60)
	if hours:
		return "%d.%02d.%02d" % (hours, minutes, secs)
	return "%d.%02d" % (minutes, secs)


def _extension_of(text):
	"""Known audio extension at the end of a path / URL, or ''."""
	if not text:
		return ""
	try:
		path = urlparse(text).path if "://" in text else text
	except ValueError:
		path = text
	ext = os.path.splitext(path)[1].lower()
	return ext if ext in _KNOWN_EXTENSIONS else ""


def _unique_path(folder, base, ext):
	path = os.path.join(folder, base + ext)
	n = 2
	while os.path.exists(path):
		path = os.path.join(folder, "%s (%d)%s" % (base, n, ext))
		n += 1
	return path


def _run_ffmpeg(ffmpeg, src, out_path, start, duration, referer=None):
	cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin"]
	if referer and "://" in src:
		cmd += ["-headers", "Referer: %s\r\n" % referer]
	cmd += [
		"-ss", "%.3f" % start,
		"-i", src,
		"-t", "%.3f" % duration,
		"-vn", "-map", "0:a:0",
		"-c", "copy",
		"-map_metadata", "0",
		out_path,
	]
	proc = subprocess.run(
		cmd,
		stdin=subprocess.DEVNULL,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		creationflags=_CREATE_NO_WINDOW if os.name == "nt" else 0,
		timeout=900,
	)
	ok = proc.returncode == 0 and os.path.isfile(out_path) and os.path.getsize(out_path) > 0
	if not ok:
		try:
			if os.path.isfile(out_path):
				os.remove(out_path)
		except OSError:
			pass
		lines = (proc.stderr or b"").decode("utf-8", "replace").strip().splitlines()
		return False, (lines[-1] if lines else "ffmpeg exit code %d" % proc.returncode)
	return True, ""


# -- public entry point ----------------------------------------------------

def start_excerpt(source, start, end, start_name, end_name, key, on_started, on_done, on_error):
	"""Cut seconds *start*..*end* out of *source* on a background thread.

	*key* identifies the section so the same one isn't cut twice at once.
	Callbacks (all called on the worker thread - marshal to the UI yourself):
	on_started(), on_done(out_path), on_error(message).
	Returns False if the same section is already being saved."""
	job = (key, round(start, 1), round(end, 1))
	with _active_lock:
		if job in _active:
			return False
		_active.add(job)

	def _run():
		tmp_dir = None
		try:
			on_started()
			ffmpeg = find_ffmpeg()
			if not ffmpeg:
				on_error("ffmpeg")
				return
			duration = end - start
			ext = (
				_extension_of(source.get("local"))
				or source.get("ext")
				or ""
			)
			folder = os.path.join(recordings_dir(), safe_name(source.get("folder")))
			os.makedirs(folder, exist_ok=True)

			parts = [source.get("prefix") or "", "%s - %s" % (start_name, end_name)]
			base = safe_name(
				" - ".join(p for p in parts if p).strip() + " (%s-%s)" % (_time_label(start), _time_label(end)),
				limit=120,
			)

			attempts = []   # (kind, src)
			local = source.get("local")
			if local and os.path.isfile(local):
				attempts.append(("local", local))
			else:
				if not source.get("prefer_download") and source.get("url"):
					attempts.append(("url", None))
				if source.get("download"):
					attempts.append(("download", None))

			last_error = ""
			for kind, src in attempts:
				referer = None
				if kind == "url":
					try:
						src = source["url"]()
					except Exception as e:
						last_error = str(e)
						continue
					if not src:
						continue
					ext = ext or _extension_of(src)
					referer = source.get("referer")
				elif kind == "download":
					tmp_dir = tmp_dir or tempfile.mkdtemp(prefix="freeAudio_excerpt_")
					src = os.path.join(tmp_dir, "source" + (ext or ".mp3"))
					try:
						source["download"](src)
					except Exception as e:
						last_error = str(e)
						continue
					if not os.path.isfile(src):
						continue
				out_ext = ext or _extension_of(src) or ".mp3"
				out_path = _unique_path(folder, base, out_ext)
				ok, err = _run_ffmpeg(ffmpeg, src, out_path, start, duration, referer)
				if ok:
					on_done(out_path)
					return
				last_error = err
			on_error(last_error or "no audio source")
		except Exception as e:
			log.error("freeAudio: saving excerpt failed", exc_info=True)
			on_error(str(e))
		finally:
			if tmp_dir:
				shutil.rmtree(tmp_dir, ignore_errors=True)
			with _active_lock:
				_active.discard(job)

	threading.Thread(target=_run, daemon=True, name="freeAudio-excerpt").start()
	return True
