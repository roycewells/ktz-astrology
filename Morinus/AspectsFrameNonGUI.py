import wx
import AspectsNonGUI


class AspectsFrame(wx.Frame):
	def __init__(self, parent, title, chrt, options, path):
		wx.Frame.__init__(self, parent, -1, title, wx.DefaultPosition, wx.Size(800, 800))

		aw = AspectsNonGUI.Aspects(self, chrt, options, parent,path)
		
		self.SetMinSize((200,200))