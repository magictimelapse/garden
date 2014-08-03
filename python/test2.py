#!/usr/bin/python
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()
class JobFunction(object):
    def job_function(self, number = 0):
        print "Hello World",number

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
#sched.add_cron_job(job_function, second='0,5,10,15,20,25,30,35,40,45,50,55')
#sched.add_interval_job(job_function, hours=2)
jobFunc = JobFunction()
sched.add_cron_job(lambda: jobFunc.job_function(1), second='0,5,10,15,20,25,30,35,40,45,50,55')
sched.add_cron_job(lambda: jobFunc.job_function(2), second='1,6,11,16,21,26,31,36,41,46,51,56')
raw_input("press enter")
