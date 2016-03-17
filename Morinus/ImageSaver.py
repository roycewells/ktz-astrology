from Morinus import mtexts
from Morinus import options

import MorinNonGUI
import NonGUInput
import AspectsFrameNonGUI
import os
import sys
import wx

class Chart(wx.App):

	def __init__(self,chrt,path,aspects=False):
		self.aspects=aspects
		self.horoscope = chrt
		self.path = path
		self.title = "Morin"
		self.options = options.Options()
		mtexts.setLang(self.options.langid)
		wx.App.__init__(self) 

	def OnInit(self):
		try:
			os.chdir("Morinus/Morinus")
		except:
			print "ERROR with file path"

		wx.SetDefaultPyEncoding('utf-8')

		if(self.aspects):
			AspectsFrameNonGUI.AspectsFrame( None,self.title, self.horoscope, self.options,self.path)
		else:
			MorinNonGUI.Morin(None, -1, mtexts.txts['Morinus'], self.options,self.horoscope,self.path)

		return True

# app = Chart( NonGUInput.test(),"",False)
