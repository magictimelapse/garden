#!/home/pi/miniconda3/envs/ml/bin/python
import apply_model
import zerorpc
import numpy as np
class CatRecognition(object):
    def cat_recognition(self,jsonobject):
        filename = jsonobject['filename']
        pred = apply_model.predict(filename)
        #pred = np.array([[1.63431e-07, 0.99999988]],np.float64)
        probabilities = {'cats': float(pred[0][0]),'noCat': float(pred[0][1])}
        return probabilities

s = zerorpc.Server(CatRecognition())
s.bind('tcp://0.0.0.0:4242')
s.run()
