# -*- coding: utf-8 -*-
# freeAudio - "Clean up" dialog (reset settings / delete saved data).
#
# Opened from the freeAudio settings category (settingsPanel.py). Lists
# everything freeAudio stores in the NVDA user configuration folder as check boxes - none checked by default - and resets or
# deletes whatever the user ticks, after a second confirmation.
#
# Deliberately NOT in the list: the recordings (the recordings folder and the
# files in it) and the saved liked-songs text file. The recordings folder
# setting and the liked-songs setting are also left as they are when the
# settings are reset.

import logging
import os
import shutil

import config
import globalVars
import gui
from gui import guiHelper, nvdaControls
import wx

import addonHandler
addonHandler.initTranslation()
_tr = globals()["_"]
_ = _tr
del _tr

log = logging.getLogger(__name__)

# Settings that a settings reset must not touch.
#  legacy_migrated  - resetting it would re-import the old FreeRadio data.
#  recordings_dir / save_liked_songs - recordings and liked songs are outside
#                     this feature on purpose.
_KEEP_SETTINGS = ("legacy_migrated", "recordings_dir", "save_liked_songs")


def _cfg_path(name):
	return os.path.join(globalVars.appArgs.configPath, name)


def _path_size(path):
	"""Total size in bytes of a file or folder (0 if it doesn't exist)."""
	try:
		if os.path.isfile(path):
			return os.path.getsize(path)
		total = 0
		for root, _dirs, files in os.walk(path):
			for name in files:
				try:
					total += os.path.getsize(os.path.join(root, name))
				except OSError:
					pass
		return total
	except OSError:
		return 0


def _format_size(size):
	if size < 1024:
		return "%d B" % size
	if size < 1024 * 1024:
		return "%.1f KB" % (size / 1024.0)
	return "%.1f MB" % (size / (1024.0 * 1024.0))


def _build_items():
	"""The list shown in the dialog: (key, label, [paths used to show a size])."""
	return [
		(
			"settings",
			# Translators: Check box in the clean-up dialog; resets freeAudio's settings to their defaults.
			_("Settings (reset to defaults; the recordings folder and the liked songs option are kept)"),
			[],
		),
		(
			"favorites",
			# Translators: Check box in the clean-up dialog; deletes the favourite stations list.
			_("Favorite stations"),
			[_cfg_path("freeAudio_favorites.json")],
		),
		(
			"catalog",
			# Translators: Check box in the clean-up dialog; deletes the downloaded station list cache.
			_("Station list cache (downloaded again when needed)"),
			[_cfg_path("freeAudio_stations_cache.json.gz")],
		),
		(
			"podcasts",
			# Translators: Check box in the clean-up dialog; deletes the podcast subscriptions.
			_("Podcast subscriptions"),
			[_cfg_path("freeAudio_podcasts.json")],
		),
		(
			"audiobooks",
			# Translators: Check box in the clean-up dialog; deletes the audio book libraries of all sources.
			_("Audio book libraries (GETEM, LibriVox, Project Gutenberg, Internet Archive)"),
			[
				_cfg_path("freeAudio_getem_library.json"),
				_cfg_path("freeAudio_librivox_library.json"),
				_cfg_path("freeAudio_gutenberg_audiobooks_library.json"),
				_cfg_path("freeAudio_archive_audiobooks_library.json"),
			],
		),
		(
			"getem_login",
			# Translators: Check box in the clean-up dialog; deletes the saved GETEM user name and password.
			_("Saved GETEM login"),
			[_cfg_path("freeAudio_getem_credentials.bin")],
		),
		(
			"jukebox",
			# Translators: Check box in the clean-up dialog; empties the Jukebox list (the music files themselves are not touched).
			_("Jukebox list (your music files are not deleted)"),
			[_cfg_path("freeAudio_jukebox.json")],
		),
		(
			"positions",
			# Translators: Check box in the clean-up dialog; deletes saved resume positions.
			_("Saved resume positions (podcasts, audio books, Jukebox folders)"),
			[
				_cfg_path("podcast_positions.json"),
				_cfg_path("jukebox_folder_positions.json"),
			],
		),
		(
			"bookmarks",
			# Translators: Check box in the clean-up dialog; deletes all bookmarks of audio books, podcast episodes and jukebox tracks, including their voice notes.
			_("Bookmarks (including their text and voice notes)"),
			[
				_cfg_path("freeAudio_bookmarks.json"),
				_cfg_path("freeAudio_bookmark_audio"),
			],
		),
		(
			"timers",
			# Translators: Check box in the clean-up dialog; deletes sleep timers and alarms.
			_("Sleep timers and alarms"),
			[_cfg_path("freeAudio_timers.json")],
		),
		(
			"schedules",
			# Translators: Check box in the clean-up dialog; deletes the scheduled recording plans (not the recordings).
			_("Scheduled recording plans (recordings themselves are not deleted)"),
			[_cfg_path("freeAudio_schedules.json")],
		),
	]


