# -*- coding: utf-8 -*-
# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _

# Add-on information variables
addon_info = AddonInfo(
	# add-on Name/identifier, internal for NVDA
	addon_name="freeAudio",
	
	# Add-on summary/title, usually the user visible name of the add-on
	# Translators: Summary/title for this add-on
	addon_summary=_("freeAudio: Radio and more"),
	
	# Add-on description
	# Translators: Long description to be shown for this add-on
	addon_description=_("""freeAudio is an internet radio, podcast, audio-book, and local music add-on for NVDA that provides seamless access to thousands of internet radio stations via the Radio Browser open directory, RSS/Atom podcast feeds, the libriVox + GETEM digital library for the visually impaired, and your own local audio files and folders through its built-in jukebox. It features a fully accessible station browser with search, country filter, favourites management, and per-station, per-podcast, per-audio-book, and per-jukebox-track audio profiles. Podcast episodes, audio book chapters, and jukebox tracks resume automatically from where you left off - jukebox folders even pick up on the last track you were playing - with adjustable pitch-preserving playback speed and independent pitch-shift (semitone transpose). Playback is handled by BASS, with support for volume control, audio effects, output device selection, and simultaneous audio mirroring to a second device. Additional features include instant and scheduled recording, time-shift rewind of live radio, sleep and alarm timers, automatic ICY metadata announcements, Shazam-based music recognition, and a liked-songs log with lyrics lookup. All controls and shortcuts are designed for NVDA accessibility."""),
	
	# version
	addon_version="2026.25.1",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
## New Features

- **Jukebox now has the same feature set as Favourites:** Jukebox entries can now be reordered in-place (comma-key pick/drop), renamed (custom display name, doesn't touch the file/folder on disk), assigned to groups, and exported/imported as JSON (full fidelity: groups + per-file audio profiles) or M3U (path + custom name only). An auto-generated NVDA Input Gestures shortcut is also created per entry under a new "freeAudio Jukebox" category — works even when the dialog is closed.

- **Per-module enable/disable:** A new "Modules" checklist in settings lets users turn the Podcasts, Audio Books, and/or Jukebox tabs off entirely. All three remain enabled by default, so existing users see no change. Disabling a module hides its tab and related gestures but never touches its saved data (subscriptions, library, jukebox entries) — re-enabling restores everything as it was.

- **Plain Left/Right for seeking in Jukebox/Audio Books/Podcasts lists:** Left/Right in these tabs' item lists now seeks within the currently playing item, calling the same methods as the global Ctrl+Win+J/K commands. Episode/chapter/track switching still works via Ctrl+Left/Right and F3/F4; the old plain Left/Right episode-switch behavior only remains as a fallback when nothing is playing yet.

## Improvements

- **Timer tab focus behaviour fixed:** Switching to the Timer tab now forces focus to the Start/Stop action radio buttons only on first open. On every later switch, focus stays where you left it — matching every other tab.

- **HLS short-segment merger removed:** The ffmpeg-based `_HlsStreamMerger` and its detection helpers have been dropped. HLS streams now always play directly through BASS, and stall reconnects use the original URL.

## Bug Fixes

- **Wrong duration in fMP4 (HLS) recordings fixed:** Fragmented MP4 recordings had no header duration and carried the stream's absolute clock, so players showed absurd lengths. After recording, files are remuxed to a standard MP4 with ffmpeg (stream copy); when ffmpeg is unavailable, fragment timestamps are rebased to zero as a fallback.
"""),
	
	# Author(s)
	addon_author="Çağrı Doğan <cagrid@hotmail.com>",
	
	# URL for the add-on documentation support
	addon_url="https://github.com/Surveyor123/freeAudio",
	
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/Surveyor123/freeAudio",
	
	# Documentation file name
	addon_docFileName="readme.html",
	
	# Minimum NVDA version supported
	addon_minimumNVDAVersion="2025.1.0",
	
	# Last NVDA version supported/tested
	addon_lastTestedNVDAVersion="2026.2.0",
	
	# Add-on update channel (None denotes stable releases)
	addon_updateChannel=None,
	
	# Add-on license
	addon_license="GPL-2.0",
	addon_licenseURL=None,
)

# Define the python files that are the sources of your add-on.
# We point to the specific directory where your code lives.
pythonSources: list[str] = [
	"addon/globalPlugins/freeAudio/*.py",
	"addon/appModules/*.py",
]

# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
excludedFiles: list[str] = []

# Base language for the NVDA add-on
# Since your code strings (e.g. _("Table")) are in English, we keep this as "en".
baseLanguage: str = "en"

# Markdown extensions for add-on documentation
markdownExtensions: list[str] = []

# Custom braille translation tables
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
symbolDictionaries: SymbolDictionaries = {}