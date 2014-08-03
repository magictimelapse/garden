

import urllib2
from pyonep import onep
from datetime import datetime,timedelta
import numpy
import time
import  json


class ExositeReader(object):
    """ receive weather information from exosite db """
    def __init__(self,config):
        self._conf = config
        self._cik = config['database']['cik']
        self._o =  onep.OnepV1()
        self._dataport_alias_temp = config['database']['aliases']['temp']
        self._dataport_alias_hum = config['database']['aliases']['hum']


    def getTemperatureData(self,durationTime):
        """ returns a 2D list containing the timestamps and temperatures from the last durationTime hours """
        now = datetime.now()
        duration =  timedelta(hours=durationTime)
        before = now - duration
        startUnixTimeStamp = int(time.mktime(before.timetuple()))
        isok = True
        try:
            isok, response = self._o.read(
            self._cik,
            {'alias': self._dataport_alias_temp},
            {'starttime': startUnixTimeStamp,'limit':50000, 'sort': 'asc', 'selection': 'all'})
        except:
            response = [[0,20],[1,20]]
        if not isok:
            response = [[0,20],[1,20]]
        return response


    def getHumidityData(self,durationTime):
        """ returns a 2D list containing the timestamps and humidities from the last durationTime hours """
        now = datetime.now()
        duration =  timedelta(hours=durationTime)
        before = now - duration
        startUnixTimeStamp = int(time.mktime(before.timetuple()))
        try:
            isok, response = self._o.read(
            self._cik,
            {'alias': self._dataport_alias_hum},
            {'starttime': startUnixTimeStamp,'limit':50000, 'sort': 'asc', 'selection': 'all'})
        except:
            response = [[0,50],[1,50]]
        if not isok:
            response = [[0,50],[1,50]]
        return response



    def getMeanTemperature(self,durationTime):
        """ returns the mean temperature from the last <time> hours"""
        data = numpy.array(self.getTemperatureData(durationTime))
        datay = (data[1:,1] + data[:-1,1])/2
        weights = data[1:,0] - data[:-1,0]
        mean = numpy.average(datay,weights=weights)
        return mean

    def getMeanHumidity(self,durationTime):
        """ returns the mean humidity from the last <time> hours"""
        data = numpy.array(self.getHumidityData(durationTime))
        datay = (data[1:,1] + data[:-1,1])/2
        weights = data[1:,0] - data[:-1,0]
        mean = numpy.average(datay,weights=weights)
        return mean


class WeatherInformation(object):
    """ receive weather information from the database """
    def __init__(self,config):
        self._conf = config
        if self._conf['database']['type'] == 'exosite':
            self._db = ExositeReader(config)


    def getMeanTemperature(self,durationTime):
        """ returns the mean temperature from the last <time> hours"""
        return self._db.getMeanTemperature(durationTime)


    def getMeanHumidity(self,durationTime):
        """ returns the mean humidity from the last <time> hours"""
        return self._db.getMeanHumidity(durationTime)
