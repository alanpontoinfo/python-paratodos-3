import urllib.request, urllib.parse, urllib.error
import json
#import ssl

#api_key = False
# se voce tem uma Google Plalces Api key, coloque aqui
# api_key = 'AIzaSy___IDByT70
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
 #  api_key = 42
  # serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#else :
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

      #ignore ssl certificado erros
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Entre localizacao:') 
    if len(address) < 1 : break

#    params = dict()  
 #   params['address'] = address
  #  if api_key is not False: params['key'] = api_key 
    url = serviceurl + urllib.parse.urlencode({'address':address})

    print('Recuperar', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Recupera', len(data), 'caracteres')

    try:
       js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat', 'lat', 'lng', 'lng')
    location = js['results'][0]['formatted_address']
print(location)