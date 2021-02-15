"""
позволяя нескольким потокам работать по очереди.
https://docs-python.ru/tutorial/mnogopotochnost-python/

https://docs-python.ru/standart-library/modul-threading-python/

Позволяет одновременно выполнять несколько разделов одной программы.

Потоки независимо планируются, и их выполнение может происходить в течение перекрывающегося периода времени. Однако, в отличие от многопроцессорной обработки, потоки существуют полностью в одном процессе ядра и совместно используют одну выделенную память (heap).

Потоки Python являются параллельными (concurrent) — несколько последовательностей машинного кода выполняются в перекрывающихся временных рамках. Но в реальности они не параллельны — выполнение не происходит одновременно на нескольких физических ядрах.

Основными недостатками потоков Python являются безопасность памяти (memory safety) и состояние гонки (race conditions).

Все дочерние потоки родительского процесса работают в одном и том же пространстве общей памяти. Без дополнительных средств защиты один поток может перезаписать общее значение в памяти, и другие потоки об этом не узнают.
Для обеспечения безопасности потоков в CPython используют GIL — это означает, что в любой момент времени выполняется только один поток.

====================
Питон использует системные нити, которые управляются ОС.

"""

# Как указано в выходных данных, все происходит за один процесс, и объем памяти значительно уменьшается.


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




# TODO ThreadPOOL









