from Morinus import options
from Morinus import astrology
from Morinus import chart
from Morinus import houses
from Morinus import planets
from Morinus import primdirs
from Morinus import common
from Morinus import util
from Morinus import mtexts


import munpsowndNonGUI


class Table():
	def __init__(self,chart):
		self.speculums = [[True, True, True, True, False, False, False, False, False, False, False, False, False, False], [True, True, True, True, False, False, False, False, False, False, False, False]]
		self.speculum = 0
		common.common = common.Common()
		common.common.addPlanets()
		self.signs = common.common.Signs1
		self.chart = chart
		self.deg_symbol = u'\u00b0'

		self.asc=[]
		self.lat=[]
		self.lon=[]
		self.plan=[]#represented by letters
		self.zo=[] #represented by numbers

		self.house_percent=[]

		self.generate_table(common)


	def generate_table(self,common):
		#AscMC
		txts = ('0', '1')
		lons = [self.chart.houses.ascmc2[houses.Houses.ASC][houses.Houses.LON], self.chart.houses.ascmc2[houses.Houses.MC][houses.Houses.LON]]

		data = ((lons[0], self.chart.houses.ascmc2[houses.Houses.ASC][houses.Houses.LAT], self.chart.houses.ascmc2[houses.Houses.ASC][houses.Houses.RA], self.chart.houses.ascmc2[houses.Houses.ASC][houses.Houses.DECL]), (lons[1], self.chart.houses.ascmc2[houses.Houses.MC][houses.Houses.LAT], self.chart.houses.ascmc2[houses.Houses.MC][houses.Houses.RA], self.chart.houses.ascmc2[houses.Houses.MC][houses.Houses.DECL]))

		for i in range(len(txts)):
			self.asc_mc(txts[i], data[i], True)


		#second chart	
		lons = []
		num = len(common.common.Planets)-1
		realnum = 0
		for i in range(num):
			lons.append(self.chart.planets.planets[i].data[planets.Planet.LONG])
			realnum += 1

		j = 0
		for i in range(num):
			if self.speculum == 0:
				self.table_with_planets(common.common.Planets[i], self.chart.planets.planets[i].speculums[self.speculum], lons[j], i, self.chart.planets.planets[i].data[planets.Planet.SPLON])
			j += 1

		munpsowndNonGUI.MunPos(self.chart,options.Options(),self.house_percent)

	def asc_mc(self,txt, data, AscMC=False):
		#draw symbols
		self.asc.append(txt)

		for i in range(planets.Planet.DECL+1):

			d,m,s = util.decToDeg(data[i])

			if i == planets.Planet.LONG:
				sign = d/chart.Chart.SIGN_DEG
				pos = d%chart.Chart.SIGN_DEG
				txt = (str(pos)).rjust(2)+self.deg_symbol+(str(m)).zfill(2)+"'"+(str(s)).zfill(2)+'"'
				#print sign, txt,"\n"
				self.zo.append(sign)
				self.lon.append(txt)

			elif i == planets.Planet.LAT:
				sign = ''
				if data[i] < 0.0:
					sign = '-'
				txt = sign+(str(d)).rjust(2)+self.deg_symbol+(str(m)).zfill(2)+"'"+(str(s)).zfill(2)+'"'
				#print txt,"\n"
				self.lat.append(txt)


	#data for latitude and longitude 2nd box where planets start
	def table_with_planets(self, txt, data, ayanlon, idxpl=0, speed=0.0):
		#print txt #name of planet
		self.plan.append(txt)
		#data
		j = 0
		for i in range(len(self.speculums[self.speculum])):

			d,m,s = util.decToDeg(data[i])

			if i == planets.Planet.LONG:
				sign = d/chart.Chart.SIGN_DEG
				pos = d%chart.Chart.SIGN_DEG
				txt = (str(pos)).rjust(2)+self.deg_symbol+(str(m)).zfill(2)+"'"+(str(s)).zfill(2)+'"'
				self.lon.append(txt)
				self.zo.append(sign)
				#print txt,sign #represents the longitude numbers in second colmn
				#print "\n"

			#gives me the latitude numbers in 2nd box	
			elif i == planets.Planet.LAT or i == planets.Planet.ADLAT:
				sign = ''
				if data[i] < 0.0:
					sign = '-'
				if i == planets.Planet.LAT and idxpl == 0:#Sun's latitude is always zero
					d, m, s = 0, 0, 0
					sign = ''
				txt = sign+(str(d)).rjust(2)+self.deg_symbol+(str(m)).zfill(2)+"'"+(str(s)).zfill(2)+'"'			
				self.lat.append(txt)
				#print txt 
				#print "\n"
			j += 1


	# def print_data(self,lat,lon,plan,zo,asc,house_percent):
	# 	for i in range(len(lat)/2):
	# 		if(i<2):
	# 			print asc[i]
	# 		else:
	# 			print plan[i-2], " ",house_percent[i-2]
	# 		print " ",lon[i]," ",lat[i]," ",zo[i]
	# 		print "\n"

	def get_data(self):
		return self.lat,self.lon,self.plan,self.zo,self.asc,self.house_percent