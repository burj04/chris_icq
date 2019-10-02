import urllib.parse
import urllib.request
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI'

while True:
	address = input("Enter location: ")
	if len(address) < 1:
		break
	url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address':address})
	
	print("Retrieving : {0}".format(url))
	url = urllib.request.urlopen(url)
	data = url.read()
	print("Retrieved {0}, Characters".format(len(data)))
	
	try:
		js = json.load(str(data))
	except: js = None
	
	if 'STATUS' not in js or js['STATUS'] != 'OK':
		print ("=== Failure To Retrieve ===")
		print (data)
		continue 
	print(json.dumps(js, indent = 4))
	
	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	print (" Latitude : {0}, Longitude : {0}".format(lat, lng))
	location = js['results'][0]['formatted_address']
	print(location)
