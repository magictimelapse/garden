#!/home/pi/miniconda3/envs/ml/bin/python
import zerorpc
import sys
if __name__=='__main__':
    filename = sys.argv[1]
    c= zerorpc.Client()
    c.connect('tcp://127.0.0.1:4242')
    print (c.cat_recognition({'filename':filename}))


