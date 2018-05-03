#!/usr/bin/env python
import os, sys
import json
import crop_images
if __name__ == "__main__":
    out_dict = {}
    out_dict['filename'] = sys.argv[1]
    out_dict['event'] = int(sys.argv[2])
    out_dict['frame_nr'] =int(sys.argv[3])
    out_dict['width'] = int(sys.argv[4])
    out_dict['height'] = int(sys.argv[5])
    out_dict['center_x'] = int(sys.argv[6])
    out_dict['center_y'] = int(sys.argv[7])
    filename = out_dict['filename']
    filename_txt = os.path.splitext(filename)[0]+'.json'
    with open(filename_txt,'w') as outfile:
        json.dump(out_dict,outfile)
    crop_images.crop_image(filename_txt)
