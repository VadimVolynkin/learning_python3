


# ===== создаем сервер для одной общей очереди, к которой могут получить доступ удаленные клиенты ==================
from multiprocessing.managers import BaseManager
from queue import Queue

queue = Queue()                                                    # создаем очередь
class QueueManager(BaseManager): pass                              # создаем свой класс менеджер

QueueManager.register('get_queue', callable=lambda:queue)          # регистрируем в этот класс очередь по идентификатору get_queue
m = QueueManager(address=('', 50000), authkey=b'abracadabra')      # создаем объект менеджера
s = m.get_server()                                                 # получаем объект сервера под управлением менеджера
s.serve_forever()                                                  # запуск сервера до прерывания


# ===== Один клиент может получить доступ к серверу следующим образом ==============================================
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager): pass                              # создаем свой класс менеджер

QueueManager.register('get_queue')
m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra') # создаем объект локального менеджера
m.connect()                                                              # подключаем локальный менеджер к удаленному менеджеру
queue = m.get_queue()                                                    # получаем объект очереди
queue.put('hello')                                                       # кладем в очередь данные


# ===== Другой клиент может получить данные с сервера ==============================================================
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager): pass

QueueManager.register('get_queue')
m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra') # создаем объект локального менеджера
m.connect()                                                              # подключаем локальный менеджер к удаленному менеджеру
queue = m.get_queue()                                                    # получаем объект очереди
queue.get()                                                              # получаем данные из очереди








