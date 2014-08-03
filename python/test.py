#!/usr/bin/python
import urllib2
from pyonep import onep
from datetime import datetime,timedelta
import numpy
import time
import  json

config =  json.loads(open("config.json").read())
cik = config['database']['exosite']['cik']
exoClient = onep.OnepV1()
dataport_alias_temp = config['database']['exosite']['aliases']['temp']

o = onep.OnepV1()

#nowUtc = datetime.utcnow()
nowUtc = datetime.now()

hours6 = timedelta(hours=6)
beforeUtc = nowUtc - hours6
startUnixTimeStamp = int(time.mktime(beforeUtc.timetuple()))
isok, response = o.read(
    cik,
    {'alias': dataport_alias_temp},
    {'starttime': startUnixTimeStamp,'limit':50000, 'sort': 'asc', 'selection': 'all'})

print isok
#print response

meanTemp = numpy.mean(numpy.array(response)[:,1])
print meanTemp
print int(time.mktime(beforeUtc.timetuple()))
print int(time.mktime(nowUtc.timetuple()))
