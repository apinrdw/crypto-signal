import os
import redis

from rq import Queue
from app import loop_script

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

q = Queue(connection=conn)
result = q.enqueue(loop_script)