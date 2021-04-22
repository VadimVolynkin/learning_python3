https://pythonchik.ru/osnovy/osnovy-oop-v-python-klassy-obekty-metody
"""
dir(a)                          show all methods
type(a)                         узнать класс переменной или значения
isinstance(1+2j, complex)       для проверки принадлежности объекта определённому классу
id(obj)                         адрес объекта в памяти

Встроенные типы данных, такие как кортежи, списки и словари, целиком реализованы на языке C.

Итерируемые типы: множества, списки, кортежи и строки
Изменяемые типы данных: списки, словари, множества, массивы байтов
Неизменяемые типы данных: строки, все числа, кортежи, неизменяемые множества, None, байтовые строки, диапазоны
callable объекты:  callable() - проверяет объект на вызов
1. встроенные функции (len, abs)
2. встроенные методы объектов
3. самописные функции
4. классы
5. экземпляры класса с методом __call__()
6. методы класса
7. функции-генераторы - содержат  yield
"""


# РАЗМЕРЫ ТИПОВ ============================================================

print('int:', int().__sizeof__())         # int: 24 max 9 digits, 32 next
print('float:', float().__sizeof__())     # float: 24 many digits
print('str:', ''.__sizeof__())            # str: 49 + 1 eng, + 2 rus
print('bool:', bool().__sizeof__())       # bool: 24
print('list:', [].__sizeof__())           # list: 40 + 8
print('dict:', {}.__sizeof__())           # dict: 48, 216(max 5 elem), 344(+ 128 next 5), 644 next...
print('set:', set().__sizeof__())         # set: 200 max 4 elem, 712 next...
print('tuple:', tuple().__sizeof__())     # tuple: 24 + 8
print('None:', None.__sizeof__())         # None: 16


# TODO ПРОВЕРКА ВОЗМОЖНОСТИ ПРИВЕДЕНИЯ ТИПОВ ============================================================



### 1. LISTS ============================================================================================
# изменяемый тип данных, упорядочен
# представляет собой список ссылок на объекты
# вес - 40 байт


l = []
"""
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

### 2. TUPLES ============================================================================================
# неизменяемый тип данных
# они упорядочены по позициям
# хранят указатели на другие объекты
# работают быстрее, чем списки
# весят меньше чем списки
# вес - 24 байта
# пустой кортеж - всегда только 1 в памяти(синглтон)
t = (1, )
"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""


### 3. DICTS ============================================================================================
# изменяемый тип данных
# неупорядоченные наборы пар ключ-значение
# объект словаря хранит лишь указатели, а не сами значения
# оптимизированы для извлечения данных по ключу, номеров позиций в словарях нет
# Ключ должен быть объектом неизменяемого типа, то есть строкой, числом или кортежем - должен быть hashable - меть хеш-значение, которое не меняется в течение его жизненного цикла.
# В роли ключей могут выступать любые неизменяемые объекты (числа, строки и кортежи)
# вес - 48 байт

d = {}
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

### 4. SETS ============================================================================================
# изменяемый тип
# неупорядоченная уникализированная последовательность
# нет доступа по индексу
# вес - 200 байт

m = {1, 2, 3}
m2 = set([1,2,3])
"""
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

### 5. STRINGS ============================================================================================
# неизменяемые последовательности символов. Создают новую строку при выполнении методов.
# вес - 49 байт
# Атомарные объект

s = 'hello'

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

### 6. NUMBERS ============================================================================================
# неизменяемый тип
# Атомарные объект
# int     вес - 24 байта
# float   вес - 24 байта
# complex вес - 32 байта


i = 1

"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
"""


f = 1.23

"""
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
"""

### 7. NONE ============================================================================================
# вес - 16 байт
n = None
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


### 8. BOOLEAN =========================================================================================
# вес - 28 байт True, 24 байта- False
b = True
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']










