# -*- coding: utf-8 -*-
# freeAudio - Core playback: pause/resume, stop, next/prev station
#
# Extracted from GlobalPlugin in __init__.py. Mixed into GlobalPlugin, so
# `self` here is a GlobalPlugin instance - self._player, self._recorder,
# self._manager, and helper methods defined elsewhere on GlobalPlugin
# (e.g. self._sync_dialog_audio, self._check_internet, self._stop_from_dialog,
# self._open_dialog_on_favorites/_search/_tab, self._announce_now) are used
# as normal instance attributes/methods via the class's MRO, no import
# needed for those.
#
# NOTE: every script here with a default gesture= must also be listed in
# GlobalPlugin's __gestures dict in __init__.py (NVDA's @script(gesture=...)
# auto-registration only sees the literal class a script is defined in, not
# the MRO - see the __gestures comment in __init__.py for details).

import threading

import config
import gui
import ui
import wx
from scriptHandler import script, getLastScriptRepeatCount

import addonHandler
addonHandler.initTranslation()
_tr = globals()["_"]
_ = _tr
del _tr

from . import _notify, _notifications_muted
from . import getem
from . import gutenberg_audiobooks
from . import jukebox
from . import librivox
from . import podcast
from .settingsPanel import freeAudioSettingsPanel


# File extensions that reliably mark a URL as a podcast episode / audio
# book chapter download rather than a live-stream URL. Live streams
# typically have no extension at all (e.g. AudioBook Radio's
# "https://audiobookradio.out.airtime.pro/audiobookradio_a") or a
# playlist extension like ".pls"/".m3u" - neither of which appears here.
# Used by _looks_like_podcast_episode_url() to distinguish a real
# seekable file URL from a live stream, so the "resume last station"
# path can tell them apart even when a tag/position-entry combination
# would otherwise be ambiguous.
_PODCAST_LIKE_EXTENSIONS = (
	".mp3", ".m4a", ".m4b", ".aac", ".ogg", ".oga",
	".opus", ".wav", ".flac", ".mp4",
)


def _looks_like_podcast_episode_url(url):
	"""Return True if *url*'s path ends with an audio-file extension
	typical of a podcast episode / audio-book chapter download.

	Used by _resume_last_station() as a sanity check on both the
	config-persisted "podcast" tag and the "safety net" that infers
	"podcast" from a recorded position entry. Without this check, a live
	stream URL that merely had a stale position entry (or that was ever
	mis-tagged as "podcast" in a prior config) would be resumed as if it
	were a seekable podcast episode - showing "Episode"/"Episode URL" in
	the station-details dialog and refusing to play properly."""
	if not url:
		return False
	try:
		from urllib.parse import urlparse
		import os.path
		path = urlparse(url).path.lower()
		return os.path.splitext(path)[1] in _PODCAST_LIKE_EXTENSIONS
	except Exception:
		return False


