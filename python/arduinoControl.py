
import threading
 
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)


import serial

class ArduinoControl(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0',9600)
        self.valveThread = None

    def openValve(self,valveNr=0):
        """ opens the valve. blocks until the arduino has closed the valve again """
        print "opening valve"
        self.ser.write('o{0}'.format(valveNr))
        #print self.ser.read()
        #print self.ser.read()

    def closeValve(self,valveNr=0):
        print "closing valve"
        self.ser.write('c{0}'.format(valveNr))

    def valveStatus(self,valvNr=0):
        if self.valveThread == None:
            return {'status':'closed'}

        if self.valveThread.isAlive():
            return {'status':'open'}
        self.valveThread = None
        return {'status':'closed'}

    
            
