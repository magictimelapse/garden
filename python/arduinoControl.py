
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

    def _openValve(self,valveNr=0):
        """ opens the valve. blocks until the arduino has closed the valve again """
        print "opening valve"
        self.ser.write('o0')
        #print self.ser.read()
        #print self.ser.read()

    def _closeValve(self,valveNr=0):
        print "closing valve"
        self.ser.write('c0')

    def valveStatus(self,valvNr=0):
        if self.valveThread == None:
            return {'status':'closed'}

        if self.valveThread.isAlive():
            return {'status':'open'}
        self.valveThread = None
        return {'status':'closed'}

    def openValve(self):
        """ calls _openValve in a thread. Returns the status (open, closed) as json """
        if self.valveThread == None or not self.valveThread.isAlive():
            self.valveThread = FuncThread(self._openValve)
            self.valveThread.start()

        

        
        return self.valveStatus()
            
