# https://docs-python.ru/standart-library/modul-threading-python/klass-thread-modulja-threading/

# ==============================================================================================
# Методы объекта Thread
# Объект Thread() запускает вызываемый объект target на исполнение в отдельном потоке.
# ==============================================================================================
import threading

th = threading.Thread(
    group=None,    # зарезервировано для реализации класса ThreadGroup.
    target=None,   # вызываемый методом Thread.run() объект (функция).
    name=None,     # имя потока. По умолчанию "Thread-N"
    args=(),       # кортеж аргументов для вызываемого объекта target
    kwargs={},     # словарь для вызываемого объекта target
    *,
    daemon=None    # является ли поток демоническим
  )

"""
Существует 2 способа запустить действие:
- Передать вызываемый объект (функцию) target в конструктор.
- Переопределить метод  Thread.run() или __init__() в подклассе. Другие методы переопределять нельзя.


Объекты фиктивного потока - чужеродные потоки - потоки управления, запускаемые вне модуля потоковой передачи, например из кода языка C. Они всегда считаются живыми и демоническими и не могут быть объединены методом Thread.join() и никогда не удаляются.
"""

Thread.start()
# запускает экземпляр Thread путем вызыва метода Thread.run() в отдельном потоке управления.

Thread.run()
# вызывает вызываемый объект (функцию) target с args и kwargs.

Thread.join(timeout=None)
# блокирует вызывающий поток до тех пор, пока не завершится поток, чей метод .join() вызван.
# при timeout=None операция будет заблокирована до завершения потока.
# Thread.join() вызывает RuntimeError при попытке присоединиться к текущему потоку (самому к себе) или до запуска Thread.start()

Thread.name
# имя потока - строка. Несколько потоков могут иметь одно и то же имя.

Thread.ident
# идентификатор потока или None, если поток не был запущен

Thread.native_id
# интегральный идентификатор потока(TID), присвоенный ОС (ядром) для идентификации в масштабах всей системы до завершения потока.

Thread.is_alive()
# является ли поток живым

Thread.daemon
# является ли поток демоническим - бесконечный цикл. Атрибут Thread.daemon должен быть установлен до вызова Thread.start(), иначе RuntimeError. 
# Начальное значение наследуется от родителя. Основной поток не является потоком демона и поэтому все потоки, созданные в основном потоке, по умолчанию daemon = False.
# Вся программа Python завершается, когда не остается живых потоков, не являющихся демонами.
# Для корректного завершения демонического потока нужно указывать True, иначе придется выполнять kill -s KILL 7689  консоле



Thread.isDaemon()
# старый API для атрибута daemon

Thread.setDaemon()
# старый API для атрибута daemon

Thread.getName()
# старый API getter для атрибута name

Thread.setName()
# старый API setter для атрибута name


# =====================================================================================================
# Пример основными методами библиотеки и методами потока Thread
# =====================================================================================================

import threading
import time

print('------------ TIMEOUT_MAX -------------------')
print(threading.TIMEOUT_MAX)                  # 9223372036.0 by default
threading.TIMEOUT_MAX = 10                    # set timeout
print(threading.TIMEOUT_MAX)                  # 10


print('------------ MAIN THREAD INFO --------------')
main_thread = threading.main_thread()
print(main_thread)                            # <_MainThread(MainThread, started 140238253035648)>
print(threading.get_ident())                  # 140238253035648
print(threading.get_native_id())              # 27250
print(threading.current_thread())             # <_MainThread(MainThread, started 140238253035648)>
print(threading.current_thread().name)        # MainThread



def say_hello():
    print('wait 5 sec...')
    print(threading.get_ident())              # 140238229350144
    print(threading.get_native_id())          # 27885
    print(threading.current_thread())         # <Thread(Thread-1, started 140238229350144)>
    print(threading.current_thread().name)    # Thread-1
    time.sleep(5)
    print('hello')

print('------------ CHILD THREAD_1 INFO -----------')
th1 = threading.Thread(target=say_hello)      # create thread
print('alive before start: ', th1.is_alive()) # False
th1.start()                                   # start thread
print('alive after start: ', th1.is_alive())  # True
print('daemon : ', th1.daemon)                # False
print('th1 name is : ', th1.name)             # Thread-1
print('active ths : ', threading.active_count())# 2
th1.join()                                    # blocks main thread


print('------------ LIST ALIVE THREADS -----------')
list_alive_threads = threading.enumerate()          
print(list_alive_threads)  # [<_MainThread(MainThread, started 140238253035648)>, <Thread(Thread-1, started 140238229350144)>]


# =====================================================================================================
# Пример создания потокового класса и потокового объекта
# Такой объект при создании создает свой поток выполнения.
# =====================================================================================================
import threading, time

class MyThread(threading.Thread):

    def __init__(self, pause, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.pause = pause


    def run(self, *args, **kwargs):
        print('Thread was started!')
        super(MyThread, self).run(*args, **kwargs)
        print('Thread was finished!')


def sleep(pause):
    print('I want to sleep {} sec'.format(pause))
    time.sleep(pause)

# создаем потоковый объект и запускаем
t = MyThread(pause=3, target=sleep, args=(3,))
t.start()












