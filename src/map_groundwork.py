import json, urllib
from urllib import urlencode

from googlemaps import Client
gmaps = Client('AIzaSyD0AJQRoThLlugn1lW_TgYhRBtRON34LDA')
start = "Bridgewater, Sa, Australia"
finish = "Stirling, SA, Australia"

url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', finish)
 ))
ur = urllib.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    print j
