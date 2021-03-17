
# https://docs-python.ru/tutorial/mnogopotochnost-python/
# https://docs-python.ru/standart-library/modul-threading-python/


# ===== Мультипоточность =========================================================================================
# Мультипоточность нужно использовать там, где не очень много задач i/o и они отвечают быстро, поэтому нет необходимости использовать асинхронность.
# ================================================================================================================

"""
===== Процесс
Запущенная программа, которая выполняет свои вычисления или ждет данные извне. 

===== Потоки
Составляющие процесса. Каждый процесс имеет минимум один поток(основной), может иметь дочерние - это уже многопоточность.
Много потоков позволяют распараллеливать выполнение одной прораммы на несколько подзадач. 
Потоки независимо планируются, и их выполнение может происходить в течение перекрывающегося периода времени(concurrent), но в реальности они не параллельны - они работают последовательно по очереди.
Питон использует системные потоки, которые управляются ОС.

Основными недостатками потоков Python являются безопасность памяти (memory safety) и состояние гонки (race conditions).
В отличие от многопроцессорной обработки, все потоки одного процесса ядра используют одну выделенную память (heap).
Без дополнительных средств защиты один поток может перезаписать общее значение в памяти, и другие потоки об этом не узнают.
Для обеспечения безопасности потоков в CPython используют GIL — это означает, что в любой момент времени выполняется только один поток на одном ядре. Остальные ядра заблокированы.

Логические ядра процессора(HyperThreding Intel) - потоки. Каждое физическое ядро имеет 2 гипертреда. Технология дает возможность докинуть к основному потоку дополнительный для более эффективной утилизации ядра. В питоне это невозможно реализовать из-за GIL. В моменте можно выполнить только 1 поток на 1 ядре. Остальные потокии ждут своей очереди.

===== Блокировки(события)
Нужны для того чтобы заблокировать поток1 ожидающий событий, которые должны быть вызванны в потоке2.

Например задача:
1. проверить есть ли элемент в массиве
2. добавить если его нет
Эта задача должна быть атомарной. Другие потоке не должны влезать в промежуток между этими операциями.
"""

from threading import Thread
import os, time, datetime, random, tracemalloc


tracemalloc.start()
children = 4    # number of child threads to spawn
maxdelay = 6    # maximum delay in seconds


def status():
    return ('Time: ' +
        str(datetime.datetime.now().time()) +
        '\t Malloc, Peak: ' +
        str(tracemalloc.get_traced_memory()))


def child(num):
    delay = random.randrange(maxdelay)
    print(f"{status()}\t\tProcess {num}, PID: {os.getpid()}, Delay: {delay} seconds...")
    time.sleep(delay)
    print(f"{status()}\t\tProcess {num}: Done.")


if __name__ == '__main__':
    print(f"Parent PID: {os.getpid()}")
    for i in range(children):
        thr = Thread(target=child, args=(i,))
        thr.start()



# Все описанные методы классов модуля threading выполняются атомарно.

threading.enumerate()
# список объектов threading.Thread() всех живых потоков.
# в список входят демонические потоки и объекты фиктивного потока + основной поток. 
# в этот список не входят завершенные потоки и потоки, которые еще не были запущены.

threading.active_count()
# количество живых потоков = длине списка, возвращаемого функцией threading.enumerate().

threading.current_thread()
# текущий поток - объект threading.Thread(), соответствующий потоку управления вызывающего объекта

threading.main_thread()
# объект основного потока - обычно это поток, из которого был запущен интерпретатор Python.

threading.excepthook(args, /)
# обрабатывает неперехваченные исключения в потоках, вызванные в методе Thread.run().
# args может содержать:
    # exc_type - тип исключения, выводится в sys.stderr
    # exc_value - значение исключения, может быть None.
    # exc_traceback: Трассировка исключения, может быть None.
    # thread: Поток, который вызвал исключение, может быть None.


threading.get_ident()
# идентификатор текущего потока для использования в качестве "волшебного" файла cookie, например для индексации словаря данных, специфичных для потока. 

threading.get_native_id()
# интегральный идентификатор текущего потока для уникальной идентификации в масштабах всей системы до тех пор, пока поток не завершится.

threading.TIMEOUT_MAX
# максимально значение для тайм-аута блокировки (Lock.acquire(), RLock.acquire(), Condition.wait(), и т. д.), превышение вызовет OverflowError.


# ================================================================================================================
# Контекстный менеджер with
# ================================================================================================================

# метод .acquire() будет вызываться при входе в блок with, а метод .release() будет вызываться при выходе из блока with.
with some_lock:
    # do something...


# то же самое без with
some_lock.acquire()        # ставим блокировку
try:
    # do something...
finally:
    some_lock.release()    # снимаем блокировку


# ================================================================================================================
# Трассировка и профилирование потоков модулем threading
# ================================================================================================================

threading.settrace(func)
# устанавливает функцию трассировки для всех потоков, запущенных из модуля threading.
# функция будет передана в sys.settrace() для каждого потока перед вызовом его метода Thread.run().


threading.setprofile(func)
# устанавливает функцию профилирования для всех потоков, запущенных из модуля threading.
# функция будет передана в sys.setprofile() для каждого потока перед вызовом его метода Thread.run().


threading.stack_size(size)
# возвращает размер стека, используемый при создании новых потоков.
# Необязательный аргумент size - размер стека, который будет использоваться для создаваемых впоследствии потоков. По умолчанию = 0 при использовании настроек платформы или > 32768(32 кб). Если указанный размер стека недействителен - ValueError.
# Если изменение размера стека потока не поддерживается, возникает ошибка RuntimeError.


# ================================================================================================================
# Обработка исключений в threading
# ================================================================================================================
# Потоки нельзя перезапускать, поэтому в случае падения потока, это может нарушить работу всей программы. Чтобы избежать, рабочий код в потоке нужно писать в блоке try.







