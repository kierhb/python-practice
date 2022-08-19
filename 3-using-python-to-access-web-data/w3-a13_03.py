# Calling a JSON API

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42 
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        print('No address...')
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    jsdata = json.loads(str(data))
    placeid = jsdata['results'][0]['place_id']
    print('Place id', placeid)

    #if not js or 'status' not in js or js['status'] != 'OK':
        #print('==== Failure To Retrieve ====')
        #print(data)
        #continue

    #print(json.dumps(js, indent=4))