class PlaybackCoreMixin:
	"""Pause/resume, stop, next/prev station, and the shared station-playing
	pipeline (_play_station / _start_playing / _on_station_selected /
	_resume_last_station) that other scripts and dialogs call into."""

	@script(
		# Translators: Name of an NVDA command; pauses playback (single press), with double/triple-press doing other actions - see the docstring above.
		description=_("Pause or resume freeAudio playback"),
		category=_("freeAudio"),
		gesture="kb:control+windows+p",
	)
	def script_pauseResume(self, gesture):
		_double_action = config.conf["freeAudio"].get("hotkey_p_double", "none")
		_triple_action = config.conf["freeAudio"].get("hotkey_p_triple", "none")

		def _run_action(action):
			if action == "favorites":
				wx.CallAfter(self._open_dialog_on_favorites)
			elif action == "search":
				wx.CallAfter(self._open_dialog_on_search)
			elif action == "recording":
				wx.CallAfter(self._open_dialog_on_tab, 2)
			elif action == "timer":
				wx.CallAfter(self._open_dialog_on_tab, 3)
			elif action == "liked":
				# Open the browser dialog and switch to the Liked Songs tab (index 4).
				wx.CallAfter(self._open_dialog_on_tab, 4)
			elif action == "settings":
				# Open NVDA Settings directly on the freeAudio category.
				wx.CallAfter(
					gui.mainFrame._popupSettingsDialog,
					gui.NVDASettingsDialog,
					freeAudioSettingsPanel,
				)
			elif action == "announce":
				# Announce the currently playing station without opening any dialog.
				wx.CallAfter(self._announce_now)
			elif action == "stop":
				# Stop radio playback immediately.
				wx.CallAfter(self._stop_from_dialog)

		repeat = getLastScriptRepeatCount()

		# Snapshot playback state once — used only by the single-press handler.
		_has_media  = self._player.has_media()
		_is_playing = self._player.is_playing()
		_last_url   = config.conf["freeAudio"].get("last_station_url", "").strip()
		_action     = config.conf["freeAudio"].get("hotkey_p_action", "resume")

		# Always cancel any pending timer so only the latest press schedules work.
		old_timer = getattr(self, "_pause_resume_timer", None)
		if old_timer:
			old_timer.Stop()
			self._pause_resume_timer = None

		# --- Triple press ---
		if repeat >= 2:
			# The double-press action must NOT have run yet (its timer is cancelled above).
			# Execute the triple action immediately.
			if _triple_action != "none":
				_run_action(_triple_action)
			return

		# --- Double press ---
		if repeat == 1:
			if _double_action == "none":
				return
			# If triple is also configured, delay execution so a third press can cancel it.
			if _triple_action != "none":
				def _do_double():
					self._pause_resume_timer = None
					_run_action(_double_action)
				self._pause_resume_timer = wx.CallLater(350, _do_double)
			else:
				# No triple configured — run double immediately.
				_run_action(_double_action)
			return

		# --- Single press ---
		def _do_single_press():
			self._pause_resume_timer = None
			if _has_media:
				if _is_playing:
					self._player.pause()
					# Translators: Spoken when the pause/resume command pauses playback.
					_notify(_("Paused"))
				else:
					self._player.resume()
					# Translators: Spoken when the pause/resume command resumes playback.
					_notify(_("Playing"))
				return
			if _action == "favorites":
				self._open_dialog_on_favorites()
			else:
				if _last_url:
					self._resume_last_station()

		# If neither double nor triple is configured, act immediately.
		if _double_action == "none" and _triple_action == "none":
			_do_single_press()
			return

		# At least double (or triple) is configured: delay single so further presses can cancel it.
		self._pause_resume_timer = wx.CallLater(350, _do_single_press)

	@script(
		# Translators: Name of an NVDA command; stops freeAudio playback outright (as opposed to pausing).
		description=_("Stop freeAudio playback"),
		category=_("freeAudio"),
		gesture="kb:control+windows+s",
	)
	def script_stop(self, gesture):
		has_instant   = self._recorder.is_recording()
		active_sched  = self._recorder.get_active_scheduled()
		has_scheduled = bool(active_sched)

		if has_instant or has_scheduled:
			# Active recording(s) in progress — inform user and ask for confirmation
			parts = []
			if has_instant:
				# Translators: Line in the stop-confirmation dialog listing an in-progress, immediately-started recording that will be cut off; %s is the station name.
				parts.append(_("Instant recording: %s") % self._recorder.get_station_name())
			for sched_rec in active_sched:
				# Translators: Line in the stop-confirmation dialog listing an active scheduled recording that will be cut off; %s is the station name.
				parts.append(_("Scheduled recording: %s") % sched_rec.station.get("name", "").strip())
			rec_list = "\n".join(parts)
			# Translators: Body text of the confirmation dialog shown when stopping playback would also cut off one or more active recordings; %s is the newline-joined list of affected recordings built just above.
			msg = _(
				"The following recordings are active and will be stopped:\n%s\n\nStop radio and end all recordings?"
			) % rec_list

			def _confirm():
				dlg = wx.MessageDialog(
					gui.mainFrame,
					msg,
					# Translators: Title of the confirmation dialog shown when stopping playback would cut off active recordings.
					_("Active Recordings"),
					wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
				)
				result = dlg.ShowModal()
				dlg.Destroy()
				if result == wx.ID_YES:
					if self._recorder.is_recording():
						self._recorder.stop(self._player)
					self._recorder.stop_active_scheduled()
					if self._player.has_media():
						self._player.stop()
					self._stations      = []
					self._current_index = -1
					# Translators: Spoken after confirming the stop when active recordings were involved.
					_notify(_("freeAudio stopped"))

			wx.CallAfter(_confirm)
			return

		if not self._player.has_media():
			gesture.send()
			return
		self._player.stop()
		self._stations      = []
		self._current_index = -1
		# Translators: Spoken when the stop command is used and there were no active recordings to confirm about.
		_notify(_("freeAudio stopped"))

	@script(
		# Translators: Name of an NVDA command; skips to the next station in the favourites list.
		description=_("Play next station"),
		category=_("freeAudio"),
		gesture="kb:control+windows+rightArrow",
	)
	def script_nextStation(self, gesture):
		favs = self._manager.get_favorites()
		if not favs or not self._player.has_media():
			gesture.send()
			return
		
		current_station = self._player.get_current_station()
		current_uuid = current_station.get("stationuuid", "") if current_station else ""
		
		# Find current index by stationuuid
		if current_uuid:
			for i, s in enumerate(favs):
				if s.get("stationuuid", "") == current_uuid:
					self._current_index = i
					break
			else:
				# If not found, reset to -1
				self._current_index = -1
		else:
			# Fallback to name comparison for backward compatibility
			current_name = self._player.get_current_name()
			fav_names = [s.get("name", "").strip() for s in favs]
			if current_name in fav_names:
				self._current_index = fav_names.index(current_name)
			else:
				self._current_index = -1
		
		self._current_index = (self._current_index + 1) % len(favs)
		self._stations = favs
		self._play_station(favs[self._current_index])

	@script(
		# Translators: Name of an NVDA command; skips to the previous station in the favourites list.
		description=_("Play previous station"),
		category=_("freeAudio"),
		gesture="kb:control+windows+leftArrow",
	)
	def script_prevStation(self, gesture):
		favs = self._manager.get_favorites()
		if not favs or not self._player.has_media():
			gesture.send()
			return
		
		current_station = self._player.get_current_station()
		current_uuid = current_station.get("stationuuid", "") if current_station else ""
		
		# Find current index by stationuuid
		if current_uuid:
			for i, s in enumerate(favs):
				if s.get("stationuuid", "") == current_uuid:
					self._current_index = i
					break
			else:
				# If not found, reset to -1
				self._current_index = -1
		else:
			# Fallback to name comparison for backward compatibility
			current_name = self._player.get_current_name()
			fav_names = [s.get("name", "").strip() for s in favs]
			if current_name in fav_names:
				self._current_index = fav_names.index(current_name)
			else:
				self._current_index = -1
		
		self._current_index = (self._current_index - 1) % len(favs)
		self._stations = favs
		self._play_station(favs[self._current_index])

	def _on_station_selected(self, station, stations, index, announce=True):
		self._stations      = stations
		self._current_index = index
		self._play_station(station, announce)

	def _rebuild_getem_resume_url(self, detail_url, chapter_index):
		"""Re-registers the given audio-book chapter (GETEM or LibriVox)
		with a freshly (re)started local streaming proxy where one is
		needed, and returns a full station_dict for it - or None if that
		isn't possible.

		GETEM chapter audio is never played directly - it's relayed
		through a local proxy (see getem._ensure_proxy_server()) whose
		registered chapter tokens (getem._proxy_chapters) live only in
		memory and are lost every NVDA restart, so simply replaying
		config.conf["freeAudio"]["last_station_url"] (a URL from the
		*previous* session) always 404s even though the proxy itself is
		listening on the same port again. This rebuilds a fresh, valid
		proxy URL for the saved chapter from the book's own library entry -
		looked up independently here since, on this NVDA-startup resume
		path, no RadioDialog exists yet to already have one loaded (see
		GlobalPlugin._download_current_getem_book() for the contrasting
		case where the dialog is guaranteed to exist). LibriVox needs no
		such rebuilding (its chapter URLs are plain public links - see
		librivox.get_stream_url()), but is resolved through the exact same
		module.get_stream_url() call so this method doesn't need to know
		in advance which source *detail_url* belongs to - it just tries
		each library in turn.

		Returns the same shape of station_dict RadioDialog._start_getem_chapter()
		builds (via book.to_dict(), plus name/url/getem_chapter_index/
		audiobook_chapter_title/station_audio) rather than just a bare
		(url, audio_profile) pair - a resumed book previously lost every
		field trackInfoMixin._build_audiobook_details() needs (author,
		narrator, publisher, description, ...), so the station-details
		dialog showed an incomplete "Audio book details" block until the
		same book/chapter was replayed from the Audio Books tab.

		Returns None if the book isn't in either library (e.g. it was
		removed) or its chapter list was never resolved, in which case the
		caller should not attempt to resume playback."""
		if not detail_url:
			return None
		try:
			chapter_index = int(chapter_index)
		except (TypeError, ValueError):
			chapter_index = 0

		book, module = None, None
		for candidate_module, library_cls in (
			(getem, getem.GetemLibrary),
			(librivox, librivox.LibrivoxLibrary),
			(gutenberg_audiobooks, gutenberg_audiobooks.GutenbergLibrary),
		):
			try:
				library = library_cls()
			except Exception:
				continue
			found = library.get_book_by_key(detail_url)
			if found:
				book, module = found, candidate_module
				break
		if not book or not book.chapters:
			return None
		if not (0 <= chapter_index < len(book.chapters)):
			chapter_index = 0
		chapter = book.chapters[chapter_index]
		chapter_url = chapter.get("url")
		if not chapter_url:
			return None
		try:
			stream_url = module.get_stream_url(chapter_url, referer=book.detail_url)
		except Exception:
			return None

		chapter_title = chapter.get("title", book.title)
		station_dict = book.to_dict()
		if book.audio_profile:
			station_dict["station_audio"] = book.audio_profile
		# Same "book — chapter" naming as RadioDialog._start_getem_chapter()/
		# _advance_getem_chapter_headless() below, for the same reason.
		if chapter_title and chapter_title != book.title:
			station_dict["name"] = "%s — %s" % (book.title, chapter_title)
		else:
			station_dict["name"] = book.title
		station_dict["url"] = stream_url
		station_dict["url_resolved"] = stream_url
		# Key resume positions on the chapter's own stable upstream URL,
		# not the session-random proxy URL - see RadioPlayer._podcast_position_key().
		station_dict["podcast_resume_key"] = chapter_url
		station_dict["getem_chapter_index"] = chapter_index
		station_dict["audiobook_chapter_title"] = chapter_title
		return station_dict

	def _advance_getem_chapter_headless(self, station, direction=1):
		"""Move an audio book (GETEM or LibriVox) to its previous/next part
		(*direction* = -1/+1) independent of any dialog UI (list
		selection/focus/"now playing" state) - either because the current
		part finished on its own while the freeAudio dialog isn't open (or
		isn't shown) to do it itself via
		RadioDialog._on_playback_finished()/_play_next_getem_chapter() (see
		GlobalPlugin._on_podcast_finished_ui() in __init__.py, always
		direction=1 for that caller - a part never finishes "backward"),
		or because TimeshiftMixin._handle_track_boundary() decided a
		Ctrl+Win+J/K seek landed too close to this part's start/end to stay
		within it (either direction).

		Returns True if the jump was made, False if there was nowhere to
		jump to (already at the first/last part, or nothing's actually
		loaded/playing) - callers that care (the boundary-jump case does;
		the natural-finish case doesn't) use this to fall back to
		whatever they'd otherwise have done.

		Playback should keep moving forward the same way a podcast
		episode's resume position keeps saving in the background,
		regardless of whether the window happens to be open - so this
		mirrors RadioDialog._start_getem_chapter()'s playback and progress-
		tracking, but without touching any dialog UI, using only the
		playing station's own "getem_detail_url"/"getem_chapter_index"
		fields plus a fresh, dialog-independent library lookup - the same
		pattern _rebuild_getem_resume_url() uses for the NVDA-startup-resume
		case, including trying both libraries since the station's own dict
		doesn't say which source it came from. If the dialog is later
		opened while this is playing,
		RadioDialog._sync_getem_now_playing_from_player() picks its state
		back up from the player, same as it does after a startup resume."""
		# Keyed off "media_kind" rather than the free-text "tags" field - see
		# radioPlayer._is_seekable_media()'s docstring for why matching
		# against "tags" is unsafe (a real Radio Browser station can
		# legitimately carry "audiobook" as a community-assigned genre tag).
		if not station or station.get("media_kind") != "audiobook":
			return False
		detail_url = station.get("getem_detail_url")
		if not detail_url:
			return False
		try:
			chapter_index = int(station.get("getem_chapter_index", 0))
		except (TypeError, ValueError):
			chapter_index = 0

		book, module, library = None, None, None
		for candidate_module, library_cls in (
			(getem, getem.GetemLibrary),
			(librivox, librivox.LibrivoxLibrary),
			(gutenberg_audiobooks, gutenberg_audiobooks.GutenbergLibrary),
		):
			try:
				candidate_library = library_cls()
			except Exception:
				continue
			found = candidate_library.get_book_by_key(detail_url)
			if found:
				book, module, library = found, candidate_module, candidate_library
				break
		if not book or not book.chapters:
			return False
		next_index = chapter_index + direction
		if next_index < 0 or next_index >= len(book.chapters):
			# Reached the start/end of the book - nothing further to jump to.
			return False
		chapter_url = book.chapters[next_index].get("url")
		if not chapter_url:
			return False
		try:
			stream_url = module.get_stream_url(chapter_url, referer=book.detail_url)
		except Exception:
			return False

		library.mark_progress(book, next_index)

		chapter_title = book.chapters[next_index].get("title", book.title)
		station_dict = book.to_dict()
		if book.audio_profile:
			station_dict["station_audio"] = book.audio_profile
		# Book title included alongside the chapter/part title for the
		# same reason as RadioDialog._format_getem_now_playing_name() -
		# this is what gets announced as "what's playing" and shown in
		# Ctrl+Win+I's station info, and a bare chapter label on its own
		# doesn't say which book it belongs to.
		if chapter_title and chapter_title != book.title:
			station_dict["name"] = "%s — %s" % (book.title, chapter_title)
		else:
			station_dict["name"] = book.title
		station_dict["url"] = stream_url
		station_dict["url_resolved"] = stream_url
		# See _rebuild_getem_resume_url() above for why this key is
		# needed here too.
		station_dict["podcast_resume_key"] = chapter_url
		station_dict["getem_chapter_index"] = next_index
		# Kept in sync with RadioDialog._start_getem_chapter() /
		# _rebuild_getem_resume_url() above, which both set this too - see
		# trackInfoMixin._build_audiobook_details()'s "Chapter" row.
		station_dict["audiobook_chapter_title"] = chapter_title
		self._play_station(station_dict)
		return True

	def _advance_jukebox_folder_headless(self, station, direction=1):
		"""Move a jukebox folder to its previous/next track (*direction* =
		-1/+1) independent of any dialog UI - either because the current
		track finished on its own while the freeAudio dialog isn't open
		(or isn't shown) to do it itself via
		RadioDialog._on_playback_finished() (see
		GlobalPlugin._on_podcast_finished_ui() in __init__.py, always
		direction=1 for that caller - a track never finishes "backward"),
		or because TimeshiftMixin._handle_track_boundary() decided a
		Ctrl+Win+J/K seek landed too close to this track's start/end to
		stay within it (either direction).

		Returns True if the jump was made, False if there was nowhere to
		jump to (already at the first/last track in the folder, this
		isn't a folder-sequence track at all, or the folder's gone) - see
		_advance_getem_chapter_headless()'s matching docstring for why
		callers care about this.

		Mirrors _advance_getem_chapter_headless() above: uses only the
		playing station's own "jukebox_folder_path"/"jukebox_track_index"
		fields (set by RadioDialog._play_jukebox_track() when a track is
		played as part of a folder sequence - see its docstring) plus a
		fresh, dialog-independent jukebox.JukeboxManager lookup, rather
		than any dialog state - so a folder keeps playing through in order
		the same way a podcast's resume position keeps saving in the
		background, regardless of whether the window happens to be open."""
		if not station or station.get("media_kind") != "jukebox":
			return False
		folder_path = station.get("jukebox_folder_path")
		if not folder_path:
			# A single file, or a track played directly from the tracks
			# list rather than through a folder sequence - nothing to
			# jump to.
			return False
		try:
			index = int(station.get("jukebox_track_index", -1))
		except (TypeError, ValueError):
			return False

		manager = jukebox.JukeboxManager()
		entry = manager.get_folder_entry(folder_path)
		if not entry:
			return False
		tracks = entry.tracks()
		next_index = index + direction
		if next_index < 0 or next_index >= len(tracks):
			if next_index >= len(tracks):
				# Played through to the last track - clear the saved
				# resume position so the folder starts over from track 1
				# next time, instead of staying "stuck" on the last track
				# forever (see RadioPlayer.save_jukebox_folder_position()).
				try:
					self._player.clear_jukebox_folder_position(folder_path)
				except Exception:
					pass
			# Reached the start/end of the folder - nothing further to jump to.
			return False
		next_track = tracks[next_index]

		station_dict = next_track.to_dict()
		profile = manager.get_track_profile(next_track.path)
		if profile:
			station_dict["station_audio"] = profile
		station_dict["jukebox_folder_path"] = entry.path
		station_dict["jukebox_track_index"] = next_index
		self._play_station(station_dict)
		# If freeAudio's dialog happens to be open and showing this same
		# folder's tracks (e.g. this jump came from a Ctrl+Win+J/K seek
		# while the dialog is visible), keep its selection in sync too -
		# mirrors _on_playback_finished()'s call to the same helper for
		# the natural-finish case. A no-op if the dialog is closed or
		# showing something else.
		dialog = getattr(self, "_dialog", None)
		if dialog:
			try:
				if dialog.IsShown():
					dialog.sync_jukebox_track_selection(entry.path, next_index)
			except Exception:
				pass
		return True

	def _resume_last_station(self):
		url  = config.conf["freeAudio"].get("last_station_url", "").strip()
		name = config.conf["freeAudio"].get("last_station_name", "").strip()
		uuid = config.conf["freeAudio"].get("last_station_uuid", "").strip()

		if not url:
			return

		station = None
		# First try to find by stationuuid
		if uuid:
			for s in self._manager.get_favorites():
				if s.get("stationuuid", "") == uuid:
					station = s
					break

		# If not found by uuid, try by URL
		if station is None:
			for s in self._manager.get_favorites():
				if s.get("url_resolved", "") == url or s.get("url", "") == url:
					station = s
					break

		if station is not None:
			# Found among the user's own favourites, so by construction a
			# plain live radio station - podcast episodes/audiobook
			# chapters/jukebox tracks never end up in favourites (see the
			# comment on the placeholder branch below) - and is played
			# exactly as saved, with none of the "tags"/podcast-position
			# reinterpretation below. That reinterpretation used to run
			# unconditionally, regardless of whether a real favourited
			# station had already been found here: a live station whose
			# own last_station_tags/podcast-position data happened to read
			# "podcast" (e.g. an older, pre-media_kind config that saved a
			# real station's raw "tags" field verbatim - see _play_station()
			# below - or, for a station named/tagged like an audio book
			# station, e.g. "AudioBook Radio", a stale podcast_positions.json
			# entry left over from before that fix) got its "media_kind"
			# overwritten to "podcast"/"audiobook" right here, so it
			# resumed stuck behind the casette.mp3 resume-wait clip trying
			# to seek to a position that was never really this station's
			# own, and its details showed "Episode"/"Episode URL" instead
			# of the normal station fields (trackInfoMixin._build_station_details()
			# keys off the same "media_kind"). A favourited station's own
			# saved dict is trusted as-is instead.
			self._play_station(station)
			return

		tags = config.conf["freeAudio"].get("last_station_tags", "").strip()

		# Sanity-check a config-persisted "podcast" tag against the URL's
		# actual shape before trusting it. This value can be stale AND
		# self-perpetuating: if a live-stream URL ever had a podcast
		# position entry (however that came about), the "safety net"
		# block further down would locally infer tags="podcast" from
		# that entry, _play_station() would then observe
		# station["media_kind"]=="podcast" and persist
		# last_station_tags="podcast" back to config - even after the
		# position entry itself is gone. From that point on, every NVDA
		# startup trusts the persisted tag and reinstates the wrong
		# "podcast" classification forever. A live-stream URL with no
		# audio-file extension and no current position entry is therefore
		# treated as a stale tag, not a real podcast episode.
		if tags == "podcast" and not _looks_like_podcast_episode_url(url):
			if not self._player.has_podcast_position_entry(url):
				tags = ""

		# Safety net for a config saved before "last_station_tags" existed
		# (or any other reason it came back empty): a URL that has a
		# recorded podcast resume position is, by construction, a podcast
		# episode, even without the tag - but only if the URL itself also
		# looks like a podcast episode. Without that shape check, a live
		# stream URL that merely had a stale position entry left over
		# from an old misclassification would be wrongly promoted back to
		# "podcast" here. Only reached past the favourites lookup above,
		# since a favourited station's own kind is never reinterpreted
		# from this - see the comment there.
		if tags != "podcast" and _looks_like_podcast_episode_url(url):
			if self._player.has_podcast_position_entry(url):
				tags = "podcast"

		# Belt-and-suspenders: collapse anything that isn't exactly one of
		# the three values this add-on itself ever writes here down to "".
		# The "==" comparisons below already can't misfire on a multi-word
		# leftover like "Pop, Haber, audiobook" (unlike the old "in"
		# substring test they replaced), but normalising up front means
		# nothing downstream has to reason about any other possible value.
		if tags not in ("podcast", "audiobook", "jukebox"):
			tags = ""

		# Not in favourites - create a minimal station object. Podcast
		# episodes never end up in favourites, so this is always the path
		# they take - carry over the saved "tags" (e.g. "podcast") so
		# _play_station()/RadioPlayer.play() still recognise it as a
		# podcast and seek to the saved position instead of restarting
		# from 0:00.
		station = {
			"name": name, 
			"url": url, 
			"url_resolved": url,
			"stationuuid": uuid, 
			"countrycode": "", 
			"tags": tags, 
			"votes": 0
		}
		# "tags" here is exactly "podcast" or "jukebox" - not the
		# free-text, possibly-multi-value list a real Radio Browser
		# station carries (see radioPlayer._is_seekable_media()'s own
		# docstring for why that distinction matters). It's set from
		# "media_kind" (never from the station's own "tags") by
		# _play_station() below, so it doubles as "media_kind" directly
		# here. Without this, _is_seekable_media() - which only ever
		# checks "media_kind", never "tags" - doesn't recognise the
		# resumed item as podcast-like: seek/speed/pitch and resume-to-
		# saved-position all silently stop working, and it plays back
		# (and responds to commands) like an ordinary live station
		# instead.
		# The GETEM "audiobook" case just below replaces this whole
		# dict with book.to_dict()'s own already-correct "media_kind",
		# so it doesn't need this.
		if tags in ("podcast", "jukebox"):
			station["media_kind"] = tags

		# GETEM audio books need their proxy URL rebuilt fresh every
		# session - see _rebuild_getem_resume_url(). Bail out rather than
		# handing the player a dead URL from the previous session, which
		# would just fail silently a moment later. The rebuilt dict comes
		# straight from the book's own to_dict() (author/narrator/
		# publisher/description/... all included), so it fully replaces
		# the minimal placeholder built above rather than just patching a
		# couple of URL fields onto it - see _rebuild_getem_resume_url()'s
		# docstring for why the placeholder alone left the station-details
		# dialog showing an incomplete "Audio book details" block.
		if tags == "audiobook":
			detail_url = config.conf["freeAudio"].get("last_station_getem_detail_url", "").strip()
			chapter_index = config.conf["freeAudio"].get("last_station_getem_chapter_index", 0)
			rebuilt = self._rebuild_getem_resume_url(detail_url, chapter_index)
			if not rebuilt:
				# Translators: Spoken on NVDA startup when resuming the last-played audio book fails because the book is no longer in the user's library.
				ui.message(_(
					"Could not resume the last audio book - it may have been "
					"removed from your library."
				))
				return
			station = rebuilt
		elif tags == "podcast":
			# Likewise, re-apply the subscribed feed's saved audio profile
			# (if any) - see _on_episode_play()/_play_station(). Unlike the
			# audiobook case, the episode URL itself is still perfectly
			# playable on its own, so a missing/removed feed just means no
			# profile (or author) to add rather than a reason to give up
			# resuming.
			feed_url = config.conf["freeAudio"].get("last_station_podcast_feed_url", "").strip()
			if feed_url:
				try:
					feed = podcast.PodcastManager().get_feed_by_url(feed_url)
				except Exception:
					feed = None
				if feed:
					station.setdefault("podcast_feed_url", feed_url)
					if feed.audio_profile:
						station["station_audio"] = feed.audio_profile
					# PodcastFeed.to_dict() persists title/author/description
					# to disk independently of its episodes list (episodes
					# themselves are never persisted - see
					# PodcastManager.load()), so the feed author survives a
					# restart and can be restored here even though the
					# episode's own description cannot be (that would need a
					# network feed refresh, which startup resume
					# deliberately doesn't do) - see
					# trackInfoMixin._build_podcast_details().
					if feed.author:
						station["podcast_author"] = feed.author

		self._play_station(station)

	def _play_station(self, station, announce=True):
		# Translators: Fallback station name used in log/error contexts if the station dict has no name field.
		name         = station.get("name", _("Unknown station")).strip()
		url_resolved = station.get("url_resolved", "")
		url          = url_resolved or station.get("url", "")
		station_uuid = station.get("stationuuid", "")

		if not url:
			# Translators: Spoken when trying to play a station that has no resolvable stream URL at all.
			ui.message(_("No stream URL available for this station"))
			return

		# Check internet connectivity before attempting to stream - not
		# applicable to jukebox tracks, which are local files (see
		# jukebox.JukeboxTrack.to_dict()) and never touch the network
		# regardless of whether one's available. Also skipped if the user
		# has disabled this check in settings.
		if station.get("media_kind") != "jukebox" and not config.conf["freeAudio"].get("disable_internet_check", False):
			if not self._check_internet():
				# Translators: Spoken when trying to play a station but the internet-connectivity pre-check fails.
				ui.message(_("No internet connection. Please check your connection and try again."))
				return

		try:
			config.conf["freeAudio"]["last_station_url"]  = url_resolved or url
			config.conf["freeAudio"]["last_station_name"] = name
			config.conf["freeAudio"]["last_station_uuid"] = station_uuid
			# Needed so a podcast episode/audio book/jukebox track resumed on
			# the next NVDA startup is still recognised as such (see
			# _resume_last_station) - without this, the reconstructed station
			# dict has no usable kind info and resume-to-saved-position never
			# triggers, so it silently restarts from 0:00 instead of
			# resuming. Keyed off "media_kind" rather than the free-text
			# "tags" field - see the comment on _advance_getem_chapter_headless()
			# above for why matching a live station's real genre tags is
			# unsafe: a live Radio Browser station (even a favourited one)
			# can legitimately carry "podcast"/"audiobook"/"jukebox" as a
			# community-assigned genre tag, and saving its raw "tags" here
			# verbatim made such a station wrongly get treated as an audio
			# book/podcast/jukebox item - and then fail to resume at all,
			# since it has no actual GETEM/podcast/jukebox data behind it -
			# on the next NVDA startup.
			_last_media_kind = station.get("media_kind")
			config.conf["freeAudio"]["last_station_tags"] = (
				_last_media_kind if _last_media_kind in ("podcast", "audiobook", "jukebox") else ""
			)
			# GETEM audio books additionally need to know which book/part
			# this was, so _resume_last_station() can rebuild a fresh proxy
			# URL for it on the next NVDA startup (last_station_url's proxy
			# URL from *this* session is dead by then - see
			# _rebuild_getem_resume_url()). Cleared to blank/0 for anything
			# else so a stale audiobook resume hint never lingers once the
			# user moves on to a station or podcast. Keyed off "media_kind"
			# rather than "tags" - see the comment on _advance_getem_chapter_headless()
			# above for why matching a live station's real genre tags is unsafe.
			if station.get("media_kind") == "audiobook":
				config.conf["freeAudio"]["last_station_getem_detail_url"] = station.get("getem_detail_url", "") or ""
				config.conf["freeAudio"]["last_station_getem_chapter_index"] = int(station.get("getem_chapter_index", 0) or 0)
			else:
				config.conf["freeAudio"]["last_station_getem_detail_url"] = ""
				config.conf["freeAudio"]["last_station_getem_chapter_index"] = 0
			# Same idea for a subscribed podcast feed's saved audio profile -
			# see _on_episode_play()/_resume_last_station(). Keyed off
			# "media_kind" rather than "tags" for the same reason as above;
			# GETEM/LibriVox chapters carry media_kind="audiobook" (never
			# "podcast"), so no separate exclusion is needed here anymore.
			if station.get("media_kind") == "podcast":
				config.conf["freeAudio"]["last_station_podcast_feed_url"] = station.get("podcast_feed_url", "") or ""
			else:
				config.conf["freeAudio"]["last_station_podcast_feed_url"] = ""
		except Exception:
			pass

		# Remember which track of a jukebox folder sequence this is, so the
		# folder can resume here next time it's played (see
		# RadioPlayer.save_jukebox_folder_position() and
		# RadioDialog._on_jukebox_entry_play()). Only set for tracks played
		# as part of a folder (_play_jukebox_folder_track()/
		# _advance_jukebox_folder_headless()) - a track played on its own
		# has no "jukebox_folder_path" and nothing to save here.
		folder_path = station.get("jukebox_folder_path")
		if folder_path:
			try:
				self._player.save_jukebox_folder_position(
					folder_path, station.get("jukebox_track_index", 0), url_resolved or url,
				)
			except Exception:
				pass

		# Apply station-specific audio profile if one exists, else restore global settings
		station_audio = station.get("station_audio")
		# This flag just means "tempo-capable local-ish media that
		# speed/transpose apply to" - podcast episodes, GETEM/LibriVox
		# audiobook chapters, and jukebox tracks all qualify. Keyed off
		# "media_kind" rather than "tags": unlike "media_kind", which is
		# only ever set internally (see radioPlayer._is_seekable_media()'s
		# docstring), a live Radio Browser station's "tags" is free-text
		# and can legitimately contain any of these words as a genre tag.
		is_podcast_like = station.get("media_kind") in ("podcast", "audiobook", "jukebox")

		# Everything below this point either waits on a blocking bass_host
		# IPC round-trip (RadioPlayer.play() -> _save_current_podcast_position_if_playing()
		# -> timeshift_status(); set_playback_rate_value()/set_transpose_value()
		# -> their bass_host "set_playback_rate"/"set_transpose" commands,
		# all of which do evt.wait(timeout=3.0) in _BassSubprocessEngine) or
		# feeds into one of those calls. _play_station() itself always runs
		# on NVDA's main/core thread (it's reached via wx.CallAfter from
		# _on_playback_finished()/_advance_jukebox_folder_headless(), or
		# directly from a script_* handler), so doing this work inline used
		# to stall NVDA's speech/input handling for as long as those
		# round-trips took - most noticeable as a brief freeze on every
		# jukebox folder track auto-advance, since is_podcast_like is True
		# for jukebox tracks and both set_playback_rate_value()/
		# set_transpose_value() are called for every one of them. Moving it
		# into a background thread keeps the same ordering/behaviour but
		# gets it off the thread NVDA itself depends on - only the pieces
		# that actually touch wx GUI state (_sync_dialog_audio, and
		# ui.message for the announce) are marshalled back with
		# wx.CallAfter. self._player.set_volume()/set_fx()/set_eq_gain()
		# are already fire-and-forget (no reply waited on), so they're kept
		# here unchanged - no benefit to moving them, and keeping them here
		# means _sync_dialog_audio() (below) reflects them immediately.
		def _apply_profile_and_play():
			if station_audio:
				vol = station_audio.get("volume", config.conf["freeAudio"]["volume"])
				fx  = station_audio.get("fx", "none")
				self._player.set_volume(vol)
				try:
					self._player.set_fx(fx)
				except Exception:
					pass
				# Apply station-specific EQ gains if present
				eq_gains = station_audio.get("eq_gains", {})
				for band, gain_db in eq_gains.items():
					try:
						self._player.set_eq_gain(band, gain_db)
					except Exception:
						pass
				wx.CallAfter(self._sync_dialog_audio, vol, fx, eq_gains=eq_gains)
			else:
				# Restore global settings
				global_vol = config.conf["freeAudio"]["volume"]
				global_fx  = config.conf["freeAudio"].get("audio_fx", "none")
				self._player.set_volume(global_vol)
				try:
					self._player.set_fx(global_fx)
				except Exception:
					pass
				# Restore global EQ gains
				_eq_defaults = {"eq_bass": 9, "eq_treble": 9, "eq_vocal": 6}
				for band, default_db in _eq_defaults.items():
					gain_db = config.conf["freeAudio"].get("eq_gain_" + band, default_db)
					try:
						self._player.set_eq_gain(band, gain_db)
					except Exception:
						pass
				wx.CallAfter(self._sync_dialog_audio, global_vol, global_fx)

			# Playback speed - podcasts/audio books only (pitch-preserving
			# tempo change, see RadioPlayer.set_playback_rate_value). Handled
			# as its own step, independent of the volume/fx branch above, so
			# it follows the same "per-item, falls back to normal 1.0x when
			# nothing is saved" rule volume/fx already follow rather than
			# staying sticky: leaving a fast-profiled book for one with no
			# profile of its own must land back on normal speed, or the second
			# book plays at whatever rate the first one left behind.
			if is_podcast_like:
				speed = station_audio.get("speed") if station_audio else None
				try:
					self._player.set_playback_rate_value(speed if speed else 1.0)
				except Exception:
					pass
				# Pitch transpose follows the same per-item, falls-back-to-normal
				# rule as speed just above, for the same reason: leaving a
				# transposed track for one with no saved transpose of its own
				# must land back on 0.0 (no shift), not carry the previous
				# track's shift over.
				transpose = station_audio.get("transpose") if station_audio else None
				try:
					self._player.set_transpose_value(transpose if transpose else 0.0)
				except Exception:
					pass

			self._icy_last_title  = None        # None = station just changed; suppress first read
			# station is passed as an explicit argument (not stashed on self and
			# read back later) so a second _play_station() call racing in
			# before this one's deferred _start_playing() runs can't clobber
			# it - each call gets its own independently-captured url/station
			# pair, however close together they happen or however this
			# background thread/wx.CallAfter ends up ordering them.
			# Previously these went through self._pending_url/self._pending_station,
			# which a fast-arriving second call (e.g. a duplicate/near-
			# simultaneous GETEM chapter auto-advance) could overwrite before
			# the first call's _start_playing() had a chance to read them -
			# the audio that actually started playing would then get tagged
			# with a *different* chapter's metadata than the one actually
			# streaming. _start_playing() itself calls RadioPlayer.play(),
			# which still needs to run somewhere - it used to be re-marshalled
			# onto the main thread via wx.CallAfter for no real reason (its
			# own blocking work is already pushed into RadioPlayer._bg_launch()
			# on a further background thread), so it's simply called directly
			# here rather than bounced back to the thread we just moved off of.
			self._start_playing(url, name, url_resolved, station)
			if announce:
				if not _notifications_muted():
					wx.CallAfter(ui.message, name)

		threading.Thread(
			target=_apply_profile_and_play, daemon=True, name="freeAudio-play-station"
		).start()

	def _format_transpose(self, semitones):
		"""Format a transpose value for announcement, e.g. "+1.25 semitones",
		"-0.5 semitones", or "Normal pitch" for 0.0."""
		if abs(semitones) < 0.001:
			# Translators: Spoken by the pitch-transpose commands when the current transpose value is back to 0 (no pitch shift applied).
			return _("Normal pitch")
		# Translators: %.2f = signed semitone value, e.g. "+1.25 semitones"
		return _("%+.2f semitones") % semitones

	@script(
		# Translators: Name of an NVDA command; raises the pitch of podcasts/audio books/jukebox tracks without changing playback speed.
		description=_("Raise pitch transpose (podcasts, audio books and jukebox tracks)"),
		category=_("freeAudio"),
		gesture="kb:shift+windows+k",
	)
	def script_transposeUp(self, gesture):
		applied, value, reason = self._player.increase_transpose()
		if applied:
			_notify(self._format_transpose(value))
		elif reason == "not_tempo_stream":
			# Translators: Spoken when the pitch-transpose commands are used while playing a live radio station rather than a podcast/audiobook/jukebox track.
			_notify(_("Transpose only applies to podcasts, audio books and jukebox tracks"))
		elif reason == "bass_fx_unavailable":
			# Translators: Spoken when pitch transpose can't be applied because the optional bass_fx library isn't installed.
			_notify(_("Transpose requires the bass_fx audio component, which isn't available"))
		else:
			_notify(self._format_transpose(value))

	@script(
		# Translators: Name of an NVDA command; lowers the pitch of podcasts/audio books/jukebox tracks without changing playback speed.
		description=_("Lower pitch transpose (podcasts, audio books and jukebox tracks)"),
		category=_("freeAudio"),
		gesture="kb:shift+windows+j",
	)
	def script_transposeDown(self, gesture):
		applied, value, reason = self._player.decrease_transpose()
		if applied:
			_notify(self._format_transpose(value))
		elif reason == "not_tempo_stream":
			# Translators: Same as the transposeUp case above: spoken when transpose is used on a live radio station.
			_notify(_("Transpose only applies to podcasts, audio books and jukebox tracks"))
		elif reason == "bass_fx_unavailable":
			# Translators: Same as the transposeUp case above: spoken when bass_fx isn't installed.
			_notify(_("Transpose requires the bass_fx audio component, which isn't available"))
		else:
			_notify(self._format_transpose(value))

	def _start_playing(self, url, name, url_resolved="", station=None):
		try:
			self._player.play(url, name, url_resolved=url_resolved, station=station or {})
		except Exception as e:
			# Only caller now is _play_station()'s _apply_profile_and_play()
			# background thread (see its comment on why it calls this
			# directly rather than via wx.CallAfter) - ui.message needs to
			# stay marshalled onto the main thread from here since we're not
			# on it.
			# Translators: Spoken when actually starting playback of a station/track fails with an exception; %s is the error message.
			wx.CallAfter(ui.message, _("Could not play station: %s") % str(e))