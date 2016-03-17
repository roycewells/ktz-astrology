import database as db


# for i in range(15):
# 	name = "ben" + str(i)
#    	db.addPerson( name + "@benconnex.com", name + " cowpig", "11/11/11", "23:12", "232.232", "121.12")

print db.addPlanetZodiacCombo("jupiter", "dog", "a cool dog is here")
print db.getPlanetZodiacCombo("jupiter", "dog")
print db.getPlanetZodiacCombo("dfd", "dfdf")