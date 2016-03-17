from Morinus import chart
from Morinus import options

import positionswndNoGUI

# def test():
# 	opts = options.Options()
# 	place = chart.Place("place",55,55,0,True,55,55,0,False,100)
# 	time = chart.Time(1996,7,14,8,8,8,True,0,0,False,8, 8,False,place)
# 	horoscope = chart.Chart("name",True,time,place,0,"",opts)

# 	table = positionswndNoGUI.Table(horoscope)
# 	lat,lon,plan,zo,asc,percent = table.get_data()
# 	table.print_data(lat,lon,plan,zo,asc,percent)

# 	return horoscope


def create_horoscope_user_input():
	opts = options.Options()
	#name and gender
	name = raw_input("Full Name")
	gender = raw_input("Gender")#boolean
	htype = int(raw_input("Type: Radix, Solar, Lunar, revolution, transit, horary, profection,pdinchar")) # 0-7

	#place input
	place = raw_input("Name of place")
	long_deg = int(raw_input("Longitude degree"))
	long_min = int(raw_input("Longitude  minute"))
	long_direciton = raw_input("E or W?")#true or false
	lat_deg = int(raw_input("Latitude  degree"))
	lat_min = int(raw_input("Latitude  minute"))
	lat_direciton = raw_input("N or S?") #true or false
	alt = int(raw_input("altitude"))
	#alt = int(raw_input("altitude"))#optional alt

	place = chart.Place(place,long_deg,long_min,0,True,lat_deg,lat_min,0,False,alt)

	#time
	year = int(raw_input("Year?")) # 1995
	month = int(raw_input("Month?")) # 2
	day = int(raw_input("Day?")) # 8
	hour = int(raw_input("Hour?"))  # 22
	minutes = int(raw_input("Minutes?")) # 30
	seconds = int(raw_input("Seconds?")) # 0
	bc = raw_input("BC or BCE?") # false
	cal = int(raw_input("Gregorian 0 or Julian 1: ")) # 0
	zonetime = int(raw_input("Zone 0, Greenwhich 1, Local Mean 2, Local Apparent 3")) # 0
	plus = raw_input("Say False") # false
	# time zone UTC offset
	zh = int(raw_input("Zone hour?")) # 5 
	zm = int(raw_input("Zone minute")) # 0
	daylightsavings = raw_input("Daylgiht savings?") #false

	time = chart.Time(year,month,day,hour,minutes,seconds,True,cal,zonetime,False,zh, zm,False,place)

	#chart = chart.Chart(name,gender,time,place,htype,notes,options)
	horoscope = chart.Chart(name,True,time,place,0,"",opts)
	return horoscope
# test()