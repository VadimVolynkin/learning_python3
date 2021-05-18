# ==============================================================================================
# POOL
# Создает объект, управляющий пулом рабочих процессов, в который могут быть отправлены задания.
# Пул рабочих процессов поддерживает асинхронное выполнение задач с тайм-аутами и обратными вызовами и имеет параллельную реализацию.
# ==============================================================================================

from multiprocessing import Pool

# создание объекта пула
pool = Pool(
    processes,         # количество используемых рабочих процессов. Если явно не указан, то os.cpu_count().
    initializer,       # вызываемый объект (функция)
    initargs,          # аргументы для initializer
    maxtasksperchild,  # макс. количество выполненных задач рабочего процесса до выхода и замены на новый процесс. По умолчанию None - живет как пул
    context            # контекст для запуска рабочих процессов
    )

# ==================================================================================

Pool.apply(func, args, kwds)
# вызывает функцию с аргументами и блокирует выполнение программы до готовности результата
# func выполняется только в одном рабочем процессе пула

Pool.apply_async(func, args, kwds, callback, error_callback)
# асинхронный вариант метода Pool.apply()

Pool.map(func, iterable, chunksize)
# многопроцессорный эквивалент встроенной функции map(), (функиция, итерируемый объект с еднственным аргументом, размер частей)
# разбивает итерируемый объект на несколько частей, которые отправляет в пул процессов как отдельные задачи
# блокирует выполнение программы до получения результатов работы всеми запущенными процессами.

Pool.map_async(func, iterable, chunksize, callback, error_callback)
# асинхронный вариант метода Pool.map()

Pool.imap(func, iterable, chunksize)
# более ленивая версия метода Pool.map()

Pool.imap_unordered(func, iterable, chunksize)
# то же самое, что и Pool.imap(), только результаты идут по готовности

Pool.starmap(func, iterable, chunksize)
# аналогичен методу Pool.map(), но аргумент может быть итерируемым iterable=[(1, 2), (3, 4)]

Pool.starmap_async(func, iterable, chunksize, callback, error_callback)
# комбинация методов Pool.starmap() и Pool.map_async()

Pool.close()
# предотвращает отправку задач в пул. Как только все задачи будут выполнены, рабочие процессы завершатся.

Pool.terminate()
# останавливает рабочие процессы немедленно, не давая завершить невыполненную работу.

Pool.join()
# ждет, пока рабочие процессы закончатся. Перед использованием Pool.join() необходимо вызвать Pool.close() или Pool.terminate().


# === Объект AsyncResult представляет собой результат, возвращаемый методами Pool.apply_async() и Pool.map_async().
AsyncResult.get(timeout)
# возвращает результат, как только он придет. Если timeout не None и результат не приходит, то исключение TimeoutError

AsyncResult.wait(timeout)
# ждет, пока будет доступен результат или пока не пройдет время timeout

AsyncResult.ready()
# проверяет, завершился ли вызов

AsyncResult.successful()
# проверяет, был ли завершен вызов без исключения. Поднимет исключение ValueError, если результат не готов.



# ==============================================================================================
# КАК ЗАПУСТИТЬ POOL
# ==============================================================================================
from multiprocessing import Pool, TimeoutError, current_process
import time, os

# какой то рабочий код
def worker(x):
    print('WORKER() => ', current_process().name)
    return x*x

if __name__ == '__main__':
    # запуск 4 рабочих процессов в пуле
    with Pool(processes=4) as pool:

        # 1. результаты получим в порядке поступления задач благодаря map
        res = pool.map(worker, range(10))
        print(res)

        # 2. результаты получим в порядке их готовности (могут быть не по порядку)
        for i in pool.imap_unordered(worker, range(10)):
            print(i, end=', ')
        print()
        
        # 3. вычислит "worker(20)" асинхронно, запустится только один процесс
        res = pool.apply_async(worker, (20,))
        # получение результата 
        async_worker = res.get(timeout=1)
        print('1 процесс, worker(20) => ', async_worker)

        # 4. вычислит "os.getpid()" асинхронно, запустится только один процесс
        res = pool.apply_async(os.getpid, ())
        # получение результата 
        async_getpid = res.get(timeout=1)
        print('1 процесс, os.getpid()  => ', async_getpid)

        # 5. запуск нескольких асинхронных вычислений, *может* использовать больше процессов
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        # получение асинхронных результатов
        async_multi = [res.get(timeout=1) for res in multiple_results]
        print('4 асинхронных процесса, os.getpid():')
        print(async_multi)

        # 6. заставим спать один рабочий процесс в течение 10 секунд
        res = pool.apply_async(time.sleep, (10,))
        try:
            # получение результата 
            res_sleep = res.get(timeout=1)
            print(res_sleep)
        except TimeoutError:
            print("time.sleep(10) => получили multiprocessing.TimeoutError")

        # print("На этот момент пул остается доступным для дополнительной работы")

    # выход из блока 'with' остановил пул
    print("Теперь пул закрыт и больше не доступен")




