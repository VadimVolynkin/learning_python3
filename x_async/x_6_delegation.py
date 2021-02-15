"""
Делегирующий генератор - генератор который вызывает другой генератор и получает его значение через return.
Подгенератор - вызываемый генератор. Должен содержать механизм завершения его
Такая конструкция позволяет разбить 1 генератор на несколько.

Конструкция yield from:
- осуществляет передачу данных и исключений. Вызывающий код напрямую управляет работой подгенератора. Пока подгенератор работает, делегирующий генератор остается заблокированным(выполняет await), ждет пока подгенератор закончит работу. yield from тоже самое что и await в других язках.
- принимает результат из любого итерируемого объекта
- возврат return из подгенератора
- содержит инициализацию подгенератора - декоратор @coroutine на нем не нужен
"""

def coroutine(func):
    """Декоратор для инициализации генератора-корутины при создании объекта"""
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    """
    Подгенератор:
    1. принимает и обрабатывает данные и исключения
    2. может что то возвращать через return
    3. должен содержать механизм завершающий его работу через break
    """
    while True:
        try:
            message = yield
        except StopIteration:
            print('bla-bla from subgen!!!')
            break                   # подгенератор должен содержать механизм завершающий его работу
        else:
            print('message from subgen', message)

    return 'Returned from subgen.'



# ===== ПРОБРОС ДАННЫХ И ИСКЛЮЧЕНИЙ ИЗ ДЕЛЕГАТОРА В ПОДГЕНЕРАТОР ============================================

@coroutine
def deligator(g):
    """
    Делегирующий генератор:
    1. принимает подгенератор и вызывает его
    2. принимает данные и перебрасывает в подгенератор через g.send(data)
    3. перехватывает исключение, сохраняет в переменную и перебрасывает его в подгенератор через g.throw(SomeException)
    4. получает то значение, которое возвращает подгенератор через return
    """
    # while True:
    #     try:
    #         data = yield              # делегирующий генератор перехватывает отсылаемые через send() данные
    #         g.send(data)              # переброска данных в подгенератор
    #     except BlaBlaException as e:  # сохраняем перехваченное исключение в переменную
    #         g.throw(e)                # переброска исключения в подгенератор

    # Конструкция yield from заменяет весь цикл выше:
    # - передачу данных и исключений
    # - возврат return из подгенератора
    # - содержит инициализацию подгенератора - декоратор @coroutine на нем не нужен
    result = yield from g
    print(result)


# создание подгенератора и делегирующего генератора
sg = subgen()              # создаем подгенератор
g = deligator(sg)          # передаем его в делигатор

# передаем в делигатор данные с пробросом в подгенератор
g.send('Hello')            # message from subgen Hello

# передаем в делигатор исключение с пробросом в подгенератор
g.throw(StopIteration)     # bla-bla from subgen!!!



# ===== ВОЗВРАТ ЗНАЧЕНИЯ ЧЕРЕЗ yield from =================================================
def a():
    yield from 'vadim'     # yield from принимает результат из любого итерируемого объекта

g = a()
print(next(g))             # v
print(next(g))             # a


