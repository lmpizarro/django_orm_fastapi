from celery import Celery
import celery.backends.redis
import time
import json
import redis
import logging

logger = logging.getLogger('celery tasks')


app = Celery('tasks', backend='redis://localhost', broker='redis://localhost//')

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
pubsub_sus_2 = r.pubsub()
pubsub_sus_2.subscribe('fast_channel')


pubsub_sus = r.pubsub()
pubsub_sus.subscribe('message')


app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)


@app.task
def add(x, y):
    return x + y
    
@app.task
def reduce_(a):   
    return sum(a)
    
@app.task
def task_message_channel(message):
    message = json.loads(message)
    print(f'DOING THE HARD PART job_id {message["job_id"]}')
    time.sleep(5)   
    return f'END THE HARD PART job_id {message["job_id"]}'
    

@app.task
def task_fast_channel(message):
    message = json.loads(message)
    print(f'DOING THE HARD PART job_id {message["job_id"]} {message["data"]}')
    time.sleep(1)   
    return f'END THE HARD PART job_id {message["job_id"]}'

 
from celery.schedules import crontab

 
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(5, receive_message.s(), name='receive_message every 5')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(1.0, receive_fast_channel.s(), name='receive_fast_channel every 1')
 

@app.task
def receive_message():
    received = pubsub_sus.get_message()
    message = 'not message'
    if received != None:
        channel = received['channel'].decode('ascii')
        
        logger.info(f'channel {channel}')
        
        try:
            message = received["data"].decode('ascii')
            task_message_channel.delay(message)
            
        except AttributeError as e:
            logger.error(f'decode message {e}')
            pass            
    else:
        pass
        
    print(f'received {message}')



@app.task
def receive_fast_channel():
    received = pubsub_sus_2.get_message()
    message = 'not message'
    if received != None:
        channel = received['channel'].decode('ascii')
        
        print(f'channel {channel}')
        
        try:
            message = received["data"].decode('ascii')
            # reduce_time.delay(message)
            task_fast_channel.delay(message)            
        except AttributeError as e:
            logger.error(f'decode message {e}')
    else:
        pass
        
    print(f'received {message}')

