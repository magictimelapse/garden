#!/usr/bin/python
import cv2
cam = cv2.VideoCapture(1)


winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
NN=4
cc = 0
while True:
  cc += 1
  if cc%25 == 0:
    print cc
  img = cv2.cvtColor(cam.read()[1],cv2.COLOR_RGB2GRAY) 
  print "start NNming"
  #for i in range(NN-1):
  #  im = cv2.cvtColor(cam.read()[1],cv2.COLOR_RGB2GRAY)
  #  img += im
 
  print "done"
  print img
  #img /= NN
  cv2.imshow( winName,img )
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
