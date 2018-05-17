#!/home/pi/miniconda3/envs/ml/bin/python
import zerorpc
import sys
sys.path.append('/home/pi/garden/python/')
import glob
import crop_images
import ov
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
        catsFound = 0
        logging.debug('num images: {0}\n'.format(len(filenames_cropped)))
        ov.o(3)
        for filename_cropped in filenames_cropped:
            logging.debug(filename_cropped)
            classification = request_server(filename_cropped)
            #0: cats, 1: noCat
            logging.debug('cats: {0}, noCat:  {1}'.format(classification['cats'],classification['noCat']))
            if classification['cats'] > 0.9:
                catsFound += 1
                newPath = '/opt/motion/cropped/cats/'
                shutil.copy2(filename_cropped, newPath)
            elif classification['noCat'] > 0.9:
                catsFound -= 2
                newPath = '/opt/motion/cropped/noCat/'
                shutil.copy2(filename_cropped, newPath)
            else:
                catsFound -= 1
                newPath = '/opt/motion/cropped/unclassified/'
                shutil.copy2(filename_cropped, newPath)

            
            if catsFound >= 2:
                logging.info('cats found!!')
                ov.o(0)
                time.sleep(4)
                ov.o(3)
                return

                
if __name__=='__main__':
    run_nr = sys.argv[1]
    main(run_nr)
    logging.info("done")
    #p = Process(target = main, args=(run_nr,))
    #p.start()
