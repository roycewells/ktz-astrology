from flask import Flask, render_template, request, jsonify, \
		url_for, redirect, make_response, session, flash
from backend import database as db
from backend import config, paypal
import hashlib, json
from flask.ext.basicauth import BasicAuth
import os
from geopy.geocoders import Nominatim
import urllib
import Morinus

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = config.secret_key

geolocator = Nominatim()

@app.route('/favicon.ico')
def icon():
	return url_for('static', filename='img/favicon.ico')

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/reading', methods=["GET"])
def sendHome():
	return redirect("/")

@app.route('/reading', methods=["POST"])
def read():
	form = request.form

	name = form.get("name")
	birth_day = form.get("birthday")
	birth_place = form.get("birthplace")
	birth_time = form.get("birthtime")

	#get latitude and longitude for birthplace
	location = geolocator.geocode(birth_place)
	if location == None:
		# handle error, can't find location
		pass
	birth_latitude = location.latitude
	birth_longitude = location.longitude

	# manipulate data for correct format
	(month, day, year) = birth_day.split("/")
	(hour, minute) = birth_time.split(":")
	year = int(year)
	month = int(month)
	day = int(day)
	hour = int(hour)
	minute = int(minute)

	print (month, day, year, hour, minute)
	
	chart = Morinus.create_chart(year, month, day, hour, minute, birth_place, birth_latitude, birth_longitude, name)
	print Morinus.get_table(chart)
	print Morinus.get_planetary_aspects(chart)
	# Morinus.save_chart(chart, "../../pics/")
	# Morinus.save_planetary_aspects(chart, "../../pics/")	
	
	return render_template('reading.html', name = name,
											birth_day = birth_day,
											birth_place = birth_place,
											birth_time = birth_time,
											birth_latitude = birth_latitude,
											birth_longitude = birth_longitude)


#--------Paypal-------------------#

@app.route('/create-payment', methods=["POST"])
def payment():
	form = request.form

	name = form.get("name")
	birthday = form.get("birthday")
	birthplace = form.get("birthplace")
	birth_latitude = form.get("birth_latitude")
	birth_longitude = form.get("birth_longitude")
	birth_time = form.get("birth_time")

	url_string = urllib.urlencode({"name" : name,
									"birthday": birthday,
									"birthplace" : birthplace,
									"birth_time" : birth_time,
									"birth_latitude" : birth_latitude,
									"birth_longitude": birth_longitude })

	payment = paypal.makePayment(url_string)
	for link in payment.links:
		if link.method == "REDIRECT":
			success_redirect = payment["links"][1]["href"]

	return redirect(success_redirect)

@app.route('/execute-payment', methods=["POST"])
def execute():
	form = request.form

	payment_id = form.get("payment_id")
	payer_id = form.get("payer_id")

	if paypal.executePayment(payment_id, payer_id):
		#add to DB
		return redirect(url_for("success"))
	#else:
		#handle payment processing error



@app.route('/finalize')
def finalize():
	args = request.args

	name = args.get("name")
	birthday = args.get("birthday")
	birthplace = args.get("birthplace")
	birth_latitude = args.get("birth_latitude")
	birth_longitude = args.get("birth_longitude")
	payment_id = args.get("paymentId")
	payer_id = args.get("PayerID")

	return render_template('review.html', name = name,
											birthday = birthday,
											birthplace = birthplace,
											birth_latitude = birth_latitude,
											birth_longitude = birth_longitude,
											payment_id = payment_id,
											payer_id = payer_id)


@app.route('/success')
def success():
	return render_template('success.html')

#--------Admin Page---------------#

#get login form
@app.route("/login", methods=["GET"])
def login():
	if ("admin" in session and session["admin"]):
		return redirect(url_for("admin"))
	return render_template('login.html')

#submit login request
@app.route("/login", methods=["POST"])
def validate():
	if checkCredentials(request.form.get("username"), request.form.get("password")):
		session["admin"] = True
		return redirect(url_for("admin"))
	flash("Incorrect username / password combination.")
	return redirect(url_for("login"))

@app.route('/logout')
def logout():
	session["admin"] = False
	return render_template('login.html')

@app.route('/admin')
def admin():
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	people = db.getPeopleToBeProcessed()

	return render_template('admin.html', people=people)

@app.route('/admin/person/<id>')
def adminPerson(id):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	person = db.getPersonByID(id)

	return render_template('admin_person.html', person=person)

@app.route('/admin/descriptions')
def descriptions():
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	return render_template('descriptions.html')

@app.route('/admin/descriptions/hp/<house>/<planet>', methods=["GET", "POST"])
def hpget(house, planet):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	if request.method == 'GET':
		val = db.getHousePlanetCombo(house,planet)
		if val is None:
			return "None"
		else:
			return val["description"]
	else: #POST
		return str(db.addHousePlanetCombo(house, planet, request.form["description"]) is not None)

@app.route('/admin/descriptions/pz/<planet>/<zodiac>', methods=["GET", "POST"])
def pzget(planet, zodiac):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	if request.method == 'GET':
		val = db.getPlanetZodiacCombo(planet, zodiac)
		if val is None:
			return "None"
		else:
			return val["description"]
	else: #POST
		return str(db.addPlanetZodiacCombo(planet, zodiac, request.form["description"]) is not None)

@app.route('/admin/descriptions/ppa/<planet1>/<planet2>/<angle>', methods=["GET", "POST"])
def ppaget(planet1, planet2, angle):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	if request.method == 'GET':
		val = db.getPlanetPlanetAngleCombo(planet1, planet2, angle)
		if val is None:
			return "None"
		else:
			return val["description"]
	else: #POST
		return str(db.addPlanetPlanetAngleCombo(planet1, planet2, angle, request.form["description"]) is not None)

@app.route('/admin/descriptions/s3h/<house>', methods=["GET", "POST"])
def s3hget(house):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	if request.method == 'GET':
		val = db.getStelliumHouseCombo(house)
		if val is None:
			return "None"
		else:
			return val["description"]
	else: #POST
		return str(db.addStelliumHouseCombo(house, request.form["description"]) is not None)

@app.route('/admin/descriptions/s3p/<planet>', methods=["GET", "POST"])
def s3pget(planet):
	if not ("admin" in session and session["admin"]):
		return redirect(url_for("login"))

	if request.method == 'GET':
		val = db.getStelliumPlanetCombo(planet)
		if val is None:
			return "None"
		else:
			return val["description"]
	else: #POST
		return str(db.addStelliumPlanetCombo(planet, request.form["description"]) is not None)


def checkCredentials(username, password):
	hashedUsername = hashlib.sha224(username).hexdigest()
	hashedPassword = hashlib.sha224(password).hexdigest()
	correctUsername = config.userHash
	correctPassword = config.passHash
	return hashedUsername == correctUsername and hashedPassword == correctPassword


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8000)
	#app.run(host = str(os.getenv('IP', '0.0.0.0')), port = int(os.getenv('PORT', 8080)))