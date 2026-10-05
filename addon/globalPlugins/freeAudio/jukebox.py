# -*- coding: utf-8 -*-
# freeAudio - Local Jukebox
#
# Manages the user's local jukebox: individually added audio files and
# folders (whose audio tracks are shown much like podcast episodes), plus
# an on-demand filename search across all locally attached drives.
#
# Mirrors the shape of podcast.py (Entry/Manager split, to_dict() producing
# a radioPlayer-compatible station dict) so the rest of the add-on - the
# playback pipeline, resume/seek/speed handling, audio profiles - can treat
# a jukebox track exactly like a podcast episode or audio-book chapter. See
# radioPlayer._is_seekable_media(): "jukebox" is included there, so every
# track played from here automatically gets the same resume/seek/speed/
# transpose treatment podcasts and audio books get, with no jukebox-specific
# code needed in radioPlayer.py itself.

import ctypes
import json
import logging
import os
import string
import struct
import time
import uuid

import addonHandler
addonHandler.initTranslation()
import globalVars

_tr = globals()["_"]
_ = _tr
del _tr
log = logging.getLogger(__name__)

# Extensions BASS (plus the bundled plugins - see bass_host.py's
# BASS_PluginLoad calls) can actually play. Kept here rather than imported
# from bass_host.py since that module only runs inside the separate host
# process and isn't importable from the main NVDA process.
AUDIO_EXTENSIONS = (
	".mp3", ".wav", ".ogg", ".oga", ".flac", ".m4a", ".m4b", ".aac",
	".wma", ".opus", ".ape", ".mpc", ".mp2", ".mp1", ".aiff", ".aif",
	".mp4", ".avi", ".mpeg", ".mpg",
	".mov", ".3gp", ".3g2", ".wmv", ".asf",
)


def _is_audio_file(path):
	return os.path.splitext(path)[1].lower() in AUDIO_EXTENSIONS


def _display_name(path):
	"""Filename without extension, used as the display label for a track."""
	return os.path.splitext(os.path.basename(path))[0]


# --- Track duration probing -------------------------------------------
#
# Jukebox tracks are local files with no feed metadata (unlike podcast
# episodes, whose duration comes from the RSS feed's <itunes:duration>),
# and BASS itself only lives in the separate bass_host.py subprocess, so
# there's nowhere to ask for a file's length without actually playing it.
# These helpers read each format's header directly (pure Python, no
# playback, no extra dependency) to get a track's total duration for
# display purposes. Formats without a lightweight/reliable header parser
# here (.ape, .mpc, raw .aac) are left unsupported - display_label()
# simply falls back to showing no duration for those, same as before.
#
# Results are cached by path, keyed on (mtime, size) so a track's
# duration is only computed once per file version - display_label() is
# called on every track in a folder each time it's selected, and again
# on every pause/finish (see refresh_jukebox_track_progress() in
# radioDialog.py), so re-parsing the header every time would be wasteful.
_duration_cache = {}  # path -> (mtime, size, duration_seconds_or_None)


def _get_track_duration(path):
	try:
		st = os.stat(path)
	except OSError:
		return None
	cached = _duration_cache.get(path)
	if cached and cached[0] == st.st_mtime and cached[1] == st.st_size:
		return cached[2]
	try:
		duration = _probe_audio_duration(path)
	except Exception as e:
		log.debug("freeAudio Jukebox: duration probe failed for %s: %s", path, e)
		duration = None
	_duration_cache[path] = (st.st_mtime, st.st_size, duration)
	return duration


def _probe_audio_duration(path):
	ext = os.path.splitext(path)[1].lower()
	if ext == ".wav":
		return _wav_duration(path)
	if ext in (".aiff", ".aif"):
		return _aiff_duration(path)
	if ext == ".flac":
		return _flac_duration(path)
	if ext in (".ogg", ".oga", ".opus"):
		return _ogg_duration(path)
	if ext in (".m4a", ".m4b", ".mp4", ".mov", ".3gp", ".3g2"):
		return _mp4_duration(path)
	if ext == ".avi":
		return _avi_duration(path)
	if ext in (".mpeg", ".mpg"):
		return _mpeg_ps_duration(path)
	if ext in (".wma", ".wmv", ".asf"):
		return _wma_duration(path)
	if ext in (".mp3", ".mp2", ".mp1"):
		return _mpeg_duration(path)
	return None


def _wav_duration(path):
	with open(path, "rb") as f:
		riff = f.read(12)
		if len(riff) < 12 or riff[:4] != b"RIFF" or riff[8:12] != b"WAVE":
			return None
		byte_rate = None
		data_size = None
		while True:
			header = f.read(8)
			if len(header) < 8:
				break
			chunk_id = header[:4]
			chunk_size = struct.unpack("<I", header[4:8])[0]
			if chunk_id == b"fmt ":
				fmt_data = f.read(chunk_size)
				if len(fmt_data) >= 16:
					byte_rate = struct.unpack("<I", fmt_data[8:12])[0]
				if chunk_size % 2:
					f.read(1)
			elif chunk_id == b"data":
				data_size = chunk_size
				break
			else:
				f.seek(chunk_size + (chunk_size % 2), 1)
		if data_size and byte_rate:
			return data_size / float(byte_rate)
	return None


def _ieee_extended_to_float(data):
	"""Convert an 80-bit IEEE extended-precision float (as used by AIFF's
	COMM chunk for the sample rate) to a Python float."""
	if len(data) < 10:
		return 0.0
	exponent = ((data[0] & 0x7F) << 8) | data[1]
	mantissa = int.from_bytes(data[2:10], "big")
	if exponent == 0 and mantissa == 0:
		return 0.0
	sign = -1.0 if data[0] & 0x80 else 1.0
	return sign * mantissa * (2.0 ** (exponent - 16383 - 63))


def _aiff_duration(path):
	with open(path, "rb") as f:
		header = f.read(12)
		if len(header) < 12 or header[:4] != b"FORM" or header[8:12] not in (b"AIFF", b"AIFC"):
			return None
		sample_rate = None
		num_frames = None
		while True:
			chunk_header = f.read(8)
			if len(chunk_header) < 8:
				break
			chunk_id = chunk_header[:4]
			chunk_size = struct.unpack(">I", chunk_header[4:8])[0]
			if chunk_id == b"COMM":
				comm = f.read(chunk_size)
				if len(comm) >= 18:
					num_frames = struct.unpack(">I", comm[2:6])[0]
					sample_rate = _ieee_extended_to_float(comm[8:18])
				if chunk_size % 2:
					f.read(1)
			else:
				f.seek(chunk_size + (chunk_size % 2), 1)
			if sample_rate and num_frames:
				break
		if sample_rate:
			return num_frames / float(sample_rate)
	return None


def _flac_duration(path):
	with open(path, "rb") as f:
		if f.read(4) != b"fLaC":
			return None
		while True:
			header = f.read(4)
			if len(header) < 4:
				return None
			is_last = bool(header[0] & 0x80)
			block_type = header[0] & 0x7F
			length = struct.unpack(">I", b"\x00" + header[1:4])[0]
			data = f.read(length)
			if block_type == 0 and len(data) >= 18:
				bits = int.from_bytes(data[10:18], "big")
				sample_rate = bits >> 44
				total_samples = bits & 0xFFFFFFFFF  # low 36 bits
				return total_samples / float(sample_rate) if sample_rate else None
			if is_last:
				return None
	return None


