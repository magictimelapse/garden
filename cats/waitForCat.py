#!/usr/bin/python
import cv2
import numpy as np
import sys,os
os.system('rm ./data/*.png')
sys.path.append("/home/pi/garden/python/")
import ov
cam = cv2.VideoCapture(1)
import time

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

def countsZero():
    return [0,0,0]

t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

rows,cols = t.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
PixelThreshold = 3

counts = countsZero()
countThreshold = 150


imgCounter=0
print "setup started"
while(1):
    diffImage = diffImg(t_minus,t,t_plus)
    #print "showing next image..."
    diffImageR = cv2.warpAffine(diffImage,M,(cols,rows))
    ## count ##
    mean = np.mean(diffImageR)
    #rms = np.sqrt(np.mean(diffImageR**2))
    rms = np.sqrt(np.mean(t**2))
    #print mean,rms
    PixelThreshold = mean + 2*rms
    count = (diffImageR>PixelThreshold).sum()
    #print count
    counts.append(count)
    counts.pop(0)
    if (np.array(counts)>countThreshold).sum() == len(counts):
        
        print counts
        
        #cv2.imshow('e2',trot)
        #if cv2.waitKey(5)==27:
        #    break
        for ii in range(2):
            ov.c(0)
            time.sleep(0.1)
            ov.c(1)
            time.sleep(0.1)
            ov.o(3)
            time.sleep(0.1)
            ov.o(2)
            time.sleep(3)
        ov.c(3)
        time.sleep(1)
        ov.c(2)
        counts = countsZero()

        trot_plus = cv2.warpAffine(t_plus,M,(cols,rows))
        trot = cv2.warpAffine(t,M,(cols,rows))
        trot_minus = cv2.warpAffine(t_minus,M,(cols,rows))
        cv2.imwrite('./data/img_t0_{0:06d}.png'.format(imgCounter),trot)
        cv2.imwrite('./data/img_tp_{0:06d}.png'.format(imgCounter),trot_plus)
        cv2.imwrite('./data/img_tm_{0:06d}.png'.format(imgCounter),trot_minus)
        imgCounter += 1
        time.sleep(2)
        t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    #print counts
    #cv2.imshow('e2',diffImageR)
    t_minus = t
    t = t_plus
    flag,img = cam.read()
    t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if not flag:
        print "problem with image"




    #cv2.imshow('e2',gimg)
  
cv2.destroyAllWindows()
