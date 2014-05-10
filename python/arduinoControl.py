
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

    def _openValve(self):
        """ opens the valve. blocks until the arduino has closed the valve again """
        self.ser.write('r')
        print self.ser.read()
        print self.ser.read()



    def valveStatus(self):
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
            