def _remove_path(path):
	"""Delete a file or folder. A missing path counts as success."""
	try:
		if os.path.isdir(path):
			shutil.rmtree(path)
		elif os.path.exists(path):
			os.remove(path)
		return True
	except OSError:
		log.warning("freeAudio: could not delete %s", path, exc_info=True)
		return False


def _reset_settings():
	from configobj.validate import Validator
	section = config.conf["freeAudio"]
	spec = config.conf.spec["freeAudio"]
	validator = Validator()
	for key in list(spec):
		if key in _KEEP_SETTINGS:
			continue
		try:
			section[key] = validator.get_default_value(spec[key])
		except Exception:
			log.debug("freeAudio: could not reset setting %s", key, exc_info=True)
	try:
		config.conf.save()
	except Exception:
		log.debug("freeAudio: could not save settings after reset", exc_info=True)
	return True


def perform_reset(keys, plugin):
	"""Reset/delete the chosen items. Returns the list of keys that failed.

	The running add-on keeps most of this data in memory and writes it back
	to disk later, so deleting only the files would let it reappear. Each
	branch clears the in-memory copy too.
	"""
	keys = set(keys)
	failed = []

	# The station browser keeps lists and libraries in memory; close it so it
	# is rebuilt from disk the next time it is opened.
	if plugin is not None and keys - {"settings"}:
		dialog = getattr(plugin, "_dialog", None)
		if dialog is not None:
			try:
				dialog._force_destroy()
			except Exception:
				log.debug("freeAudio: could not close the station browser", exc_info=True)
			plugin._dialog = None

	paths_by_key = {key: paths for key, _label, paths in _build_items()}

	for key in (
		"favorites", "catalog", "podcasts", "audiobooks", "getem_login",
		"jukebox", "positions", "bookmarks", "timers", "schedules",
	):
		if key not in keys:
			continue
		ok = True
		try:
			if key == "favorites" and plugin is not None:
				plugin._manager._favorites.clear()
			elif key == "catalog" and plugin is not None:
				plugin._manager._catalog = None
			elif key == "positions" and plugin is not None:
				player = plugin._player
				with player._podcast_positions_lock:
					player._podcast_positions.clear()
				with player._jukebox_folder_positions_lock:
					player._jukebox_folder_positions.clear()
			elif key == "bookmarks":
				from . import bookmarks
				bookmarks.get_manager().clear_all()
				if plugin is not None:
					plugin._player.clear_loop()
			elif key == "timers" and plugin is not None:
				manager = plugin._timer_manager
				for entry in manager.get_timers():
					manager.remove(entry[0])
			elif key == "schedules" and plugin is not None:
				recorder = plugin._recorder
				for rec in recorder.get_schedules():
					recorder.remove_schedule(rec)
		except Exception:
			log.warning("freeAudio: could not clear in-memory data for %s", key, exc_info=True)
			ok = False
		for path in paths_by_key.get(key, []):
			if not _remove_path(path):
				ok = False
		# Things built from the data need rebuilding.
		if plugin is not None:
			try:
				if key == "favorites":
					plugin._rebuild_station_scripts()
				elif key == "jukebox":
					plugin._rebuild_jukebox_scripts()
			except Exception:
				log.debug("freeAudio: could not rebuild scripts after %s", key, exc_info=True)
		if not ok:
			failed.append(key)

	if "settings" in keys:
		try:
			_reset_settings()
		except Exception:
			log.warning("freeAudio: settings reset failed", exc_info=True)
			failed.append("settings")

	return failed


