
def func():
    pass

print(func.__dict__)
print(dir(func))

['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# === РЕКУРСИВНЫЕ ФУНКЦИИ ========================================================================
Рекурсивная функция вызывает сама себя.


# === MAP =============================================================================
Позволяет преобразовывать элементы итерируемого объекта в соответствии с некоторой указанной функцией: map(func, *iterables).
lst = [1,-2,3,-4,-5]
def sq(x):
    return x**2

b = map(sq, lst)
b = (sq(x) for x in lst)           # эквивалент

print(next(b))
print(b)                           # <map object at 0x7faf12eee100>
a = list(b)                        # make list

b = map(lambda x: x[::-1], lst)    # получим строки наоборот


# === FILTER =============================================================================
Возвращает элементы, для которых, переданная ей функция возвращает True: filter(func, *iterables)
a=[1,2,3,4,5,6,7,8,9,10]

def odd(x):
    return x%2

b = filter(odd, a)
b = filter(lambda x: x%2, a)       # эквивалент

print(next(b))
print(b)                           # <filter object at 0x7fac7762cf10>
c = list(b)                        # make list



# === ZIP =============================================================================
Позволяет объединять между собой элементы упорядоченных коллекций по индексам в кортежи.
zip формирует выходной список, длина которого равна длине наименьшей из указанных коллекций.

a = [1,2,3,4]
b = [5,6,7,8]

it = zip(a, b)

print(next(b))
print(it)                          # <zip object at 0x7fa4fd575540>
print(list(it))                    # make list [(1, 5), (2, 6), (3, 7), (4, 8)]


# === REDUCE =============================================================================




# === SORT =============================================================================
List имеет встроенный метод sort, который меняет его состояние и расставляет элементы по возрастанию:

a=[1,-45,3,2,100,-4]
a.sort()



# === SORTED =============================================================================
Функция применяется для кортежей и строк.
На выходе всегда будем получать новый список отсортированных данных, исходник не меняется.
Именованный параметр key принимает ссылку на сортирующую функцию.

a=(1,-45,3,2,100,-4)

b = sorted(a)

def funcSort(x):
    if x%2 == 0:
        return x
    else:
        return x+100

print(sorted(a, key=funcSort))
print(sorted(a, key=lambda x: x%2))


# === ENUMERATE =============================================================================
enumerate(sequence, start=0) первым параметром - любой итерируемый объект), start – начальное значение индекса, а при переборе элементов она выдает кортеж из двух значений: (индекс, значение элемента.)
a = [1, 4, 2, -5, 0, 11]

for e in enumerate(a):
    print(e)

print(a)

g = enumerate(a)          # <enumerate object at 0x01B5F628>
print(next(g))


# TODO LAMBDA =============================================================================
# === РЕКУРСИВНЫЕ ФУНКЦИИ ================================================================

30 встроенных функций https://pythonru.com/osnovy/vstroennye-funkcii-python

Декораторы функций и замыкания


сравнить с генераторами и функциями по timeit
http://pythonicway.com/python-functinal-programming


функция сначала пытается найти нужную переменную внутри собственной области видимости, и если не находит, то переходит на более высокий уровень, в данном случае – глобальной области.

func.__dict__

"""
=== Генератор ==========================================================================
Генератор – это функция, которая воспроизводит последовательность значений и может использоваться
при выполнении итераций.
Слово yield объявляет объект-генератор.
Объект-генератор выполняет функцию, когда вызывается метод __next__(). Метод работает пока не будет
встречена инструкция yield, которая остановит выполнение и вернет результат
"""
def foo(x):
    while 1:
        print(x)
        yield x
        x += 1

c = foo(5)
c.__next__()
c.__next__()








