# -*- coding: utf-8 -*-
# freeAudio - Volume, EQ/bass-treble-vocal boost, crossfade, playback rate
#
# Extracted from GlobalPlugin in __init__.py. Mixed into GlobalPlugin, so
# `self` here is a GlobalPlugin instance - self._player and self._dialog
# (defined elsewhere on GlobalPlugin) are used as normal instance
# attributes via the class's MRO, no import needed for those.
#
# NOTE: every script here with a default gesture= must also be listed in
# GlobalPlugin's __gestures dict in __init__.py (see the __gestures
# comment there for why). Most scripts in this file have no default
# gesture, but volumeUp/volumeDown/playbackRateUp/playbackRateDown do.

import config
import ui
from scriptHandler import script

import addonHandler
addonHandler.initTranslation()
_tr = globals()["_"]
_ = _tr
del _tr

from . import _notify
from .graphicEqConfig import get_graphic_eq_gains


class AudioFxMixin:
	"""Volume, playback-rate, EQ band boosts, and crossfade/station-
	transition controls, plus the dialog-sync helpers they share."""

	@script(
		# Translators: Name of an NVDA command; raises freeAudio's playback volume by 5 (of 200 max, capped at 100 when saved).
		description=_("Increase freeAudio volume by 5"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		gesture="kb:control+windows+upArrow",
	)
	def script_volumeUp(self, gesture):
		vol = min(200, self._player.get_volume() + 5)
		self._player.set_volume(vol)
		config.conf["freeAudio"]["volume"] = min(100, vol)
		# Translators: Spoken after volume is changed with the volume-up/down commands; %d is the new volume level.
		_notify(_("Volume %d") % vol)
		self._sync_dialog_volume(vol)

	@script(
		# Translators: Name of an NVDA command; lowers freeAudio's playback volume by 5.
		description=_("Decrease freeAudio volume by 5"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		gesture="kb:control+windows+downArrow",
	)
	def script_volumeDown(self, gesture):
		vol = max(0, self._player.get_volume() - 5)
		self._player.set_volume(vol)
		config.conf["freeAudio"]["volume"] = min(100, vol)
		# Translators: Spoken after volume is changed; %d is the new volume level.
		_notify(_("Volume %d") % vol)
		self._sync_dialog_volume(vol)

	@script(
		# Translators: Name of an NVDA command; speeds up playback rate, podcasts/audiobooks/GETEM chapters only.
		description=_("Increase podcast, audio book and jukebox playback speed"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		gesture="kb:control+windows+shift+k",
	)
	def script_playbackRateUp(self, gesture):
		self._report_playback_rate(*self._player.increase_playback_rate())

	@script(
		# Translators: Name of an NVDA command; slows down playback rate, podcasts/audiobooks/GETEM chapters only.
		description=_("Decrease podcast, audio book and jukebox playback speed"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		gesture="kb:control+windows+shift+j",
	)
	def script_playbackRateDown(self, gesture):
		self._report_playback_rate(*self._player.decrease_playback_rate())

	def _report_playback_rate(self, applied, rate, reason):
		if applied:
			if abs(rate - 1.0) < 0.05:
				# Translators: Spoken when the playback-rate command returns the rate to normal (1.0x).
				_notify(_("Rate normal"))
			else:
				# Translators: Spoken after changing playback rate; %.1f is the new rate, e.g. '1.5' meaning 1.5x speed.
				_notify(_("Rate %.1f") % rate)
			return
		if reason == "bass_fx_unavailable":
			# Translators: Spoken when playback-rate change fails because the optional bass_fx library used for time-stretching isn't installed.
			_notify(_("Playback speed control needs the bass_fx add-on library — see the freeAudio docs."))
		elif reason in ("not_tempo_stream", "wrong_backend"):
			# Translators: Spoken when the user tries to change playback rate while playing a live radio station rather than a podcast/audiobook.
			_notify(_("Playback speed control is only available for podcasts."))
		else:
			# Translators: Generic fallback spoken when the playback-rate change fails for an unrecognised reason.
			_notify(_("Could not change playback speed."))

	def _sync_dialog_volume(self, vol):
		"""Update the volume SpinCtrl in the browser dialog if it is open."""
		if self._dialog and self._dialog.IsShown():
			try:
				self._dialog._vol_spin.SetValue(vol)
			except Exception:
				pass

	def _sync_dialog_audio(self, vol, fx_str, eq_gains=None):
		"""Update both the volume SpinCtrl and effects CheckListBox in the browser dialog."""
		if self._dialog and self._dialog.IsShown():
			try:
				self._dialog._vol_spin.SetValue(vol)
			except Exception:
				pass
			try:
				active = {x.strip() for x in fx_str.split(",") if x.strip() != "none"}
				for i, key in enumerate(self._dialog._fx_keys):
					self._dialog._fx_choice.Check(i, key in active)
			except Exception:
				pass
			# Sync EQ gain spin controls
			if eq_gains and hasattr(self._dialog, "_eq_spins"):
				for band, gain_db in eq_gains.items():
					try:
						self._dialog._eq_spins[band].SetValue(int(gain_db))
					except Exception:
						pass
			# Update EQ row visibility
			try:
				self._dialog._update_eq_row_visibility(list(active))
			except Exception:
				pass

	@script(
		# Translators: Name of an NVDA command; toggles a low-frequency EQ boost on/off.
		description=_("Toggle bass boost"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		# No gesture assigned by default; bind one via NVDA's Input Gestures dialog.
	)
	def script_toggleBassBoost(self, gesture):
		# Translators: Short label used in the 'X enabled/disabled' announcement (see _toggle_eq_band) when toggling the bass-boost EQ band.
		self._toggle_eq_band("eq_bass", _("EQ: Bass Boost"))

	@script(
		# Translators: Name of an NVDA command; toggles a high-frequency EQ boost on/off.
		description=_("Toggle treble boost"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		# No gesture assigned by default; bind one via NVDA's Input Gestures dialog.
	)
	def script_toggleTrebleBoost(self, gesture):
		# Translators: Short label used in the 'X enabled/disabled' announcement when toggling the treble-boost EQ band.
		self._toggle_eq_band("eq_treble", _("EQ: Treble Boost"))

	@script(
		# Translators: Name of an NVDA command; toggles a mid-range EQ boost tuned for vocal clarity on/off.
		description=_("Toggle vocal boost"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		# No gesture assigned by default; bind one via NVDA's Input Gestures dialog.
	)
	def script_toggleVocalBoost(self, gesture):
		# Translators: Short label used in the 'X enabled/disabled' announcement when toggling the vocal-boost EQ band.
		self._toggle_eq_band("eq_vocal", _("EQ: Vocal Boost"))

	def _toggle_eq_band(self, band, label):
		"""Toggle an EQ band on/off.

		The BASS engine only applies a ParamEQ gain if the corresponding
		effect name (e.g. "eq_bass") is part of the active FX list, so
		toggling must add/remove that name from "audio_fx" via set_fx,
		in addition to (re)applying the saved gain via set_eq_gain.
		"""
		fx_str = config.conf["freeAudio"].get("audio_fx", "none")
		active = [f.strip() for f in fx_str.split(",") if f.strip() and f.strip() != "none"]

		gain_key = "eq_gain_" + band
		_eq_defaults = {"eq_bass": 9, "eq_treble": 9, "eq_vocal": 6}

		if band in active:
			# Currently on: remove from the active FX list.
			active.remove(band)
			turning_on = False
		else:
			# Currently off: add to the active FX list.
			active.append(band)
			turning_on = True
			# Ensure a sensible (non-zero) gain is set.
			if config.conf["freeAudio"].get(gain_key, 0) == 0:
				config.conf["freeAudio"][gain_key] = _eq_defaults.get(band, 6)

		new_fx_str = ",".join(active) if active else "none"
		config.conf["freeAudio"]["audio_fx"] = new_fx_str
		gain_db = config.conf["freeAudio"].get(gain_key, _eq_defaults.get(band, 6))

		if self._player is not None:
			try:
				self._player.set_fx(new_fx_str)
				self._player.set_eq_gain(band, gain_db)
			except Exception:
				pass

		# Keep the settings panel's effects list and EQ spin controls in sync.
		if self._dialog is not None:
			try:
				if hasattr(self._dialog, "_fx_choice") and hasattr(self._dialog, "_fx_keys"):
					if band in self._dialog._fx_keys:
						idx = self._dialog._fx_keys.index(band)
						self._dialog._fx_choice.Check(idx, turning_on)
						if hasattr(self._dialog, "_update_eq_spins_visibility"):
							self._dialog._update_eq_spins_visibility()
				if hasattr(self._dialog, "_eq_spins_settings"):
					spin = self._dialog._eq_spins_settings.get(band)
					if spin is not None:
						spin.SetValue(gain_db)
			except Exception:
				pass

		# Keep the station browser dialog's effects list and EQ spin controls in sync.
		self._sync_dialog_audio(
			self._player.get_volume() if self._player is not None else 0,
			new_fx_str,
			eq_gains={band: gain_db},
		)

		# Translators: Announcement after toggling an EQ band; %(effect)s is one of the 'EQ: ... Boost' labels above, %(state)s is 'enabled'/'disabled' below.
		ui.message(_("%(effect)s %(state)s") % {
			"effect": label,
			"state": (
				# Translators: EQ band state word spoken after the EQ band name when the band is turned on, e.g. "EQ: Bass Boost enabled".
				_("enabled") if turning_on else
				# Translators: EQ band state word spoken after the EQ band name when the band is turned off, e.g. "EQ: Bass Boost disabled".
				_("disabled")
			),
		})

	@script(
		# Translators: Name of an NVDA command; cycles the sound effect played when switching stations (crossfade/instant cut/tuning effect).
		description=_("Toggle station switch transition (crossfade)"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
		# No gesture assigned by default; bind one via NVDA's Input Gestures dialog.
	)
	def script_toggleStationTransition(self, gesture):
		_cf_order = ["off", "short", "normal", "tuning"]
		_cf_labels = {
			# Translators: One of the station-transition modes cycled by the crossfade command: plays no transition sound, cuts instantly.
			"off":    _("Instant cut (no crossfade)"),
			# Translators: One of the station-transition modes: a brief 1-second audio crossfade between the old and new station.
			"short":  _("Short crossfade (1 second)"),
			# Translators: One of the station-transition modes: a longer 2-second audio crossfade between the old and new station.
			"normal": _("Normal crossfade (2 seconds)"),
			# Translators: One of the station-transition modes: plays a radio-tuning sound effect instead of a crossfade.
			"tuning": _("Station tuning sound effect"),
		}
		_cf_map = {"off": 0.0, "short": 1.0, "normal": 2.0, "tuning": 0.0}

		current = config.conf["freeAudio"].get("crossfade", "off")
		try:
			idx = _cf_order.index(current)
		except ValueError:
			idx = 0
		new_value = _cf_order[(idx + 1) % len(_cf_order)]

		config.conf["freeAudio"]["crossfade"] = new_value
		if self._player is not None:
			try:
				self._player.set_tuning_effect_enabled(new_value == "tuning")
				self._player.set_crossfade_duration(_cf_map.get(new_value, 0.0))
			except Exception:
				pass

		# Keep the settings panel's choice control in sync if it's open.
		if self._dialog is not None and hasattr(self._dialog, "_crossfade_choice"):
			try:
				self._dialog._crossfade_choice.SetSelection(_cf_order.index(new_value))
			except Exception:
				pass

		ui.message(_cf_labels.get(new_value, new_value))


	@script(
		# Translators: Name of an NVDA command; toggles the "Weird" audio effect on/off.
		description=_("Toggle Weird"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
	)
	def script_toggleWeird(self, gesture):
		section = config.conf["freeAudio"]
		active = [x.strip() for x in self._player.get_fx().split(",") if x.strip() and x.strip() != "none"]
		enabled = "weird" not in active
		if enabled:
			active.append("weird")
		else:
			active.remove("weird")
		fx = ",".join(active) or "none"
		section["audio_fx"] = fx
		self._player.set_fx(fx)
		self._sync_dialog_audio(self._player.get_volume(), fx)
		ui.message(
			# Translators: Spoken when the "Weird" audio effect is turned on with its command.
			_("Weird enabled") if enabled else
			# Translators: Spoken when the "Weird" audio effect is turned off with its command.
			_("Weird disabled")
		)

	@script(
		# Translators: Name of an NVDA command; turns the ten-band graphic equalizer on/off.
		description=_("Toggle Equalizer"),
		# Translators: Name of the NVDA Input Gestures category that groups all freeAudio commands; normally the add-on name.
		category=_("freeAudio"),
	)
	def script_toggleGraphicEqualizer(self, gesture):
		section = config.conf["freeAudio"]
		enabled = not section["graphic_eq_enabled"]
		section["graphic_eq_enabled"] = enabled
		self._player.set_graphic_eq(enabled, get_graphic_eq_gains(section))
		if self._dialog and hasattr(self._dialog, "_graphic_eq_toggle"):
			self._dialog._graphic_eq_toggle.SetValue(enabled)
		ui.message(
			# Translators: Spoken when the ten-band graphic equalizer is turned on with its command.
			_("Equalizer enabled") if enabled else
			# Translators: Spoken when the ten-band graphic equalizer is turned off with its command.
			_("Equalizer disabled")
		)
