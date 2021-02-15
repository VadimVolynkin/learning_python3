"""
Корутины(Сопрограммы) по своей природе это генераторы, которые могут в процессе работы принимать извне какие то данные с помощью метода send().

При первой итерации всегда передается в send(None) или делаем вызов next(gen) - так происходит инициализация генератора.

В корутину можно передать любое исключение g.throw(StopIteration).


"""
# ====== Корутина инициализируется декоратором =====================================================

def coroutine(func):
    """Декоратор инициализирует генератор-корутину в момент создания"""
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)                  # инициализация
        return g                      # вернет проинициализированное
    return inner                      # вызов внутренней функции


# ====== Корутина возвращает сообщение =============================================================

from inspect import getgeneratorstate     # проверят состояние генератора

@coroutine                                # самописный инициализатор корутин. Передает None при создании объекта корутины.
def subgen():
    x = 'Ready to accept message'
    message = yield x                     # yield примет значение, запишет его в message. yield отдаст в консоль x.
    print('Subgen received: ', message)


# g = subgen()
# print(getgeneratorstate(g))        # GEN_CREATED   генератор только что создан
# g.send(None)                       # генератор сначала должен получить None или вызов next(g). yield отдаст x
# print(getgeneratorstate(g))        # GEN_SUSPENDED генератор приостановлен - он принял None и теперь готов принять данные
# g.send('hello world')              # yield примет значение, запишет его в message


# ====== Корутина считает среднее значение =============================================================

class BlaBlaException(Exception):
    pass


def average():
    """Считает среднее значение"""
    count = 0
    summ = 0
    average = None

    while True:                                   # бесконечный цикл
        try:
            x = yield average                     # на каждой итерации отдает в консоль результат
        except StopIteration:
            print('Done')
            break                                 # при исключении выкинет из генератора без отработки else
        except BlaBlaException:
            print('....................')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average                                # возвращает результат при выходе из while через break


g = average()                  # создание генератора
g.send(None)                   # инициализация генератора
g.send(4)
g.send(14)
# g.throw(StopIteration)         # вызываем исключение. Сработает print('Done') + отработает else если нет break + выход из генератора

# делаем исключение и сразу обрабатываем его с выводом результата через e.value
try:
    g.throw(StopIteration)
except StopIteration as e:
    print('Average: ', e.value)  # Done Average:  9.0


