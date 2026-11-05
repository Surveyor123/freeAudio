# -*- coding: utf-8 -*-
"""Keyboard-accessible nine-band graphic equalizer page."""
import wx
import config
import ui
import addonHandler
addonHandler.initTranslation()

FREQUENCIES = (62, 125, 250, 500, 1000, 2000, 4000, 8000.2, 16000)


class GainAccessible(wx.Accessible):

	def GetValue(self, childId):
		if childId == 0:
			return wx.ACC_OK, _("%+d dB") % self.GetWindow().GetValue()
		return wx.ACC_NOT_IMPLEMENTED, ""


class EqualizerPanel(wx.Panel):

	def __init__(self, parent, player):
		super().__init__(parent)
		self.player = player
		section = config.conf["freeAudio"]
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.toggle = wx.CheckBox(self, label=_("Equalizer On/Off"))
		self.toggle.SetValue(section["graphic_eq_enabled"])
		self.toggle.Bind(wx.EVT_CHECKBOX, self.on_toggle)
		sizer.Add(self.toggle, 0, wx.ALL, 6)
		self.sliders = []
		for i, freq in enumerate(FREQUENCIES):
			row = wx.BoxSizer(wx.HORIZONTAL)
			label = _("%g Hz") % freq
			row.Add(wx.StaticText(self, label=label), 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 8)
			slider = wx.Slider(self, value=section["graphic_eq_%d" % i], minValue=-20, maxValue=20, style=wx.SL_HORIZONTAL)
			slider.SetName(label)
			slider.SetLineSize(1)
			slider.SetPageSize(1)
			slider.SetAccessible(GainAccessible(slider))
			slider.Bind(wx.EVT_SLIDER, lambda event, band=i: self.on_gain(event, band))
			self.sliders.append(slider)
			row.Add(slider, 1, wx.EXPAND)
			sizer.Add(row, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 6)
		buttons = wx.BoxSizer(wx.HORIZONTAL)
		for label, handler in ((_("Reset"), self.on_reset), (_("Save"), self.on_save)):
			button = wx.Button(self, label=label)
			button.Bind(wx.EVT_BUTTON, handler)
			buttons.Add(button, 0, wx.ALL, 6)
		sizer.Add(buttons)
		self.SetSizer(sizer)

	def apply(self):
		section = config.conf["freeAudio"]
		self.player.set_graphic_eq(section["graphic_eq_enabled"], [section["graphic_eq_%d" % i] for i in range(9)])

	def on_toggle(self, event):
		enabled = self.toggle.GetValue()
		config.conf["freeAudio"]["graphic_eq_enabled"] = enabled
		self.apply()
		ui.message(_("Equalizer enabled") if enabled else _("Equalizer disabled"))

	def on_gain(self, event, band):
		value = self.sliders[band].GetValue()
		config.conf["freeAudio"]["graphic_eq_%d" % band] = value
		self.apply()
		# Explicit unit announcement also covers NVDA versions that use the
		# native slider value rather than the custom MSAA value.
		ui.message(_("%(frequency)g Hz, %(gain)+d dB") % {"frequency": FREQUENCIES[band], "gain": value})

	def on_reset(self, event):
		for i, slider in enumerate(self.sliders):
			slider.SetValue(0)
			config.conf["freeAudio"]["graphic_eq_%d" % i] = 0
		self.apply()
		ui.message(_("Equalizer reset"))

	def on_save(self, event):
		try:
			config.conf.save()
		except Exception:
			ui.message(_("Could not save Equalizer settings"))
		else:
			ui.message(_("Equalizer settings saved"))
