# -*- coding: utf-8 -*-
# freeAudio - Bookmark list widget used by the Podcasts, Audio Books and
# Jukebox tabs of the station browser dialog: the list itself, '.'-marking,
# the context menu and its actions, and the voice-note recording dialog.

import ctypes
import os

import ui
import wx

import addonHandler
addonHandler.initTranslation()
_tr = globals()["_"]
_ = _tr
del _tr
ngettext = globals().get("ngettext", lambda s, p, n: s if n == 1 else p)

from . import bookmarks


class BookmarkEntry:
	def __init__(self, key, bookmark, prefix="", extra=None):
		self.key = key
		self.bookmark = bookmark
		self.prefix = prefix
		self.extra = extra   # owner-defined (e.g. chapter index for audio books)


class VoiceRecorder:
	"""Records the default microphone to a .wav file through the Windows
	MCI interface (no extra dependencies)."""

	_ALIAS = "freeAudioBookmarkRec"

	def __init__(self):
		self._open = False

	def _mci(self, command):
		buf = ctypes.create_unicode_buffer(255)
		return ctypes.windll.winmm.mciSendStringW(command, buf, 254, 0)

	def start(self):
		self._mci("close " + self._ALIAS)
		if self._mci("open new type waveaudio alias " + self._ALIAS) != 0:
			return False
		self._open = True
		if self._mci("record " + self._ALIAS) != 0:
			self.cancel()
			return False
		return True

	def stop_and_save(self, path):
		if not self._open:
			return False
		self._mci("stop " + self._ALIAS)
		err = self._mci('save %s "%s"' % (self._ALIAS, path))
		self._mci("close " + self._ALIAS)
		self._open = False
		return err == 0

	def cancel(self):
		if self._open:
			self._mci("stop " + self._ALIAS)
			self._mci("close " + self._ALIAS)
			self._open = False


class VoiceNoteDialog(wx.Dialog):
	"""Starts recording as soon as it opens; OK saves, Cancel discards."""

	def __init__(self, parent, out_path):
		# Translators: Title of the dialog used to record a voice note for a bookmark.
		super().__init__(parent, title=_("Voice Note"))
		self._out_path = out_path
		self._recorder = VoiceRecorder()
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(
			# Translators: Text of the voice-note recording dialog.
			wx.StaticText(self, label=_("Recording from the microphone. Press Stop and Save when you are done.")),
			0, wx.ALL, 10,
		)
		btns = wx.StdDialogButtonSizer()
		# Translators: Button label; stops the voice-note recording and saves it to the bookmark.
		ok_btn = wx.Button(self, wx.ID_OK, label=_("&Stop and Save"))
		ok_btn.SetDefault()
		cancel_btn = wx.Button(self, wx.ID_CANCEL)
		btns.AddButton(ok_btn)
		btns.AddButton(cancel_btn)
		btns.Realize()
		sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 8)
		self.SetSizer(sizer)
		self.Fit()
		ok_btn.Bind(wx.EVT_BUTTON, self._on_ok)
		cancel_btn.Bind(wx.EVT_BUTTON, self._on_cancel)
		self.Bind(wx.EVT_CLOSE, self._on_cancel)
		wx.CallAfter(self._start)

	def _start(self):
		if not self._recorder.start():
			# Translators: Spoken when the microphone can't be opened for a voice note.
			ui.message(_("Could not start recording. Check that a microphone is available."))
			self.EndModal(wx.ID_CANCEL)
			return
		# Translators: Spoken when voice-note recording has started.
		ui.message(_("Recording"))

	def _on_ok(self, event):
		if self._recorder.stop_and_save(self._out_path):
			self.EndModal(wx.ID_OK)
		else:
			# Translators: Spoken when the recorded voice note could not be saved.
			ui.message(_("Could not save the voice note"))
			self.EndModal(wx.ID_CANCEL)

	def _on_cancel(self, event):
		self._recorder.cancel()
		self.EndModal(wx.ID_CANCEL)