def _ogg_duration(path):
	"""Ogg Vorbis/Opus: sample rate comes from the identification packet
	in the first page; total duration comes from the granule position of
	the file's last page (found by scanning backwards from the end)."""
	with open(path, "rb") as f:
		head = f.read(65536)
	if head[:4] != b"OggS" or len(head) < 28:
		return None
	num_segments = head[26]
	seg_table = head[27:27 + num_segments]
	if len(seg_table) < num_segments:
		return None
	payload_start = 27 + num_segments
	payload_len = sum(seg_table)
	payload = head[payload_start:payload_start + payload_len]
	sample_rate = None
	is_opus = False
	if payload[:8] == b"OpusHead":
		is_opus = True
		sample_rate = 48000  # Opus granule positions are always counted at 48kHz
	elif len(payload) >= 16 and payload[0:1] == b"\x01" and payload[1:7] == b"vorbis":
		sample_rate = struct.unpack("<I", payload[12:16])[0]
	if not sample_rate:
		return None
	file_size = os.path.getsize(path)
	with open(path, "rb") as f:
		f.seek(max(0, file_size - 65536))
		tail = f.read()
	idx = tail.rfind(b"OggS")
	if idx == -1 or idx + 14 > len(tail):
		return None
	granule = struct.unpack("<Q", tail[idx + 6:idx + 14])[0]
	return granule / float(sample_rate)


def _mp4_read_atoms(f, end):
	atoms = []
	while f.tell() < end:
		header = f.read(8)
		if len(header) < 8:
			break
		size = struct.unpack(">I", header[:4])[0]
		atype = header[4:8]
		if size == 1:
			largesize = struct.unpack(">Q", f.read(8))[0]
			body_start = f.tell()
			body_size = largesize - 16
		elif size == 0:
			body_start = f.tell()
			body_size = end - body_start
		else:
			body_start = f.tell()
			body_size = size - 8
		atoms.append((atype, body_start, body_size))
		if body_size < 0:
			break
		f.seek(body_start + body_size)
	return atoms


def _mp4_duration(path):
	"""MP4/M4A container: total duration lives in the "mvhd" atom inside
	"moov", as (duration, timescale)."""
	file_size = os.path.getsize(path)
	with open(path, "rb") as f:
		top_atoms = _mp4_read_atoms(f, file_size)
		moov = next((a for a in top_atoms if a[0] == b"moov"), None)
		if not moov:
			return None
		f.seek(moov[1])
		children = _mp4_read_atoms(f, moov[1] + moov[2])
		mvhd = next((a for a in children if a[0] == b"mvhd"), None)
		if not mvhd:
			return None
		f.seek(mvhd[1])
		version = f.read(1)[0]
		f.read(3)  # flags
		if version == 1:
			f.read(16)  # creation + modification time (8 bytes each)
			timescale = struct.unpack(">I", f.read(4))[0]
			duration = struct.unpack(">Q", f.read(8))[0]
		else:
			f.read(8)  # creation + modification time (4 bytes each)
			timescale = struct.unpack(">I", f.read(4))[0]
			duration = struct.unpack(">I", f.read(4))[0]
		return duration / float(timescale) if timescale else None


# ASF "File Properties Object" GUID (8CABDCA1-A947-11CF-8EE4-00C00C205365),
# in the byte order it's actually stored in on disk.
_ASF_FILE_PROPERTIES_GUID = bytes((
	0xA1, 0xDC, 0xAB, 0x8C, 0x47, 0xA9, 0xCF, 0x11,
	0x8E, 0xE4, 0x00, 0xC0, 0x0C, 0x20, 0x53, 0x65,
))


def _wma_duration(path):
	"""WMA (ASF container): the File Properties Object holds a Play
	Duration field (100-nanosecond units), but that value includes the
	Preroll (milliseconds of client-side buffering) baked in, so it has
	to be subtracted back out to get the actual content duration -
	otherwise every file reads a couple of seconds too long."""
	with open(path, "rb") as f:
		data = f.read(200000)
	idx = data.find(_ASF_FILE_PROPERTIES_GUID)
	if idx == -1:
		return None
	# Object layout: 16-byte GUID + 8-byte object size, then File ID(16) +
	# File Size(8) + Creation Date(8) + Data Packets Count(8), then Play
	# Duration(8) + Send Duration(8) + Preroll(8), all QWORDs.
	play_duration_offset = idx + 24 + 40
	preroll_offset = play_duration_offset + 16
	if preroll_offset + 8 > len(data):
		return None
	play_duration_100ns = struct.unpack(
		"<Q", data[play_duration_offset:play_duration_offset + 8])[0]
	preroll_ms = struct.unpack("<Q", data[preroll_offset:preroll_offset + 8])[0]
	seconds = (play_duration_100ns - preroll_ms * 10000) / 10000000.0
	return seconds if seconds > 0 else None


_MPEG_BITRATES = {
	(1, 1): (0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, None),
	(1, 2): (0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, None),
	(1, 3): (0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, None),
	(2, 1): (0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256, None),
	(2, 2): (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, None),
	# MPEG Version 2/2.5 Layer III uses the exact same bitrate table as
	# Layer II (2, 2) above - the two layers share one table at this
	# version per the MPEG audio spec. Without this entry, every MPEG-2/
	# 2.5 Layer III frame (common for lower sample-rate MP3s - 24000/
	# 22050/16000 Hz for MPEG2, 12000/11025/8000 Hz for MPEG2.5) fails
	# this lookup and _parse_mpeg_frame_header() returns None for every
	# real frame in the file, so callers scan past all of them into raw
	# compressed audio data and eventually lock onto a coincidental,
	# meaningless byte sequence that happens to look like a valid header -
	# producing a bogus bitrate/sample rate/channel count and, since
	# duration is computed from that same false match, a bogus duration
	# too.
	(2, 3): (0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, None),
}
_MPEG_SAMPLE_RATES = {
	1: (44100, 48000, 32000, None),
	2: (22050, 24000, 16000, None),
	2.5: (11025, 12000, 8000, None),
}