class ResetDialog(wx.Dialog):

	def __init__(self, parent, plugin):
		super().__init__(
			parent,
			# Translators: Title of the clean-up dialog opened from freeAudio's settings.
			title=_("Reset settings / delete saved data"),
		)
		self._plugin = plugin
		self.settings_reset = False
		self._items = _build_items()

		main = wx.BoxSizer(wx.VERTICAL)
		helper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		labels = []
		for key, label, paths in self._items:
			size = sum(_path_size(p) for p in paths)
			if paths:
				if size > 0:
					label = "%s - %s" % (label, _format_size(size))
				else:
					# Translators: Added after a clean-up item's name when there is nothing saved for it.
					label = "%s - %s" % (label, _("nothing saved"))
			labels.append(label)

		self._list = helper.addLabeledControl(
			# Translators: Label of the check list in the clean-up dialog.
			_("Select what to reset or delete (nothing is selected by default):"),
			nvdaControls.CustomCheckListBox,
			choices=labels,
		)
		self._list.SetSelection(0)

		# Translators: Note in the clean-up dialog.
		note = wx.StaticText(self, label=_("Recordings and liked songs are never touched by this."))
		helper.addItem(note)

		buttons = guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: Button in the clean-up dialog; checks every item.
		select_all = buttons.addButton(self, label=_("Select &all"))
		select_all.Bind(wx.EVT_BUTTON, self._on_select_all)
		# Translators: Button in the clean-up dialog; resets/deletes the checked items.
		self._go_btn = buttons.addButton(self, label=_("&Reset / delete selected"))
		self._go_btn.Bind(wx.EVT_BUTTON, self._on_go)
		close_btn = buttons.addButton(self, id=wx.ID_CANCEL)
		# Translators: Button in the clean-up dialog; closes it without doing anything.
		close_btn.SetLabel(_("&Cancel"))
		helper.addItem(buttons.sizer)

		main.Add(helper.sizer, border=guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.SetSizer(main)
		main.Fit(self)
		self.SetEscapeId(wx.ID_CANCEL)
		self.CentreOnScreen()
		self._list.SetFocus()

	def _on_select_all(self, event):
		for i in range(self._list.GetCount()):
			self._list.Check(i, True)
		self._list.SetFocus()

	def _checked_keys(self):
		return [
			self._items[i][0]
			for i in range(self._list.GetCount())
			if self._list.IsChecked(i)
		]

	def _label_for(self, key):
		for item_key, label, _paths in self._items:
			if item_key == key:
				return label
		return key

	def _on_go(self, event):
		keys = self._checked_keys()
		if not keys:
			gui.messageBox(
				# Translators: Shown in the clean-up dialog when the reset/delete button is pressed with nothing checked.
				_("Nothing is selected."),
				# Translators: Title of messages shown by the clean-up dialog.
				_("freeAudio"),
				wx.OK | wx.ICON_INFORMATION,
				self,
			)
			self._list.SetFocus()
			return

		names = "\n".join("- " + self._label_for(k) for k in keys)
		answer = gui.messageBox(
			# Translators: Confirmation in the clean-up dialog. {items} is the list of checked items, one per line.
			_("The following will be reset or deleted. This cannot be undone.\n\n{items}\n\nContinue?").format(
				items=names
			),
			_("freeAudio"),
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
			self,
		)
		if answer != wx.YES:
			self._list.SetFocus()
			return

		failed = perform_reset(keys, self._plugin)
		self.settings_reset = "settings" in keys and "settings" not in failed

		if failed:
			message = (
				# Translators: Shown after the clean-up when some items could not be removed. {items} is the list, one per line.
				_("Done, except for the following, which could not be removed (a file may be in use):\n\n{items}").format(
					items="\n".join("- " + self._label_for(k) for k in failed)
				)
			)
			icon = wx.ICON_WARNING
		else:
			# Translators: Shown after the clean-up finished without problems.
			message = _("Done.")
			icon = wx.ICON_INFORMATION
		if self.settings_reset:
			message += "\n\n" + (
				# Translators: Added to the clean-up result when settings were reset.
				_("Settings were reset. Changes made on the freeAudio settings page before this will not be saved. "
				"Restarting NVDA is recommended so every setting takes effect.")
			)
		gui.messageBox(message, _("freeAudio"), wx.OK | icon, self)
		self.EndModal(wx.ID_OK)
