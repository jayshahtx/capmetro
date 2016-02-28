# misc
import pdb, sys, datetime
from api_fns.api import get_bus_data
import logging


# scheduling
from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn

# initialize scheduling objects
sched = BlockingScheduler()
q = Queue(connection=conn)
logging.basicConfig()

# schedule a job to run every 120 seconds
@sched.scheduled_job('interval',seconds=120)
def hit_api():
    job = q.enqueue(get_bus_data)
    print "Posted job at " + str(datetime.datetime.now())
    sys.stdout.flush()
       
sched.start()
