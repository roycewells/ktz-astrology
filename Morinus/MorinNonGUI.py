from Morinus import graphchart
from Morinus import common

import wx

class Morin(wx.Frame):

	def __init__(self, parent, id, title, opts, chart,fpath):
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(800, 800))
		self.horoscope = chart
		self.options = opts
		common.common = common.Common()
		common.common.update(self.options)
		self.fpath=fpath
		self.drawBkg()
		self.saveAsBitmap()
		#self.Close()

	def drawBkg(self):
		wx.EmptyBitmap(800,800)
		gchart = None
		gchart = graphchart.GraphChart(self.horoscope, self.GetClientSize(), self.options, self.options.bw)

		if gchart != None:
			self.buffer = gchart.drawChart()

	def saveAsBitmap(self):	
		self.fpath+="chart.png"
		self.buffer.SaveFile(self.fpath, wx.BITMAP_TYPE_BMP)	
	