def _parse_mpeg_frame_header(b):
	"""Parse a 4-byte MPEG audio frame header. Returns a dict of the
	fields needed to locate a Xing/VBRI tag and to estimate duration, or
	None if this isn't a valid frame header."""
	if len(b) < 4 or b[0] != 0xFF or (b[1] & 0xE0) != 0xE0:
		return None
	version_bits = (b[1] >> 3) & 0x3
	layer_bits = (b[1] >> 1) & 0x3
	bitrate_idx = (b[2] >> 4) & 0xF
	samplerate_idx = (b[2] >> 2) & 0x3
	padding = (b[2] >> 1) & 0x1
	version_map = {0: 2.5, 2: 2, 3: 1}
	layer_map = {1: 3, 2: 2, 3: 1}
	if version_bits not in version_map or layer_bits not in layer_map:
		return None
	version = version_map[version_bits]
	layer = layer_map[layer_bits]
	sample_rates = _MPEG_SAMPLE_RATES.get(2.5 if version == 2.5 else version)
	if not sample_rates or samplerate_idx >= len(sample_rates) or sample_rates[samplerate_idx] is None:
		return None
	sample_rate = sample_rates[samplerate_idx]
	bitrates = _MPEG_BITRATES.get((1 if version == 1 else 2, layer))
	if not bitrates or bitrate_idx >= len(bitrates) or not bitrates[bitrate_idx]:
		return None
	bitrate = bitrates[bitrate_idx] * 1000
	samples_per_frame = 384 if layer == 1 else (1152 if version == 1 else 576)
	if layer == 1:
		frame_size = (12 * bitrate // sample_rate + padding) * 4
	else:
		frame_size = 144 * bitrate // sample_rate + padding
	return {
		"sample_rate": sample_rate,
		"bitrate": bitrate,
		"samples_per_frame": samples_per_frame,
		"frame_size": frame_size,
	}


def _avi_duration(path):
	"""AVI (RIFF container): the Main AVI Header ("avih" chunk, inside
	the "hdrl" LIST near the start of the file) has a frame count and a
	microseconds-per-frame value for the file's main stream - together
	they give the overall duration, the same value AVI-aware players use."""
	with open(path, "rb") as f:
		riff = f.read(12)
		if len(riff) < 12 or riff[:4] != b"RIFF" or riff[8:12] != b"AVI ":
			return None
		while True:
			header = f.read(8)
			if len(header) < 8:
				return None
			chunk_id = header[:4]
			chunk_size = struct.unpack("<I", header[4:8])[0]
			if chunk_id != b"LIST":
				f.seek(chunk_size + (chunk_size % 2), 1)
				continue
			list_type = f.read(4)
			list_end = f.tell() + chunk_size - 4
			if list_type != b"hdrl":
				f.seek(list_end)
				continue
			while f.tell() < list_end:
				sub_header = f.read(8)
				if len(sub_header) < 8:
					return None
				sub_id = sub_header[:4]
				sub_size = struct.unpack("<I", sub_header[4:8])[0]
				if sub_id == b"avih":
					avih = f.read(sub_size)
					if len(avih) < 20:
						return None
					micros_per_frame = struct.unpack("<I", avih[0:4])[0]
					total_frames = struct.unpack("<I", avih[16:20])[0]
					if not micros_per_frame or not total_frames:
						return None
					return total_frames * micros_per_frame / 1000000.0
				f.seek(sub_size + (sub_size % 2), 1)
			return None
	return None


def _scan_mpeg_pts(data):
	"""Return every presentation timestamp (a 90kHz clock value) found in
	MPEG-2 Program Stream PES packet headers within *data*, in the order
	encountered. Used by _mpeg_ps_duration() to estimate an MPEG program
	stream's duration from its first and last timestamps.

	Only genuine MPEG-2 PES optional headers are accepted: byte data[i+6]
	must carry the mandatory '10' marker that starts that header
	extension, and the PTS field itself must carry its own marker bits
	(top nibble matching pts_dts_flags, plus the fixed '1' bits within
	the 5-byte timestamp). Without these checks, a 00 00 01 <stream_id>
	match that ISN'T actually followed by an MPEG-2 PES extension - most
	notably in MPEG-1 Program Streams, which use a different optional-
	header layout with no flags/header_len bytes at these offsets at all -
	gets its next few payload/stuffing bytes misread as flags/header_len
	and PTS, producing a plausible-looking but wrong duration instead of
	safely finding nothing."""
	pts_values = []
	i = 0
	n = len(data)
	while i < n - 9:
		if data[i] == 0 and data[i + 1] == 0 and data[i + 2] == 1:
			stream_id = data[i + 3]
			if 0xC0 <= stream_id <= 0xEF:  # audio (C0-DF) or video (E0-EF) stream
				marker = data[i + 6]
				if (marker & 0xC0) != 0x80:
					# Not a real MPEG-2 PES header extension (e.g. an
					# MPEG-1 stream, or a coincidental start-code-like
					# byte sequence) - don't trust flags/header_len below.
					i += 1
					continue
				flags = data[i + 7]
				pts_dts_flags = (flags >> 6) & 0x3
				header_len = data[i + 8]
				if pts_dts_flags in (0x2, 0x3) and i + 9 + 5 <= n:
					pb = data[i + 9:i + 14]
					expected_top_nibble = 0x2 if pts_dts_flags == 0x2 else 0x3
					valid_markers = (
						(pb[0] >> 4) == expected_top_nibble
						and (pb[0] & 0x01) == 1
						and (pb[2] & 0x01) == 1
						and (pb[4] & 0x01) == 1
					)
					if valid_markers:
						pts = (
							((pb[0] & 0x0E) << 29) | (pb[1] << 22) |
							((pb[2] & 0xFE) << 14) | (pb[3] << 7) | (pb[4] >> 1)
						)
						pts_values.append(pts)
				i += 9 + header_len
				continue
		i += 1
	return pts_values


def _mpeg_ps_duration(path):
	"""MPEG-1/2 Program Stream (.mpeg/.mpg): unlike the other containers
	there's no compact duration field to read, so this scans PES packet
	headers near the start and end of the file for presentation
	timestamps and takes the difference. Works for MPEG-2 program
	streams, which is what modern encoders (ffmpeg included) produce;
	plain MPEG-1 streams use a slightly different PES header layout and
	are simply left without a duration rather than risking a wrong one."""
	file_size = os.path.getsize(path)
	chunk = min(file_size, 2 * 1024 * 1024)
	with open(path, "rb") as f:
		head = f.read(chunk)
		f.seek(max(0, file_size - chunk))
		tail = f.read()
	first_ptses = _scan_mpeg_pts(head)
	last_ptses = _scan_mpeg_pts(tail)
	if not first_ptses or not last_ptses:
		return None
	first_pts = min(first_ptses)
	last_pts = max(last_ptses)
	if last_pts <= first_pts:
		return None
	return (last_pts - first_pts) / 90000.0


def _mpeg_duration(path):
	"""MP3/MP2/MP1: uses the Xing/Info or VBRI tag (frame count) for an
	exact duration when present (typical for VBR encodes); otherwise
	falls back to a CBR estimate from the first frame's bitrate and the
	remaining file size."""
	with open(path, "rb") as f:
		offset = 0
		start = f.read(10)
		if start[:3] == b"ID3":
			size = (
				(start[6] & 0x7F) << 21 | (start[7] & 0x7F) << 14 |
				(start[8] & 0x7F) << 7 | (start[9] & 0x7F)
			)
			offset = 10 + size
		# Always resync to *offset* (0 when there's no ID3v2 tag) before
		# reading the scan window - f.read(10) above already moved the file
		# pointer to byte 10 even when no tag was found, and without this
		# seek the very first 10 bytes of a tagless file are silently
		# skipped and every position computed from here on (frame_offset,
		# the later f.seek() back into the file, the Xing/Info/VBRI search)
		# is off by that same 10 bytes - misreading duration/bitrate/sample
		# rate/channels for any file that doesn't start with an ID3v2 tag.
		f.seek(offset)
		window = f.read(8192)
		header = None
		frame_offset = None
		pos = 0
		while pos < len(window) - 4:
			if window[pos] == 0xFF and (window[pos + 1] & 0xE0) == 0xE0:
				parsed = _parse_mpeg_frame_header(window[pos:pos + 4])
				if parsed:
					header = parsed
					frame_offset = offset + pos
					break
			pos += 1
		if not header:
			return None
		f.seek(frame_offset)
		frame_data = f.read(header["frame_size"] + 4)
		for tag in (b"Xing", b"Info"):
			tag_pos = frame_data.find(tag)
			if tag_pos != -1 and tag_pos + 16 <= len(frame_data):
				flags = struct.unpack(">I", frame_data[tag_pos + 4:tag_pos + 8])[0]
				if flags & 0x1:
					num_frames = struct.unpack(">I", frame_data[tag_pos + 8:tag_pos + 12])[0]
					total_samples = num_frames * header["samples_per_frame"]
					return total_samples / float(header["sample_rate"])
				break
		vbri_pos = frame_data.find(b"VBRI")
		if vbri_pos != -1 and vbri_pos + 26 <= len(frame_data):
			num_frames = struct.unpack(">I", frame_data[vbri_pos + 14:vbri_pos + 18])[0]
			total_samples = num_frames * header["samples_per_frame"]
			return total_samples / float(header["sample_rate"])
		# No VBR tag: estimate assuming a constant bitrate for the rest
		# of the file - accurate for CBR files, an approximation for
		# untagged VBR ones.
		file_size = os.path.getsize(path)
		audio_bytes = max(0, file_size - frame_offset)
		return audio_bytes * 8 / float(header["bitrate"]) if header["bitrate"] else None


# --- Track technical-info probing (bitrate/sample rate/channels/etc.) --
#
# Powers the "Track details" block shown in the station-details dialog
# (Ctrl+Win+I, 2x press) for jukebox tracks - see
# trackInfoMixin._build_jukebox_details(). Each probe below reads a
# little more of the same header the corresponding _xxx_duration()
# function above already reads, rather than reusing/refactoring those
# (kept deliberately separate to avoid risking the already-working
# duration probes above). Formats without a probe here (.ape, .mpc, raw
# .aac, .avi, .mpeg/.mpg, .wma/.wmv/.asf, .m4a/.m4b/.mp4/.mov/.3gp/.3g2)
# simply get "sample_rate"/"channels"/"bit_depth" of None and fall back
# to a whole-file average bitrate (size/duration) - see
# _get_track_audio_info(). None of these probes raise on a malformed or
# truncated file; each returns None (folded into {} by the caller) so a
# bad file just means fewer detail rows shown, not a crash.


def _wav_info(path):
	with open(path, "rb") as f:
		riff = f.read(12)
		if len(riff) < 12 or riff[:4] != b"RIFF" or riff[8:12] != b"WAVE":
			return None
		while True:
			header = f.read(8)
			if len(header) < 8:
				return None
			chunk_id = header[:4]
			chunk_size = struct.unpack("<I", header[4:8])[0]
			if chunk_id == b"fmt ":
				fmt_data = f.read(chunk_size)
				if len(fmt_data) < 16:
					return None
				channels = struct.unpack("<H", fmt_data[2:4])[0]
				sample_rate = struct.unpack("<I", fmt_data[4:8])[0]
				byte_rate = struct.unpack("<I", fmt_data[8:12])[0]
				bit_depth = struct.unpack("<H", fmt_data[14:16])[0] if len(fmt_data) >= 16 else None
				return {
					"sample_rate": sample_rate or None,
					"channels": channels or None,
					"bit_depth": bit_depth or None,
					"bitrate_kbps": int(round(byte_rate * 8 / 1000.0)) if byte_rate else None,
				}
			f.seek(chunk_size + (chunk_size % 2), 1)


def _aiff_info(path):
	with open(path, "rb") as f:
		header = f.read(12)
		if len(header) < 12 or header[:4] != b"FORM" or header[8:12] not in (b"AIFF", b"AIFC"):
			return None
		while True:
			chunk_header = f.read(8)
			if len(chunk_header) < 8:
				return None
			chunk_id = chunk_header[:4]
			chunk_size = struct.unpack(">I", chunk_header[4:8])[0]
			if chunk_id == b"COMM":
				comm = f.read(chunk_size)
				if len(comm) < 18:
					return None
				channels = struct.unpack(">H", comm[0:2])[0]
				bit_depth = struct.unpack(">H", comm[6:8])[0]
				sample_rate = _ieee_extended_to_float(comm[8:18])
				return {
					"sample_rate": int(round(sample_rate)) if sample_rate else None,
					"channels": channels or None,
					"bit_depth": bit_depth or None,
					"bitrate_kbps": None,
				}
			f.seek(chunk_size + (chunk_size % 2), 1)


def _flac_info(path):
	with open(path, "rb") as f:
		if f.read(4) != b"fLaC":
			return None
		while True:
			header = f.read(4)
			if len(header) < 4:
				return None
			is_last = bool(header[0] & 0x80)
			block_type = header[0] & 0x7F
			length = struct.unpack(">I", b"\x00" + header[1:4])[0]
			data = f.read(length)
			if block_type == 0 and len(data) >= 18:
				bits = int.from_bytes(data[10:18], "big")
				sample_rate = bits >> 44
				channels = ((bits >> 41) & 0x7) + 1
				bit_depth = ((bits >> 36) & 0x1F) + 1
				return {
					"sample_rate": sample_rate or None,
					"channels": channels,
					"bit_depth": bit_depth,
					"bitrate_kbps": None,  # FLAC is variable-rate by nature
				}
			if is_last:
				return None


def _ogg_info(path):
	"""Vorbis/Opus, from the identification packet in the file's first
	page - see _ogg_duration() for the shared page/packet layout this
	reads from. Vorbis' identification packet also states a nominal
	bitrate; Opus doesn't carry one directly, so its bitrate is left for
	_get_track_audio_info()'s whole-file average to fill in."""
	with open(path, "rb") as f:
		head = f.read(65536)
	if head[:4] != b"OggS" or len(head) < 28:
		return None
	num_segments = head[26]
	seg_table = head[27:27 + num_segments]
	if len(seg_table) < num_segments:
		return None
	payload_start = 27 + num_segments
	payload_len = sum(seg_table)
	payload = head[payload_start:payload_start + payload_len]
	if payload[:8] == b"OpusHead" and len(payload) >= 10:
		return {
			"sample_rate": None,  # always played back at 48kHz regardless of input_sample_rate
			"channels": payload[9] or None,
			"bit_depth": None,
			"bitrate_kbps": None,
		}
	if len(payload) >= 28 and payload[0:1] == b"\x01" and payload[1:7] == b"vorbis":
		channels = payload[11]
		sample_rate = struct.unpack("<I", payload[12:16])[0]
		bitrate_nominal = struct.unpack("<i", payload[20:24])[0]
		return {
			"sample_rate": sample_rate or None,
			"channels": channels or None,
			"bit_depth": None,
			"bitrate_kbps": int(round(bitrate_nominal / 1000.0)) if bitrate_nominal > 0 else None,
		}
	return None


def _mp3_info(path):
	"""MP3/MP2/MP1, from the same first valid frame header
	_mpeg_duration() locates - re-scanned independently here (see the
	module note above on why these probes don't share code with the
	duration ones). The channel mode (stereo/joint stereo/dual channel/
	mono) lives in the 2 bits right after the ones _parse_mpeg_frame_header()
	already decodes, so it's read directly from the frame bytes here.

	VBR-encoded files (the large majority of MP3s in the wild) don't start
	with a real audio frame at all - the first frame is a dummy "Xing"/
	"Info"/"VBRI" header frame (see _mpeg_duration()'s docstring for why
	that function specifically looks for it). That frame's own bitrate
	field is a throwaway placeholder value picked by the encoder (commonly
	the lowest one legal for the file's MPEG version/sample rate, since
	real decoders never play this frame), not the track's actual bitrate -
	so it must never be reported as one. When the first frame found is one
	of these header frames, its bitrate is left out entirely (None here,
	so _get_track_audio_info() falls back to an accurate whole-file
	average computed from size/duration - and duration is already correct
	for these files via _mpeg_duration()'s own Xing/VBRI parsing), and
	sample_rate/channels are read from the first genuine audio frame right
	after it instead, since a few older/nonstandard encoders don't keep
	those fields on the placeholder frame in sync with the real stream
	either."""
	with open(path, "rb") as f:
		offset = 0
		start = f.read(10)
		if start[:3] == b"ID3":
			size = (
				(start[6] & 0x7F) << 21 | (start[7] & 0x7F) << 14 |
				(start[8] & 0x7F) << 7 | (start[9] & 0x7F)
			)
			offset = 10 + size
		# Always resync to *offset* (0 when there's no ID3v2 tag) before
		# reading the scan window - f.read(10) above already moved the file
		# pointer to byte 10 even when no tag was found, and without this
		# seek the very first 10 bytes of a tagless file are silently
		# skipped and every position computed from here on (frame_offset,
		# the later f.seek() back into the file, the Xing/Info/VBRI search)
		# is off by that same 10 bytes - misreading duration/bitrate/sample
		# rate/channels for any file that doesn't start with an ID3v2 tag.
		f.seek(offset)
		window = f.read(8192)
		pos = 0
		while pos < len(window) - 4:
			if window[pos] == 0xFF and (window[pos + 1] & 0xE0) == 0xE0:
				parsed = _parse_mpeg_frame_header(window[pos:pos + 4])
				if parsed:
					frame_offset = offset + pos
					tag_region = window[pos:pos + parsed["frame_size"] + 4]
					is_vbr_header = any(tag in tag_region for tag in (b"Xing", b"Info", b"VBRI"))
					if is_vbr_header:
						# Placeholder frame, not real audio - hunt for the next
						# valid frame right after it and use that one's fields
						# instead; bitrate is left for the whole-file-average
						# fallback in _get_track_audio_info().
						f.seek(frame_offset + parsed["frame_size"])
						next_window = f.read(8192)
						npos = 0
						while npos < len(next_window) - 4:
							if next_window[npos] == 0xFF and (next_window[npos + 1] & 0xE0) == 0xE0:
								next_parsed = _parse_mpeg_frame_header(next_window[npos:npos + 4])
								if next_parsed:
									channel_mode = (next_window[npos + 3] >> 6) & 0x3
									channels = 1 if channel_mode == 3 else 2
									return {
										"sample_rate": next_parsed["sample_rate"],
										"channels": channels,
										"bit_depth": None,
										"bitrate_kbps": None,
									}
							npos += 1
						# No real audio frame turned up after the header (an
						# unusually short/truncated file) - fall back to the
						# header frame's own sample_rate/channels rather than
						# nothing.
						channel_mode = (window[pos + 3] >> 6) & 0x3
						channels = 1 if channel_mode == 3 else 2
						return {
							"sample_rate": parsed["sample_rate"],
							"channels": channels,
							"bit_depth": None,
							"bitrate_kbps": None,
						}
					channel_mode = (window[pos + 3] >> 6) & 0x3
					channels = 1 if channel_mode == 3 else 2
					return {
						"sample_rate": parsed["sample_rate"],
						"channels": channels,
						"bit_depth": None,  # MP3 has no fixed bit depth - it's a lossy, block-based codec
						"bitrate_kbps": parsed["bitrate"] // 1000,
					}
			pos += 1
	return None


_PROBE_BY_EXTENSION = {
	".wav": _wav_info,
	".aiff": _aiff_info, ".aif": _aiff_info,
	".flac": _flac_info,
	".ogg": _ogg_info, ".oga": _ogg_info, ".opus": _ogg_info,
	".mp3": _mp3_info, ".mp2": _mp3_info, ".mp1": _mp3_info,
}

_audio_info_cache = {}  # path -> (mtime, size, info_dict)


def _get_track_audio_info(path):
	"""Returns a dict describing *path*'s audio properties for the
	jukebox "Track details" block (trackInfoMixin._build_jukebox_details()):
	"duration" (seconds, reusing _get_track_duration()'s own cache),
	"size_bytes" (from os.stat - always available, for every format),
	"sample_rate" (Hz), "channels", "bit_depth" (bits per sample - only
	meaningful for uncompressed/lossless formats, None for lossy ones),
	"bitrate_kbps", and "format" (the file extension in upper case,
	purely for display - not a real codec probe). Any field a
	format-specific probe above doesn't supply is None; "bitrate_kbps"
	specifically then falls back to a whole-file average computed from
	size/duration, so every playable file still shows *some* bitrate
	even when the exact encoded value isn't cheaply readable (MP4/WMA/
	AVI/MPEG-PS, and FLAC/AIFF/Opus, which are lossless/variable enough
	that no single header field states one).

	Cached by path, keyed on (mtime, size) exactly like
	_get_track_duration() - see that function's docstring for why."""
	try:
		st = os.stat(path)
	except OSError:
		return None
	cached = _audio_info_cache.get(path)
	if cached and cached[0] == st.st_mtime and cached[1] == st.st_size:
		return cached[2]
	duration = _get_track_duration(path)
	probe = _PROBE_BY_EXTENSION.get(os.path.splitext(path)[1].lower())
	extra = {}
	if probe:
		try:
			extra = probe(path) or {}
		except Exception as e:
			log.debug("freeAudio Jukebox: technical-info probe failed for %s: %s", path, e)
	bitrate_kbps = extra.get("bitrate_kbps")
	if bitrate_kbps is None and duration and duration > 0:
		bitrate_kbps = int(round(st.st_size * 8 / duration / 1000.0))
	info = {
		"duration": duration,
		"size_bytes": st.st_size,
		"sample_rate": extra.get("sample_rate"),
		"channels": extra.get("channels"),
		"bit_depth": extra.get("bit_depth"),
		"bitrate_kbps": bitrate_kbps,
		"format": os.path.splitext(path)[1].lstrip(".").upper(),
	}
	_audio_info_cache[path] = (st.st_mtime, st.st_size, info)
	return info


class JukeboxTrack:
	"""A single playable audio file - either a manually added file, or one
	discovered inside a manually added folder."""

	def __init__(self, path, audio_profile=None):
		self.path = path
		self.title = _display_name(path)
		# Optional dict of {"volume": int, "fx": str, "eq_gains": {...},
		# "speed": float, "transpose": float} - passed in by the caller
		# (typically from JukeboxManager.get_track_profile()) rather than
		# stored on the track itself, since profiles are keyed by absolute
		# file path in the manager and a track object is recreated fresh
		# every time the list is rebuilt. See JukeboxManager._track_profiles.
		self.audio_profile = audio_profile

	def to_dict(self):
		"""Convert to a radioPlayer-compatible station dict - see
		podcast.PodcastEpisode.to_dict() for the equivalent podcast version
		and radioPlayer._is_seekable_media() for why "media_kind":"jukebox"
		alone is enough to get resume/seek/speed/transpose support.

		Also includes this file's technical properties (size/duration/
		bitrate/sample rate/channels/bit depth/format - see
		_get_track_audio_info()) under "jukebox_*" keys, so the
		station-details dialog (trackInfoMixin._build_jukebox_details())
		can show them without re-probing the file itself.

		If an audio_profile was supplied, it's included as "station_audio"
		so playbackCoreMixin._play_station() applies it automatically the
		same way it does for podcasts and audio books."""
		d = {
			"name": self.title,
			"url": self.path,
			"url_resolved": self.path,
			"stationuuid": "jukebox-" + str(uuid.uuid4()),
			"countrycode": "",
			"tags": "jukebox",
			"media_kind": "jukebox",
			"description": "",
		}
		info = _get_track_audio_info(self.path)
		if info:
			# Read back by trackInfoMixin._build_jukebox_details() to
			# show file size/duration/bitrate/sample rate/channels/bit
			# depth in the station-details dialog. Any field the probe
			# for this format couldn't determine (see
			# _get_track_audio_info()) is simply absent/None here, and
			# that row is omitted there rather than shown as "Unknown".
			d["jukebox_size_bytes"] = info.get("size_bytes")
			d["jukebox_duration_seconds"] = info.get("duration")
			d["jukebox_bitrate_kbps"] = info.get("bitrate_kbps")
			d["jukebox_sample_rate"] = info.get("sample_rate")
			d["jukebox_channels"] = info.get("channels")
			d["jukebox_bit_depth"] = info.get("bit_depth")
			d["jukebox_format"] = info.get("format")
		if self.audio_profile:
			d["station_audio"] = self.audio_profile
		return d

	def display_label(self, player=None, probe_duration=True):
		"""Mirrors podcast.PodcastEpisode.display_label() for the elapsed/
		total duration display, but deliberately skips the "[Listened]"
		prefix: that marker fits podcast episodes, which are normally
		consumed once, but not jukebox tracks, which are expected to be
		replayed - flagging a song "[Listened]" after one pass would just
		be noise (or misleading, once the user plays it again).

		The total duration comes from _get_track_duration() (a header
		probe of the file itself, cached by path - see the "Track
		duration probing" section above), since jukebox tracks have no
		feed metadata to supply it the way podcast episodes do. Two
		cases: never played (or fully played through - pos == -1.0 is
		folded into this case too) shows just the total; partially
		played shows elapsed / total.

		*probe_duration* lets a caller skip the header read for this call
		(the label then just shows the title, plus elapsed position if
		any). RadioDialog._on_jukebox_entry_selected() passes False for
		the initial, synchronous population of a folder's track list -
		one probe_duration=True call per file is a disk read, which for a
		folder with many tracks would otherwise block the UI (and NVDA's
		speech) until every file in it has been opened and parsed; the
		real durations are filled in afterwards by a background thread -
		see RadioDialog._probe_jukebox_track_durations()."""
		from . import _format_duration
		label = self.title
		duration = _get_track_duration(self.path) if probe_duration else None
		total_str = _format_duration(duration) if duration else None
		if not player:
			return label + (" (%s)" % total_str if total_str else "")
		pos = player.get_podcast_position(self.path)
		if pos and pos > 0.0:
			if total_str:
				return label + " (%s / %s)" % (_format_duration(pos), total_str)
			return label + " (%s)" % _format_duration(pos)
		if total_str:
			return label + " (%s)" % total_str
		return label


class JukeboxEntry:
	"""A single item the user added to the jukebox: either one file, or a
	folder whose audio files are shown as its "tracks" (the folder itself
	isn't playable; picking it plays/queues its first track).

	Deliberately has no audio-profile field of its own. Audio profiles
	are per file (JukeboxManager._track_profiles, keyed by absolute
	path): a folder's contents can change over time, and a folder-wide
	profile would then silently apply to files the user never set it for.
	Storing per file also means a profile survives a folder rescan and a
	folder being removed and later re-added."""

	def __init__(self, path, kind, added=None, group="", custom_name=None):
		self.path = path
		self.kind = kind  # "file" | "folder"
		self.added = added if added is not None else time.time()
		# User-assigned folder/group name (mirrors favourites' "group" field
		# in stationManager - see RadioDialog._on_jukebox_assign_group()).
		# Display-only, like favourites: never changes anything on disk.
		self.group = group or ""
		# User-assigned display name, overriding the name derived from the
		# path (mirrors favourites' rename - see JukeboxManager.rename_entry()).
		# None means "no override, use the derived name".
		self.custom_name = custom_name or None
		self._tracks = None  # lazily scanned for folders; see tracks()

	@property
	def title(self):
		if self.custom_name:
			return self.custom_name
		if self.kind == "folder":
			return os.path.basename(os.path.normpath(self.path)) or self.path
		return _display_name(self.path)

	def exists(self):
		return os.path.isdir(self.path) if self.kind == "folder" else os.path.isfile(self.path)

	def tracks(self, force_rescan=False):
		"""Audio files inside this entry. For a "file" entry that's just
		itself (one-element list); for a "folder" entry it's every audio
		file found under it (recursively), sorted so results are stable
		and predictable - alphabetically by the path relative to the
		folder, which naturally groups subfolders together.

		Returned JukeboxTrack objects carry no profile of their own -
		the caller (RadioDialog) looks up each track's profile by path
		via JukeboxManager.get_track_profile() when it's about to play
		it, so this scan never has to know or care about profiles."""
		if self.kind == "file":
			return [JukeboxTrack(self.path)] if os.path.isfile(self.path) else []
		if self._tracks is not None and not force_rescan:
			return self._tracks
		found = []
		try:
			for root, _dirs, files in os.walk(self.path):
				for name in files:
					if _is_audio_file(name):
						found.append(os.path.join(root, name))
		except Exception as e:
			log.warning("freeAudio Jukebox: folder scan failed for %s: %s", self.path, e)
		found.sort(key=lambda p: os.path.relpath(p, self.path).lower())
		self._tracks = [JukeboxTrack(p) for p in found]
		return self._tracks

	def display_label(self):
		if self.kind == "folder":
			count = len(self.tracks())
			# Translators: %(name)s = folder name, %(count)d = number of audio files found in it
			label = _("%(name)s (folder, %(count)d tracks)") % {"name": self.title, "count": count}
		else:
			label = self.title
		# Mirrors RadioDialog._fav_display_label()'s " — Group" suffix for
		# favourites - display-only, never touches self.path/title.
		if self.group:
			label += " — " + self.group
		return label

	def to_dict(self):
		d = {"path": self.path, "kind": self.kind, "added": self.added}
		if self.group:
			d["group"] = self.group
		if self.custom_name:
			d["custom_name"] = self.custom_name
		return d

	@classmethod
	def from_dict(cls, data):
		return cls(
			data["path"], data.get("kind", "file"), data.get("added", 0.0),
			group=data.get("group", ""), custom_name=data.get("custom_name"),
		)


class JukeboxManager:
	"""Manages the persisted list of jukebox entries (files/folders the
	user explicitly added) and their per-file audio profiles."""

	def __init__(self):
		self._entries = []  # list of JukeboxEntry
		# Maps absolute file path -> profile dict
		# {"volume": int, "fx": str, "eq_gains": {...}, "speed": float,
		#  "transpose": float}. Kept as a flat path-keyed dict rather than
		# stored on JukeboxEntry because a folder's contents are scanned
		# dynamically - a profile for a file inside a folder must persist
		# independently of when that folder was last rescanned, and of
		# the folder entry itself existing at all.
		self._track_profiles = {}
		self._load()

	def _profile_key(self, path):
		# Match the same normalisation has_path()/get_folder_entry()/
		# remove_entry()/rescan_folder() already apply to entry paths, so
		# a profile saved under one casing/path form is still found when
		# the same file is later referenced through a different one
		# (case-insensitive filesystems, mapped drives, or callers that
		# didn't pre-normalise the path).
		if not path:
			return path
		return os.path.normcase(os.path.normpath(path))

	def _get_path(self):
		return os.path.join(globalVars.appArgs.configPath, "freeAudio_jukebox.json")

	def _load(self):
		path = self._get_path()
		if not os.path.exists(path):
			return
		try:
			with open(path, "r", encoding="utf-8") as f:
				data = json.load(f)
			# Backwards compatibility: earlier builds wrote a bare list of
			# entry dicts; the current format is {"entries": [...],
			# "track_profiles": {...}}.
			if isinstance(data, list):
				entries_data = data
				track_profiles = {}
			else:
				entries_data = data.get("entries", [])
				track_profiles = dict(data.get("track_profiles", {}))
				# Migration: an intermediate build briefly stored one
				# profile on a "file" entry itself (rather than per
				# track). Fold it into the per-file map so it keeps
				# applying after the upgrade. Folders are skipped - a
				# folder-wide profile was never a supported concept in
				# the shipped format, so there's nothing to migrate.
				for item in entries_data:
					legacy = item.get("audio_profile")
					if legacy and item.get("kind", "file") == "file":
						track_profiles.setdefault(item.get("path"), legacy)
			self._entries = [JukeboxEntry.from_dict(item) for item in entries_data]
			# One-time migration: rewrite every profile key through
			# _profile_key() so a profile saved verbatim by an earlier
			# version (before path normalisation was added here) is still
			# found by get_track_profile() afterwards - a file whose path
			# happens to come back in a different casing/form on the next
			# run (case-insensitive filesystem, mapped drive letter, etc.)
			# would otherwise lose its saved profile silently. Also folds
			# the legacy entry-level "audio_profile" field (already moved
			# into track_profiles just above) into the same normalised-key
			# map.
			self._track_profiles = {
				self._profile_key(k): v for k, v in track_profiles.items()
			}
		except Exception as e:
			log.warning("freeAudio Jukebox: failed to load library: %s", e)
			self._entries = []
			self._track_profiles = {}

	def _save(self):
		path = self._get_path()
		data = {
			"entries": [e.to_dict() for e in self._entries],
			"track_profiles": self._track_profiles,
		}
		tmp_path = path + ".tmp"
		try:
			with open(tmp_path, "w", encoding="utf-8") as f:
				json.dump(data, f, ensure_ascii=False, indent=2)
			os.replace(tmp_path, path)
		except Exception as e:
			log.warning("freeAudio Jukebox: failed to save library: %s", e)
			try:
				os.remove(tmp_path)
			except OSError:
				pass

	def save(self):
		"""Public alias for _save() - callers outside this module (the
		audio-profile save/clear actions in RadioDialog) shouldn't need
		to reach into the private method to persist a profile change."""
		self._save()

	def get_track_profile(self, path):
		"""Return the audio profile saved for the file at *path*, or
		None. Keyed by normalised absolute file path, so two files
		inside the same folder entry keep independent profiles and a
		path arriving in a different casing still resolves to the same
		saved profile."""
		if not path:
			return None
		return self._track_profiles.get(self._profile_key(path))

	def set_track_profile(self, path, profile):
		"""Save *profile* for the file at *path*. Passing None (or an
		empty dict) removes any saved profile. Persists immediately."""
		if not path:
			return
		key = self._profile_key(path)
		if profile:
			self._track_profiles[key] = profile
		else:
			self._track_profiles.pop(key, None)
		self._save()

	def get_folder_entry(self, path):
		"""Look up a folder entry by its absolute path. Used to headlessly
		resume/advance a folder-sequence auto-advance (see
		GlobalPlugin._advance_jukebox_folder_headless() in __init__.py and
		RadioDialog._on_playback_finished() in radioDialog.py) from just
		the path carried in a finished station's own "jukebox_folder_path"
		field - the same way _rebuild_getem_resume_url()/
		_advance_getem_chapter_headless() look a GETEM book back up by its
		detail_url, without needing any dialog state to still exist."""
		norm = os.path.normcase(os.path.normpath(path))
		for e in self._entries:
			if e.kind == "folder" and os.path.normcase(os.path.normpath(e.path)) == norm:
				return e
		return None

	def get_entries(self):
		return list(self._entries)

	def has_path(self, path):
		norm = os.path.normcase(os.path.normpath(path))
		return any(os.path.normcase(os.path.normpath(e.path)) == norm for e in self._entries)

	def add_file(self, path):
		"""Add a single audio file. Returns (entry, error_message)."""
		if not os.path.isfile(path):
			# Translators: Error returned by JukeboxManager.add_file() when the given path does not exist; %s is the file path.
			return None, _("File not found: %s") % path
		if not _is_audio_file(path):
			# Translators: Error returned by JukeboxManager.add_file() when the file's extension isn't one of the supported audio formats; %s is the file path.
			return None, _("Not a recognized audio file: %s") % path
		if self.has_path(path):
			# Translators: Error returned by JukeboxManager.add_file()/add_folder() when that exact path is already saved in the jukebox library.
			return None, _("Already in the jukebox.")
		entry = JukeboxEntry(path, "file")
		self._entries.append(entry)
		self._save()
		return entry, None

	def add_folder(self, path):
		"""Add a folder; its audio files are scanned on demand (see
		JukeboxEntry.tracks()). Returns (entry, error_message)."""
		if not os.path.isdir(path):
			# Translators: Error returned by JukeboxManager.add_folder() when the given folder path does not exist; %s is the folder path.
			return None, _("Folder not found: %s") % path
		if self.has_path(path):
			# Translators: See the add_file() comment above: same message, returned by add_folder() when the folder is already in the jukebox.
			return None, _("Already in the jukebox.")
		entry = JukeboxEntry(path, "folder")
		tracks = entry.tracks()
		if not tracks:
			# Translators: Error returned by JukeboxManager.add_folder() when the folder was scanned but contains no recognized audio files.
			return None, _("No audio files found in that folder.")
		self._entries.append(entry)
		self._save()
		return entry, None

	def remove_entry(self, path):
		"""Remove an entry from the list. Any per-file profiles that were
		saved for files owned by it are deliberately left in place: a
		removed folder can be added back later and users expect their
		saved profiles to still be there, and orphan profile entries are
		tiny (a few fields per file, nothing like the audio itself).
		Users who want a clean slate can clear profiles file-by-file
		from the context menus before removing the entry."""
		norm = os.path.normcase(os.path.normpath(path))
		for e in self._entries:
			if os.path.normcase(os.path.normpath(e.path)) == norm:
				self._entries.remove(e)
				self._save()
				return True
		return False

	def rescan_folder(self, path):
		"""Force a fresh directory scan for a folder entry (e.g. after the
		user adds files to disk outside the add-on)."""
		norm = os.path.normcase(os.path.normpath(path))
		for e in self._entries:
			if e.kind == "folder" and os.path.normcase(os.path.normpath(e.path)) == norm:
				return e.tracks(force_rescan=True)
		return []

	def rename_entry(self, path, new_name):
		"""Give the entry at *path* a custom display name (JukeboxEntry.
		custom_name), mirroring favourites' rename - see
		RadioDialog._on_rename_station(). Never touches the file/folder on
		disk itself. Passing an empty/None *new_name* clears the override,
		reverting to the name derived from the path. Returns True if an
		entry was found and changed."""
		norm = os.path.normcase(os.path.normpath(path))
		for e in self._entries:
			if os.path.normcase(os.path.normpath(e.path)) == norm:
				e.custom_name = (new_name or "").strip() or None
				self._save()
				return True
		return False

	def set_entry_group(self, path, group):
		"""Assign (or, with an empty *group*, clear) the folder/group name
		for the entry at *path* - mirrors favourites' Assign to Group, see
		RadioDialog._on_fav_assign_group(). Returns True if an entry was
		found and changed."""
		norm = os.path.normcase(os.path.normpath(path))
		for e in self._entries:
			if os.path.normcase(os.path.normpath(e.path)) == norm:
				e.group = (group or "").strip()
				self._save()
				return True
		return False

	def set_order(self, entries):
		"""Replace the entry list with *entries* (the same JukeboxEntry
		objects, reordered) and persist - used by the Jukebox tab's
		comma-key move/reorder command (mirrors favourites' own reordering
		in RadioDialog._handle_fav_move_x(), which manipulates
		StationManager's list directly; this does the equivalent through a
		proper method since JukeboxManager's entry list isn't a plain list
		of dicts)."""
		self._entries = list(entries)
		self._save()

	def export_entries_json(self, path):
		"""Write every entry (path/kind/group/custom name) and every saved
		per-file audio profile to a JSON file - mirrors
		StationManager.export_favorites_json(). The full-fidelity format:
		see export_entries_m3u() for the lighter alternative, which drops
		the group and the per-file audio profiles."""
		data = {
			"entries": [e.to_dict() for e in self._entries],
			"track_profiles": self._track_profiles,
		}
		with open(path, "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False, indent=2)

	def export_entries_m3u(self, path):
		"""Write every entry's path (file or folder) to an M3U playlist,
		with a preceding #EXTINF line carrying the entry's custom name
		where one was set - mirrors StationManager.export_favorites_m3u().
		Deliberately lighter than export_entries_json(): the group and any
		per-file audio profiles aren't representable in M3U and are left
		out, same as import_entries_m3u() never restores them. A folder
		entry is written as its own single line (its own path, not each
		track inside it) - import_entries_m3u() tells files and folders
		apart again by checking the path on disk."""
		lines = ["#EXTM3U"]
		for e in self._entries:
			if e.custom_name:
				# Translators: not shown to the user - "-1" is the M3U #EXTINF duration field (meaning "unknown/not applicable", since this is a local file or folder, not a timed stream), kept untranslated; only the following entry name is ever seen (in the file itself, if opened).
				lines.append("#EXTINF:-1,%s" % e.custom_name)
			lines.append(e.path)
		with open(path, "w", encoding="utf-8") as f:
			f.write("\n".join(lines) + "\n")

	def import_entries_json(self, path, merge=True):
		"""Load entries (and their profiles) from a file written by
		export_entries_json(). With merge=True, entries already present
		(by path) are skipped and existing profiles are kept unless the
		import provides one; merge=False replaces the whole library.
		Returns how many entries were newly added. Raises ValueError if
		the file isn't in the expected format."""
		with open(path, "r", encoding="utf-8") as f:
			data = json.load(f)
		if not isinstance(data, dict) or "entries" not in data:
			raise ValueError(_("Not a valid jukebox export file."))
		imported_entries = [JukeboxEntry.from_dict(item) for item in data.get("entries", [])]
		imported_profiles = {
			self._profile_key(k): v for k, v in dict(data.get("track_profiles", {})).items()
		}

		if not merge:
			self._entries = imported_entries
			self._track_profiles = dict(imported_profiles)
			self._save()
			return len(self._entries)

		existing_norms = {os.path.normcase(os.path.normpath(e.path)) for e in self._entries}
		added = 0
		for entry in imported_entries:
			norm = os.path.normcase(os.path.normpath(entry.path))
			if norm in existing_norms:
				continue
			self._entries.append(entry)
			existing_norms.add(norm)
			added += 1
		for key, profile in imported_profiles.items():
			self._track_profiles.setdefault(key, profile)
		self._save()
		return added

	def import_entries_m3u(self, path, merge=True):
		"""Load entries from an M3U playlist written by
		export_entries_m3u() (or any plain M3U of local file/folder paths).
		Only the path and, where a preceding #EXTINF line gave one, a
		custom name are restored - there's no group or per-file audio
		profile to bring back, since M3U never carries them in the first
		place (see export_entries_m3u()'s docstring). A listed path is
		added as a folder entry if it's currently a directory on disk,
		otherwise as a file entry - same validation as add_file()/
		add_folder() (a missing/unreadable/non-audio path is silently
		skipped, same as a dedupe'd path already in the library).

		With merge=True (the default), existing entries are kept and only
		new paths are added. With merge=False, the existing entries are
		replaced outright - but unlike import_entries_json()'s replace,
		the saved per-file audio profiles are left untouched: M3U has
		nothing to replace them *with*, so clearing them here would just
		be silent data loss with no corresponding data gained.

		Returns how many entries were newly added. Raises ValueError if
		the file doesn't look like an M3U playlist at all."""
		with open(path, "r", encoding="utf-8") as f:
			raw_lines = f.read().splitlines()
		if not raw_lines or not raw_lines[0].strip().upper().startswith("#EXTM3U"):
			raise ValueError(_("Not a valid M3U playlist file."))

		parsed = []   # list of (path, custom_name_or_None)
		pending_name = None
		for line in raw_lines[1:]:
			line = line.strip()
			if not line:
				continue
			if line.startswith("#EXTINF:"):
				# Everything after the first comma is the title; the field
				# before it (duration, "-1" in our own exports) is ignored.
				_duration, _sep, title = line.partition(",")
				pending_name = title.strip() or None
				continue
			if line.startswith("#"):
				continue
			parsed.append((line, pending_name))
			pending_name = None

		if not merge:
			self._entries = []

		existing_norms = {os.path.normcase(os.path.normpath(e.path)) for e in self._entries}
		added = 0
		for entry_path, custom_name in parsed:
			norm = os.path.normcase(os.path.normpath(entry_path))
			if norm in existing_norms:
				continue
			if os.path.isdir(entry_path):
				entry, error = self.add_folder(entry_path)
			elif os.path.isfile(entry_path):
				entry, error = self.add_file(entry_path)
			else:
				entry, error = None, None   # Gone from disk - skip quietly, like a dedupe.
			if error or entry is None:
				continue
			if custom_name:
				entry.custom_name = custom_name
				self._save()
			existing_norms.add(norm)
			added += 1
		if not merge:
			# Persist even if the playlist turned out to add nothing (e.g.
			# every path was missing from disk) - the clear-out itself
			# still happened and must stick.
			self._save()
		return added


# --- Disk search -----------------------------------------------------------
#
# Searches every locally attached, ready drive for audio files whose
# filename contains the search text. Deliberately filename-only (not tags/
# metadata) and deliberately synchronous - callers (the Jukebox tab's search
# box) run this on a background thread and marshal results back to the UI
# thread with wx.CallAfter, the same pattern podcast search results already
# use.

# Directory names skipped everywhere to keep a full-disk search fast and to
# avoid wandering into places that are slow, irrelevant, or that Windows
# blocks non-elevated access to anyway.
_SKIP_DIR_NAMES = {
	"$recycle.bin", "system volume information", "windows", "node_modules",
	"__pycache__", ".git", ".svn",
}

# GetDriveTypeW's "network drive" constant - see _get_drive_type()/
# _list_drive_roots() below.
_DRIVE_REMOTE = 4


def _get_drive_type(root):
	"""Return the Windows drive type constant for *root* (e.g. "C:\\") via
	kernel32.GetDriveTypeW - DRIVE_REMOTE (4) identifies a mapped/UNC
	network drive. Returns 0 (DRIVE_UNKNOWN) if the call fails for any
	reason, which _list_drive_roots() treats as "not remote" so a drive
	it couldn't classify is never silently excluded."""
	try:
		return ctypes.windll.kernel32.GetDriveTypeW(root)
	except Exception:
		return 0


def _list_drive_roots(include_network=False):
	"""Return every ready, locally-reachable drive root (e.g. "C:\\",
	"D:\\") - fixed disks, removable drives, and optical drives are all
	included; only drives that fail a basic access check are skipped
	(e.g. an empty optical or card reader).

	Network (mapped/UNC) drives are excluded by default: walking a share
	over SMB means every listdir()/stat() call is a network round trip,
	which can turn a search that takes a second on a local disk into one
	that takes minutes - or hangs outright if the share has gone
	unreachable, since a single blocked filesystem call inside os.walk()
	can't be interrupted by *cancel_event*. Pass include_network=True to
	search them anyway; see search_disk_for_audio()'s include_network
	parameter and the "Search network drives when searching the jukebox"
	setting in settingsPanel.py that controls it."""
	roots = []
	for letter in string.ascii_uppercase:
		root = "%s:\\" % letter
		if not os.path.isdir(root):
			continue
		if not include_network and _get_drive_type(root) == _DRIVE_REMOTE:
			continue
		try:
			os.listdir(root)
		except Exception:
			continue
		roots.append(root)
	return roots


def search_disk_for_audio(query, limit=10000, roots=None, cancel_event=None, include_network=False):
	"""Walk every attached drive (or *roots*, if given) looking for audio
	files whose filename contains *query* (case-insensitive). Stops early
	once *limit* matches are found. If *cancel_event* is given and gets
	set, the walk stops as soon as possible so a fresh search can start
	without waiting for a slow, stale one to finish.

	*include_network* controls whether mapped/UNC network drives are
	included when *roots* isn't given explicitly - see
	_list_drive_roots(). Ignored when *roots* is passed directly, since
	the caller has already decided exactly which roots to search.

	Returns a list of absolute file paths.
	"""
	query = (query or "").strip().lower()
	if not query:
		return []
	results = []
	for root in (roots or _list_drive_roots(include_network=include_network)):
		if cancel_event is not None and cancel_event.is_set():
			break
		for dirpath, dirnames, filenames in os.walk(root):
			if cancel_event is not None and cancel_event.is_set():
				break
			# Prune skip-list directories in place so os.walk doesn't
			# descend into them at all.
			dirnames[:] = [d for d in dirnames if d.lower() not in _SKIP_DIR_NAMES]
			for name in filenames:
				if not _is_audio_file(name):
					continue
				if query in name.lower():
					results.append(os.path.join(dirpath, name))
					if len(results) >= limit:
						return results
	return results