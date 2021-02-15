"""
https://docs-python.ru/tutorial/mnogopotochnost-python/
Параллелизм -способнось  делать сразу несколько вычислений, используя несколько ядер процессора.

Используйте модуль multiprocessing для решения проблем, связанных с операциями ЦП. Этот модуль использует весь потенциал всех ядер в процессоре.

Инструкции выполняются параллельно на нескольких процессорах(ядрах)
Каждый процесс имеет свой независимый кусок памяти(heap).

"""
from multiprocessing import Process
import os, time, datetime, random, tracemalloc


tracemalloc.start()
children = 4    # number of child processes to spawn
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
        proc = Process(target=child, args=(i,))
        proc.start()



















