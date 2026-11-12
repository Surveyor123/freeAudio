# -*- coding: utf-8 -*-
"""Keyboard-accessible ten-band graphic equalizer page."""
import wx
import config
import ui
import addonHandler
from .graphicEqConfig import GRAPHIC_EQ_KEYS, get_graphic_eq_gains
addonHandler.initTranslation()

FREQUENCIES = (62, 125, 250, 500, 1000, 2000, 4000, 8000, 12000, 16000)


class GainAccessible(wx.Accessible):

	def GetValue(self, childId):
		if childId == 0:
			# Translators: Value spoken for an equalizer band slider. %+d is the gain in decibels with an explicit sign, e.g. "+5 dB" or "-3 dB".
			return wx.ACC_OK, _("%+d dB") % self.GetWindow().GetValue()
		return wx.ACC_NOT_IMPLEMENTED, ""


class EqualizerPanel(wx.Panel):

	def __init__(self, parent, player):
		super().__init__(parent)
		self.player = player
		section = config.conf["freeAudio"]
		sizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: Label of the checkbox that turns the ten-band graphic equalizer on or off.
		self.toggle = wx.CheckBox(self, label=_("Equalizer On/Off"))
		self.toggle.SetValue(section["graphic_eq_enabled"])
		self.toggle.Bind(wx.EVT_CHECKBOX, self.on_toggle)
		sizer.Add(self.toggle, 0, wx.ALL, 6)
		self.sliders = []
		for i, freq in enumerate(FREQUENCIES):
			row = wx.BoxSizer(wx.HORIZONTAL)
			# Translators: Label (and accessible name) of one equalizer band slider. %g is the band's centre frequency in hertz, e.g. "62 Hz" or "12000 Hz".
			label = _("%g Hz") % freq
			row.Add(wx.StaticText(self, label=label), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 8)
			slider = wx.Slider(self, value=section.get(GRAPHIC_EQ_KEYS[i], 0), minValue=-20, maxValue=20, style=wx.SL_HORIZONTAL)
			slider.SetName(label)
			slider.SetLineSize(1)
			slider.SetPageSize(1)
			slider.SetAccessible(GainAccessible(slider))
			slider.Bind(wx.EVT_SLIDER, lambda event, band=i: self.on_gain(event, band))
			self.sliders.append(slider)
			row.Add(slider, 1, wx.EXPAND)
			sizer.Add(row, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 6)
		buttons = wx.BoxSizer(wx.HORIZONTAL)
		for label, handler in (
			# Translators: Label of the equalizer button that sets every band back to 0 dB.
			(_("Reset"), self.on_reset),
			# Translators: Label of the equalizer button that saves the equalizer settings to the configuration.
			(_("Save"), self.on_save),
		):
			button = wx.Button(self, label=label)
			button.Bind(wx.EVT_BUTTON, handler)
			buttons.Add(button, 0, wx.ALL, 6)
		sizer.Add(buttons)
		self.SetSizer(sizer)

	def apply(self):
		section = config.conf["freeAudio"]
		self.player.set_graphic_eq(section["graphic_eq_enabled"], get_graphic_eq_gains(section))

	def on_toggle(self, event):
		enabled = self.toggle.GetValue()
		config.conf["freeAudio"]["graphic_eq_enabled"] = enabled
		self.apply()
		ui.message(
			# Translators: Spoken when the equalizer is turned on with the checkbox.
			_("Equalizer enabled") if enabled else
			# Translators: Spoken when the equalizer is turned off with the checkbox.
			_("Equalizer disabled")
		)

	def on_gain(self, event, band):
		value = self.sliders[band].GetValue()
		config.conf["freeAudio"][GRAPHIC_EQ_KEYS[band]] = value
		self.apply()
		# Explicit unit announcement also covers NVDA versions that use the
		# native slider value rather than the custom MSAA value.
		# Translators: Spoken after an equalizer slider is changed. %(frequency)g is the band's centre frequency in hertz and %(gain)+d is the new gain in decibels with an explicit sign, e.g. "1000 Hz, +4 dB". Keep both placeholders.
		ui.message(_("%(frequency)g Hz, %(gain)+d dB") % {"frequency": FREQUENCIES[band], "gain": value})

	def on_reset(self, event):
		for i, slider in enumerate(self.sliders):
			slider.SetValue(0)
			config.conf["freeAudio"][GRAPHIC_EQ_KEYS[i]] = 0
		self.apply()
		# Translators: Spoken after the Reset button sets all equalizer bands back to 0 dB.
		ui.message(_("Equalizer reset"))

	def on_save(self, event):
		try:
			config.conf.save()
		except Exception:
			# Translators: Spoken when saving the equalizer settings to the configuration fails.
			ui.message(_("Could not save Equalizer settings"))
		else:
			# Translators: Spoken after the equalizer settings were saved to the configuration.
			ui.message(_("Equalizer settings saved"))
