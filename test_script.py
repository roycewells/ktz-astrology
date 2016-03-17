import Morinus

year = 1995 
month = 2
day = 8
hour = 22
minute = 30
place_name = "new britian connecticut"
lat = 41.6750
lon = -72.7872
name = "gilad"

chart = Morinus.create_chart(year, month, day, hour, minute, place_name, lat, lon, name)
print Morinus.get_table(chart)
print Morinus.get_planetary_aspects(chart)
Morinus.save_chart(chart, "../../pics/")
Morinus.save_planetary_aspects(chart, "../../pics/")