#!/usr/bin/python

import json
import urllib2
from pyonep import onep
import time

config=json.loads(open("/home/pi/garden/python/config.json").read())

o = onep.OnepV1()

cik =  config['database']['cik']

dataport_alias_hum  = config['database']['aliases']['hum']
dataport_alias_temp = config['database']['aliases']['temp']
location = config['location']

while True:
    try:
        data = json.load(urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q={0}'.format(location)))
    #print json.dumps(data,indent=4,sort_keys=True)
        hum = float(data["main"]["humidity"])
        temp = float(data["main"]["temp"]-272.15)
        o.write(cik,
                {"alias":dataport_alias_hum},
                hum,
                {})
        o.write(cik,
                {"alias":dataport_alias_temp},
                temp,
                {})
        time.sleep(300)
    except:
        time.sleep(10)
                
        
