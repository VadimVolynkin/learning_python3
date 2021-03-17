# https://docs-python.ru/standart-library/modul-threading-python/klass-local-modulja-threading/

# =====================================================================================================
# Пример установки локальных данных для потока с помощью threading.local()
# =====================================================================================================
# Локальные данные потока - это данные, значения которых являются специфичными для потока.
# Объект local() может скрывать значения от просмотра в отдельных потоках. Значения экземпляра будут разными для разных потоков - конфликта имен быть не может.

import threading
import random


def show_value(data):
    name_thread = threading.current_thread().name                    # имя потока
    try:                                                             # пробуем получить value установленное в осн. потоке
        val = data.value                                             # если нет такого атрибута(а его в этом потоке еще нет)
    except AttributeError:
        print(f'{name_thread}: Нет локального значения value')
    else:
        print(f'{name_thread}: value={val}')                         # если есть - показываем


def worker(data):
    name_thread = threading.current_thread().name
    show_value(data)                                                 # первый вызов вызовет ошибку и установит значение
    print(f'Установка значения value для потока {name_thread}.')
    data.value = random.randint(1, 100)                              # устанавливаем значение для конкретного потока
    show_value(data)                                                 # второй вызов покажет установленное значение


# создаем хранилище и устанавливаем в него значение аргумента value для основного потока
local_data = threading.local()
local_data.value = 1000


# создаем потоки с передачей объекта local_data
for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()


# вывод значения для основного потока
print('основной поток value', local_data.value)


# =====================================================================================================
# Пример установки общего стартового значения для всех потоков через подкласс threading.local()
# =====================================================================================================

import threading, random

def show_value(data):
    name_thread = threading.current_thread().name                    # имя потока
    try:                                                             # пробуем получить value установленное в осн. потоке
        val = data.value                                             # если нет такого атрибута(а его в этом потоке еще нет)
    except AttributeError:
        print(f'{name_thread}: Нет локального значения value')
    else:
        print(f'{name_thread}: value={val}')                         # если есть - показываем

def worker(data):
    name_thread = threading.current_thread().name
    show_value(data)                                                 # первый вызов вызовет ошибку и установит значение
    print(f'Установка значения value для потока {name_thread}.')
    data.value = random.randint(1, 100)                              # устанавливаем значение для конкретного потока
    show_value(data)                                                 # второй вызов покажет установленное значение


class MyLocal(threading.local):
    # переопределяем конструктор класса
    def __init__(self, value):
        super().__init__()                                           # сначала вызывается конструктор базового класса
        self.value = value                                           # установка стартового значения атрибута value
        self.name = threading.current_thread().name                  # установка имени текущего потока 
        print(f'{self.name} стартовое значение {self.value}')


# создаем локаьлное хранилище в основном потоке
local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()






