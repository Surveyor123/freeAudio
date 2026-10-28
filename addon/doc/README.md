# freeAudio — NVDA Add-on

freeAudio is a full-featured internet radio, podcast, audio-book, and local-jukebox add-on for the NVDA screen reader. What began as a simple way to stream internet radio stations has grown into a complete, fully accessible listening hub — every screen, dialog, and control is designed from the ground up for keyboard and screen-reader use, with no mouse required at any point.

## What freeAudio Can Do

- **Internet radio** — Browse and search over 50,000 stations from the [Radio Browser](https://www.radio-browser.info/) directory, with results supplemented by TuneIn and iHeartRadio. Save favourites, reorder them, and jump straight to any of them with a global keyboard shortcut from anywhere in Windows — see [Radio Browser Directory](#radio-browser-directory) and [Favourites](#favourites).
- **Podcasts** — Subscribe to any RSS/Atom feed, or search Apple's podcast directory and preview episodes before subscribing. Playback position is saved automatically and resumes where you left off — see [Podcasts](#podcasts).
- **Audio books** — Search, stream and download books from three sources: [GETEM](https://getem.boun.edu.tr/), Boğaziçi University's digital library for the visually impaired; [LibriVox](https://librivox.org/), the volunteer-read public-domain audiobook project; and the Project Gutenberg Open Audiobook Collection. LibriVox and Project Gutenberg need no account. Multi-part works resume automatically where you left off — see [Audio Books (GETEM, LibriVox and Project Gutenberg)](#audio-books-getem-librivox-and-project-gutenberg).
- **Local Jukebox** — Search audio files stored on any attached drive by filename, or build a personal library of files and folders, and play them back with the same resume, seek, speed and pitch tools podcasts and audio books use — see [Local Jukebox](#local-jukebox).
- **Bookmarks** — Drop a bookmark at the current position of any audio book part, podcast episode or jukebox track, then jump back to it later. A bookmark can carry a text note or a recorded voice note that plays when playback reaches it, and two bookmarks can be used to repeat the section between them — see [Bookmarks](#bookmarks).
- **Recording** — Record what's playing instantly, record a single song from its start to its end, record every song on a station to its own file until you stop, or schedule one-off and recurring recordings — all without interrupting playback — see [Recording](#recording).
- **Time-shift (rewind live radio)** — Pause and rewind a live station like a DVR, then catch back up to live whenever you want — see [Time-Shift (Rewind Live Radio)](#time-shift-rewind-live-radio).
- **Music recognition and liked songs** — Identify tracks with no metadata using Shazam-based recognition, save liked songs to a text file, and look up their lyrics — see [Music Recognition](#music-recognition) and [Liked Songs](#liked-songs).
- **Audio profiles and effects** — Save separate volume, effects, EQ, and playback-speed settings per station, per podcast, per audio book, or per jukebox track, and apply real-time effects (Chorus, Reverb, EQ boosts, and more) through the BASS backend — see [Station Audio Profile](#station-audio-profile).
- **Transpose (pitch shift)** — Shift the pitch of podcasts, audio books and jukebox tracks up or down without changing their speed, using the bundled `bass_fx` component — see [Transpose (Pitch Shift)](#transpose-pitch-shift).
- **Audio mirroring** — Send the same stream to two audio output devices at once, such as speakers and headphones simultaneously — see [Audio Mirror](#audio-mirror).
- **Obligato mode (background music)** — Loop a chosen favourite station quietly in the background, on its own output device and volume, no matter what plays (or doesn't play) as your main media — see [Obligato Mode](#obligato-mode).
- **Timers** — Schedule a favourite station to start playing, or schedule playback to stop, at a specific time — see [Timer](#timer).
- **Deep keyboard and braille access** — Every feature is reachable entirely from the keyboard, with global shortcuts that work from anywhere in Windows (including `Ctrl+Win+F3` / `Ctrl+Win+F4` to skip between stations, episodes, books and tracks without opening the window), direct hotkeys for individual favourite stations, jukebox entries and audio books, and optional braille output for all of freeAudio's spoken notifications.

## Radio Browser Directory

freeAudio uses the [Radio Browser](https://www.radio-browser.info/) open database for its station catalogue. Radio Browser is a community-managed, free directory hosting more than 50,000 internet radio stations from around the world. No registration or account is required and its API is open to everyone. Each station includes address, country, genre, language and bitrate information; stations are ranked by user votes. freeAudio connects to this API through mirror servers located in Germany, the Netherlands and Austria; if one server is unreachable, it automatically switches to the next.

To keep the browser responsive and avoid hitting the API on every search or country change, freeAudio keeps a local cache of the station catalogue on disk. This cache is refreshed automatically in the background on a periodic schedule, so the list you see is normally already up to date without any action on your part. You can also force an immediate re-sync at any time with the **Update Station List** button — see [Station Browser](#station-browser) below.

## Adding a Station to Radio Browser

If a station you are looking for is not in the Radio Browser directory, you can submit it yourself at [https://www.radio-browser.info/add](https://www.radio-browser.info/add). No account or registration is needed.

Fill in the form on that page:

- **Stream URL** *(required)* — the direct URL of the audio stream, ending in `.mp3`, `.aac`, `.ogg` or similar. This is not the station website address; it is the raw stream address you would paste into a media player. Most stations publish their stream URL on their website or in their "Listen live" section.
- **Station name** *(required)* — the name of the station as it should appear in the directory.
- **Homepage** — the station's website address.
- **Country and language** — select the country and the broadcast language from the dropdown lists.
- **Tags** — genre or topic keywords separated by commas, for example `news`, `jazz`, `classical`. These are used for searching and filtering.
- **Logo URL** — a direct link to the station's logo image, if available.

After submitting, the station is reviewed and added to the public directory. Once accepted it will appear in freeAudio's search and country listings automatically, since the directory is refreshed from the live API.

## Requirements

- NVDA 2025.1 or later
- Windows 10 or later
- Internet connection

## Installation

Download the `.nvda-addon` file, press Enter on it and restart NVDA when prompted.

## Keyboard Shortcuts

All shortcuts can be reassigned from NVDA Menu → Preferences → Input Gestures → freeAudio. These shortcuts work from anywhere, regardless of which window has focus.

Some of these shortcuts overlap with ones Windows itself uses. If you'd rather keep Windows' own shortcut without reassigning freeAudio's, press `NVDA+F2` (Pass next key through) right before the key combination — NVDA will send that one key combination straight to Windows instead of intercepting it for freeAudio.

| Shortcut | Function | Description |
|---|---|---|
| `Ctrl+Win+R` | Open station browser | Opens the browser window if closed, or brings it to the foreground if already open. |
| `Ctrl+Win+O` | Open Podcasts tab | Opens the station browser (if closed) or brings it to the foreground, and switches directly to the **Podcasts** tab. |
| `Ctrl+Win+L` | Open Audio Books tab | Opens the station browser (if closed) or brings it to the foreground, and switches directly to the **Audio Books** tab. |
| `Ctrl+Win+U` | Open Jukebox tab | Opens the station browser (if closed) or brings it to the foreground, and switches directly to the **Jukebox** tab, focused on the devices search box. |
| `Ctrl+Win+P` | Pause / resume | Pauses the current station if playing; resumes if paused. If nothing is playing, starts the last station or opens the favourites list depending on your setting. Pressing twice in quick succession jumps directly to a tab of your choice. Pressing three times can trigger a separate action depending on your setting. |
| `Ctrl+Win+S` | Stop | Fully stops the current station and resets the player. |
| `Ctrl+Win+→` | Next favourite | Moves to the next station in the favourites list. Wraps around to the beginning at the end of the list. |
| `Ctrl+Win+←` | Previous favourite | Moves to the previous station in the favourites list. Jumps to the end when at the beginning. |
| `Ctrl+Win+F3` | Previous item | The Station Browser's `F3` key, available with the window closed. What it does depends on what is playing: **radio** — previous station; **podcast** — previous episode; **audio book** — previous book; **jukebox** — previous track in the folder. Announces "Already at first …" at the start of a list. If nothing is playing, the key is passed through unchanged. See [Skipping Items With the Station Browser Closed](#skipping-items-with-the-station-browser-closed). |
| `Ctrl+Win+F4` | Next item | The Station Browser's `F4` key, available with the window closed: next station, podcast episode, audio book or jukebox track, depending on what is playing. |
| `Ctrl+Win+Shift+F3` | Previous feed / part / entry | The Station Browser's `Shift+F3` key, available with the window closed: **radio** — previous station (same as `Ctrl+Win+F3`); **podcast** — previous subscribed podcast; **audio book** — previous part of the book; **jukebox** — previous jukebox entry (file or folder). |
| `Ctrl+Win+Shift+F4` | Next feed / part / entry | The Station Browser's `Shift+F4` key, available with the window closed: next station, subscribed podcast, audio book part or jukebox entry, depending on what is playing. |
| `Ctrl+Win+↑` | Volume up | Increases volume by 5; maximum 200. |
| `Ctrl+Win+↓` | Volume down | Decreases volume by 5; minimum 0. |
| `Ctrl+Win+V` | Add to favourites / Download the Media | Adds the currently playing station to the favourites list or downloads the currently playing podcast episode or audio book. Announces if the station is already in the list or if the media was already downloaded. Not applicable when a jukebox track is playing: freeAudio tells you the shortcut is only for stations, podcasts or audio books. |
| `Ctrl+Win+Shift+K` | Increase playback speed | Increases the playback speed of a podcast episode, audio book, or jukebox track by 0.1x (pitch-preserving). Range: 0.5x to 2.0x. |
| `Ctrl+Win+Shift+J` | Decrease playback speed | Decreases the playback speed of a podcast episode, audio book, or jukebox track by 0.1x. |
| `Shift+Win+K` | Transpose up | Raises the pitch of a podcast episode, audio book, or jukebox track in 1/8 whole-tone (0.25 semitone) steps, without changing its speed. Range: −12.00 to +12.00 semitones. See [Transpose (Pitch Shift)](#transpose-pitch-shift). |
| `Shift+Win+J` | Transpose down | Lowers the pitch by 1/8 whole-tone steps, without changing speed. |
| `Ctrl+Win+F12` | Add bookmark | Adds a bookmark at the current playback position of an audio book part, podcast episode or jukebox track. Not available for live radio stations. See [Bookmarks](#bookmarks). |
| `Ctrl+Win+I` | Station info | Announces the currently playing station name, podcast episode, audio book or jukebox track. Press twice to show details such as country, genre and bitrate in a dialog. Press three times to copy the current track info (ICY metadata) to the clipboard if available; if no metadata is present, starts Shazam music recognition instead. Press four times to force music recognition in case of wrong ICY metadata. While a recording is running, its name is announced as well; during an every-song recording this is the song being recorded right now. |
| `Ctrl+Win+M` | Audio mirror | Mirrors the current stream or media to an additional audio output device simultaneously. Press again to stop mirroring. |
| `Ctrl+Win+Shift+M` | Obligato mode (background music) | Loops a chosen favourite station quietly in the background, on its own output device and volume, no matter what plays as the main media. First press opens a dialog to pick the station, output device, and relative volume. Press again to stop it. |
| `Ctrl+Win+E` | Recording (instant / song / every song) | Press once to start recording the current station; press again to stop. Press **twice** to record the **current song**: the file is named after the track and the recording stops by itself when the track changes. Press **three times** to record **every song** until you stop it: each song is saved to its own file. Press twice while a song or every-song recording is running to stop it. Playback continues uninterrupted in all recording modes. Song and every-song recording work only on stations that send track titles (ICY metadata) inside the stream, and every-song recording does not work on HLS (`.m3u8`) stations. See [Recording](#recording). |
| `Ctrl+Win+W` | Open recordings folder | Opens the folder containing recorded files in File Explorer. |
| `Ctrl+Win+J` | Time-shift rewind / podcast, audio book & jukebox seek back | For live radio: rewinds 15 seconds. The first press enters time-shift mode; each further press moves 15 seconds further back, up to the buffer limit set in the freeAudio settings. Requires the time-shift buffer to be enabled in Settings. For a podcast, audio book, or jukebox track, this key seeks within the file instead, and scales with how you press it: **holding it down** keeps stepping back 5 seconds per repeat, exactly as before; a **single deliberate tap** seeks back 12 seconds; **two taps** in quick succession seek back 1 minute; **three or more taps** seek back 5 minutes. Only one seek happens per tap sequence, sized for however many taps were made — taps don't add up. Works regardless of the time-shift setting. |
| `Ctrl+Win+K` | Time-shift fast-forward / podcast, audio book & jukebox seek forward | For live radio: moves forward 15 seconds while time-shifted. Once the live edge is reached, playback automatically returns to live and this becomes a no-op until you rewind again. For a podcast, audio book, or jukebox track, this key seeks forward within the file using the same tap/hold scaling as `Ctrl+Win+J` above (hold = 5 seconds per repeat; 1 tap = 12 seconds; 2 taps = 1 minute; 3+ taps = 5 minutes). Works regardless of the time-shift setting. |
| `Ctrl+Win+Alt+J` | Fine rewind (1 second) | Rewinds by exactly 1 second, for small corrections. On a podcast, audio book or jukebox track it seeks 1 second back in the file; on live radio it moves 1 second back in the time-shift buffer (the time-shift buffer must be enabled, and the first press enters time-shift mode like `Ctrl+Win+J`). See [Fine Seeking (1 Second)](#fine-seeking-1-second). |
| `Ctrl+Win+Alt+K` | Fine forward (1 second) | Moves forward by exactly 1 second. On a podcast, audio book or jukebox track it seeks 1 second forward in the file; on live radio it moves 1 second forward while time-shifted. See [Fine Seeking (1 Second)](#fine-seeking-1-second). |
| `Ctrl+Win+T` | Toggle time-shift buffer | Enables or disables the time-shift buffer on the fly, mirroring the Settings checkbox. Disabling immediately returns to live playback if time-shifted and stops the background capture. No effect on podcast, audio book or jukebox playbacks. |
| *(unassigned)* | Select output device | Opens an on-demand list of the available main output devices. The list is shown only when BASS detects more than one physical output device. Assign a key combination via NVDA Menu → Preferences → Input Gestures → freeAudio. |
| *(unassigned)* | Toggle mute notifications | Toggles the Mute Notifications setting on the fly. Assign a key combination via NVDA Menu → Preferences → Input Gestures → freeAudio. |
| *(unassigned)* | Play favourite station directly | Each station in your favourites list appears as a separate entry in NVDA Menu → Preferences → Input Gestures → **freeAudio Stations**. Assign any keyboard shortcut to a station to start playing it instantly from anywhere, without opening the browser. |
| *(unassigned)* | Play jukebox entry directly | Each file or folder in your Jukebox list appears as a separate entry in NVDA Menu → Preferences → Input Gestures → **freeAudio Jukebox**. See [Direct Keyboard Shortcuts for Jukebox Entries](#direct-keyboard-shortcuts-for-jukebox-entries). |
| *(unassigned)* | Play audio book directly | Each book in your Audio Books library — from GETEM, LibriVox or Project Gutenberg — appears as a separate entry in NVDA Menu → Preferences → Input Gestures → **freeAudio Audio Books**. Assign any keyboard shortcut to a book to resume it instantly from anywhere, without opening the browser. See [Direct Keyboard Shortcuts for Audio Books](#direct-keyboard-shortcuts-for-audio-books). |

`Ctrl+Win+→` / `Ctrl+Win+←` only navigate the favourites list; they do not work with the all stations list — use `Ctrl+Win+F4` / `Ctrl+Win+F3` (see below) to step through whichever list the current station was started from. When a list is focused in the browser window, the left and right arrow keys serve the same purpose — see In-Dialog Shortcuts.

### Skipping Items With the Station Browser Closed

Inside the Station Browser, `F3`, `F4`, `Shift+F3` and `Shift+F4` do different things depending on which tab is active. The global versions — `Ctrl+Win+F3`, `Ctrl+Win+F4`, `Ctrl+Win+Shift+F3` and `Ctrl+Win+Shift+F4` — work from anywhere in Windows, whether or not the window is open. With no tab to look at, freeAudio decides by **what is playing right now**:

| Playing | `Ctrl+Win+F3` / `Ctrl+Win+F4` | `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` |
|---|---|---|
| Radio station | Previous / next station in the list it was last started from (All Stations results or Favourites), wrapping around at the ends. If the station is not in that list, the favourites list is used. | Same as without `Shift`. |
| Podcast episode | Previous / next episode of the same feed. | Previous / next subscribed podcast. Because there is no list to highlight a feed in, its first listed episode is played. |
| Audio book | Previous / next book in your library, resuming at the part you last listened to. | Previous / next part of the current book. |
| Jukebox track | Previous / next track of the folder being played. | Previous / next entry in the Jukebox list; a folder resumes from where it was last left off. |

A few things to know:

- If nothing is playing, the key combination is passed through to Windows untouched, the same as `Ctrl+Win+→` / `Ctrl+Win+←`.
- At either end of a list (except radio, which wraps), NVDA announces "Already at first …" or "Already at last …" and nothing changes. A jukebox track that was not started as part of a folder has no neighbours, so it reports the same.
- **Automatic advance is not interrupted.** After you skip within a jukebox folder or an audio book, the next track or part still starts by itself when the current one ends, with the Station Browser open or closed. Pressing next on the last track of a folder does not reset the folder's saved position.
- A podcast's episode list is only kept in memory for the current NVDA session. If it has not been loaded yet — for example right after NVDA started — NVDA asks you to open the Station Browser and select that podcast once; after that the keys work with the window closed.
- If the Station Browser is open, an audio book skipped from the keyboard also updates the window's "now playing" book and part, so its own automatic advance carries on from the right place.

Like every freeAudio command, these can be reassigned from NVDA Menu → Preferences → Input Gestures → freeAudio.

## Station Browser

freeAudio also adds a **freeAudio** submenu to the NVDA Tools menu. From there you can directly open the Station Browser and freeAudio Settings.

The window opened with `Ctrl+Win+R` contains eight tabs: All Stations, Favourites, Recording, Timer, Liked Songs, Podcasts, Audio Books and Jukebox. You can navigate between tabs with `Ctrl+Tab` or using `Alt+1` through `Alt+8`. The Podcasts, Audio Books and Jukebox tabs can be switched off with the **Modules** setting (see [Settings](#settings)); tabs that are switched off are not shown.

When the All Stations tab opens, the top 1,000 most-voted stations are automatically loaded from Radio Browser. Selecting a country from the dropdown updates the list to show that country's stations. Typing in the search field instantly performs a full search across the entire Radio Browser database simultaneously by name, country and genre.

When searching, results from Radio Browser are supplemented with stations from TuneIn and iHeartRadio (when available). These external sources are searched in the background and their results are merged into the list automatically, giving you access to even more stations without any extra action.

The **Output Device** dropdown at the bottom of the browser window — outside the tabs — lists all BASS-recognised audio output devices. Selecting a device immediately redirects audio output to it and saves the choice permanently; the same device is used automatically in the next session. If the selected device is not connected, the add-on falls back to the system default automatically. Press `F11` to open a simpler on-demand device picker from anywhere in the Station Browser. The picker is not shown automatically and opens only when BASS detects more than one physical output device. When just one is available, no selection is needed and freeAudio uses the system default output.

The **Volume** (0–200) and **Effects** controls in the same area can be adjusted at any time while the window is open. From the Effects list, Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, EQ: Bass Boost, EQ: Treble Boost and EQ: Vocal Boost can be enabled simultaneously; changes are applied to the active stream instantly. Each effect can also be toggled instantly with `Ctrl+1` through `Ctrl+0` without leaving the keyboard — see [Effect Shortcuts](#effect-shortcuts).

When one or more EQ effects are enabled, a **gain control** appears for each active band. The gain can be set between −15 dB and +15 dB; the default values are Bass +9 dB, Treble +9 dB, and Vocal +6 dB. The gain controls are shown only for the EQ bands that are currently checked, and are hidden automatically when an EQ effect is unchecked. Gain values are saved globally and restored on the next session.

The **Play/Pause** button is also located at the bottom of the window. If no station is playing it starts the selected station; if a station is already playing it pauses playback.

The **Update Station List** button re-syncs the local station catalogue from the Radio Browser API immediately, instead of waiting for the periodic background refresh. While the refresh is running the button is disabled and NVDA announces that a refresh is in progress; if you press it again before the current refresh finishes, NVDA lets you know one is already underway. Once the refresh completes, NVDA announces that the station list has been updated and the currently displayed search results or country listing are refreshed automatically to reflect the new data.

When a station is selected in the list, the **Station Details** button displays information such as country, language, genre, format, bitrate, website and stream URL in a separate dialog. Each field appears in its own read-only text box; you can move between fields with Tab and copy all information to the clipboard at once with the **Copy all to clipboard** button. This button is available in both the All Stations and Favourites tabs.

### Station Context Menu

Right-click a station in the All Stations or Favourites list, or select it and press the Applications key or `Shift+F10`, to open a context menu with quick actions:

- **Station Details** — same as the Station Details button described above.
- **Add to Favourites** *(All Stations tab)* / **Delete Station** *(Favourites tab)*.
- **Rename Station** *(Favourites tab)* — same as `F9`.
- **Save Audio Profile for This Station** / **Clear Audio Profile** *(Favourites tab)* — see [Station Audio Profile](#station-audio-profile).
- **Test URL** — checks whether the selected station's stream is currently reachable without starting playback, and announces the result (reachable, or the reason it failed, such as an HTTP error or network timeout).

Only the items relevant to the current tab and selection are shown as available.

### In-Dialog Shortcuts

The following keys work only while the Station Browser window is active.

#### F Keys

| Shortcut | Function | Description |
|---|---|---|
| `F1` | Help guide | Opens the add-on's help file in the default browser. The guide for the active NVDA language is searched first; if not found, the default guide is opened. |
| `F2` | What's playing | Announces the currently playing station and track name. Press twice to show details such as country, genre and bitrate in a dialog. Press three times to copy the current track info (ICY metadata) to the clipboard if available; if no metadata is present, starts Shazam music recognition instead. Press four times to force music recognition in case of wrong ICY metadata. While a recording is running, its name is announced as well. |
| `F3` | Previous item | On All Stations or Favourites tabs: moves to the previous station and starts playing immediately. On Podcasts tab: moves to the previous episode in the episode list and plays it. On Audio Books tab: moves to the previous book and starts playing it. On Jukebox tab: moves to the previous track in the selected jukebox item and plays it; in a folder, the following tracks keep starting automatically. The global equivalent is `Ctrl+Win+F3` — see [Skipping Items With the Station Browser Closed](#skipping-items-with-the-station-browser-closed). |
| `F4` | Next item | On All Stations or Favourites tabs: moves to the next station and starts playing immediately. On Podcasts tab: moves to the next episode and plays it. On Audio Books tab: moves to the next book and starts playing it. On Jukebox tab: moves to the next track in the selected jukebox item and plays it; in a folder, the following tracks keep starting automatically. The global equivalent is `Ctrl+Win+F4`. |
| `Shift+F3` | Previous feed / part / item | On Podcasts tab: moves up one feed in the subscriptions list. On Audio Books tab: moves to the previous part of the currently playing book. On Jukebox tab: moves up one jukebox entry (file or folder) in the main list. The global equivalent is `Ctrl+Win+Shift+F3`, which also plays the entry. |
| `Shift+F4` | Next feed / part / item | On Podcasts tab: moves down one feed in the subscriptions list. On Audio Books tab: moves to the next part of the currently playing book. On Jukebox tab: moves down one jukebox entry in the main list. The global equivalent is `Ctrl+Win+Shift+F4`, which also plays the entry. |
| `F5` | Volume down | Decreases volume by 5 (minimum 0). |
| `F6` | Volume up | Increases volume by 5 (maximum 200). |
| `F7` | Pause / resume | Pauses if a station is playing; resumes if paused and media is loaded. |
| `F8` | Stop | Fully stops the current station and resets the player. |
| `F9` | Rename | Opens rename dialog for the focused station in the Favourites tab. |
| `F11` | Select output device | Opens the main output-device picker when BASS detects more than one physical output device. The current device is preselected; Enter applies and saves the choice. |
| `F12` | Add bookmark | Adds a bookmark at the current playback position of an audio book part, podcast episode or jukebox track — the in-window equivalent of `Ctrl+Win+F12`. See [Bookmarks](#bookmarks). |

#### List and Navigation Shortcuts

| Shortcut | Function | Description |
|---|---|---|
| `→` | Next item / Seek forward | On a station list (All Stations / Favourites), moves to the next station and plays it immediately, wrapping to the beginning at the end of the list. On the Podcasts, Audio Books or Jukebox item lists (and the bookmark list below each), while something is loaded and playing, seeks forward instead — the same as the global `Ctrl+Win+K` command (see [Podcast Playback Details](#podcast-playback-details) for how tapping and holding change the step). On the Podcasts episode list specifically, if nothing is loaded yet, it falls back to moving to the next episode and playing it. |
| `←` | Previous item / Seek backward | On a station list, moves to the previous station and plays it, jumping to the end when at the beginning. On the Podcasts, Audio Books or Jukebox item lists (and the bookmark list below each), while something is loaded and playing, seeks backward instead — the same as the global `Ctrl+Win+J` command. On the Podcasts episode list, if nothing is loaded yet, it falls back to moving to the previous episode and playing it. |
| `Shift+→` | Transpose up | On the Podcasts, Audio Books or Jukebox item lists and their bookmark lists: raises the pitch of the current playback by one step (0.25 semitone), the same as the global `Shift+Win+K` command. |
| `Shift+←` | Transpose down | On the Podcasts, Audio Books or Jukebox item lists and their bookmark lists: lowers the pitch of the current playback by one step (0.25 semitone), the same as the global `Shift+Win+J` command. |
| `Page Up` | Playback speed up | On the Podcasts, Audio Books or Jukebox item lists and their bookmark lists: increases playback speed, the same as the global `Ctrl+Win+Shift+K` command. |
| `Page Down` | Playback speed down | On the Podcasts, Audio Books or Jukebox item lists and their bookmark lists: decreases playback speed, the same as the global `Ctrl+Win+Shift+J` command. |
| `Alt+→` | Fine seek forward (1 second) | In any tab of the Station Browser, while something is loaded: seeks forward by exactly 1 second, the same as the global `Ctrl+Win+Alt+K` command. See [Fine Seeking (1 Second)](#fine-seeking-1-second). |
| `Alt+←` | Fine seek backward (1 second) | In any tab of the Station Browser, while something is loaded: seeks backward by exactly 1 second, the same as the global `Ctrl+Win+Alt+J` command. |
| `Ctrl+→` | Next episode / book / track | On Podcasts tab: moves to the next episode and plays it. On Audio Books tab (library list focused): moves to the next book. On Jukebox tab (either the entries list or the tracks list focused): moves to the next track in the selected jukebox item and plays it. |
| `Ctrl+←` | Previous episode / book / track | On Podcasts tab: moves to the previous episode and plays it. On Audio Books tab: moves to the previous book. On Jukebox tab: moves to the previous track in the selected jukebox item and plays it. |
| `Enter` | Play / Add | On a station or episode list: starts playing the selected item immediately. On the Jukebox tab's search results: adds the selected file to the jukebox. On the Jukebox tab's entries or tracks list: plays the focused item directly. |
| `Space` | Play / Pause / Preview | Pauses if something is playing; otherwise starts playing the selected item. On the Jukebox tab's search results: toggles preview (play/stop) of the selected file. On the Jukebox tab's entries or tracks list: pauses if playing, otherwise plays the focused item. |
| `Ctrl+Tab` | Next tab | Switches to the next tab (All Stations → Favourites → Recording → Timer → Liked Songs → Podcasts → Audio Books → Jukebox). |
| `Ctrl+Shift+Tab` | Previous tab | Switches to the previous tab. |
| `Escape` | Hide | Hides the window; the add-on continues playing in the background. |

#### Volume Shortcuts

| Shortcut | Function | Description |
|---|---|---|
| `Ctrl+↑` | Volume up | Increases volume by 5. Only works while the browser window is open. |
| `Ctrl+↓` | Volume down | Decreases volume by 5. Only works while the browser window is open. |

#### Effect Shortcuts

| Shortcut | Function | Description |
|---|---|---|
| `Ctrl+1` | Toggle Chorus | Enables or disables the Chorus effect and applies it to the active stream instantly. |
| `Ctrl+2` | Toggle Compressor | Enables or disables the Compressor effect and applies it to the active stream instantly. |
| `Ctrl+3` | Toggle Distortion | Enables or disables the Distortion effect and applies it to the active stream instantly. |
| `Ctrl+4` | Toggle Echo | Enables or disables the Echo effect and applies it to the active stream instantly. |
| `Ctrl+5` | Toggle Flanger | Enables or disables the Flanger effect and applies it to the active stream instantly. |
| `Ctrl+6` | Toggle Gargle | Enables or disables the Gargle effect and applies it to the active stream instantly. |
| `Ctrl+7` | Toggle Reverb | Enables or disables the Reverb effect and applies it to the active stream instantly. |
| `Ctrl+8` | Toggle EQ: Bass Boost | Enables or disables the Bass Boost EQ band and applies it to the active stream instantly. |
| `Ctrl+9` | Toggle EQ: Treble Boost | Enables or disables the Treble Boost EQ band and applies it to the active stream instantly. |
| `Ctrl+0` | Toggle EQ: Vocal Boost | Enables or disables the Vocal Boost EQ band and applies it to the active stream instantly. |

Each shortcut mirrors checking or unchecking the corresponding entry in the **Effects** list: NVDA announces whether the effect was enabled or disabled, the change is saved automatically, and the EQ gain control for that band (if applicable) appears or disappears accordingly.

#### Alt Key Shortcuts

| Shortcut | Function | Description |
|---|---|---|
| `Alt+R` | Go to search field | Moves focus to the search text box. Searches Radio Browser with the text in the search field; name, country and genre are searched simultaneously. |
| `Alt+V` | Add / remove favourite | Adds the selected station to favourites; removes it if already in the list. |
| `Alt+1` | All Stations | Switches to the All Stations tab. |
| `Alt+2` | Favourites | Switches to the Favourites tab. |
| `Alt+3` | Recording | Switches to the Recording tab. |
| `Alt+4` | Timer | Switches to the Timer tab. |
| `Alt+5` | Liked Songs | Switches to the Liked Songs tab. |
| `Alt+6` | Podcasts | Switches to the Podcasts tab. |
| `Alt+7` | Audio Books | Switches to the Audio Books tab. |
| `Alt+8` | Jukebox | Switches to the Jukebox tab, focused on the devices search box. |
| `Alt+K` | Close | Closes the window; the add-on continues playing in the background. |

## Favourites

The favourites list is a personal station collection stored permanently. To add a station, select it in the list and press the Add to Favourites button or use the `Alt+V` shortcut. The same shortcut removes a station that is already in the list when it is selected.

Favourites can be played with `Ctrl+Win+→` and `Ctrl+Win+←`; these shortcuts work even when the browser window is not open.

To delete a station from the favourites list, select it and press the **Delete Station** button or the `Delete` key. After deletion, focus and selection automatically move to the next station in the list. If the deleted station was the last one, focus moves to the previous station. If the list becomes empty, focus moves to the Play button.

### Marking and Removing Multiple Items

Favourites, Liked Songs, the Audio Books library, and the Jukebox list all support marking several items and removing them together in one step:

- Press **`.`** (period) on a highlighted item to mark or unmark it. NVDA announces the change, and a marked item's row is labelled "(marked)" so its status stays clear while you keep arrowing through the list.
- Press **`Shift+Home`** to mark or unmark every item from the current one up to the first item in the list, or **`Shift+End`** to do the same down to the last item. Whether the range is marked or unmarked is decided by the current item's own state, so the whole range always moves the same way in one action. Focus moves to the far end of the range afterwards, and NVDA announces how many items changed.
- Press **`Delete`** to remove every marked item at once. If nothing is marked, `Delete` still removes just the currently selected item, as before.
- The right-click context menu (Applications key / `Shift+F10`) of each list includes a **Remove Selected** command, enabled only when at least one item is marked, that does the same thing.
- Before anything is deleted, a single confirmation dialog summarizes how many items are about to be removed.

Marks are per-list and are cleared once you remove the items (or unmark them individually); they are not saved between sessions.

The bookmark lists on the Podcasts, Audio Books and Jukebox tabs use the same `.` marking, and marked bookmarks are what the **Delete Selected** and **Repeat Between Marked Bookmarks** commands act on — see [Bookmarks](#bookmarks).

### Exporting and Importing Favourites

The Favourites tab includes two buttons for backing up and restoring your station list:

**Export Favourites…** — saves your entire favourites list to a file. A save dialog lets you choose between two formats:

- **JSON** (`.json`) — a complete backup that preserves station names, stream URLs, and all metadata. Recommended for restoring your list later or moving it to another computer.
- **M3U playlist** (`.m3u`) — a standard playlist format compatible with most media players and radio apps. Note that M3U does not store all station metadata, so restoring from M3U may result in less detail than a JSON backup.

**Import Favourites…** — loads stations from a previously exported JSON or M3U file. After selecting the file, you are asked how to add the stations:

- **Yes (Merge)** — adds the imported stations to your existing list without removing any current favourites. Duplicate stations are not added twice.
- **No (Replace)** — clears your current favourites list entirely and replaces it with the contents of the imported file.
- **Cancel** — returns to the browser without making any changes.

After a successful import, the favourites list, scheduled-recording station list, and timer station list are all refreshed automatically.

### Organising Favourites into Groups

Favourites can belong to a folder/group, shown as a "— Group" suffix after the station name in the list (for example, "NPR Newscast — NPR").

- **Importing from M3U** — if the file uses the `group-title` tag (the convention used by DVBViewer and most other M3U editors and players) to organise stations into folders, freeAudio reads it and keeps each station's group on import. Exporting your favourites back to M3U writes the same tag, so the folder structure survives a round trip through freeAudio.
- **Assigning or removing a group by hand** — mark one or more favourites with `.` (see [Marking and Removing Multiple Items](#marking-and-removing-multiple-items) above), then choose **Assign to Group…** from the context menu (Applications key / `Shift+F10`) and type a group name. Leave the field empty to remove the marked favourites from their group instead. If nothing is marked, the command applies to the currently selected favourite.
- **Filtering by group** — the Filter field above the favourites list also matches against group names, and accepts multiple words that can each match a different field. For example, typing `Houston Classical` finds "Houston Public Media Classical" even though that exact phrase never appears anywhere — "Houston" matches the group and "Classical" matches the station name.

### Reordering Favourites

With a station selected in the Favourites tab, press `comma` to enter move mode — you will hear a beep. Navigate to the target position with the arrow keys, then press `comma` again. The station is placed at the chosen position and the new order is saved immediately. Pressing `comma` again at the same position cancels the move.

### Direct Keyboard Shortcuts for Favourite Stations

Every station in your favourites list is registered as a separate script in NVDA's Input Gestures dialog, under the **freeAudio Stations** category. You can assign any keyboard shortcut to any station and press it from anywhere — no need to open the browser window first.

To assign a shortcut:

1. Open NVDA Menu → Preferences → Input Gestures.
2. Expand the **freeAudio Stations** category.
3. Find the station by name, select it, and press **Add**.
4. Press the desired key combination and confirm.

The shortcut activates the station immediately. If the station is later removed from your favourites, its entry disappears from the category and any shortcut assigned to it is automatically cleared by NVDA. When a new station is added to favourites, it appears in the category straight away — the Input Gestures dialog does not need to be reopened.

### Adding a Custom Station

To add a station that is not in Radio Browser, use the Add Custom Station button. In the dialog that appears, enter the station name and stream URL to add it directly to your favourites. Custom stations can be played and reordered just like any other favourite.

Two additional buttons are available in this dialog:

- **Test URL** — checks the stream URL you've entered before adding the station, and announces whether it is reachable. Useful for catching a typo or a dead link before it ends up in your favourites list.
- **Add to Radio Browser directory…** — opens the [Radio Browser submission page](https://www.radio-browser.info/add) in your default browser, so you can share the station with the wider Radio Browser community once you've confirmed it works. See [Adding a Station to Radio Browser](#adding-a-station-to-radio-browser) above for what the submission form expects.

### Station Audio Profile

The Favourites tab includes two buttons for managing per-station audio settings:

**Save Audio Profile for This Station** — saves the current volume level, active effects (chorus, EQ, etc.), and EQ gain values as a profile tied to that specific station. Whenever that station starts playing, its saved volume, effects and gain settings are automatically applied, overriding the global defaults.

**Clear Audio Profile** — removes the saved audio profile from the selected station. After clearing, the station reverts to the global volume, effects and EQ gain settings. This button is only active when the selected station already has a saved profile.

Both buttons are located below the favourites list and are only enabled when a station in the list is selected.

## Music Recognition

Pressing `Ctrl+Win+I` three times triggers Shazam-based music recognition for the currently playing stream. Recognition only starts when no ICY metadata (track info broadcast by the station) is available; if metadata is present, it is copied to the clipboard instead. Pressing `Ctrl+Win+I` four times forces recognition even when the station sends metadata, which helps when that metadata is wrong.

Recognition works as follows: a short audio sample is captured from the stream using ffmpeg (which identifies itself the way a media player does, so stations that refuse unknown programs still answer), the Shazam fingerprinting algorithm is applied, and the result is sent to Shazam's servers. If recognition succeeds, the track title, artist, album and release year are announced by NVDA and automatically copied to the clipboard. If the **Save liked songs to a text file** option is enabled, the recognition result is also appended to `likedSongs.txt`.

If ffmpeg cannot read the stream directly — for example because the station refuses its connection, or because the stream address ends in `.nsv` (typical of SHOUTcast servers), which makes ffmpeg misdetect the audio format — freeAudio records a short sample from the stream itself and has ffmpeg decode that file instead. This happens automatically; there is no setting for it.

**Audio feedback:** Two rising beeps sound when recognition starts, and two falling beeps when it ends. A short beep plays every 2 seconds while the process is running.

**Requirement:** ffmpeg.exe is required. An ffmpeg.exe placed in the add-on folder is used automatically; if it is in a different location, the path can be set in Settings. Download ffmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).

**A note on stations that insert ads:** some stations serve a short ad to every brand-new connection made to their stream, separate from the broadcast you're already listening to. Recognition avoids sampling that ad by reusing freeAudio's existing background stream connection (the same one used for [Time-Shift (Rewind Live Radio)](#time-shift-rewind-live-radio)) instead of opening a new one, so it identifies whatever is actually playing rather than an ad. This works automatically and needs no configuration.

## Audio Mirror

The `Ctrl+Win+M` shortcut mirrors the currently playing stream to a second audio output device simultaneously. This is useful for listening on two different devices at the same time, such as speakers and headphones.

On first press, a selection dialog listing the available output devices appears. Once a device is chosen, mirroring begins and main playback continues uninterrupted. Pressing the shortcut again stops mirroring.

**Use cases:**

- **Speakers + headphones** — Let a guest follow the same broadcast on headphones while you listen through the computer speakers.
- **Recording setup** — Route the main output to speakers and the second output to an external recorder or audio interface for external capture.
- **Multi-room** — Play through a Bluetooth speaker and the built-in speaker simultaneously; no extra software needed to carry audio to another room.
- **Remote monitoring** — In a screen-sharing or remote desktop session, both the local and remote sides can hear the same stream simultaneously.

## Obligato Mode

The `Ctrl+Win+Shift+M` shortcut plays a favourite station quietly in the background on a completely separate audio engine from the main player — like a soft musical backdrop running underneath whatever you're actually doing.

On first press, a dialog opens with three controls:

- **Background station** — a list of your favourite stations to choose which one loops in the background. Requires at least one favourite; if your favourites list is empty, freeAudio tells you to add a station first (`Ctrl+Win+V` while a station is playing).
- **Audio output** — which device the background station plays through: **Same as main output** (the default), **System default**, or any specific device freeAudio can see.
- **Background volume** — how loud the background station plays, as a percentage of the main player's current volume (25%, 50%, 75%, 100%, 125%, or 150%). Your choices are remembered for next time.

Once started, the background station keeps playing independently of the main player — switching stations, podcasts, or audio books on the main player, or stopping it altogether, does not interrupt Obligato mode. Two things stay linked to the main player automatically:

- **Volume** — the background volume is continuously kept at the chosen percentage of whatever the main player's volume currently is, so raising or lowering the main volume (`Ctrl+Win+↑`/`↓`) scales the background music the same way.
- **Pause** — pausing the main player (`Ctrl+Win+P`) pauses the background station too, and resuming the main player resumes it. A full stop of the main player is not treated as a pause, so the background station keeps playing through it.

Press `Ctrl+Win+Shift+M` again at any time to stop Obligato mode.

## Recording

Recordings are saved to `Documents\freeAudio Recordings\` by default. The filename includes the station name (or the song title, in the song recording modes) and the time the recording started. The recordings folder can be changed at any time from NVDA Menu → Preferences → Settings → freeAudio → **Recordings folder**.

The **Recording output format** setting controls how completed recordings are saved:

- **Original stream format** writes the stream exactly as received. An HLS broadcast may therefore produce a `.ts` file.
- **Audio only, original codec** removes the video/container layer without re-encoding the audio. For example, AAC audio from an HLS `.ts` recording is normally saved as `.m4a`, preserving broadcast quality.
- **MP3** converts the audio after recording using the selected bitrate. Conversion uses the `ffmpeg.exe` bundled with freeAudio and runs in the background so NVDA stays responsive. If conversion fails, the original recording is retained.

**Instant recording:** While a station is playing, press `Ctrl+Win+E` once. Press again to stop. Playback continues uninterrupted throughout.

**Song recording (current song):** Press `Ctrl+Win+E` **twice** in quick succession while a station that broadcasts ICY metadata is playing. The recording starts a moment after the second press — freeAudio waits briefly in case you press a third time — and is named after the current track title. When the station announces the next track, the recording stops at that point and NVDA announces the saved filename. To end it early, press `Ctrl+Win+E` twice again. If the current station does not broadcast ICY metadata, song recording is not available and NVDA will inform you.

**Every-song recording:** Press `Ctrl+Win+E` **three times** in quick succession to record every song the station plays until you stop it. freeAudio keeps one connection open and starts a new file at each track change, so nothing is lost between songs. Each song is saved as its own file, named after the track and the time it started. When recording starts, NVDA announces that every song is being recorded and gives the current title. To stop, press `Ctrl+Win+E` twice; NVDA announces how many songs were saved.

A few details about every-song recording:

- The first song (recorded from the moment you pressed the keys) and the last song (cut off when you stop) are incomplete, so their filenames contain **(partial)** — for example `Artist - Title (partial) - 2026-10-09 10-15.mp3`.
- Pieces shorter than 15 seconds — jingles, ad stingers, or a title that flickers between two values — are discarded instead of being saved.
- It needs the station to send its track titles inside the audio stream itself (ICY metadata). HLS (`.m3u8`) stations, and servers that do not send titles that way, cannot be split into songs; NVDA tells you so and nothing is recorded.
- While it runs, `Ctrl+Win+I` announces the song being recorded right now, not the one it started with.

**Scheduled recording:** Open the Recording tab in the browser. Select a station from your favourites, enter the start time in HH:MM format and the duration in minutes, select one or more active days, then choose a recurrence mode and a recording mode:

A **Filter** field above the station list lets you narrow the favourites list in real time, so you can quickly find the station you want to schedule.

**Active days:** Check one or more days of the week. In single-recording mode, a separate entry is created for each selected day, each placed on the next upcoming occurrence of that day. In recurring mode, the recording repeats only on the checked days. If no days are checked, the recording is not restricted to specific days.

**Recurrence:**

- **Record once** — records a single time on each selected day. Each entry is placed on the next upcoming occurrence of that day; if the selected time has already passed today, the entry moves to the same day next week automatically.
- **Repeat weekly** — repeats every week on the selected active days until removed from the schedule list.

**Save recording to:** For each scheduled recording, you can choose to save to the default recordings folder or a custom folder. Use the **Browse...** button to select a folder interactively. If the chosen folder becomes unavailable, the recording falls back to the default folder and you are notified.

**Recording mode:**

- **Record while listening** — plays and records simultaneously through the BASS backend.
- **Record only** — records silently in the background without any audio output; the recording engine connects directly to the stream.

Once a schedule is added, it appears in the list below. Use the **Remove Selected** button to delete a schedule, or **Edit Selected** to modify its time, duration, recurrence, active days, recording mode, or output folder.

NVDA announces when a recording starts and when it finishes. If NVDA is restarted while a scheduled recording is active, the recording resumes automatically on startup.

**How recordings connect:** Instant, song and every-song recordings open their own connection to the station instead of copying what you are hearing, so an instant or every-song recording keeps going when you pause playback or switch to another station — it carries on with the station it started on. Stopping playback with `Ctrl+Win+S` while a recording is running asks you to confirm first, because it also ends the recording. The trade-off of a separate connection is that a station which serves a short advertisement to every brand-new connection may put that advertisement at the start of the file.

## Time-Shift (Rewind Live Radio)

Time-shift lets you rewind the station you're currently listening to, like a DVR or a cassette tape — pause the moment, go back a few minutes, and catch up to live again whenever you want. Playback never has to stop for this: rewinding and fast-forwarding both happen instantly on the same audio stream.

This feature is **disabled by default**. Enable it from NVDA Menu → Preferences → Settings → freeAudio → **Enable time-shift buffer (rewind live radio)**, or toggle it instantly at any time with `Ctrl+Win+T`.

> **Note:** freeAudio keeps a small background capture of the currently playing station running at all times — not just when this setting is enabled — because [Music Recognition](#music-recognition) relies on it for the ad-avoidance behaviour described in that section. When this setting is **off**, that background capture is kept to about the last 45 seconds and `Ctrl+Win+J`/`Ctrl+Win+K` remain unavailable — only the buffer size changes, not whether it runs. Enabling the setting grows the same capture to the full rewind buffer described below.

### How It Works

Once enabled, freeAudio continuously captures the currently playing station into a rolling local buffer in the background, independently of normal playback. The buffer holds the most recent audio, up to the length set by the **Time-shift buffer duration** setting; older audio is automatically discarded from the front as new audio arrives, so the buffer always represents "the recent past" relative to the live edge.

- **`Ctrl+Win+J`** — Rewind 15 seconds. The first press switches you from live playback into time-shifted playback, starting 15 seconds behind the live edge. Each further press moves another 15 seconds further back, up to the buffer limit.
- **`Ctrl+Win+K`** — Fast-forward 15 seconds while time-shifted. Once you reach the live edge, playback automatically switches back to the live stream and NVDA announces "Back to live" — you don't need to do anything extra to resume normal listening.
- **`Ctrl+Win+Alt+J`** / **`Ctrl+Win+Alt+K`** — The same rewind and fast-forward, but in steps of 1 second instead of 15, for fine adjustments. See [Fine Seeking (1 Second)](#fine-seeking-1-second).
- **`Ctrl+Win+T`** — Turns the whole feature on or off. Turning it off while time-shifted immediately returns you to live playback and stops the background capture for the current station.

Background capture keeps running the entire time you're time-shifted, so the live edge keeps moving forward even while you're listening to something a few minutes old — exactly like a real DVR.

### Enabling and Buffer Warm-Up

The buffer starts filling as soon as a station starts playing (once the feature is enabled) or the moment you enable the feature while already listening to a station. Because of this, rewinding is only possible once a few seconds of audio have actually been captured — if you press `Ctrl+Win+J` immediately after switching stations, NVDA will let you know there isn't enough buffered audio yet. Simply wait a few seconds and try again.

Switching to a different station always restarts the buffer for the new station; the previous station's buffered audio is discarded.

### Supported Streams

Time-shift works with the same range of streams freeAudio already supports:

- Plain HTTP/HTTPS streams (MP3, AAC, OGG, etc.), including Shoutcast/Icecast-style servers.
- **HLS (`.m3u8`) streams** — freeAudio resolves the station's master playlist, follows the media playlist, and downloads segments in the background to keep the buffer filled, the same way it works for plain streams.

In the rare case that a station's playlist cannot be read at all (for example, a broken or unreachable `.m3u8` manifest), NVDA will tell you rewinding isn't available for that particular station.

### Requirements and Limitations

- **Requires the BASS backend**, which freeAudio always uses for playback (see [Playback](#playback)).
- The length of the buffer is set by the **Time-shift buffer duration** setting — see [Settings](#settings).
- The buffer is per-station: switching stations, stopping playback, or restarting NVDA clears it and starts fresh.
- Time-shifted playback uses its own local buffer file and does not produce a saved recording — if you want to keep the audio permanently, use Instant Recording (`Ctrl+Win+E`) as well.

## Timer

Open the Timer tab in the station browser (`Alt+4`). Two types of timer can be added:

When choosing a station for an alarm timer, a **Filter** field above the station list lets you narrow the favourites list in real time.

**Alarm — start radio:** Automatically starts playing a selected station from your favourites at the specified time. Choose a station and enter the time in HH:MM format.

**Sleep — stop radio:** Stops playback at the specified time. When the timer fires, volume is gradually reduced over 60 seconds before playback stops. No station selection is needed; just enter the time.

For both types, if the entered time has already passed the action is scheduled for the following day. Adding a timer is blocked if another timer — of any type — already exists at the same time; a message informs you of the conflict and prompts you to remove the existing entry first. Pending timers are listed in the tab; select one and press the Remove Selected Timer button to cancel it.

**Recurring timers:** Under **Recurrence**, choose **Repeat weekly** instead of the default one-time option to have the timer fire every week rather than once. An **Active days** checklist then lets you pick which days of the week it repeats on; leaving every day unchecked repeats it every day. A recurring timer keeps firing on schedule until you remove it from the pending-timers list — it is not a one-off entry that disappears after firing.

## Podcasts

freeAudio includes a full-featured podcast player. You can subscribe to any RSS or Atom podcast feed, browse episodes, play them, download them, and resume playback from where you left off — all fully accessible.

### Accessing the Podcasts Tab

Open the station browser with `Ctrl+Win+R` and switch to the **Podcasts** tab using `Ctrl+Tab` or `Alt+6`. The tab is organised into three main areas:

1. **Search and add** — top section for discovering new podcasts, including a preview list that shows the episodes of whichever search result is currently selected.
2. **Subscriptions** — list of your subscribed feeds.
3. **Episodes** — list of episodes for the selected feed, with playback controls. A **Bookmarks** list directly below it shows the bookmarks of the selected episode — see [Bookmarks](#bookmarks).

### Adding a Podcast Feed

You can add a podcast feed in two ways:

**By URL:**

- In the **Search** field, paste the full RSS or Atom feed URL (e.g. `https://example.com/feed.xml`).
- Press Enter.
- freeAudio fetches the feed, validates it, and adds it to your subscriptions. If the feed is valid, you will hear a confirmation with the feed title. If it fails, an error message explains why.

**By searching:**

- In the **Search** field, type a keyword (podcast title, topic, or host name) and press Enter.
- freeAudio searches the iTunes podcast directory and displays matching podcasts in the **Search results** list.
- Selecting a result fetches that feed in the background and lists its episodes in the **Episodes in selected result** list right below, so you can preview what the show actually contains before deciding to subscribe — see [Previewing Episodes Before Subscribing](#previewing-episodes-before-subscribing) below.
- Once you're happy with what you see, select the result and either press `Enter`, or open its context menu (Applications key / `Shift+F10`, or right-click) and choose **Subscribe**, to add it to your subscriptions. The feed is added immediately and appears in your subscriptions list. There is no separate "Add Selected from Search" button — `Enter` or the context menu is the only way to subscribe from search results, keeping the interface clean and accessible.

> **Tip:** You can also type a feed URL directly into the search field — if it looks like a valid URL, the add-on will attempt to add it as a feed without searching.

**Context menu for search results:** Right-click a search result, or select it and press the Applications key / `Shift+F10`, to open a menu with a single **Subscribe** action, identical to pressing `Enter` on the result.

### Previewing Episodes Before Subscribing

Before committing to a subscription, you can listen to a podcast's episodes straight from the search results. Whenever you select a podcast in the **Search results** list, freeAudio fetches that feed and shows its episodes — title and publish date — in the **Episodes in selected result** list underneath.

- Select an episode in that preview list and press `Enter`, or open its context menu (Applications key / `Shift+F10`, or right-click) and choose **Preview**, to start playing it through the normal player. All the usual playback controls (pause, volume, time-shift, etc.) work on it exactly as they would on any other station or episode.
- While an episode is being previewed, the same context menu shows **Stop Preview** in place of **Preview** — choose it, or press `Enter` again on that episode, to stop.
- Previewing does not subscribe you to anything; it's purely for listening before you decide. The preview list itself is temporary — it's replaced as soon as you select a different search result, and it does not persist anywhere the way your actual subscriptions do.

### Managing Subscriptions

Once you have added some feeds, they appear in the **Subscriptions** list. Each entry shows the feed title and the number of episodes available.

- **Select a feed** to see its episodes in the lower list. The **Feed details** read-only text box below the subscriptions list shows the feed title, author, description, episode count, and URL.
- **Refresh a feed** — select it and press the **Refresh Feed** button (available via context menu, see below) to fetch the latest episodes. All feeds are also refreshed automatically in the background when you open the Podcasts tab, so you usually see the most recent episodes without manual intervention.
- **Remove a feed** — select it and press `Delete` or use the context menu to remove it from your subscriptions. You will be asked for confirmation before removal.

**Context menu for feeds:** Right-click a feed, or select it and press the Applications key / `Shift+F10`, to open a menu with:

- **Refresh Feed** — fetch new episodes now.
- **Save Audio Profile for This Podcast** / **Clear Audio Profile** — see [Podcast Audio Profile](#podcast-audio-profile).
- **Remove Feed** — delete the subscription.
- **Copy Feed URL** — copy the feed URL to the clipboard.

### Browsing and Playing Episodes

Select a feed in the subscriptions list; its episodes appear in the **Episodes** list below. Each episode shows:

- Its episode number (1 = the oldest episode in the feed, counting up to the newest).
- Its publication date (if available).
- Its title.
- A **"Listened"** prefix if the episode has been fully played.
- A duration suffix, either total duration (if never played) or elapsed/total progress (if partially played).

**Playback:**

- Select an episode and press `Enter` or `Space` to start playing it. If an episode was partially played before, it resumes from where you left off.
- The row does *not* update while the episode is playing — this is intentional, so NVDA doesn't repeatedly re-announce the row while you're sitting on it. Its "Listened" flag and duration are refreshed immediately the moment you pause the episode or it finishes playing, so the display is always accurate right when it matters; it simply doesn't tick up second by second during playback.
- Use `F3` / `F4` on the Podcasts tab to move to the previous / next episode and play it immediately. You can also use `←` / `→` while the episode list is focused, or `Ctrl+←` / `Ctrl+→` anywhere on the Podcasts tab — both work identically.
- Use `Shift+F3` / `Shift+F4` to move between feeds without playing episodes.
- Press `Space` while an episode is playing to pause or resume playback.

**Resuming playback:** freeAudio saves your position in each podcast episode automatically — immediately whenever you pause or the episode finishes, and every 15 seconds in the background while you keep listening, so a crash or unexpected restart won't lose much progress. If you stop or pause playback and come back later, the episode resumes from the saved position. If you play the episode to the very end (within the last 3 seconds), it is marked as "Listened" and will not resume — it starts from the beginning next time, and the "Listened" prefix appears in the list.

**Context menu for episodes:** Right-click an episode, or select it and press the Applications key / `Shift+F10`, to open a menu with:

- **Play Episode** — start playback.
- **Download Episode** — download the episode file to your recordings folder.
- **Save Audio Profile for This Podcast** / **Clear Audio Profile** — same commands as the feed's own context menu, included here for convenience so you don't have to switch back to the Subscriptions list. They still save one profile for the whole podcast, not a separate one for this episode — see [Podcast Audio Profile](#podcast-audio-profile).
- **Copy Episode URL** — copy the direct audio URL to the clipboard.

### Downloading Episodes

Select an episode and click the **Download Episode** button (or use the context menu). The episode is downloaded to your recordings folder (`Documents\freeAudio Recordings\` by default). The filename is based on the episode title and the detected file extension (`.mp3`, `.m4a`, `.ogg`, etc.). NVDA announces when the download starts and finishes. If the file already exists, you are informed and the download is skipped.

### Filtering Episodes

Above the episode list is a **Filter** field. As you type, the episode list is filtered in real time to show episodes whose title contains the typed text, or whose episode number matches it exactly — so typing `47` jumps straight to episode 47 even if "47" doesn't appear anywhere in its title. NVDA announces the number of matching episodes after each change. Press the `Down` arrow from the filter field to move focus directly into the filtered list.

### Podcast Playback Details

Podcast episodes are played using the **BASS backend** (the same engine used for radio streams, and the only playback backend freeAudio uses). Because episodes are downloaded progressively and are seekable, you can use the time-shift rewind/forward shortcuts (`Ctrl+Win+J`/`Ctrl+Win+K`) while playing a podcast to seek within the episode. The position is saved automatically so you can resume later.

**Tiered seeking:** Unlike live radio's fixed 15-second rewind, seeking within a podcast, audio book, or jukebox track scales with how you press the key, so you can make a small correction or jump a long way without repeated presses:

- **Holding the key down** (auto-repeat) steps back or forward **5 seconds** per repeat — the same small step the shortcut uses on files.
- **One deliberate tap** seeks **12 seconds**.
- **Two taps** in quick succession seek **1 minute**.
- **Three or more taps** seek **5 minutes**; further taps in the same burst don't escalate any further.

A deliberate tap is held for a brief moment before it actually seeks, in case another tap is still coming — only one seek happens per tap sequence, sized for however many taps were ultimately made, not the sum of each tap's amount. After a seek, NVDA announces the resulting elapsed/remaining position in the episode rather than just "X seconds forward/back".

### Fine Seeking (1 Second)

For small corrections, such as replaying a word you just missed, freeAudio has a separate pair of commands that always move by exactly **1 second**, regardless of how you press them:

- **`Ctrl+Win+Alt+J`** — 1 second back, from anywhere in Windows.
- **`Ctrl+Win+Alt+K`** — 1 second forward, from anywhere in Windows.
- **`Alt+←`** / **`Alt+→`** — the same two commands inside the Station Browser, on any tab.

On a podcast episode, audio book part or jukebox track they work exactly like the normal seek commands, only with a 1-second step: NVDA announces the resulting elapsed/remaining position, and on an audio book or jukebox folder the part and track boundaries behave as described for `Ctrl+Win+J` / `Ctrl+Win+K` (a forward seek past the end moves on to the next part or track; a rewind past the start first parks at 0:00 and only a second rewind within 10 seconds goes back to the previous part or track).

On a live radio station they move by 1 second in the time-shift buffer. As with `Ctrl+Win+J`, the buffer must be enabled in the settings, and the first rewind switches from live playback into time-shifted playback. A fast-forward that ends up within about 2 seconds of the live edge returns to live and announces "Back to live".

**Playback speed:** You can adjust the playback speed of podcast episodes, audio books, and jukebox tracks using `Ctrl+Win+Shift+K` (faster) and `Ctrl+Win+Shift+J` (slower). The speed changes in 0.1x increments, ranging from 0.5x to 2.0x, with pitch preserved.

**Transpose (pitch shift):** Independent of playback speed, you can shift the pitch of a podcast episode, audio book, or jukebox track up or down with `Shift+Win+K` / `Shift+Win+J` — see [Transpose (Pitch Shift)](#transpose-pitch-shift).

**Resume sound effect:** Whenever an episode resumes from a saved position, freeAudio briefly plays a soft cassette-loading sound effect on a separate channel while it seeks back to your saved spot, instead of letting the episode's own audio play audibly from 0:00 in the meantime. This is independent of the **Station switch transition** setting — that setting only affects switching between live radio stations, not resuming podcasts or audio books.

### Podcast Audio Profile

Right-click a podcast in the Subscriptions list, or right-click any of its episodes, and choose **Save Audio Profile for This Podcast** to save the current volume, effects, EQ gains and/or playback speed as a profile tied to that podcast. Whenever any episode of that podcast plays, the saved settings are applied automatically, overriding the global defaults. Because the command is available from both the feed context menu and the episode context menu, you can reach it without switching back to the Subscriptions list — either way, it always saves one profile for the whole podcast, not a separate one per episode.

A dialog with 15 options lets you choose exactly what to save:

- **Volume only**
- **Effects only**
- **Volume and effects**
- **Volume and playback speed**
- **Effects and playback speed**
- **Playback speed only**
- **Volume, effects, and playback speed**
- **Pitch transpose only**
- **Volume and pitch transpose**
- **Effects and pitch transpose**
- **Playback speed and pitch transpose**
- **Volume, effects, and pitch transpose**
- **Volume, playback speed, and pitch transpose**
- **Effects, playback speed, and pitch transpose**
- **Volume, effects, playback speed, and pitch transpose**

Only the pieces you pick are written to the profile; anything left out keeps whatever was already saved for it. For example, choosing **Playback speed only** on a podcast that already has a saved volume/effects profile updates just the speed and leaves the rest untouched.

**Clear Audio Profile** removes the saved profile from the podcast, from either context menu. It is only enabled when the podcast currently has a saved profile.

### Podcast Data Storage

Your subscriptions are stored in `freeAudio_podcasts.json` in the NVDA user configuration folder. Episode positions are stored separately in `podcast_positions.json` in the same location. Both files are plain JSON and can be backed up or transferred to another computer.

## Audio Books (GETEM, LibriVox and Project Gutenberg)

freeAudio includes an audio book player that searches, plays, and downloads books from three sources:

- **[GETEM](https://getem.boun.edu.tr/)** — the digital library run by Boğaziçi University's Center for the Visually Impaired. Requires a free membership to stream or download a book's audio (browsing does not) — see [Signing In](#signing-in) below.
- **[LibriVox](https://librivox.org/)** — the volunteer-read public-domain audiobook project. No account or sign-in of any kind is needed; its whole catalogue, including the audio files themselves, is public domain and openly reachable.
- **Project Gutenberg Open Audiobook Collection** — human- and computer-narrated public-domain audiobooks hosted on [archive.org](https://archive.org/), companion to the Project Gutenberg text library. Like LibriVox, no account or sign-in is needed.

Results from all three sources appear together in a single merged **Search results** list and a single merged **Library** list — there is no separate tab or dropdown to switch between them. Each book's source (GETEM, LibriVox or Project Gutenberg) is shown as a label next to its title, and in its details, so you can always tell which one you're looking at. You can search, preview, add, play, and download books from any source exactly the same way; play multi-part works with automatic resume across parts; and download books for offline listening — all fully accessible.

Any source can be turned off individually from **NVDA Menu → Preferences → Settings → freeAudio** with the **Audio book sources** checklist, if you only want to search some of them. All three are enabled by default.

> **Note:** Listening to a GETEM book requires a free GETEM membership. Browsing GETEM's catalogue does not need an account, but resolving and playing a GETEM book's audio does — see [Signing In](#signing-in) below. LibriVox and Project Gutenberg books never require an account.

### Accessing the Audio Books Tab

Open the station browser with `Ctrl+Win+R` and switch to the **Audio Books** tab using `Ctrl+Tab` or `Alt+7`. The tab has three main areas:

1. **Search** — a text field to search all enabled catalogues at once, with a results list that appears once a search is run.
2. **Library** — the list of books you have added from any source, where you play, download and manage them. A **Bookmarks** list directly below it shows the bookmarks of the selected book — see [Bookmarks](#bookmarks).
3. **Details** — a read-only box showing the source, title, author, narrator, publisher, format, number of parts, description and catalogue URL of whichever book is selected, in either list.

### Signing In

GETEM requires being a registered member to stream or download a book's actual audio, even though the catalogue itself can be searched freely. Enter your GETEM username and password once in **NVDA Menu → Preferences → Settings → freeAudio**; they are stored encrypted on disk (via the Windows Data Protection API, tied to your Windows user account) and reused automatically afterward. If you try to play or download a GETEM book before entering credentials, freeAudio tells you to add them in Settings first.

LibriVox and Project Gutenberg need no sign-in step at all — their results and audio can be searched, previewed, played and downloaded immediately, with no credentials to enter.

### Searching for Audio Books

Type a search term into the search field and press `Enter`. freeAudio searches whichever sources are enabled in Settings and merges the results into one list:

- **GETEM** is searched by title, author, narrator, subject and publisher at once, since GETEM's own search form only supports narrowing by all of them together rather than a single search across any of them. Only works that are actually available as audio (human or computer narration, audio description, radio drama, DAISY talking books, etc.) are shown; braille, large-print and other non-audio formats are filtered out automatically.
- **LibriVox** is searched by title or author/reader against its public-domain catalogue.
- **Project Gutenberg** is searched by title or author against the Open Audiobook Collection on archive.org.

Pasting a book's catalogue/detail page URL directly into the search field (a GETEM catalogue page, or an archive.org "details" page for a LibriVox or Project Gutenberg title) resolves that single book directly instead of running a keyword search.

NVDA announces how many audio books were found in total.

Selecting a result shows its details — author, narrator, publisher, format and part count — in the details box below.

**Previewing:** Select a result and press `Space`, or open its context menu (Applications key / `Shift+F10`, or right-click) and choose **Preview**, to start playing it from its first part without adding it to your library. While a book is being previewed, the same context menu shows **Stop Preview** in its place — choose it, or press `Space` again, to stop. Previewing a book does not save your listening position, since that is only tracked for books already in your library.

**Adding to your library:** Select a result and press `Enter`, or use its context menu and choose **Add to Library**, to add it. freeAudio tells you if the book is already there.

### Your Library

Books you've added appear in the **Library** list, showing title, author and format. Selecting one shows its details below.

- Press `Enter` or `Space` to play the selected book. If nothing is loaded, `Space` starts it; if something is already playing, `Space` pauses it instead, matching the rest of the player.
- Use `F3` / `F4` on the Audio Books tab to move to the previous / next **book** in your library and start playing it. `Ctrl+←` / `Ctrl+→` do the same while the library list is focused.
- Use `Shift+F3` / `Shift+F4` to move between **parts** of the currently playing book instead — the reverse of the Podcasts tab, where F3/F4 move between episodes and Shift+F3/F4 move between feeds. This is because a book is a single library entry even when it has several parts, so the finer-grained "part" navigation sits on the Shift-modified keys here.
- With the Station Browser closed, `Ctrl+Win+F3` / `Ctrl+Win+F4` (previous / next book) and `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (previous / next part) do the same thing — see [Skipping Items With the Station Browser Closed](#skipping-items-with-the-station-browser-closed).

**Context menu for library entries:** Right-click a book, or select it and press the Applications key / `Shift+F10`, to open a menu with:

- **Play Media** — start playing, same as `Enter`.
- **Download Book** — download every part of the book; see [Downloading Audio Books](#downloading-audio-books) below.
- **Copy the URL** — copy the book's catalogue page URL to the clipboard (the GETEM catalogue page for a GETEM book, or the archive.org details page for a LibriVox or Project Gutenberg book).
- **Save Audio Profile for This Book** / **Clear Audio Profile** — see [Audio Book Audio Profile](#audio-book-audio-profile) below.
- **Remove from the Library** — delete the book from your library.

You can also mark several books at once and remove them all together — see [Marking and Removing Multiple Items](#marking-and-removing-multiple-items) under Favourites.

### Playback and Resuming

A multi-part work is treated as a single item in the player, not one row per part — the same way a podcast episode is a single item regardless of how it's delivered. freeAudio remembers which part you last listened to and resumes there automatically the next time you play that book, even across an NVDA restart.

When one part finishes, freeAudio automatically starts the next part of the same book — you don't need to select it manually. This happens even if the Station Browser window is closed at the time; the "now playing" part shown in the Library list is resynced automatically the next time the window is opened.

Playback streams through a small local relay rather than downloading the whole part first, so listening starts as soon as the first bytes arrive — the same immediate-start behaviour podcasts use. All the usual player controls (pause, volume, time-shift, playback speed, transpose, output device, etc.) work on an audio book exactly as they would on a station or podcast episode.

Like podcasts, resuming a book from its saved position plays a brief cassette-loading sound effect while freeAudio seeks to your saved spot — see the **Resume sound effect** note in [Podcast Playback Details](#podcast-playback-details).

### Audio Book Audio Profile

Right-click a book in your Library list and choose **Save Audio Profile for This Book** to save the current volume, effects, EQ gains and/or playback speed as a profile tied to that book. Whenever the book (or any of its parts) plays, the saved settings are applied automatically, overriding the global defaults. This works exactly the same way as [Podcast Audio Profile](#podcast-audio-profile) above, including the same set of save options (volume, effects, and/or playback speed, in any combination) and the same partial-update behaviour.

**Clear Audio Profile** removes the saved profile from the book; it is only enabled when the book currently has a saved profile.

### Downloading Audio Books

Select a book in your library and choose **Download Book** from its context menu to save every part to its own folder (named after the book) inside your recordings folder (`Documents\freeAudio Recordings\` by default). Files are numbered so the parts always sort back into listening order, regardless of what GETEM itself calls them. NVDA announces how many parts were saved once the download finishes; if a part fails, the last error is reported alongside the count.

### Direct Keyboard Shortcuts for Audio Books

Every book in your Audio Books library — whether it comes from GETEM, LibriVox or Project Gutenberg — is registered as a separate script in NVDA's Input Gestures dialog, under the **freeAudio Audio Books** category, exactly like [Direct Keyboard Shortcuts for Favourite Stations](#direct-keyboard-shortcuts-for-favourite-stations) and [Direct Keyboard Shortcuts for Jukebox Entries](#direct-keyboard-shortcuts-for-jukebox-entries). You can assign any keyboard shortcut to any book and press it from anywhere — no need to open the browser window first. No shortcuts are assigned by default.

To assign a shortcut:

1. Open NVDA Menu → Preferences → Input Gestures.
2. Expand the **freeAudio Audio Books** category.
3. Find the book by title (each entry is named "*title* playback shortcut"), select it, and press **Add**.
4. Press the desired key combination and confirm.

The shortcut starts the book immediately, resuming at the part you last listened to; the position inside that part is restored the same way as when you play the book from the library list. If the book's list of parts has not been fetched yet, NVDA says "Loading *title*" and playback starts as soon as it is ready (a GETEM book needs your saved login — see [Signing In](#signing-in)). When a part ends, the next one starts automatically, with or without the Station Browser open.

When you add a book to the library or remove one, the **freeAudio Audio Books** category is updated straight away — the Input Gestures dialog does not need to be reopened for the change to show once you open it again. If a book is removed, its entry disappears and any shortcut assigned to it is automatically cleared by NVDA; should a stale shortcut still fire, NVDA says the audio book is no longer in the library.

### Audio Book Data Storage

Each source keeps its own library file, even though they're displayed merged in the Audio Books tab. Your GETEM library (added books and their listening progress) is stored in `freeAudio_getem_library.json`, your LibriVox library is stored separately in `freeAudio_librivox_library.json`, and your Project Gutenberg library is stored separately in `freeAudio_gutenberg_library.json` — all three in the NVDA user configuration folder. Your encrypted GETEM credentials are stored separately in `freeAudio_getem_credentials.bin` in the same location, and can only be decrypted by the same Windows user account that saved them. LibriVox and Project Gutenberg have no credentials file, since neither requires an account.

## Local Jukebox

freeAudio's **Jukebox** tab gives you two ways to play audio files that are already on your computer: search every attached drive for files by name, or build a persistent personal library of files and folders. Whatever you play from here gets the same treatment as a podcast or audio book — automatic resume, tiered rewind/fast-forward, playback speed, pitch transpose, and per-item audio profiles all work exactly the same way.

### Accessing the Jukebox Tab

Open the station browser with `Ctrl+Win+R` and switch to the **Jukebox** tab with `Ctrl+Tab` or `Alt+8`, or open it directly from anywhere with the global shortcut `Ctrl+Win+U`. The tab is organised into three main areas:

1. **Search on devices** — a text field that searches every locally attached, ready drive for audio files whose filename contains the typed text. Press `Enter` to start the search.
2. **Search results** — a list that appears once a search has been run, showing the matching files. Hidden until then, so the tab stays uncluttered when there's nothing to search.
3. **Jukebox and Tracks** — the persistent list of items you've added, followed by the list of tracks in whichever entry is selected (for a file entry, just that one file; for a folder entry, every audio file found inside it). A **Bookmarks** list follows the Tracks list and shows the bookmarks of the selected track — see [Bookmarks](#bookmarks).

The **Add File…**, **Add Folder…**, **Remove**, **Export Jukebox…** and **Import Jukebox…** buttons sit at the bottom of the tab.

### Searching for Files on Devices

Type any part of a filename into the **Search on devices** field and press `Enter`. freeAudio walks every locally attached drive — fixed disks, USB drives and memory cards — looking for audio files (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus`, and several more) whose filename contains the search text. The search runs in the background, so NVDA stays responsive. Network drives are skipped by default, because searching a network share can turn a one-second search into one that takes minutes, or hangs if the share cannot be reached. To include them, turn on **Include network drives when searching the jukebox** in the settings.

- **Space** on a search result previews it — starts playback through the normal player. Press **Space** again on the same file to stop the preview.
- **Enter** on a search result adds it to your jukebox.
- The context menu (Applications key / `Shift+F10`, or right-click) offers the same two actions: **Preview** / **Stop Preview** and **Add to Jukebox**.
- Starting a new search cancels any search still running, so a slow search on a large drive never delays a fresh one.

### Building Your Jukebox

The Jukebox list is your persistent personal library. Two kinds of item can be added:

- **Add File…** — opens a file picker that lets you add one or more individual audio files. All chosen files are added in one go.
- **Add Folder…** — opens a folder picker that lets you select multiple folders at once. Every audio file found inside each chosen folder, including in its subfolders, is treated as one of that folder's **tracks**. Each folder is added as its own single entry in your Jukebox list; the files inside it are listed in the Tracks list when the folder is selected. NVDA announces how many folders were added once the picker closes.
- **Remove** — deletes the currently selected entry from your Jukebox. Removing a folder entry does not delete any files from disk or device; it just forgets the folder. You can also mark several entries at once and remove them all together — see [Marking and Removing Multiple Items](#marking-and-removing-multiple-items) under Favourites.

Your Jukebox list is saved automatically, so it survives NVDA restarts. Folder contents are scanned on demand and cached, so adding a folder is instantaneous even for very large collections — the full scan happens the first time you select that folder. If you add files to a folder outside freeAudio, use the **Rescan Folder** item in the folder's context menu to pick them up.

### Adding Items from Windows Explorer

Two more commands, available only while a file or folder is focused in Windows Explorer's file list (the Details/Icons list — not the address bar, folder tree, ribbon, or search box), let you skip the Add File…/Add Folder… dialogs above entirely:

- **Play the focused file with freeAudio** — plays the highlighted audio file directly, without needing it to already be in your Jukebox list. Works only on files; using it on a folder tells you to add the folder to the jukebox instead.
- **Add the focused item to the freeAudio jukebox** — adds the highlighted file or folder to your Jukebox list, exactly as if you'd used **Add File…** or **Add Folder…** above.

Neither command has a default key assigned. Assign one from NVDA Menu → Preferences → Input Gestures → freeAudio **while focused inside a File Explorer window**.

### Playing from the Jukebox

- **Enter** on a Jukebox entry plays it directly: for a file entry, the file itself; for a folder entry, the folder in order — starting from the track highlighted in the Tracks list or, if none is highlighted, from where the folder was last left off (the first track if it has never been played). When a track ends, the next track in the folder starts automatically.
- **Space** on a Jukebox entry pauses playback if anything is playing; otherwise it plays the focused entry.
- **Enter** or **Space** on the Tracks list plays the focused track. **Space** pauses first if something is already playing. A track started this way plays on its own and does not continue to the next track when it ends; use `F3` / `F4` or play the folder entry itself for continuous playback.
- **F3 / F4** on the Jukebox tab move between tracks within the currently selected entry and play immediately. In a folder entry the track is played as part of the folder, so the following tracks still start automatically when it ends.
- **Shift+F3 / Shift+F4** move between entries in the Jukebox list (files and folders), mirroring how these keys move between feeds on the Podcasts tab.
- **Ctrl+← / Ctrl+→** while the entries or tracks list is focused do the same as F3/F4 on the tracks list — previous / next track, with automatic continuation in a folder.
- With the Station Browser closed, `Ctrl+Win+F3` / `Ctrl+Win+F4` (previous / next track) and `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (previous / next entry) do the same — see [Skipping Items With the Station Browser Closed](#skipping-items-with-the-station-browser-closed).

### Jukebox Playback Details

Every track played from the Jukebox gets the full local-media treatment:

- **Resume:** freeAudio remembers your position in each track, saves it on pause and periodically while playing, and resumes from that point when you play it again — even across an NVDA restart.
- **Automatic next track:** when a track played as part of a folder ends, the next track in that folder starts by itself, whether or not the Station Browser is open, and keeps doing so after you skip tracks with `F3` / `F4` or `Ctrl+Win+F3` / `Ctrl+Win+F4`. When the last track has finished, the folder's saved position is cleared so it starts again from the first track next time. Pressing next on the last track by hand does not clear it.
- **Tiered seeking:** `Ctrl+Win+J` / `Ctrl+Win+K` seek within the track using the same tap/hold scaling as podcasts and audio books — hold for 5 seconds per repeat, one tap for 12 seconds, two taps for 1 minute, three or more taps for 5 minutes. `Ctrl+Win+Alt+J` / `Ctrl+Win+Alt+K` seek exactly 1 second — see [Fine Seeking (1 Second)](#fine-seeking-1-second).
- **Playback speed:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` adjust speed in 0.1x steps from 0.5x to 2.0x, with pitch preserved.
- **Transpose:** `Shift+Win+J` / `Shift+Win+K` shift pitch without changing speed — see [Transpose (Pitch Shift)](#transpose-pitch-shift).


> **Note:** The time-shift buffer (used for rewinding live radio) is deliberately **not** started for Jukebox tracks — they're already seekable local files, so a background capture has no purpose and would only consume disk space. Rewind and fast-forward still work because they act directly on the file being played.

### Renaming Jukebox Entries

Choose **Rename…** from a Jukebox entry's context menu (Applications key / `Shift+F10`) to give it a custom display name. The custom name replaces the file or folder name in the Jukebox list and is written into the `#EXTINF` line when the entry is exported to M3U (see [Exporting and Importing the Jukebox Library](#exporting-and-importing-the-jukebox-library) below). Leave the field empty to clear the custom name and fall back to the original file or folder name.

### Organising the Jukebox into Groups

Jukebox entries can belong to a group, shown as a "— Group" suffix after the entry name in the list, exactly like [Organising Favourites into Groups](#organising-favourites-into-groups):

- Mark one or more entries with `.` (see [Marking and Removing Multiple Items](#marking-and-removing-multiple-items) above), then choose **Assign to Group…** from the context menu and type a group name. Leave the field empty to remove the marked entries from their group instead. If nothing is marked, the command applies to the currently selected entry.
- The Filter field above the Jukebox list also matches against group names, the same way it does for Favourites.

### Reordering the Jukebox

With an entry selected in the Jukebox list, press `comma` to enter move mode — you will hear a beep. Navigate to the target position with the arrow keys, then press `comma` again. The entry is placed at the chosen position and the new order is saved immediately. Pressing `comma` again at the same position cancels the move.

### Exporting and Importing the Jukebox Library

The Jukebox tab includes two buttons for backing up and restoring your library, at the bottom of the tab:

**Export Jukebox…** — saves your entire Jukebox list to a file. A save dialog lets you choose between two formats:

- **JSON** (`.json`) — a complete backup that preserves every entry's path, custom name, group, and saved audio profile. Recommended for restoring your library later or moving it to another computer.
- **M3U playlist** (`.m3u`) — a lighter format compatible with most media players, listing each entry's path with its custom name (if any) in a preceding `#EXTINF` line. Groups and audio profiles are not included in M3U, so restoring from M3U loses that detail.

**Import Jukebox…** — loads entries from a previously exported JSON or M3U file. After selecting the file, you are asked how to add the entries:

- **Yes (Merge)** — adds the imported entries to your existing library without removing any current entries. Entries whose path matches one already in your library are not added twice.
- **No (Replace)** — clears your current Jukebox list entirely and replaces it with the contents of the imported file.
- **Cancel** — returns to the browser without making any changes.

### Direct Keyboard Shortcuts for Jukebox Entries

Every entry in your Jukebox list is registered as a separate script in NVDA's Input Gestures dialog, under the **freeAudio Jukebox** category, exactly like [Direct Keyboard Shortcuts for Favourite Stations](#direct-keyboard-shortcuts-for-favourite-stations). You can assign any keyboard shortcut to any entry and press it from anywhere — no need to open the browser window first.

To assign a shortcut:

1. Open NVDA Menu → Preferences → Input Gestures.
2. Expand the **freeAudio Jukebox** category.
3. Find the entry by name, select it, and press **Add**.
4. Press the desired key combination and confirm.

The shortcut plays the entry immediately — for a file entry, the file itself; for a folder entry, the track where the folder was last left off (its first track if it has never been played), after which the following tracks play automatically, even with the Station Browser closed. If the entry is later removed from your Jukebox, its entry disappears from the category and any shortcut assigned to it is automatically cleared by NVDA. When a new entry is added, it appears in the category straight away — the Input Gestures dialog does not need to be reopened.

## Bookmarks

Bookmarks let you mark a spot in an **audio book part**, a **podcast episode** or a **jukebox track** and come back to it later. They are not available for live radio stations, which have no fixed positions to return to.

### Adding a Bookmark

- Press **`Ctrl+Win+F12`** from anywhere in Windows, or **`F12`** while the Station Browser is active, to add a bookmark at the current playback position.
- NVDA announces the bookmark's name and position, for example "Bookmark added: Bookmark 2, 12:30".
- If nothing is playing, or a live radio station is playing, freeAudio tells you so and no bookmark is added.

A bookmark's default name is its **ordinal position** among the item's bookmarks, earliest first: "Bookmark 1", "Bookmark 2", and so on. Because the number follows the position in the item, adding an earlier bookmark renumbers the later ones that still have a default name. Bookmarks you have renamed keep their own name.

### The Bookmark List

Each of the Podcasts, Audio Books and Jukebox tabs has a **Bookmarks** list right next to the item it belongs to:

- **Podcasts** — directly below the Episodes list, showing the bookmarks of the selected episode.
- **Audio Books** — directly below the Library list, showing the bookmarks of every part of the selected book. When a book has several parts, each row starts with the part's title.
- **Jukebox** — directly below the Tracks list, showing the bookmarks of the selected track.

Each row shows the bookmark's name and position. A **[text]** or **[voice note]** marker is added when the bookmark has a text note or a voice note, and **(marked)** when you have marked it with `.`. The list follows the selection above it and is also refreshed when you add a bookmark with `Ctrl+Win+F12` while the window is open.

While a bookmark list has focus, the playback keys of the tab above it also work there: `←` / `→` seek, `Shift+←` / `Shift+→` transpose, `Page Up` / `Page Down` change the playback speed, `Ctrl+←` / `Ctrl+→` switch to the previous or next episode, book or track, and `Alt+←` / `Alt+→` seek by 1 second.

| Key | Action |
|---|---|
| `.` | Marks or unmarks the focused bookmark. See [Marking and Removing Multiple Items](#marking-and-removing-multiple-items). |
| `Enter` | Plays from the focused bookmark. |
| `Space` | Pauses if something is playing; otherwise plays from the focused bookmark. |
| `Delete` | Deletes every marked bookmark, or the focused one if none is marked. A confirmation dialog appears first. |
| Applications key / `Shift+F10` | Opens the bookmark context menu. |

### Bookmark Context Menu

- **Play from Bookmark** — if the item is already loaded, playback jumps to the bookmark; otherwise the item starts playing from that position.
- **Rename…** — gives the bookmark a custom name. Leave the field empty to go back to the default name.
- **Delete Selected** — deletes the marked bookmarks, or the focused one if none is marked.
- **Add or Edit Text…** — opens a multi-line field for a text note. Leave it empty to remove the text.
- **Add Voice Note…** — opens a dialog that starts recording from the default microphone as soon as it appears. Press **Stop and Save** to attach the recording to the bookmark, or **Cancel** to discard it. Adding a new voice note replaces the previous one.
- **Clear Notes** — removes both the text note and the voice note of the focused bookmark. Enabled only when the bookmark has a note.
- **Repeat Between Marked Bookmarks** — see below. Enabled when at least two bookmarks are marked.
- **Stop Repeat** — turns repeat mode off. Enabled while a repeat is active.

### What Happens When Playback Reaches a Bookmark

During normal playback, when the position reaches a bookmark, freeAudio plays **two quick beeps**. If the bookmark has no note, playback simply carries on.

If the bookmark has a text note and/or a voice note, playback is **paused**, the text is spoken by NVDA's current synthesizer and the voice note is played, and then playback **resumes where it left off**. If you stop playback or start something else while the note is playing, playback is not resumed.

Bookmarks are detected while playing normally. Seeking or jumping past a bookmark does not trigger it.

### Repeating the Section Between Bookmarks

Mark two or more bookmarks of the **same item** with `.`, then choose **Repeat Between Marked Bookmarks**. Playback jumps to the earliest marked bookmark and loops between the earliest and the latest marked bookmark, and NVDA announces the two positions. This is useful for going over a hard-to-follow passage, a language-learning phrase or a piece of music you are practising. Choose **Stop Repeat** to return to normal playback. The repeat is not saved between sessions, and if a different item starts playing the repeat range is ignored and dropped after about 20 seconds.

### Bookmark Data Storage

Bookmarks are stored in `freeAudio_bookmarks.json` in the NVDA user configuration folder, and voice notes are stored as `.wav` files in the `freeAudio_bookmark_audio` folder next to it. Both can be backed up or transferred to another computer. Deleting a bookmark also deletes its voice note file. All bookmarks and voice notes can be removed at once with the **Bookmarks** item of the clean-up dialog — see [Clean Up: Reset Settings and Delete Saved Data](#clean-up-reset-settings-and-delete-saved-data).

Each bookmark belongs to the item's own resume key — the episode's URL, the audio book part's stable catalogue URL, or the jukebox track's file path. A jukebox file that is moved or renamed outside freeAudio is therefore treated as a different item and does not show its old bookmarks.

## Transpose (Pitch Shift)

Transpose shifts the **pitch** of what's playing up or down without changing its **speed** — the opposite of the "chipmunk effect" you'd get from simply speeding a track up. It's useful for matching the natural range of a particular narrator, transposing music to a friendlier key, or just adjusting a recording to sit more comfortably on your ears.

Transpose is available for **podcasts**, **audio books** and **jukebox tracks** — the same "local, seekable, tempo-capable media" the playback-speed shortcuts already apply to. It is not available for live radio stations, which have no fixed pitch to shift.

- **`Shift+Win+K`** — Raises the pitch by one step.
- **`Shift+Win+J`** — Lowers the pitch by one step.

Each step is **one eighth of a whole tone** — that is, **0.25 semitones** (a whole tone is 2 semitones, so 8 steps make a whole tone, and 48 steps make an octave). The range is **−12.00 to +12.00 semitones**, i.e. one full octave up or down. NVDA announces the new value after each step, for example "**+1.25 semitones**"; returning to 0.0 announces "**Normal pitch**".

Transpose is remembered across tracks, the same way playback speed is: setting it once while a track is playing means the next tempo-capable track you play starts with the same shift, unless that track's own saved audio profile overrides it. Playing a track with no saved transpose value resets the shift back to 0.0 (Normal pitch), just like the same rule already applies to speed.

## Liked Songs

When the **Save liked songs to a text file** option is enabled, track info copied to the clipboard by pressing `Ctrl+Win+I` three times is also appended line by line to `Documents\freeAudio Recordings\likedSongs.txt`.

On stations that broadcast ICY metadata, the track title and artist are saved directly. On stations without ICY metadata, the Shazam recognition result is saved to the same file — both sources share the same list. The file is created automatically if it does not exist; each entry is appended to the end of the file and previous entries are never deleted.

## Liked Songs Tab

The **Liked Songs** tab in the station browser displays all tracks saved in `likedSongs.txt`. The list is automatically reloaded from the file each time the tab is opened. Right-click a song, or select it and press the Applications key / `Shift+F10`, to open a context menu with the same actions described below.

A **Filter** field above the list lets you narrow the displayed tracks in real time. Type any part of a song title or artist name and the list updates instantly on every keystroke. NVDA announces the number of matching results after each change. Press the `Down` arrow from the filter field to move focus directly into the list.

Selecting a track from the list enables the following actions:

- **Play on Spotify:** Tries to open the Spotify desktop app directly. If the app is not installed, falls back to the Spotify website and automatically starts playing the first result.
- **Play on YouTube (`Alt+O`):** Searches YouTube for the selected track and opens the results in the default browser.
- **Show Lyrics:** Fetches and displays the lyrics for the selected track. Lyrics are retrieved from [lrclib.net](https://lrclib.net) (free, no account required). A short "Fetching lyrics…" message is announced while the search runs in the background. If lyrics are found, they open in a read-only dialog where you can read them with NVDA and copy them to the clipboard. If no lyrics are found, NVDA announces this. The button is temporarily disabled while a fetch is in progress to prevent duplicate requests.
- **Remove (`Alt+M`):** Deletes the selected track from `likedSongs.txt` and updates the list. The `Delete` key also triggers this button when the list is focused. You can also mark several songs at once and remove them all together — see [Marking and Removing Multiple Items](#marking-and-removing-multiple-items) under Favourites.
- **Refresh (`Alt+E`):** Reloads the list from the file.

The Spotify, YouTube, Show Lyrics, and Remove buttons are only enabled when a real track is selected in the list.

### Lyrics Service

freeAudio uses [lrclib.net](https://lrclib.net) to fetch lyrics — a free, open database that requires no API key or account. The lookup process parses the track string stored in `likedSongs.txt` and tries progressively looser queries until lyrics are found:

1. Exact match using the full artist name and cleaned title (noise suffixes such as "Remastered", "Live", or year tags are stripped before searching).
2. Exact match using the full artist name and the original title (if cleaning changed it).
3. Exact match using only the first artist name and the cleaned title (for multi-artist strings such as "Artist A & Artist B").
4. Fuzzy search using the first artist name and the cleaned title.
5. Fuzzy search using the raw track string as a last resort.

When plain lyrics are available they are shown as-is. When only time-synced LRC lyrics are available, the timestamps are stripped and the plain text is shown. Instrumental tracks are reported as not found.

## Settings

The following options can be configured from NVDA Menu → Preferences → Settings → freeAudio:

| Option | Description |
|---|---|
| Track change voice | Choose whether auto-announced track changes are spoken using the NVDA synthesizer or a selected SAPI5 voice. |
| SAPI5 voice | When **Track change voice** is set to SAPI5, selects which installed SAPI5 voice is used to announce track changes. The list is populated in the background from the voices installed on the system. |
| Audio output device | Sets the audio output device for radio playback. The list includes all BASS-compatible devices on the system plus a "System default" option. Changes are applied immediately on save; if the selected device is disconnected, the add-on automatically falls back to the system default and announces the change. |
| Audio device refresh mode | Controls how freeAudio refreshes BASS output-device numbers. **Reliable** mode (default) probes devices live and tracks Bluetooth/USB changes more accurately, but can make device changes slightly slower. **Fast** mode uses the current BASS device list and is quicker, but device numbers may stay stale until BASS or NVDA is restarted. |
| Volume | Sets the add-on's starting volume (0–100). During playback, `Ctrl+Win+↑` can raise the volume up to 200, but the starting volume saved here is capped at 100. |
| Audio effects | Sets which effects (Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, and the three EQ boosts) are active when NVDA starts or a station begins playing. Multiple effects can be checked at once, matching the Effects list in the Station Browser. |
| EQ gain (Bass / Treble / Vocal) | Sets the gain level in dB for each EQ band (−15 to +15). These values apply when the corresponding EQ effect is active and are saved globally. Per-station overrides can be stored using the **Save Audio Profile** button in the Favourites tab. |
| Station switch transition | Controls the transition behaviour when switching between **live radio stations**. **Instant cut** (default) stops the previous station immediately before the new one starts. **Short crossfade (1 second)** and **Normal crossfade (2 seconds)** start the new station immediately with no gap, then gradually fade out the previous station in the background once the new stream is confirmed active. **Station tuning sound effect** stops the previous station immediately and plays a station tuner sound effect before the new one starts. Has no effect and no performance impact when set to Instant cut. Does not apply to podcasts, audio books, or jukebox tracks — resuming those always plays its own brief cassette sound effect regardless of this setting; see [Podcast Playback Details](#podcast-playback-details). |
| Resume last station on NVDA startup | When enabled, the last played station automatically restarts every time NVDA starts. |
| Auto-announce track changes (ICY metadata) | When enabled, NVDA automatically reads the new track name each time it changes on a station that broadcasts ICY metadata. The first track is also announced immediately when switching to a new station. Disabled by default. |
| Mute notifications | When enabled, NVDA does not announce station changes, playback state changes (play, pause, stop), or recording events (started, stopped, finished). Error messages, favourites feedback, music recognition results, and update notifications are not affected. Can also be toggled on the fly via an unassigned input gesture. Disabled by default. |
| Show freeAudio messages on the braille display | When enabled, freeAudio also sends its notifications directly to the braille display. This is useful for track titles, station changes, playback state and volume changes. Disabled by default. |
| Enable time-shift buffer (rewind live radio) | Turns the rewind controls (`Ctrl+Win+J`/`Ctrl+Win+K`) on or off and grows the background capture from ~45 seconds up to the **Time-shift buffer duration**. A small background capture of the currently playing station always runs, even when this is off — see the note in the **Time-Shift (Rewind Live Radio)** section above. Can also be toggled instantly with `Ctrl+Win+T`. Disabled by default — see the **Time-Shift (Rewind Live Radio)** section above for full details. It has no effect on podcasts and audio books. |
| Time-shift buffer duration | Sets the maximum length of the rewind buffer. Options range from 10 minutes up to 5 hours. Longer buffers consume more temporary disk space. |
| Save liked songs to a text file | When enabled, track info copied to the clipboard by pressing `Ctrl+Win+I` three times is also appended to `Documents\freeAudio Recordings\likedSongs.txt`. If no ICY metadata is available, the Shazam recognition result is saved to the same file. Disabled by default. |
| When Ctrl+Win+P is pressed with no active playback | Determines what happens when this shortcut is pressed and nothing is playing: start the last station or open the favourites list. |
| When Ctrl+Win+P is pressed twice | Selects what happens when the shortcut is pressed twice in quick succession: do nothing, open the favourites list, open the recording tab or open the timer tab. When "do nothing" is selected, the first press responds instantly with no delay. |
| When Ctrl+Win+P is pressed three times | Selects what happens when the shortcut is pressed three times in quick succession: do nothing, open the favourites list, open station search, open the recording tab or open the timer tab. |
| Automatically check for updates on startup | When enabled, a background update check runs each time NVDA starts; you are notified if a new version is found. When disabled, automatic checks stop but manual checks remain available. |
| Check for Updates Now | A button that checks for a new version immediately, even when automatic checks are turned off. While the check runs, the button reads "Checking...". |
| ffmpeg.exe path | Path to the ffmpeg.exe used for music recognition. If left blank, an ffmpeg.exe in the add-on folder is used automatically. |
| Recordings folder | Sets the folder where recorded files are saved. If left blank, the default location `Documents\freeAudio Recordings\` is used. A Browse button lets you select the folder interactively. Changes take effect immediately after saving. |
| Modules | A checklist of the optional parts of freeAudio: **Podcasts**, **Audio Books** and **Jukebox**. All three are enabled by default. Unchecking one removes its tab from the Station Browser and its commands from NVDA's Input Gestures dialog, without deleting anything you have saved there (subscriptions, library, Jukebox list); checking it again brings everything back. Changes apply the next time the Station Browser is opened. |
| Include network drives when searching the jukebox | When enabled, the Jukebox's **Search on devices** also scans network drives. Disabled by default, because searching a network share can take minutes, or hang if the share cannot be reached. |
| Audio book sources | A checklist selecting which audio-book sources (**GETEM**, **LibriVox**, **Project Gutenberg**) are searched and shown in the Audio Books tab. All three are enabled by default. Unchecking a source hides its books from the merged search results and library list without deleting anything you've already added from it — see [Audio Books (GETEM, LibriVox and Project Gutenberg)](#audio-books-getem-librivox-and-project-gutenberg). |
| GETEM username / GETEM password | Your [GETEM](https://getem.boun.edu.tr/) audio-book membership credentials, needed to stream or download a book's audio — see [Signing In](#signing-in). Stored encrypted on disk via the Windows Data Protection API, tied to your Windows user account; never stored as plain text. Leaving both fields empty and saving removes any stored credentials. LibriVox and Project Gutenberg require no account and have no equivalent field. |
| Recording output format | Keeps the original stream, extracts audio without changing its codec, or converts completed recordings to MP3. The default is the original stream format. |
| MP3 recording bitrate | Sets the bitrate used when the recording output format is MP3. The default is 128 kb/s. |
| Disable internet connectivity check before playing | Recommended for users who experience a delay before a station starts playing. Also useful when DNS is blocked. |
| Clean up: reset settings and delete saved data... | A button that opens a dialog for resetting freeAudio's settings and deleting the data it has saved — see [Clean Up: Reset Settings and Delete Saved Data](#clean-up-reset-settings-and-delete-saved-data). |

### Clean Up: Reset Settings and Delete Saved Data

The **Clean up: reset settings and delete saved data...** button at the bottom of the freeAudio settings page opens the **Reset settings / delete saved data** dialog. It lists what freeAudio stores in the NVDA configuration folder as check boxes. **Nothing is checked by default.** Each item shows how much space it takes, or "nothing saved":

- **Settings** — reset to their defaults. The recordings folder and the **Save liked songs to a text file** option are kept.
- **Favourite stations**
- **Station list cache** — downloaded again when needed.
- **Podcast subscriptions**
- **Audio book libraries** — GETEM, LibriVox and Project Gutenberg.
- **Saved GETEM login** — the stored user name and password.
- **Jukebox list** — your music files are not deleted.
- **Saved resume positions** — podcasts, audio books and Jukebox folders.
- **Bookmarks** — every bookmark, including its text note and voice note.
- **Sleep timers and alarms**
- **Scheduled recording plans** — the recordings themselves are not deleted.

**Select all** checks every item. **Reset / delete selected** carries out your choice; if nothing is checked, freeAudio says "Nothing is selected." **Cancel** (or `Escape`) closes the dialog without doing anything.

Before anything is changed, freeAudio lists the checked items, warns that this cannot be undone and asks you to confirm; the default answer is **No**. Afterwards a message says "Done.", or lists the items that could not be removed — usually because a file is in use. If the Station Browser is open when saved data is deleted, it is closed, and it is rebuilt from the remaining data the next time you open it.

Recordings, the recordings folder and the liked songs text file are **never** touched, and a settings reset does not make freeAudio import data from the earlier FreeRadio add-on again.

After a settings reset, the values still showing on the settings page are not saved when you press OK, so they cannot undo the reset. Restarting NVDA is recommended so that every setting takes effect.

## Mute Notifications

When **Mute notifications** is enabled in Settings, NVDA silences the following automatic announcements:

- Station name when a new station starts playing
- Playback state changes: play, pause, stop
- Obligato mode: started / stopped
- Recording events: started, stopped, finished (instant, song, every-song and scheduled recordings)
- ICY track change announcements, even when **Auto-announce track changes** is also enabled
- The notice that a station is being played in a special compatibility mode (see [Playback](#playback))

The following announcements are intentionally **not** affected: error messages, favourites feedback (added / already in list), music recognition results, and update notifications.

The setting can be toggled from NVDA Menu → Preferences → Settings → freeAudio, or instantly at any time via an unassigned input gesture (assign one from NVDA Menu → Preferences → Input Gestures → freeAudio). When toggled, NVDA announces "Notifications muted" or "Notifications unmuted" once to confirm the change.

## Auto-announce Track Changes

When the **Auto-announce track changes** option is enabled in Settings, freeAudio checks the active station's ICY metadata stream in the background approximately every 5 seconds. When the track changes, the new title is automatically read by NVDA — no keypress required.

When switching to a new station, the first track info is announced as soon as the connection is established. If you switch to a station that does not broadcast ICY metadata, the system stays silent and the previous station's track info is not repeated.

This feature is disabled by default and can be toggled from NVDA Menu → Preferences → Settings → freeAudio.

## Playback

freeAudio uses **BASS** as its sole playback backend for everything — internet radio, podcasts, audio books, and jukebox tracks. No separate installation is required; it is bundled with the add-on. freeAudio does not use VLC, PotPlayer or Windows Media Player.

BASS sends audio directly to the Windows audio stack and appears in the Windows volume mixer as an independent audio source named "pythonw.exe", separate from NVDA. This means freeAudio audio flows on a completely separate channel from NVDA speech: the radio does not cut out, mix with, or get affected by NVDA's own audio settings while NVDA is speaking. The user can adjust the radio volume independently from NVDA in the Windows Volume Mixer. Supports HTTP, HTTPS and most embedded stream formats.

Podcast episodes, audio book chapters, and jukebox tracks are played through BASS because it can open the stream as a seekable file (even while downloading), allowing precise position tracking, tiered rewind/fast-forward, playback speed, pitch transpose, and resuming. Audio mirroring, time-shift, and podcast/audio-book/jukebox seek and resume all depend on BASS and are always available.

**HLS stations that need a compatibility mode:** a few HLS (`.m3u8`) stations package their audio in a way BASS cannot read smoothly — it keeps reopening the stream, which sounds like constant stuttering. For these (currently the ABC Australia radio streams) freeAudio automatically re-wraps the same audio, without re-encoding it, in a conventional layout, using a small server that runs only on your own computer, and plays that instead. Nothing needs to be configured. The first time you play such a station after NVDA starts, NVDA announces "This station uses a special playback mode to prevent stuttering." This announcement follows the **Mute notifications** setting.

## Update Check

freeAudio automatically checks for new versions via GitHub.

**Automatic check:** Runs silently in the background 15 seconds after NVDA starts. If a new version is found, you are notified; if none is found, no message is shown.

**Manual check:** Can be triggered on demand from NVDA Tools → freeAudio → **Check for Updates…**. When started this way, the result is announced even if the version is up to date.

**When an update is found:** A dialog opens showing the version number and your installed version.

- If a directly downloadable `.nvda-addon` file is available on the GitHub release, a **Download and Install** button is shown. Once confirmed, the file is downloaded in the background, NVDA announces when the download starts, and NVDA's own installation screen opens automatically.
- If no direct download link is available, an **Open Page** button is shown and the GitHub release page opens in the default browser.

**To disable automatic checks:** Turn off the **Automatically check for updates on startup** option from NVDA Menu → Preferences → Settings → freeAudio.

## Acknowledgments & Credits

* **Original Foundation & Concepts:** Sincere thanks to **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) for the original radio add-on concepts and core favourite management structures that served as a foundational base for this project.
* **AI & LLM Tools:** Grateful acknowledgment to modern Large Language Model (LLM) tools (including Claude, ChatGPT, and Gemini) for assistance during the development, code refactoring, and feature implementation phases.
* **Directory Service:** Station directory powered by the [Radio Browser API](https://www.radio-browser.info/).
* **Community:** Sincere thanks to all NVDA community members and translators for their continuous support, feedback, and localisation contributions.

## License

GPL v2