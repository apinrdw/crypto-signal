from redis import Redis
from rq import Queue
from app import loop_script

q = Queue(connection=Redis())
result = q.enqueue(loop_script)