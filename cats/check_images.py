#!/usr/bin/env python
import glob
import os
import prediction
image_path = '/tmp/motion/'
filenames = glob.glob(os.path.join(image_path,"*.jpg"))

for filename in filenames:
    predictions = prediction.predict(filename)
    print(filename)
    print(predictions)
    print("#############")
