https://docs-python.ru/standart-library/paket-multiprocessing-python/klass-basemanager-modulja-multiprocessing-managers/

# ==============================================================================================
# multiprocessing.managers.BaseManager() удаленный менеджер процессов.
# BaseManager используется для создания нестандартных классов-менеджеров, управляющих пользовательскими объектами. Он создает и запускает сервер диспетчера на одной машине и позволяет клиентам с других машин использовать его ресурсы.
# Менеджер - отдельный процесс, в котором существует объект-сервер к которому другие процессы с помощью прокси-объектов(объектов-клиентов) могут обращаться для получения доступа к общим объектам.
# ==============================================================================================

import multiprocessing.managers

# 1. создаем объект менеджер BaseManager
multiprocessing.managers.BaseManager(
  address,                      # адрес, на котором прослушиваются соединения. Если None, то произвольный.
  authkey                       # ключ аутентификации, для проверки соединений. Если authkey=None, то используется Process.аuthkey, в противном случае используется переданная строка байтов authkey.
  )


# 2. вызываем один из методов ниже
BaseManager.start()             
BaseManager.get_server()


# 3. запускаем сервер менеджера в текущем процессе
Server.serve_forever()

# ===== МЕТОДЫ BaseManager ====================================================================================================

BaseManager.start(initializer, initargs)
# Если initializer не равен None, то запускает дочерний процесс и затем сервер менеджера в этом процессе.

BaseManager.shutdown()
# останавливает процесс, используемый менеджером. Доступен если был вызван BaseManager.start(). Можно вызывать несколько раз.

BaseManager.get_server()
# возвращает объект Server под управлением Manager, который поддерживает Server.serve_forever()

BaseManager.connect()
# подключает локальный менеджер к удаленному менеджеру

BaseManager.register(typeid, callable, proxytype, exposed, method_to_typeid, create_method)
# регистрирует вызываемый объект в менеджере
# typeid - "строка идентификатор типа" для идентификации определенного типа общего объекта.
# callable - вызываемый объект для создания объектов для этого идентификатора типа.
# proxytype - подкласс BaseProxy для создания прокси для общих объектов с идентификатором типа typeid. Если proxytype=None, то прокси-класс создается автоматически.
# exposed указывает последовательность имен методов, к которым прокси-серверы для типа typeid должны иметь доступ с помощью BaseProxy._callmethod(). 
# method_to_typeid - сопоставление (словарь) для указания типа возвращаемого значения тех открытых методов, которые должны возвращать прокси.

BaseManager.address
# возвращает адрес, используемый менеджером для прослушивания соединений.


# ==============================================================================================
# Пример использования удаленного менеджера
# Создадим сервер для одной общей очереди, к которой могут получить доступ удаленные клиенты.
# ==============================================================================================


# ===== 1. создаем сервер и общую очередь ==========================================================================
from multiprocessing.managers import BaseManager
from queue import Queue

queue = Queue()                                                    # создаем очередь
class QueueManager(BaseManager): pass                              # создаем свой класс менеджер

QueueManager.register('get_queue', callable=lambda:queue)          # регистрируем в этот класс очередь по идентификатору get_queue
m = QueueManager(address=('', 50000), authkey=b'abracadabra')      # создаем объект менеджера
s = m.get_server()                                                 # получаем объект сервера под управлением менеджера
s.serve_forever()                                                  # запуск сервера до прерывания


# ===== 2. Один клиент кладет данные в очередь ======================================================================
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager): pass                                    # создаем свой класс менеджер

QueueManager.register('get_queue')                                       # регистрируем вызываемый объект в менеджере
m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra') # создаем объект локального менеджера
m.connect()                                                              # подключаем локальный менеджер к удаленному менеджеру
queue = m.get_queue()                                                    # получаем объект очереди
queue.put('hello')                                                       # кладем в очередь данные


# ===== 3. Другой клиент может получить данные с сервера ============================================================
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager): pass                                    # создаем свой класс менеджер

QueueManager.register('get_queue')                                       # регистрируем вызываемый объект в менеджере
m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra') # создаем объект локального менеджера
m.connect()                                                              # подключаем локальный менеджер к удаленному менеджеру
queue = m.get_queue()                                                    # получаем объект очереди
queue.get()                                                              # получаем данные из очереди



# ===== 4. Локальные процессы тоже могут получить доступ к очереди ==================================================
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager

class Worker(Process):                                                   # создаем с свой класс процесса
    def __init__(self, q):
        self.q = q                                                       # добавляем очередь в конструктор
        super(Worker, self).__init__()
        
    def run(self):                                                       # при вызове run в очередь будем добавлять приветствие
        self.q.put('local hello')

queue = Queue()                                                          # создаем экземпляр очереди
w = Worker(queue)                                                        # создаем процесс с передачей в него очереди
w.start()                                                                # запускаем процесс

class QueueManager(BaseManager): pass                                    # создаем свой класс менеджер

QueueManager.register('get_queue', callable=lambda: queue)               # регистрируем очередь по идентификатору get_queue          
m = QueueManager(address=('', 50000), authkey=b'abracadabra')            # создаем объект менеджера      
s = m.get_server()                                                       # получаем объект сервера под управлением менеджера
s.serve_forever()                                                        # запуск сервера до прерывания










