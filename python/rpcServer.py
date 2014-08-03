#!/usr/bin/python
import zerorpc
import arduinoControl
import json
#if "__name__" == "__main__":
config=json.loads(open("/home/pi/garden/python/config.json").read())
s = zerorpc.Server(arduinoControl.ArduinoControl(config))
s.bind("tcp://0.0.0.0:4242")
s.run()
