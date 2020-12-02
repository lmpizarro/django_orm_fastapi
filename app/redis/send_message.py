import asyncio
import aioredis

'''
https://redislabs.com/blog/beyond-the-cache-with-python/
https://aioredis.readthedocs.io/en/v1.3.1/start.html
https://itnext.io/event-data-pipelines-with-redis-pub-sub-async-python-and-dash-ab0a7bac63b0
https://tech.webinterpret.com/redis-notifications-python/
https://github.com/jonathanslenders/asyncio-redis
https://lightbus.org/latest/

https://www.programmersought.com/article/94442180903/
https://www.techevents.online/real-time-game-health-analytics-with-websockets-python-3-and-redis-pubsub/

https://tirkarthi.github.io/programming/2018/08/20/redis-streams-python.html


https://github.com/andymccurdy/redis-py

https://github.com/celery/kombu

https://pypi.org/project/djangoceleryrpc/


https://github.com/ideawu/ssdb
http://ideawu.github.io/ssdb-docs/
SSDB is a high performace key-value(key-string, key-zset, key-hashmap) NoSQL database, an alternative to Redis

https://itnext.io/event-data-pipelines-with-redis-pub-sub-async-python-and-dash-ab0a7bac63b0


https://pypi.org/project/aiojobs/
https://apscheduler.readthedocs.io/en/stable/
https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/

https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64
https://trstringer.com/logging-flask-gunicorn-the-manageable-way/
https://medium.com/@trstringer/logging-flask-and-gunicorn-the-manageable-way-2e6f0b8beb2f
https://oss.redislabs.com/redisjson/


https://dzone.com/articles/sql-access-to-redis-data

https://redislabs.com/blog/get-sql-like-experience-redis/

https://github.com/thumbor/thumbor

https://realpython.com/python-redis/#using-hiredis

https://redis.io/topics/twitter-clone

https://redis.io/documentation

https://rednafi.github.io/digressions/python/database/2020/05/25/python-redis-cache.html

https://redislabs.com/ebook/part-2-core-concepts/chapter-6-application-components-in-redis/6-6-distributing-files-with-redis/

https://stackoverflow.com/questions/32276493/how-to-store-and-retrieve-a-dictionary-with-redis
https://github.com/seperman/redisworks
https://msgpack.org/index.html

https://pypi.org/project/redis-helper/

https://pypi.org/project/kinto-redis/

python orm redis
https://pypi.org/project/redis-astra/
https://github.com/josiahcarlson/rom

https://pypi.org/project/redis-timeseries/
https://pythonhosted.org/python-stdnet/examples/columnts.html ****
https://blog.yugabyte.com/extending-redis-api-with-a-native-time-series-data-type/

https://pypi.org/project/pydantic-redis/

https://pypi.org/project/redis-limpyd/

https://pypi.org/project/coralillo/


https://www.cockroachlabs.com/case-studies/healthcare-company-migrates-from-oracle-to-cockroachdb-for-effortless-scale/

https://lyz-code.github.io/blue-book/coding/python/tinydb/
https://www.opensourceforu.com/2017/05/three-python-databases-pickledb-tinydb-zodb/

https://github.com/HarilalOP/OCR-Identity-Cards

id cards text recognition
https://nanonets.com/blog/id-card-digitization-deep-learning/
https://nanonets.com/blog/ocr-for-passports-and-id-cards/
https://github.com/HarilalOP/OCR-Identity-Cards

https://github.com/argman/EAST
https://github.com/hwalsuklee/awesome-deep-text-detection-recognition
https://awesomeopensource.com/projects/text-detection

https://github.com/emedvedev/attention-ocr

https://modelzoo.co/model/attentionocr

https://github.com/da03/Attention-OCR


https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework

https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker
https://www.jeffastor.com/blog/pairing-a-postgresql-db-with-your-dockerized-fastapi-app
https://www.jeffastor.com/blog/hooking-fastapi-endpoints-up-to-a-postgres-database/
https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest
https://www.jeffastor.com/blog/marketplace-functionality-in-fastapi

https://github.com/jordaneremieff/asgi-examples
https://www.encode.io/articles/hello-asgi
https://github.com/florimondmanca/awesome-asgi
https://fastapi.tiangolo.com/advanced/middleware/

https://kx.com/


'''
async def main():

  redis = await aioredis.create_redis('redis://localhost:6379/0', encoding='utf-8')

  await asyncio.gather(
    add_to_stream(redis, 1, 'Possible vocalizations east of Makanda', 'Class B'),
    add_to_stream(redis, 2, 'Sighting near the Columbia River', 'Class A'),
    add_to_stream(redis, 3, 'Chased by a tall hairy creature', 'Class A'))

  redis.close()
  await redis.wait_closed()

def add_to_stream(redis, id, title, classification):
  return redis.xadd('bigfoot:sightings:stream', {
    'id': id, 'title': title, 'classification': classification })

asyncio.run(main())
