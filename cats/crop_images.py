#!/usr/bin/env python
from PIL import Image
import json
import os
import sys
def crop_image(jfilename):
    data = json.load(open(jfilename))
    ifilename = data['filename']
    img = Image.open(ifilename)
    left = data['center_x'] - data['width']/2
    right = data['center_x'] + data['width']/2
    top = data['center_y'] - data['height']/2
    bottom = data['center_y'] + data['height']/2
    cropped_img = img.crop((left,top,right,bottom))
    path,filename = os.path.split(ifilename)
    path = os.path.join(path,'cropped')
    
    filename_cropped = os.path.join(path,os.path.splitext(filename)[0] + '_cropped.jpg')
    
    cropped_img.save(filename_cropped)


if __name__=="__main__":
    path = sys.argv[1]
    import glob
    jfilenames = glob.glob(os.path.join(path, '*.json'))
    for j in jfilenames:
        crop_image(j)

