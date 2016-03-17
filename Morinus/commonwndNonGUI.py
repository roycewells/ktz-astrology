from Morinus import mtexts

import os
import wx

class CommonWnd(wx.ScrolledWindow):
	SCROLL_RATE = 20
	BORDER = 20

	def __init__(self, parent, chrt, options, id = -1, size = wx.DefaultSize):
		wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=size, style=wx.SUNKEN_BORDER)

		self.parent = parent
		self.chart = chrt
		self.options = options
		self.bw = self.options.bw

		self.SetBackgroundColour(self.options.clrbackground)


		if (self.bw):
			mbw.Check()


	def onPopupMenu(self, event):
		self.PopupMenu(self.pmenu, event.GetPosition())


	def onSaveAsBitmap(self, event):
		name = "aspects"
		fpath = name+".png"
		self.buffer.SaveFile(fpath, wx.BITMAP_TYPE_BMP)		


	def onBlackAndWhite(self, event):
		if (self.bw != event.IsChecked()):
			self.bw = event.IsChecked()
			self.drawBkg()
			self.Refresh()


	def OnPaint(self, event):
		dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)




