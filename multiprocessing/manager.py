https://docs-python.ru/standart-library/paket-multiprocessing-python/klass-manager-modulja-multiprocessing/
https://docs-python.ru/standart-library/paket-multiprocessing-python/proksi-obekty-menedzhera-modulja-multiprocessing/

# ==============================================================================================
# multiprocessing.Manager()
# создает данные для общего использования разными процессами
# ==============================================================================================

import multiprocessing

proxy = multiprocessing.Manager()  
# запущенный объект SyncManager для общего использования объектов между процессами. 
# Объект-менеджер SyncManager представляет собой подкласс BaseManager для синхронизации процессов. 
# Объект-менеджер SyncManager управляет серверным процессом, который управляет общими объектами. Другие процессы могут получить доступ к общим объектам с помощью прокси.

# ======================================================================

Методы объект-менеджера SyncManager создают и возвращают прокси-объекты для ряда часто используемых типов данных, которые должны быть синхронизированы между процессами. Эти типы, в частности, включают в себя обычные списки и словари Python.



SyncManager.Barrier(parties, action, timeout)
# возвращает прокси для threading.Barrier

SyncManager.BoundedSemaphore(value)
# возвращает прокси для threading.BoundedSemaphore

SyncManager.Condition(lock)
# возвращает прокси для threading.Condition

SyncManager.Event()
# возвращает прокси для threading.Event

SyncManager.Lock()
# возвращает прокси для threading.Lock

SyncManager.RLock()
# возвращает прокси для threading.RLock

SyncManager.Semaphore(value)
# возвращает прокси для threading.Semaphore

SyncManager.Queue(maxsize)
# возвращает прокси для queue.Queue

SyncManager.Array(typecode, sequence)
# возвращает прокси для multiprocessing.Array

SyncManager.Value(typecode, value)
# возвращает прокси для multiprocessing.Value

SyncManager.Namespace()
# возвращает прокси для Namespace

SyncManager.dict()
SyncManager.dict(mapping)
SyncManager.dict(sequence)
# возвращает прокси обычного словаря Python

SyncManager.list()
SyncManager.list(sequence)
# возвращает прокси для обычного списка Python



























