from celery import group, chain
from tasks import add, reduce_
import time

header = [add.s(i, i) for i in range(10)]
res = group(header)()


a = res.get(timeout=1)

print(a)

t = reduce_.delay(a)

while not t.ready():
    
    time.sleep(.1)

print(t.state, t.get())


12029503640
 
Rroe6844d$99
