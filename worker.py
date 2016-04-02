""" 
    Standard worker setup, taken from Heroku tutorial
    Worker listens for new jobs in the Redis queue
"""

import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        r = redis.from_url(redis_url) 
        r.flushdb()
        worker = Worker(map(Queue, listen))
        worker.work()
        