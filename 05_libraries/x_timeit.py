# https://pythononline.ru/osnovy/timeit-python

import asyncio
import time
import timeit


timeit.timeit(stmt='myfunc()', setup='from __main__ import myfunc', timer=<default timer>, number=1000000, globals=None)
# stmt='pass' - проверяемый код,
# setup='pass' - настройка кода,
# timer=<default timer> - используемый таймер,
# number=1000000 - число циклов измерений,
# globals=None - область видимости.

def some():
    time.sleep(2)


# 1. timeit.timeit
timeit.timeit(stmt='some()', setup='from __main__ import some', number=1, globals=None)

t1 = timeit.timeit(some, number=1)
print(t1)


# 2. Timer
from timeit import Timer
t = Timer(some())
print (t.timeit(number=1))


print(time.ctime())











