# =====================================================================================================
# Синхронизация потоков при помощи threading.Semaphore() реализует семафорные объекты, которые управляют атомарным счетчиком.
# Атомарный счетчик = количество вызовов .release() - количество вызовов .acquire() + начальное значение value. 
# Используются для защиты ресурсов с ограниченной емкостью. Если семафор запускается слишком много раз, то это признак ошибки.
# =====================================================================================================
# Счетчик уменьшается при каждом вызове .acquire() и увеличивается при каждом вызове .release(). Счетчик никогда не может опуститься ниже нуля.
# Если метод .acquire() обнаруживает, что счетчик = 0, то он блокируется, ожидая, пока какой-либо другой поток не вызовет .release().

# Класс BoundedSemaphore() реализует ограниченные объекты семафоров. Ограниченный семафор проверяет, не превышает ли его текущее значение его начальное значение value. Если это так, то возникает исключение ValueError. 


import threading

# обычный семафор
sem = threading.Semaphore(value=1)     # value=1 - внутренний счетчик семафора по умолчанию. Если указать меньше 0 - ValueError.
  
# ограниченный семафор
sem_bound = threading.BoundedSemaphore(value=1)

# =============================================================================

Semaphore.acquire(blocking=True, timeout=None)
# Если при вызове метода счетчик > 0, то уменьшает его на 1 и немедленно возвращает True.
# Если при вызове счетчик = 0, то этот вызов метода блокируется, пока внутренний счетчик не увеличится вызовом .release(). После пробуждения и если счетчик больше 0, то уменьшает его на 1 и возвращает True. Каждым вызовом метода .release() будет разбужен ровно один поток. Не следует полагаться на порядок, в котором пробуждаются потоки.
# При вызове с blocking=False проверяет, если бы вызов без аргументов был бы заблокирован, то немедленно вернет значение False. В противном случае сделает то же самое, что и при вызове без аргументов и вернет значение True.
# При timeout, отличным > 0 будет блокироваться ... секунд. Если получение не завершилось успешно в течение этого интервала, вернет значение False. В противном случае вернет значение True.

Semaphore.release(n=1)
# увеличивает значение семафора
# Если при вызове счетчик = 0 и другие потоки ждали, что он снова станет > 0, то разбудит n из этих потоков.


# =====================================================================================================
# Пример ограничения параллельного доступа к ресурсу более чем одному потоку одновременно, ограничивая при этом общее количество потоков. 
# =====================================================================================================

import threading, random, time

class ActivePool:
    """Воображаемый пул соединений"""

    start = time.time()

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')


def worker(sem, pool):
    with sem:
        th_name = threading.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeActive(th_name)
        time.sleep(0.5)
        pool.makeInactive(th_name)

# семафор максимум на 2 потока
sem = threading.Semaphore(2)

# воображаемый пул соединений
pool = ActivePool()

# запускаем 4 потока
for i in range(4):
    t = threading.Thread(
        target=worker,
        args=(sem, pool),
    )
    t.start()





