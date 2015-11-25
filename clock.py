# misc
import pdb, sys, datetime
from api_fns.api import get_bus_data
import logging

logging.basicConfig()

# scheduling
from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn

sched = BlockingScheduler()
q = Queue(connection=conn)

@sched.scheduled_job('interval',seconds=1)
def hit_api():
    vehicles = q.enqueue(get_bus_data,)
    print datetime.datetime.now()
    sys.stdout.flush()
       

sched.start()
