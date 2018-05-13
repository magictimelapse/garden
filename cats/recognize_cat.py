#!/home/pi/miniconda3/envs/ml/bin/python
import zerorpc
import sys
import glob
import crop_images
import random
import shutil
import time
import os
from multiprocessing import Process
import logging
logging.basicConfig(filename='/opt/motion/cat.log',level=logging.DEBUG)

def request_server(filename):
    c = zerorpc.Client()
    c.connect('tcp://127.0.0.1:4242')
    return c.cat_recognition({'filename':filename})
 
def main(run_nr):
        
        logging.debug('running : {0}'.format(run_nr))
        time.sleep(6)
        img_path = '/opt/motion/cropped'
        filenames_cropped = glob.glob(os.path.join(img_path,'{0}-*cropped.jpg'.format(run_nr)))
        filenames_cropped = filenames_cropped[:16]
        print (filenames_cropped)
        
        logging.debug('num images: {0}\n'.format(len(filenames_cropped)))
            
        for filename_cropped in filenames_cropped:
            logging.debug(filename_cropped)
            classification = request_server(filename_cropped)
            #0: cats, 1: noCat
            logging.debug('cats: {0}, noCat:  {1}'.format(classification['cats'],classification['noCat']))
            if classification['cats'] > 0.9:
                newPath = '/opt/motion/cropped/cats/'
                shutil.copy2(filename_cropped, newPath)
            elif classification['noCat'] > 0.9:
                newPath = '/opt/motion/cropped/noCat/'
                shutil.copy2(filename_cropped, newPath)
            else:
                newPath = '/opt/motion/cropped/unclassified/'
                shutil.copy2(filename_cropped, newPath)

if __name__=='__main__':
    run_nr = sys.argv[1]
    main(run_nr)
    #p = Process(target = main, args=(run_nr,))
    #p.start()
