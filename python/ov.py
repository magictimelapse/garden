import json
import arduinoControl
from time import sleep
config =  json.loads(open("/home/pi/garden/python/config.json").read())
ac = arduinoControl.ArduinoControl(config)

def o(valveNumber=0,times=1):
    for ii in range(times):
        ac.openValve(valveNumber)
        if times != 1:
            sleep(25)
            print (ii)

def c(valveNumber=0):
    ac.closeValve(valveNumber)
    
