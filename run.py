import os
import redis

# from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime
from app import loop_script

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

# q = Queue(connection=conn)
# result = q.enqueue(loop_script)

scheduler = Scheduler(connection=conn)

if len(scheduler.get_jobs()) > 0:
    for job in scheduler.get_jobs():
        scheduler.cancel(job)

scheduler.schedule(
    scheduled_time=datetime.utcnow(),
    func=loop_script,
    interval=30
)

print(scheduler.get_jobs())