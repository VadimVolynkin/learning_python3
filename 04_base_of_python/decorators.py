
Декоратор в Python – это функция, которая в качестве аргумента принимает другую функцию и расширяет ее функционал без изменения последней.
https://python-scripts.com/decorators-one

https://proproprogs.ru/python_base/dekoratory-funkciy-i-zamykaniya

https://python-scripts.com/decorator-arguments

import time




testTime (нашего декоратора) объявлена еще одна функция wrapper (обертка), внутри которой уже и происходит вызов некой функции fn



в конце сам декоратор возвращает ссылку на функцию wrapper.


Здесь вот эта вложенная функция как раз и расширяет функционал для fn, не меняя ее саму.

def testTime(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = fn(*args, **kwargs)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
        return res
    return wrapper



def timeit(method):
   def timed(*args, **kw):
       ts = time.time()
       result = method(*args, **kw)
       te = time.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result
   return timed

   
# The way to use this decorator is:
@timeit
def my_view(request):
    ...











