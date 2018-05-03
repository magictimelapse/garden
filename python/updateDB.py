import urllib2
#from pyonep import onep
from datetime import datetime,timedelta
import numpy
import time
import  json


class ExositeWriter(object):
    def __init__(self,config):
        self._conf = config
        self._cik = config['database']['cik']
        self._o =  onep.OnepV1()
        self._dataport_alias_duration = [config['database']['aliases']['wateringDuration0'],config['database']['aliases']['wateringDuration1']]


    def updateWateringDuration(self,duration,valve):
        try:
            #print "trying to update: ",duration,valve
            #print self._dataport_alias_duration[valve]
            self._o.write(self._cik, {"alias": self._dataport_alias_duration[valve]}, duration/2., {})
        except Exception as e:
            print e
            pass
        
        




class UpdateDB(object):
    def __init__(self,config):
        self._conf = config
        if self._conf['database']['type'] == 'exosite':
            self._db = ExositeWriter(self._conf)


    def updateWateringDuration(self,duration,valve):
        if False:
            self._db.updateWateringDuration(duration,valve)
