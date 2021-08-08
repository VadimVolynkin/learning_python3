"""Здесь можно писать комментарии к модулю, что он делает.

Первая строка - заголовок. Должен быть коротким с точкой в конце, может начинаться сразу после кавычек.
После него обыно идет пустая строка. За ней короткое описание, как в этом блоке строк.
Затем пустая строка и полное описание.

Максимальная длина строки
Ограничьте длину строки максимум 79 символами, строки документации 72 символа.
Нормально увеличение длины строки с 80 до 100 символов, если строки документации все еще будут 72 символа.

Отступы в коде
Используйте 4 пробела на каждый уровень отступа.

Закрывающие кавычки должны быть на отдельной строке.
"""

# __future__ всегда вверху после комментариев к модулю
from __future__ import barry_as_FLUFL

# dunders должны быть перед импортами
__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'


# ===== ИМПОРТЫ ПО PEP8
# Имена модулей: module.py, my_module.py. Важно использовать достаточно короткие имена модулей.
# Имена пакетов: package, mypackage. Не рекомендуется использовать символ подчёркивания.
# каждый на своей строке
# Импорты всегда помещаются в начале файла после комментариев к модулю и строк документации, и перед объявлением констант.
# Порядок групп импортов, вставляйте пустую строку между каждой группой импортов.
# 1.импорты из стандартной библиотеки
# 2.импорты сторонних библиотек
# 3.импорты модулей текущего проекта

import os
import sys
from datetime import datetime

import pytz

from myclass import MyClass
from foo.bar.yourclass import YourClass


# ===== КОНСТАНТЫ ПО PEP8
# Имена констант: CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT, _CONST_NOT_FOR_IMPORT

SSL_PORT = 443          # комментарий может быть справа или сверху
HOST = 'localhost'

# переменная с подчеркиванем - не для импорта
_DAYS_IN_MONTH =[-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# ===== ПОСЛЕДОВАТЕЛЬНОСТИ ПО PEP8
# закрывающая скобка на новой строке

my_list = [
    1, 2, 3,
    4, 5, 6,
]

# ===== ФУНКЦИИ ПО PEP8
# Имена функций: function, my_function
# Перменные: x, var, my_variable
# Функции отделяются 2 пустыми строками. Для разделения групп похожих функций можно использовать дополнительные строки.
# Логические разделы внутри функции разделяются пустой строкой
# Логические разделы могут иметь комментарии

def top_level_function():
    """Правильный многострочный комментарий.

    Пояснения к аргументам:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    Закрывающие кавычки находятся на новой строке.
    """

    # Без отступов
    if (this_is_one_thing and
        that_is_another_thing):
        do_something()

    # Без отступов и с комментарием для различения
    if (this_is_one_thing and
        that_is_another_thing):
        # Комментарий для отеделения от тела.
        do_something()

    # С дополнительным отступом
    if (this_is_one_thing
            and that_is_another_thing):
        do_something()


# Выровнено по открывающему разделителю
def long_function_name(var_one, var_two,
                    var_three, var_four):
     """Короткий комментарий в 1 сроку."""

    return var_one 


# Перевод на новую строку с дополнительными пробелами
# для визуального отделения переменных от названия функции
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    # code
    pass

# выызов функции с выравниванием по открываюзему разделителю
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# вызов функции с висячими строками и отступом
# можно использовать только в вызывах функций
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


# длинный код удобно переносить внутри скобок с операндом вначале
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


# для переноса длинных строк можно использовать обратный слеш
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())


# ===== КЛАССЫ ПО PEP8
# Имена классов: Model, MyClass
# Имена методов: class_method, method
# Методы в классах отделяются пустой строкой
# Методы могут иметь комментарии
# Логические разделы внутри методов разделяются пустой строкой
# Логические разделы могут иметь комментарии

class FooBar:
    
    # сеттер имени
    def set_name(self, name):
        self.name = name

    # сеттер возраста
    def set_age(self, age):
        self.age = age








