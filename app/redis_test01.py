import time
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379)

pubsub = redis.pubsub()
pubsub.psubscribe('__keyspace@0__:*')

print('Starting message loop')
while True:
    message = pubsub.get_message()
    if message:
        print(message)
    else:
        time.sleep(0.01)
