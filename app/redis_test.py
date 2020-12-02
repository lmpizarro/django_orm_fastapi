import time
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379)

def event_handler(msg):
    print(msg)
    thread.stop()  

pubsub = redis.pubsub()
pubsub.psubscribe(**{'__keyevent@0__:expired': event_handler})
thread = pubsub.run_in_thread(sleep_time=0.01)
