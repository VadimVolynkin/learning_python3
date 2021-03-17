# https://docs-python.ru/standart-library/paket-multiprocessing-python/primitivy-sinhronizatsii-protsessov-modulja-multiprocessing/

# ==============================================================================================
# Примитивы синхронизации
# Синхронизирует процессы выполнения.
# ==============================================================================================

"""
Примитивы синхронизации с помощью объекта Manager.


"""
multiprocessing.Barrier(parties, action, timeout)
# примитив синхронизации Barrier - полный клон объекта threading.Barrier(количество потоков, вызываемый объект, таймаут)

multiprocessing.Semaphore(value)
# примитив синхронизации Semaphore - близкий аналог объекта threading.BoundedSemaphore.

multiprocessing.BoundedSemaphore(value)
# примитив синхронизации BoundedSemaphore(Ограниченный семафор) - близкий аналог объекта threading.BoundedSemaphore.

multiprocessing.Condition(lock)
# примитив синхронизации Condition - псевдоним объекта threading.Condition. lock - объект Lock или RLock из multiprocessing.

multiprocessing.Event
# примитив синхронизации Event - полный клон объекта threading.Event.

multiprocessing.Lock
# примитив синхронизации Lock(Простая блокировка) - близкий аналог threading.Lock(). Вернет экземпляр multiprocessing.synchronize.Lock.
# Если процесс или поток получил блокировку, то попытки получить ее от любого процесса или потока будут блокироваться до тех пор, пока она не будет снята. Любой процесс или поток может освободить его. 
Lock.acquire(block=True, timeout=None)  # ставит блокирующую или неблокирующую блокировку на макс. кол-во секунд.
Lock.release()                          # может быть вызван из любого процесса или потока, а не только из заблокированного

multiprocessing.RLock
# примитив синхронизации RLock возвращает объект рекурсивной блокировки - близкий аналог threading.RLock. 
# Рекурсивная блокировка должна быть снята процессом или потоком, который ее получил.
RLock.acquire(block=True, timeout=None) # устанавливает блокирующую или неблокирующую блокировку. При block=True, блокируется пока не перейдет в состояние ullock (не будет принадлежать ни одному процессу или потоку).
RLock.release() # опускает блокировку, уменьшив уровень рекурсии. 