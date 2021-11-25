import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
	serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	parms = dict()
	parms['address'] = address
	if api_key is not False: parms['key'] = api_key
	url = serviceurl + urllib.parse.urlencode(parms)

	print('Retrieving', url)
	uh = urllib.request.urlopen(url, context=ctx)
	data = uh.read().decode()
	print('Retrieved', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print('==== Failure To Retrieve====')
		print(data)
		continue

	print(json.dumps(js, indent=4))

	check = -1 #starts at -1 because you want to start checking at index 0
	for item in js['results'][0]['address_components']:
		check += 1
		if js['results'][0]['address_components'][check]['types'] == ['country','political']:
			print(js['results'][0]['address_components'][check]['short_name'])
			break
		else:
			continue
	print('==== Country Not Found ====')