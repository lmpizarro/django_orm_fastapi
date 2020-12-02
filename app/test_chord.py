from celery import group, chord
from tasks import add, reduce_
import time

callback = reduce_.s()
header = [add.s(i, i) for i in range(10)]

res = chord(header)(callback)


a = res.get(timeout=1)

print(a)
