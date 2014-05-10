#!/usr/bin/python
import zerorpc
import arduinoControl

#if "__name__" == "__main__":
s = zerorpc.Server(arduinoControl.ArduinoControl())
s.bind("tcp://0.0.0.0:4242")
s.run()
