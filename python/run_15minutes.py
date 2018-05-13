#!/usr/bin/env python
import time
import ov

ov.o(1)
time.sleep(5)
for ii in range(30):
    ov.o(3)
    time.sleep(5)
    ov.o(1)
    time.sleep(20)
