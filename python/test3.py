#!/usr/bin/python
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()
scheduler.start()

def myFunc():
    print "hello world!"

job = scheduler.add_job(myFunc, 'interval', minutes=2)
