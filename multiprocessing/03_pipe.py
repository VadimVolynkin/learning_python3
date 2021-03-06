# https://docs-python.ru/standart-library/paket-multiprocessing-python/klass-pipe-modulja-multiprocessing/

# ==============================================================================================
# Методы объекта Pipe
# Обмен данными между процессами при помощи канала
# ==============================================================================================


import multiprocessing


pipe = multiprocessing.Pipe([duplex])
# вернет кортеж из объктов Connection (conn1, conn2) - 2 конца одного канала
# Объкты Connection позволяют получать picklable объекты или текстовые или байтовые строки. Работают как сокеты для сообщений.
# duplex=True (по умолчанию) - канал является двунаправленным. 
# duplex=False однонаправленным conn1 - для приема, conn2 - для отправки)


Connection.send(obj)
# отправляет объект упакованный picklable на другой конец соединения, там его можно прочитать с помощью .recv()

Connection.recv()
# возвращает объект, отправленный с другого конца соединения. Блокируется до тех пор, пока есть что получить. 

Connection.fileno()
# возвращает файловый дескриптор соединения

Connection.close()
# закрывает соединение, вызывается автоматически при сборке мусора.

Connection.poll(timeout)
# возвращает, если есть какие-либо данные.
# Если timeout не указан, то возвращает результат немедленно. 
# timeout - максимальное время блокировки в секундах.
# Если timeout=None, то бесконечно ждет пока не поступят данные.

Connection.send_bytes(buffer, offset, size)
# отправляет байтовые данные из байтового объекта
# Если задано смещение offset, то данные считываются из этой позиции в буфере buffer.
# Блокируется до тех пор, пока есть что получить. 

Connection.recv_bytes(maxlength)
# возвращает полное сообщение байтовых данных с другого конца соединения в виде строки.
# Если сообщение длиннее maxlength, то ошибка OSError, а соединение больше не будет читаться.

Connection.recv_bytes_into(buffer, offset)
# читает в буфер полное сообщение байтовых данных с другого конца соединения и возвращает количество байтов в сообщении. 
# Блокируется, пока есть что получить. Поднимает EOFError, если больше нечего получить, а другой конец был закрыт.
# Если задано смещение offset, то сообщение будет записано в буфер с этой позиции.



# ==============================================================================================
# Пример работы с Pipe
# ==============================================================================================

from multiprocessing import Pipe

# создание канала(вернет кортеж - 2 конца канала)
a, b = Pipe()

# a отправлякет, b принимает
a.send([1, 'hello', None])
b.recv()                   # [1, 'hello', None]

# b отправлякет, a принимает
b.send_bytes(b'thank you')
a.recv_bytes()             # b'thank you'

# ==================================================
import array


arr1 = array.array('i', range(5))
arr2 = array.array('i', [0] * 10)
print(arr1)                                  # array('i', [0, 1, 2, 3, 4])
print(arr2)                                  # array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


a.send_bytes(arr1)                           # а отправляет байты
count = b.recv_bytes_into(arr2)              # b считает количество байтов в сообщении
print(count)                                 # 20

assert count == len(arr1) * arr1.itemsize
arr2                                         # array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])















