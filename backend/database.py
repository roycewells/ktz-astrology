import pymongo
from bson.objectid import ObjectId


MONGODB_URI = "mongodb://development:astrology@ds059661.mongolab.com:59661/astrology"

client = pymongo.MongoClient(MONGODB_URI)
db = client.astrology
combinations_db = db.combinations

#all users
users_db = db.users

'''status:
	"paid" - ready to be processed
	"completed" - already processed
'''



#----------people database-------------#

def addPerson(email, name, birthday, birth_time, birth_latitude, birth_longitude):
    '''add a person to the database and mark them as paid and ready for processing'''

    person = {"email" : email,
                "name" : name,
                "birthday": birthday,
                "birth_latitude" : birth_latitude,
                "birth_longitude": birth_longitude,
                "status" : "paid"}

    return users_db.insert(person)


def markCompleted(object_id):
	'''mark a person completed by id as having been processed'''
	users_db.find_one_and_update({"_id" : ObjectId(object_id)}, { "$set" : {"status" : "completed"}})


def getPeopleToBeProcessed():
	people = []
	for person in users_db.find({"status" : "paid"}):
		people.append(person)

	return people

def getPersonByEmail(email):
    return users_db.find_one({"email": email})

def getPersonByID(object_id):
    return users_db.find_one({"_id": ObjectId(object_id)})



#-----------combinations database---------#


def addHousePlanetCombo(house, planet, description):
    combo = {"house" : house,
             "planet" : planet}

    return combinations_db.update(combo, { "$set" : {"description" : description }}, upsert = True)

def getHousePlanetCombo(house, planet):
    return combinations_db.find_one({"house" : house, "planet" : planet})



def addPlanetZodiacCombo(planet, zodiac, description):
    combo = {"zodiac" : zodiac,
             "planet" : planet}

    return combinations_db.update(combo, { "$set" : {"description" : description }}, upsert = True)

def getPlanetZodiacCombo(planet, zodiac):
    return combinations_db.find_one({"zodiac" : zodiac, "planet" : planet})


def addPlanetPlanetAngleCombo(planet1, planet2, angle, description):
    #ensure planet1 is first alphabetically
    if planet1 > planet2:
        planet1, planet2 = planet2, planet1

    combo = {"planet1" : planet1,
             "planet2" : planet2,
             "angle"   : angle}

    return combinations_db.update(combo, { "$set" : {"description" : description }}, upsert = True)

def getPlanetPlanetAngleCombo(planet1, planet2, angle):
    if planet1 > planet2:
        planet1, planet2 = planet2, planet1

    return combinations_db.find_one({"planet1" : planet1, "planet2" : planet2, "angle" : angle})



def addStelliumHouseCombo(house, description):
    combo = {"stellium" : "house",
             "house" : house}

    return combinations_db.update(combo, { "$set" : {"description" : description }}, upsert = True)

def getStelliumHouseCombo(house):
    return combinations_db.find_one({"house" : house, "stellium" : "house"})



def addStelliumPlanetCombo(planet, description):
    combo = {"stellium" : "planet",
         "planet" : planet}

    return combinations_db.update(combo, { "$set" : {"description" : description }}, upsert = True)

def getStelliumPlanetCombo(planet):
    return combinations_db.find_one({"zodiac" : planet, "stellium" : "zodiac"})



# to store email maps to
# birthday information, paypal info,
# description



#13 planets
#12 zodiacs
#12 houses


