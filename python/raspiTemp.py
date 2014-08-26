#!/usr/bin/python

from pyonep import onep
import time
import json
config=json.loads(open("/home/pi/garden/python/config.json").read())

o = onep.OnepV1()

cik = config['database']['cik']

dataport_alias = 'RaspiTemp'


while True:
    tempC = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
    try:
        o.write(cik,
                {"alias":dataport_alias},
                tempC,
                {})
        time.sleep(300)
    except:
        time.sleep(10)
