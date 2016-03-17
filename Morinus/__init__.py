# -*- coding: utf-8 -*-
import sys

from Morinus import chart, options
import positionswndNoGUI
import json
import ImageSaver

#zodiacs:
# ARIES = 0
# TAURUS = 1
# GEMINI = 2
# CANCER = 3
# LEO = 4
# VIRGO = 5
# LIBRA = 6
# SCORPIO = 7
# SAGITTARIUS = 8
# CAPRICORNUS = 9
# AQUARIUS = 10
# PISCES = 11

#planets:etc

#A SUN
#B MOON
#C MERCURY
#D VENUS
#E MARS
#F JUPITER
#G SATERN
#H URANUS
#I NEPTUNE
#J PLUTO
#K 
#L



#these are symbols in planatary aspects

#S - trianlge
#R - square
#P - astrics
#W - the 0-0 looking one(its slanted)



# Morinus
# gen chart
# name gilad
# male True
# time <chart.Time instance at 0x111d8e560>
# htype 0
# notes 
# options <options.Options instance at 0x111d76518>
# time.year: 1995
# time.month: 2
# day 9
# hour: 22
# minute 30
# second 0
# bc False
# cal 0
# zt 0
# plus False
# zh 5
# zm 0
# time.daylightsaving False
# place.deglon 72
# place.minlon 47
# place.seclon 0
# place.east False
# place.deglat 41
# place.minlat 47
# place.seclat 0
# place.north True
# place.altitude 100
# <houses.Houses instance at 0x111d8e5f0>
# 2015-04-08 19:13:15.003 Python[78409:38941205] Communications error: <OS_xpc_error: <error: 0x7fff75eecb60> { count = 1, contents =
# 	"XPCErrorDescription" => <string: 0x7fff75eecfa8> { length = 22, contents = "Connection interrupted" }
# }>

def create_chart(year, month, day, hour, minutes, place_name, lat, lon, name,altitude=0,bc=False,cal=0,zt=0,zm=0):

	opts = options.Options()

	from LatLon import LatLon
	loc = LatLon(lat, lon)
	(deglon, minlon, seclon, east) = loc.get_lon()
	(deglat, minlat, seclat, north) = loc.get_lat()

	from datetime import datetime, tzinfo

	def unix_time(dt):
		epoch = datetime.utcfromtimestamp(0)
		delta = dt - epoch
		return int(delta.total_seconds())

	microsecond = 0
	seconds = 0
	timestamp = unix_time(datetime(year, month, day, hour, minutes, seconds, microsecond))
	
	import requests
	r = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location=' + str(lat) + ',' + str(lon) + '&timestamp=' + str(timestamp) + '&key=AIzaSyAZdlmF3MQHJpQBBZxbzcC1HOPSARHeLV0')
	offset = int(r.json()['rawOffset'])
	daylightsaving = True if int(r.json()['dstOffset']) > 0 else False
	timezone = offset/3600
	plus = True if timezone > 0 else False # whether +/- GMT
	zh = abs(timezone)	
	
	place = chart.Place(place_name,deglon,minlon,seclon,east,deglat,minlat,seclat,north,altitude)
	time = chart.Time(year,month,day,hour,minutes,seconds,bc,cal,zt,plus,zh,zm,daylightsaving,place)
	return chart.Chart(name,True,time,place,0,"",opts)	

def save_chart(chrt,path=""):
	ImageSaver.Chart(chrt,path)
	
def save_planetary_aspects(chrt,path=""):
	ImageSaver.Chart(chrt,path,True)

def get_planetary_aspects(chart):
		t={}
		chart.get_aspmatrix_data(t,chart)
		# print json.dumps(t, sort_keys=True, indent=4, ensure_ascii=False)
		return json.dumps(t, sort_keys=True, indent=4, ensure_ascii=False)
#lower case a stands for (asC) and lower case m is mc
def get_table(chart):
	field_names = ['houses','zodiac','lat','lon']
	t = {}

	table = positionswndNoGUI.Table(chart)
	lat,lon,plan,zo,asc,houses = table.get_data()
	
	for i in range(len(lat)/2):
		if(i<2):
			t[asc[i]] = {
				field_names[0] : None,
				field_names[1] : zo[i],
				field_names[2] : lat[i],
				field_names[3] : lon[i]
			}

			# print asc[i]
		else:
			t[plan[i-2]] = {
				field_names[0] : houses[i-2],
				field_names[1] : zo[i],
				field_names[2] : lat[i],
				field_names[3] : lon[i]
			}
			# print plan[i-2], " ",percent[i-2]
	
		# print " ",lon[i]," ",lat[i]," ",zo[i]
		# print "\n"
		
	# print json.dumps(t, sort_keys=True, indent=4, ensure_ascii=False)
	return json.dumps(t, sort_keys=True, indent=4, ensure_ascii=False)
	
