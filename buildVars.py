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
	addon_version="2026.25.3",
	
	# Brief changelog for this version
	# Translators: what's new content for the add-on version
	addon_changelog=_("""
## Changelog for 2026.25.3

- Compatible with NVDA 2026.3.

### New
- Added global shortcuts that work while the freeAudio window is closed:

  - Ctrl+Win+F3 / Ctrl+Win+F4: previous / next item.
  - Ctrl+Win+Shift+F3 / Ctrl+Win+Shift+F4: previous / next group.
- What they do depends on what is playing:
  - Radio station: previous / next station (the Shift variants do the same).
  - Podcast: previous / next episode; with Shift, previous / next feed.
  - Audio book: previous / next book; with Shift, previous / next part.
  - Jukebox: previous / next track; with Shift, previous / next library entry.
- If nothing is playing, the keys are passed through to Windows unchanged.
- Audio book library entries now appear in NVDA's Input Gestures dialog under "freeAudio Audio Books", so you can assign a shortcut to any book.

### Improved
- Automatic track and part advance keeps working after a manual skip, with the window open or closed.
- Pressing "next" on the last track of a jukebox folder no longer resets the folder's saved position.
- With the window open, skipping an audio book from the keyboard keeps the window's "now playing" state in sync, so its own auto-advance continues from the right part.

### Fixed
- F3/F4 and Ctrl+Left/Right on the Jukebox tab now play the track as part of its folder. Previously this stopped automatic advance to the next track.
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