class BookmarkList:
	"""A labelled list of the bookmarks of whatever item is currently
	selected in the owning tab.

	*provider* returns [(key, label_prefix, extra), ...] - the item key(s)
	whose bookmarks to list. *start_fn(entry)* starts playing the item the
	entry belongs to (its resume position has already been set).
	*source_fn(entry)* (optional) describes where the entry's item can be
	read from, as a dict for excerptExport.start_excerpt(); it is what
	enables "Save Excerpt Between Marked Bookmarks"."""

	def __init__(self, dialog, panel, sizer, provider, start_fn, source_fn=None):
		self._dialog = dialog
		self._provider = provider
		self._start_fn = start_fn
		self._source_fn = source_fn
		self._entries = []
		self._marked = set()   # bookmark ids
		self._pending_id = None

		# Translators: Label above the list of bookmarks of the selected podcast episode / audio book / jukebox track.
		label = wx.StaticText(panel, label=_("Bookmarks:"))
		self.listbox = wx.ListBox(panel, style=wx.LB_SINGLE)
		# Translators: Accessible name of the bookmarks list.
		self.listbox.SetName(_("Bookmarks of the selected item"))
		self.listbox.SetMinSize((-1, 70))
		sizer.Add(label, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 8)
		sizer.Add(self.listbox, 0, wx.EXPAND | wx.ALL, 8)
		self.listbox.Bind(wx.EVT_SET_FOCUS, self._on_focus)

	# -- list contents -----------------------------------------------------

	def _label(self, entry):
		from . import _format_duration
		mgr = bookmarks.get_manager()
		bm = entry.bookmark
		text = "%s — %s" % (mgr.display_name(entry.key, bm), _format_duration(bm.position))
		if entry.prefix:
			# Part (chapter) the bookmark belongs to, shown after the bookmark itself.
			text += " — " + entry.prefix
		if bm.text:
			# Translators: Marker appended to a bookmark's list row when it has a text note.
			text += " " + _("[text]")
		if bm.audio:
			# Translators: Marker appended to a bookmark's list row when it has a voice note.
			text += " " + _("[voice note]")
		return self._dialog._with_marked_suffix(text, bm.id in self._marked)

	def selected(self):
		idx = self.listbox.GetSelection()
		if idx == wx.NOT_FOUND or idx >= len(self._entries):
			return None
		return self._entries[idx]

	def marked_entries(self):
		return [e for e in self._entries if e.bookmark.id in self._marked]

	def refresh(self):
		mgr = bookmarks.get_manager()
		current = self.selected()
		prev_id = current.bookmark.id if current else self._pending_id
		try:
			items = self._provider() or []
		except Exception:
			items = []
		entries = []
		for key, prefix, extra in items:
			for bm in mgr.get(key):
				entries.append(BookmarkEntry(key, bm, prefix, extra))
		self._entries = entries
		self._marked &= {e.bookmark.id for e in entries}
		self.listbox.Clear()
		for e in entries:
			self.listbox.Append(self._label(e))
		self._pending_id = prev_id
		# Setting a selection while another control has focus makes NVDA
		# announce it, so only do it when this list is the focused one.
		if entries and wx.Window.FindFocus() is self.listbox:
			self._select_id(prev_id)

	def _select_id(self, bookmark_id):
		idx = 0
		for i, e in enumerate(self._entries):
			if e.bookmark.id == bookmark_id:
				idx = i
				break
		if self._entries:
			self.listbox.SetSelection(idx)

	def _on_focus(self, event):
		self.refresh()
		if self._entries and self.listbox.GetSelection() == wx.NOT_FOUND:
			self._select_id(self._pending_id)
		event.Skip()

	# -- keyboard ----------------------------------------------------------

	def handle_key(self, event):
		"""Called from the dialog's char hook while this list has focus.
		Returns True if the key was consumed."""
		key = event.GetKeyCode()
		if key == wx.WXK_WINDOWS_MENU or (key == wx.WXK_F10 and event.ShiftDown()):
			self.show_menu()
			return True
		if event.ControlDown() or event.AltDown():
			return False
		if key == ord("."):
			self.toggle_mark()
			return True
		if key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			self.play_from()
			return True
		if key == wx.WXK_SPACE:
			if self._dialog._player.is_playing():
				self._dialog._player.pause()
			else:
				self.play_from()
			return True
		if key == wx.WXK_DELETE:
			self.remove_selected()
			return True
		return False

	def toggle_mark(self):
		entry = self.selected()
		if not entry:
			return
		idx = self.listbox.GetSelection()
		bid = entry.bookmark.id
		name = bookmarks.get_manager().display_name(entry.key, entry.bookmark)
		if bid in self._marked:
			self._marked.discard(bid)
			# Translators: Spoken after unmarking a bookmark; %s is its name.
			ui.message(_("Unmarked: %s") % name)
		else:
			self._marked.add(bid)
			# Translators: Spoken after marking a bookmark; %s is its name.
			ui.message(_("Marked: %s") % name)
		self.listbox.SetString(idx, self._label(entry))
		self.listbox.SetSelection(idx)

	# -- actions -----------------------------------------------------------

	def _seek_or_start(self, entry, position):
		"""Move playback of the entry's item to *position* - seeking if it
		is already loaded, otherwise starting it from there."""
		player = self._dialog._player
		current = player.get_current_station() or {}
		if player.has_media() and player.bookmark_key(current) == entry.key:
			if player.seek_to(position):
				if not player.is_playing():
					player.resume()
				return
		player.set_resume_position(entry.key, position)
		self._start_fn(entry)

	def play_from(self, entry=None):
		entry = entry or self.selected()
		if not entry:
			return
		# Speak the bookmark's text / play its voice note first, if it has any.
		plugin = getattr(self._dialog, "_plugin", None)
		if plugin is not None and entry.bookmark.has_note():
			plugin.play_bookmark_notes_then(
				entry.bookmark,
				lambda: self._seek_or_start(entry, entry.bookmark.position),
			)
			return
		self._seek_or_start(entry, entry.bookmark.position)

	def rename(self):
		entry = self.selected()
		if not entry:
			return
		mgr = bookmarks.get_manager()
		dlg = wx.TextEntryDialog(
			self._dialog,
			# Translators: Prompt of the bookmark rename dialog; leaving it empty restores the default name.
			_("Enter a new name for the bookmark (leave empty for the default name):"),
			# Translators: Title of the bookmark rename dialog.
			_("Rename Bookmark"),
			mgr.display_name(entry.key, entry.bookmark),
		)
		if dlg.ShowModal() != wx.ID_OK:
			dlg.Destroy()
			return
		name = dlg.GetValue().strip()
		dlg.Destroy()
		unchanged_default = (not entry.bookmark.name) and name == mgr.display_name(entry.key, entry.bookmark)
		if not unchanged_default:
			mgr.rename(entry.key, entry.bookmark.id, name)
		self.refresh()
		# Translators: Spoken after renaming a bookmark; %s is its new name.
		ui.message(_("Renamed to: %s") % mgr.display_name(entry.key, entry.bookmark))

	def remove_selected(self):
		targets = self.marked_entries()
		if not targets and self.selected():
			targets = [self.selected()]
		if not targets:
			return
		count = len(targets)
		# Translators: Body of the confirmation dialog for deleting bookmarks; %d is how many.
		message = ngettext(
			"Do you want to delete %d bookmark?",
			"Do you want to delete %d bookmarks?",
			count,
		) % count
		# Translators: Title of the delete-bookmarks confirmation dialog.
		if not self._dialog._confirm_bulk_remove(count, _("Delete Bookmarks"), message):
			return
		idx = self.listbox.GetSelection()
		mgr = bookmarks.get_manager()
		by_key = {}
		for e in targets:
			by_key.setdefault(e.key, []).append(e.bookmark.id)
		for key, ids in by_key.items():
			mgr.remove(key, ids)
		self._marked.clear()
		self.refresh()
		# Translators: Spoken after deleting bookmarks; %d is how many were deleted.
		ui.message(ngettext("%d bookmark deleted", "%d bookmarks deleted", count) % count)
		left = self.listbox.GetCount()
		if left:
			self.listbox.SetSelection(min(max(idx, 0), left - 1))
			self.listbox.SetFocus()

	def edit_text(self):
		entry = self.selected()
		if not entry:
			return
		dlg = wx.TextEntryDialog(
			self._dialog,
			# Translators: Prompt of the bookmark text-note dialog; the text is spoken by NVDA when playback reaches the bookmark. Empty removes the text.
			_("Text spoken when playback reaches this bookmark (leave empty to remove it):"),
			# Translators: Title of the bookmark text-note dialog.
			_("Bookmark Text"),
			entry.bookmark.text,
			style=wx.TextEntryDialogStyle | wx.TE_MULTILINE,
		)
		if dlg.ShowModal() != wx.ID_OK:
			dlg.Destroy()
			return
		text = dlg.GetValue().strip()
		dlg.Destroy()
		bookmarks.get_manager().set_text(entry.key, entry.bookmark.id, text)
		self.refresh()
		# Translators: Spoken after saving a bookmark's text note.
		ui.message(_("Text saved") if text else _("Text removed"))

	def add_voice_note(self):
		entry = self.selected()
		if not entry:
			return
		mgr = bookmarks.get_manager()
		path = mgr.audio_path_for(entry.bookmark.id)
		dlg = VoiceNoteDialog(self._dialog, path)
		saved = dlg.ShowModal() == wx.ID_OK
		dlg.Destroy()
		if saved:
			mgr.set_audio(entry.key, entry.bookmark.id, path)
			self.refresh()
			# Translators: Spoken after a voice note was saved to a bookmark.
			ui.message(_("Voice note saved"))

	def clear_notes(self):
		entry = self.selected()
		if not entry:
			return
		mgr = bookmarks.get_manager()
		mgr.set_text(entry.key, entry.bookmark.id, "")
		mgr.set_audio(entry.key, entry.bookmark.id, "")
		self.refresh()
		# Translators: Spoken after removing a bookmark's text and voice notes.
		ui.message(_("Notes removed"))

	def _marked_span(self):
		"""(first, last) of the marked bookmarks - earliest and latest
		position - or None (after telling the user) unless two or more
		bookmarks of the same item are marked."""
		marked = self.marked_entries()
		if len(marked) < 2 or len({e.key for e in marked}) != 1:
			# Translators: Spoken when the repeat command is used without two or more marked bookmarks of the same item.
			ui.message(_("Mark at least two bookmarks of the same item with the period key first."))
			return None
		first = min(marked, key=lambda e: e.bookmark.position)
		last = max(marked, key=lambda e: e.bookmark.position)
		return first, last

	def repeat_between_marked(self):
		from . import _format_duration
		span = self._marked_span()
		if span is None:
			return
		first, last = span
		start, end = first.bookmark.position, last.bookmark.position
		player = self._dialog._player
		player.set_loop_range(first.key, start, end)
		self._seek_or_start(first, start)
		# Translators: Spoken when repeat mode starts; %(start)s and %(end)s are the positions it repeats between.
		ui.message(_("Repeating between %(start)s and %(end)s") % {
			"start": _format_duration(start), "end": _format_duration(end)})

	def stop_repeat(self):
		self._dialog._player.clear_loop()
		# Translators: Spoken when repeat mode between bookmarks is turned off.
		ui.message(_("Repeat stopped"))

	def save_excerpt_between_marked(self):
		"""Save the section between the earliest and latest marked bookmark
		(the same section repeat mode loops) as an audio file in
		<recordings folder>\\<media name>\\."""
		from . import _notify, excerptExport
		if self._source_fn is None:
			return
		span = self._marked_span()
		if span is None:
			return
		first, last = span
		start, end = first.bookmark.position, last.bookmark.position
		if end - start < 0.5:
			# Translators: Spoken when the marked bookmarks are (almost) at the same position, so there is nothing to save as an excerpt.
			ui.message(_("The marked bookmarks are too close together to save an excerpt."))
			return
		try:
			source = self._source_fn(first)
		except Exception:
			source = None
		if not source:
			# Translators: Spoken when an audio excerpt can't be saved because the source of the item isn't known.
			ui.message(_("Could not find the audio of this item."))
			return
		mgr = bookmarks.get_manager()
		start_name = mgr.display_name(first.key, first.bookmark)
		end_name = mgr.display_name(last.key, last.bookmark)

		def _started():
			# Translators: Spoken when saving the audio between two bookmarks starts.
			wx.CallAfter(_notify, _("Saving excerpt..."))

		def _done(path):
			# Translators: Spoken when an audio excerpt was saved; %s is the file name.
			wx.CallAfter(_notify, _("Excerpt saved: %s") % os.path.basename(path))

		def _failed(reason):
			if reason == "ffmpeg":
				# Translators: Spoken when an audio excerpt can't be saved because ffmpeg could not be found.
				message = _("Could not save the excerpt: ffmpeg was not found.")
			else:
				# Translators: Spoken when saving an audio excerpt failed; %s is the error.
				message = _("Could not save the excerpt: %s") % reason
			wx.CallAfter(ui.message, message)

		started = excerptExport.start_excerpt(
			source, start, end, start_name, end_name, first.key, _started, _done, _failed)
		if not started:
			# Translators: Spoken when the same excerpt is already being saved.
			ui.message(_("This excerpt is already being saved."))

	# -- context menu --------------------------------------------------------

	def show_menu(self):
		entry = self.selected()
		has = entry is not None
		player = self._dialog._player
		menu = wx.Menu()
		dlg = self._dialog

		def add(label, handler, enabled=True):
			item = menu.Append(wx.ID_ANY, label)
			item.Enable(enabled)
			dlg.Bind(wx.EVT_MENU, lambda e: handler(), item)
			return item

		# Translators: Bookmark context-menu item; plays the item starting at the selected bookmark.
		add(_("&Play from Bookmark"), self.play_from, has)
		# Translators: Bookmark context-menu item; renames the selected bookmark.
		add(_("Re&name..."), self.rename, has)
		# Translators: Bookmark context-menu item; deletes the bookmarks marked with '.' (or the focused one if none are marked).
		add(_("&Delete Selected"), self.remove_selected, has)
		menu.AppendSeparator()
		# Translators: Bookmark context-menu item; adds or edits a text note spoken by NVDA when playback reaches the bookmark.
		add(_("Add or Edit &Text..."), self.edit_text, has)
		# Translators: Bookmark context-menu item; records a voice note that plays when playback reaches the bookmark.
		add(_("Add &Voice Note..."), self.add_voice_note, has)
		# Translators: Bookmark context-menu item; removes the text and voice note of the bookmark.
		add(_("&Clear Notes"), self.clear_notes, has and entry.bookmark.has_note())
		menu.AppendSeparator()
		# Translators: Bookmark context-menu item; plays the section between the bookmarks marked with '.' over and over.
		add(_("&Repeat Between Marked Bookmarks"), self.repeat_between_marked, len(self._marked) >= 2)
		# Translators: Bookmark context-menu item; turns off the repeat mode.
		add(_("St&op Repeat"), self.stop_repeat, player.get_loop_range() is not None)
		if self._source_fn is not None:
			# Translators: Bookmark context-menu item; saves the section between the bookmarks marked with '.' as an audio file in the recordings folder, in a folder named after the media.
			add(_("Save &Excerpt Between Marked Bookmarks"), self.save_excerpt_between_marked, len(self._marked) >= 2)

		dlg.PopupMenu(menu, self.listbox.GetScreenPosition() - dlg.GetScreenPosition())
		menu.Destroy()