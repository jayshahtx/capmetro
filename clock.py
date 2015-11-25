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

# schedule a job to run every 5 seconds
@sched.scheduled_job('interval',seconds=5)
def hit_api():
    result = q.enqueue(get_bus_data)
    print result
    sys.stdout.flush()
       
sched.start()
