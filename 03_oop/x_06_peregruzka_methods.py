# ================================================================================================================
# ПЕРЕГРУЗКА ОПЕРАТОРОВ КЛАССА
# ================================================================================================================
Перерузка операторов - один из вариантов реализации полиморфизма: мы можем задать свою реализацию метода в собствеенном классе.


# ================================================================================================================
# Пример 1: сложить атрибуты 2-x объектов соответственно
# ================================================================================================================
class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # перегрузка магического метода __add__  определяет как мы будем складывать 2 объекта Coord
    # хотим складывать x с x, y с y
    # метод вернет новый объект этого же класса с результатом операции
    def __add__(self, other):
        if isinstance(other, Coord):      #  является ли второе слагаемое объектом Coord
            return Coord(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Needs Coord obj')

    # вернет этот же объект с результатом операции
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # это мы получим при вызове print(obj)
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    # вернет пару модулей от x и y 
    def __abs__(self):
        return math.hypot(self.x, self.y)

    # если хоть 1 аргумент не 0, то правда
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # вернет новый объект с аргументами с обратным знаком
    def __neg__(self):
        return Coord(-self.x, -self.y)


a = Coord(10, 20)
b = Coord(15, 25)

# получаем новый объект в результате сложения __add__
r = a + b
print(r.x, r.y)           # (25 45)
print(r)                  # (25, 45)

# получаем этот же объект после вычисления __iadd__
a+=b
print(a)                  # (25, 45)

# вернет новый объект с обратным знаком у пары
invert_a = -a
print(invert_a)           # (-25, -45)

# логика
print(bool(a))            # True

# ================================================================================================================
# ПЕРЕГРУЗКА МАГИЧЕСКИХ МЕТОДОВ
# ================================================================================================================
__new__(cls[, ...])              # управляет созданием экземпляра. Возвращает экземпляр класса для передачи в __init__.
__init__(self[, ...])            # конструктор
__del__(self)                    # вызывается при удалении объекта сборщиком мусора


__repr__(self)                   # возвращает "сырые" данные для внутреннего представления в python
__str__(self)                    # вызывается функциями str, print и format. Возвращает строковое представление объекта.

__bytes__(self)                  # вызывается функцией bytes при преобразовании к байтам

__format__(self, format_spec)    # используется функцией format (а также методом format у строк)


__lt__(self, other)              # x < y вызывает x.__lt__(y)
__le__(self, other)              # x ≤ y вызывает x.__le__(y)
__eq__(self, other)              # x == y вызывает x.__eq__(y)
__ne__(self, other)              # x != y вызывает x.__ne__(y)
__gt__(self, other)              # x > y вызывает x.__gt__(y)
__ge__(self, other)              # x ≥ y вызывает x.__ge__(y)

__hash__(self)                   # получение хэш-суммы объекта, например, для добавления в словарь.
__bool__(self)                   # проверка истинности. Если метод не определён, вызывается __len__ (объекты, имеющие ненулевую длину, считаются истинными).


__getattr__(self, name)          # вызывается, когда атрибут экземпляра класса не найден
__setattr__(self, name, value)   # назначение атрибута
__delattr__(self, name)          # удаление атрибута (del obj.name)

__getitem__(self, key)           # доступ по индексу (или ключу)
__setitem__(self, key, value)    # назначение элемента по индексу
__delitem__(self, key)           # удаление элемента по индексу

__call__(self[, args...])        # вызов экземпляра класса как функции

__len__(self)                    # длина объекта

__iter__(self)                   # возвращает итератор для контейнера

__reversed__(self)               # итератор из элементов, следующих в обратном порядке

__contains__(self, item)         # проверка на принадлежность элемента контейнеру (item in self)


# ================================================================================================================
# ПЕРЕГРУЗКА АРИФМЕТИЧЕСКИХ ОПЕРАТОРОВ
# ================================================================================================================
__add__(self, other)              # сложение. x + y вызывает x.__add__(y)
__sub__(self, other)              # вычитание (x - y)

__mul__(self, other)              # умножение (x * y)
__truediv__(self, other)          # деление (x / y)
__floordiv__(self, other)         # целочисленное деление (x // y)
__mod__(self, other)              # остаток от деления (x % y)
__divmod__(self, other)           # частное и остаток (divmod(x, y))
__pow__(self, other[, modulo])    # возведение в степень (x ** y, pow(x, y[, modulo]))

__lshift__(self, other)           # битовый сдвиг влево (x << y)
__rshift__(self, other)           # битовый сдвиг вправо (x >> y)

__and__(self, other)              # битовое И (x & y)
__xor__(self, other)              # битовое ИСКЛЮЧАЮЩЕЕ ИЛИ (x ^ y)
__or__(self, other)               # битовое ИЛИ (x | y)


# ===== Следующие методы делают то же самое, что и арифметические операторы, перечисленные выше, но для аргументов, находящихся справа, и только в случае, если для левого операнда не определён соответствующий метод.
# Например, операция x + y будет сначала пытаться вызвать x.__add__(y), и только в том случае, если это не получилось, будет пытаться вызвать y.__radd__(x).

__radd__(self, other)
__rsub__(self, other)

__rmul__(self, other)
__rtruediv__(self, other)
__rfloordiv__(self, other)
__rmod__(self, other)
__rdivmod__(self, other)
__rpow__(self, other)            

__rlshift__(self, other)             
__rrshift__(self, other)            

__rand__(self, other)             
__rxor__(self, other)             


# ===== Возврат этого же объекта с результатом ===============================================================

__iadd__(self, other)              # +=
__isub__(self, other)              # -=
__imul__(self, other)              # *=

__itruediv__(self, other)          # /=
__ifloordiv__(self, other)         #' //=
__imod__(self, other)              # %=
__ipow__(self, other[, modulo])    # **=

__ilshift__(self, other)           # <<=
__irshift__(self, other)           # >>=

__iand__(self, other)              # &=
__ixor__(self, other)              # ^=
__ior__(self, other)               # |=

__neg__(self)                      # унарный -
__pos__(self)                      # унарный +

__abs__(self)                      # модуль (abs())
__invert__(self)                   # инверсия (~)

__complex__(self)                  # приведение к complex
__int__(self)                      # приведение к int
__float__(self)                    # приведение к float

__round__(self[, n])               # округление

__enter__(self), __exit__(self, exc_type, exc_value, traceback)              # реализация менеджеров контекста





























=======================================================================================================

Python позволяет одному и тому же оператору иметь разные значения в зависимости от контекста ссылки.
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
https://pythononline.ru/osnovy/peregruzka-operatorov-python

# методы и двойные операторы
__add__(self, other)            # +            
__sub__(self, other)            # – 
__mul__(self, other)            # * 
__truediv__(self, other)        # / 
__floordiv__(self, other)       # остаток //
__mod__(self, other)            # % 
__pow__(self, other)            # ** 



class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Need to be int number')

        self.__secs = secs % self.__DAY   # если передано больше суток, покажет остаток


    def getFormatTime(self):
        s = self.__secs % 60               # остаток в секундах
        m = (self.__secs // 60) % 60       # вычисляем кол-во минут и остаток в минутах
        h = (self.__secs // 3600) % 24     # вычисляем часы
        return(f'{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}')

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0' + str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        self.__secs += other.getSeconds()
        return self


    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        return self.__secs == other.getSeconds()


    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Need to be string')

        if item == 'hour':
            return (self.__secs // 3600) % 24

        elif item == 'min':
            return (self.__secs // 60) % 60

        elif item == 'sec':
            return self.__secs % 60

        return 'Wrong key'


    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Need to be string')

        if not isinstance(value, int):
            raise ValueError('Need to be int')

        s = self.__secs % 60               # остаток в секундах
        m = (self.__secs // 60) % 60       # вычисляем кол-во минут и остаток в минутах
        h = (self.__secs // 3600) % 24     # вычисляем часы

        if key == 'hour':
            self.__secs = s + 60 * m + value * 3600
        elif key == 'min':
            self.__secs = s + 60 * value + h * 3600
        elif key == 'sec':
            self.__secs = value + 60 * m + h * 3600




c1 = Clock(8000)
c2 = Clock(200)
c3 = Clock(200)
# c3 += c1 + c2
# print(c2 == c3)

c1['hour'] = 12
print(c1.getFormatTime())
print(c1['hour'], c1['min'], c1['sec'])







