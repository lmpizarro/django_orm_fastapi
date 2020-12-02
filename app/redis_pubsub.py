import asyncio
import aioredis
import time
import json



async def main():
    # Redis client bound to single connection (no auto reconnection).
    redis = await aioredis.create_redis( 'redis://localhost')
    await redis.set('my-key', 'value')
    val = await redis.get('my-key')
    print(val)

    # gracefully closing underlying connection
    redis.close()
    await redis.wait_closed()


async def redis_pool():
    # Redis client bound to pool of connections (auto-reconnecting).
    redis = await aioredis.create_redis_pool(
        'redis://localhost')
    await redis.set('my-key', 'value')
    val = await redis.get('my-key')
    print(val)

    # gracefully closing underlying connection
    redis.close()
    await redis.wait_closed()


async def redis_publish_message():
    # Redis client bound to pool of connections (auto-reconnecting).
    print('init message') 
    redis = await aioredis.create_redis('redis://localhost')
    
    n = 1
    while True:
        await asyncio.sleep(10)
        data = {"job_id": n, "data": {'name': 'pepe', 'doc_id': 233456678}}
        json_data = json.dumps(data)
    
        await redis.publish('message', json_data)
        print('send message channel')
 
        n += 1
       
        # gracefully closing underlying connection
    redis.close()
    await redis.wait_closed()


async def redis_publish_fast_channel():
    # Redis client bound to pool of connections (auto-reconnecting).
    redis = await aioredis.create_redis('redis://localhost')

    n = 1
    while True:
        await asyncio.sleep(4)
        data = {"job_id": n, "data": {'name': 'pepe', 'doc_id': 233456678}}
        json_data = json.dumps(data)
        print('send fast channel')
        await redis.publish('fast_channel',  json_data)

        n += 1
    
        # gracefully closing underlying connection
    redis.close()
    await redis.wait_closed()


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        redis_publish_fast_channel(),
        redis_publish_message(),
    )

if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.run(redis_publish_message())
    # asyncio.run(redis_publish_fast_channel())

