import multiprocessing

# Очереди позволяют обмениваться данными между процессами.
# В multiprocessing существует 3 вида очередей, построенных на основе обычной многопоточной очереди FIFO queue.Queue
# Все 3 вида очередей могут иметь несколько производителей и потребителей.

# ==============================================================================================
# 1. Методы объекта Queue (очередь FIFO)
# Общая очередь процесса, реализованная с помощью канала и нескольких блокировок/семафоров.
# ==============================================================================================
queue = multiprocessing.Queue([maxsize])


Queue.qsize()
# возвращает примерный размер очереди. вызов метода ненадежен. Нужна небольшая задержка после старта процесса для адекватной оценки

Queue.empty()
# проверяет, что очередь пуста. вызов метода ненадежен

Queue.full()
# проверяет, очередь заполнена. вызов метода ненадежен

Queue.put(obj, block, timeout)
# Ставит элемент в очередь.
# При block=True (по умолчанию) и timeout=None (по умолчанию) блокируется, пока не станет доступен свободный слот.
# Если timeout > 0, то исключение queue.Full, если в течение этого времени не стал доступен свободный слот.
# Если block=False и свободный слот доступен, то поместит элемент в очередь, иначе queue.Full. timeout игнорируется.

Queue.put_nowait(obj)
# эквивалент метода Queue.put(obj, False)

Queue.get(block, timeout)
# удаляет и возвращает элемент из очереди
# Если block=True (по умолчанию) и timeout=None(по умолчанию), то блокируйтся, пока элемент не станет доступным.
# Если timeout > 0, то блокируется не более timeout секунд и поднимает исключение queue.Empty, если ни один элемент не был доступен.
# Если block=False и элемент доступен, то извлечет его, иначе исключение queue.Empty. В этом случае тайм-аут timeout игнорируется.

Queue.get_nowait()
# эквивалент метода Queue.get(False)

Queue.close()
# закрывает очередь. Текущий процесс больше не будет помещать данные в очередь.
# фоновый поток завершиться как только сбросит данные из буфера в очередь
# метод срабатывает автоматически при запуске сборщика мусора.

Queue.join_thread()
# Присоединяется к фоновому потоку.
# Метод можно вызвать только после вызова метода Queue.close()
# Если процесс не является создателем очереди, то при выходе он попытается присоединиться к фоновому потоку очереди

Queue.cancel_join_thread()
# Предотвращает операцию блокировки методом Queue.join_thread().
# Предотвращает автоматическое присоединение фонового потока при выходе из процесса.
# Применяется если нужно срочно завершить процесс не дожидаясь отправки данных в очредь.



# ==============================================================================================
# 2. Методы объекта JoinableQueue
# Наследует все методы Queue + свои методы `.task_done()` и `.join()`.
# ==============================================================================================
queue_join = multiprocessing.JoinableQueue([maxsize])


JoinableQueue.task_done()
# Метод вызывается при каждом извлечении Queue.get() задачи из очереди чтобы сообщить очереди о завершении задачи.

JoinableQueue.join()
# Блокирует, пока все элементы в очереди не будут получены и обработаны. Когда количество незавершенных задач упадет до нуля, метод разблокирует дальнейший ход программы.
# Счетчик задач увеличивается при добавлении задач и уменьшается при извлечении и удалении.


# ==============================================================================================
# 3. Методы объекта SimpleQueue
# Упрощенная очередь, похожа на объект канала `Pipe`, работающий в однонаправленном режиме duplex=False.
# ==============================================================================================
queue_simple = multiprocessing.SimpleQueue()


SimpleQueue.put()
# ставит элемент в очередь

SimpleQueue.get()
# возвращает и удаляет элемент из очереди

SimpleQueue.empty()
# проверяет, что очередь пуста

SimpleQueue.close()
# закрывает очередь  освобождает внутренние ресурсы. Очпредь не может использоваться после вызова этого метода.


####### ПРИМЕР ОЧЕРЕДИ 1 ################################################################################################
import multiprocessing
import time

def summa(q):
    q.put('hello')                                            # ставим объекты ав очередь
    q.put('world')
    q.put('vadim')

if __name__ == "__main__":
    q = multiprocessing.Queue()                               # создаем очередь
    p = multiprocessing.Process(target=summa, args=(q,))      # создаем процесс(функция, очередь)
    p.start()                                                 # стартуем
    time.sleep(0.01)                                          # задержка перед оценкой размера очереди
    print(q.qsize())                                          # 3 размер очереди сейчас
    print(q.get())                                            # берем первый элемент и удаляем его из очереди
    print(q.qsize())                                          # 2 осалось
    p.join()                                                  # ждем завершения всех процессов



####### ПРИМЕР ОЧЕРЕДИ 2 ################################################################################################
# 1. Создаем задачи
# 2. Закидываем их в очередь
# 3. Запускаем процессы

import multiprocessing
import time, random

def worker(input, output):                         # принимает объекты очереди input и output(ниже определены task_queue, done_queue)
    """Функция, выполняемая рабочими процессами"""
    for func, args in iter(input.get, 'STOP'):     # берет кортеж(функция, аргументы) из очереди input или вернет STOP если пусто
        result = calculate(func, args)             # вычисляет результат
        output.put(result)                         # помешает результат в output


def calculate(func, args):                                                   # принимает функцию и аргументы
    """Функция, используемая для вычисления результата"""
    proc_name = multiprocessing.current_process().name                       # получаем имя текущего процесса
    result = func(*args)                                                     # вычисляет результат функции с ее аргументами
    return f'{proc_name}, результат функции {func.__name__}{args} = {result}'# вывод

########################################
# Функции, на которые ссылаются задачи #
########################################
def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b




# создаем главную функцию для запуска всего
def main():
    NUMBER_OF_PROCESSES = 4                                    # сколько хотим процессов
    TASKS1 = [(mul, (i, 7)) for i in range(20)]                # генерим список задач вида кортеж (mul, (i, 7))
    TASKS2 = [(plus, (i, 8)) for i in range(10)]               # генерим список задач вида кортеж (plus, (i, 8))

    # Создание очередей
    task_queue = multiprocessing.Queue()                       # очередь задач для вычисления
    done_queue = multiprocessing.Queue()                       # очередь готовых задач для вывода

    # Заполнение очереди заданий
    for task in TASKS1:
        task_queue.put(task)


    # Запуск рабочих процессов
    for i in range(NUMBER_OF_PROCESSES):
        multiprocessing.Process(target=worker, args=(task_queue, done_queue)).start()

    # Получение и печать результатов
    print('НЕУПОРЯДОЧЕННЫЕ РЕЗУЛЬТАТЫ:\n')
    print('TASKS1:\n')
    for i in range(len(TASKS1)):
        print('\t', done_queue.get())

    # Добавляем больше задач с помощью метода `put()`
    for task in TASKS2:
        task_queue.put(task)

    # Выводим еще несколько результатов
    print('TASKS2:\n')
    for i in range(len(TASKS2)):
        print('\t', done_queue.get())

    # Говорим дочерним процессам остановиться
    print('STOP.')
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')


# запуск всего кода
if __name__ == '__main__':
    main()





