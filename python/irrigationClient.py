#!/usr/bin/python
import zerorpc
import weatherInformation
import time
import json
from apscheduler.scheduler import Scheduler
import ov
import random
import logging;logging.basicConfig(level=logging.DEBUG,filename='/home/pi/garden/python/irrigation.log',format='%(asctime)s %(message)s')
logging.debug('irrugation loading')

class IrrigationClient(object):
    def __init__(self,config):
        self._conf = config
        self._weatherInformation = weatherInformation.WeatherInformation(self._conf)
        

    def getWateringDuration(self,valve):
        meanTemperature = self._weatherInformation.getMeanTemperature(6)
        baseWateringDuration = self._conf['valve'][valve]['baseWateringDuration']
        maxWateringDuration = self._conf['valve'][valve]['maxWateringDuration']
        thresholdTemperature = self._conf['valve'][valve]['thresholdTemperature']
        linearModel = self._conf['valve'][valve]['linearModel']
        if meanTemperature > thresholdTemperature:
            wateringDuration = baseWateringDuration + (meanTemperature - thresholdTemperature)*linearModel
            if wateringDuration > maxWateringDuration:
                wateringDuration = maxWateringDuration

        else:
            wateringDuration = baseWateringDuration
        
        print "watering duration:",wateringDuration
        return int(wateringDuration)


    def irrigate(self,valve):
        wateringDuration = self.getWateringDuration(valve)
        #zclient = zerorpc.Client()
        #zclient.connect("tcp://127.0.0.1:4242")
        ### sleep some random time <5 seconds
        time.sleep(5*random.random())
        print "opening valve {0} for {1}".format(valve,wateringDuration)
        logging.info( "opening valve {0} for {1}".format(valve,wateringDuration))
        for ii in range(wateringDuration):
            print "opening: {0}".format(ii)
            logging.info("opening: {0}".format(ii))
            #zclient.openValve(valve)
            ov.o(3) # always open valve 3 (main valve)
            time.sleep(3)
            ov.o(valve)
            time.sleep(25)



if __name__ == "__main__":
    conf = json.loads(open("/home/pi/garden/python/config.json").read())
    ig = IrrigationClient(conf)
    # Start the scheduler
    sched = Scheduler()
    sched.start()

    for ii in range(len(conf['valve'])):
        wateringHour = conf['valve'][ii]['wateringHour']
        vv =  int(conf['valve'][ii]['nr'])
        print "scheduling", wateringHour, vv
        logging.info("scheduling {0} {1}".format( wateringHour, vv))
        
        sched.add_cron_job(ig.irrigate,args=[vv], hour = wateringHour, minute=40)

    ## endless loop ##
    while True:
        with open('/home/pi/garden/python/schedlog.log','a') as f:
            sched.print_jobs(f)

        time.sleep(1800)
        

