import os

from rq import Queue
from redis import Redis
from app import loop_script

redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
conn = Redis.from_url(redis_url)

q = Queue(connection=Redis())
result = q.enqueue(loop_script)