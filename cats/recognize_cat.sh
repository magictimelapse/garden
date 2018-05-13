#!/bin/bash
echo "running rec cat " >> /opt/motion/rrr.log
setsid /home/pi/cat_recognition/recognize_cat.py $1 >> /opt/motion/rrr.log 2>&1 &
