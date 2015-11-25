# misc
import pdb, sys, datetime
from api_fns.api import get_bus_data

# scheduling
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval',seconds=5)
def hit_api():
    vehicles = get_bus_data()
    print datetime.datetime.now()
    sys.stdout.flush()
       

sched.start()

