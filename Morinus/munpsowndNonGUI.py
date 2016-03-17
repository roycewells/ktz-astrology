from Morinus import chart
from Morinus import houses
from Morinus import astrology
from Morinus import planets
from Morinus import common
from Morinus import commonwnd
from Morinus import options
from Morinus import util

import os 
# import NonGUInput

class MunPos():
	def __init__(self, chrt, options,percent):
		self.percent=percent
		self.chart = chrt
		self.chart.setHouseSystem()
		self.options=options
		common.common = common.Common()
		common.common.update(self.options)
		self.signs = common.common.Signs1
		self.houses = self.chart.get_houses
		print "made it"
		self.COLUMN_NUM = 1

		ii = 0
		for i in range(len(common.common.Planets)-1):
			if self.options.intables and ((i == astrology.SE_URANUS and not self.options.transcendental[chart.Chart.TRANSURANUS]) or (i == astrology.SE_NEPTUNE and not self.options.transcendental[chart.Chart.TRANSNEPTUNE]) or (i == astrology.SE_PLUTO and not self.options.transcendental[chart.Chart.TRANSPLUTO]) or (i == astrology.SE_MEAN_NODE and not self.options.shownodes)):
				continue
			self.calculate_house_percent(i)
			ii += 1


	def calculate_house_percent(self,idx):
		for i in range(self.COLUMN_NUM+1+1):#+1 is the leftmost column
			if i == 1:
				txt = common.common.Planets[idx]
			elif i != 0:
				ret, serr = astrology.swe_house_pos(self.chart.houses.ascmc[1], self.chart.place.lat, self.chart.obl[0], ord(self.chart.houses.hsys), self.chart.planets.planets[idx].data[planets.Planet.LONG], self.chart.planets.planets[idx].data[planets.Planet.LAT])
#				ret = int(ret*100.0)/100.0
				txt = str(ret)
				i = int(ret)
				self.percent.append(i)
				#print i

# horoscope = NonGUInput.test()
# options = options.Options()
# MunPos(horoscope,options)