# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
# https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/

# ================================================================================================================
# STRINGS
# ================================================================================================================
# Неизменяемые последовательности символов. Создают новую строку при выполнении методов.
# доступны индексы и срезы
# вес - 49 байт
# Атомарные объект(присваивается значение, а не ссылка на объект)
# интернирование - одинаковые строки могут храниться как 1 объект
# В Python 3 строки str состоят из символов Юникода utf-8. Каждому символу Юникода присвоен свой кодовый пункт, который может быть записан как U+XXXX, где XXXX – последовательность из четырех или более шестнадцатеричных цифр.
# str может содержать любые символы Юникода. Символы Юникода могут занимать от одного до четырёх байт. 
# bytes представляет двоичные данные, последовательность байт, без указания на кодировку.

print('str:', ''.__sizeof__())            # str: 49 байт пустая строка
print('str:', 'hello'.__sizeof__())       # str: 49 + 1 байт за каждый символ на англ
print('str:', 'ж'.__sizeof__())           # str: 78 + 2 байта за каждый символ на русском

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

# ===== МЕТОДЫ СТРОК =======================================================================

s = 'hello world From PYTHON'
p = '  hello world From PYTHON  '
n = 'hello world\nFrom PYTHON'
tab = '\thello world From PYTHON'
l = ['hello', 'world', 'From', 'PYTHON']
sp = ' '

i = '45'
f = '5.45'

iden = 'MyClass'
rus = 'привет'

upper = 'UPPER UPPER'
lower = 'lower lower'
title = 'Title Title'


# === ИЗМЕНЕНИЕ РЕГИСТРА
x = s.title()                  # Hello World From Python перевод первой буквы всех слов в верхний регистр, остальных – в нижний
x = s.capitalize()             # Hello world from python перевод первой буквы в верхний регистр, остальных – в нижний
x = s.upper()                  # HELLO WORLD FROM PYTHON перевод всех символов в верхний регистр
x = s.lower()                  # hello world from python перевод всех символов в нижний регистр
x = s.casefold()               # hello world from python перевод всех символов в нижний регистр агрессивно
x = s.swapcase()               # HELLO WORLD fROM python меняет регистр символов на обратный

# === УДАЛЕНИЕ И ДОБАВЛЕНИЕ СИМВОЛОВ, ЗАМЕНА
x = p.lstrip()                 # hello world From PYTHON  убирает пробелы только слева
x = p.rstrip()                 #   hello world From PYTHON убирает пробелы только справа
x = s.strip()                  # hello world From PYTHON убирает пробелы слева и справа

x = s.center(35, '=')          # ======hello world From PYTHON====== по центру(нужная длина, символ заполнения)
x = s.ljust(30, '=')           # hello world From PYTHON======= добавит справа(нужная длина, символ заполнения)
x = s.ljust(len(s)+7, '=')     # hello world From PYTHON======= добавит 7 справа
x = s.rjust(30, '=')           # =======hello world From PYTHON добавит слева(нужная длина, символ заполнения)

x = i.zfill(5)                 # 00045 начало строки будет заполнено цифрой ASCII 0, до указанной длины

x = tab.expandtabs(tabsize=8)  #          hello world From PYTHON заменяет табуляцию \t проблеами

x = s.replace('world', 'Vadim', 1)  # hello Vadim From PYTHON (старое, новое, число замен)

tt = {'h': 'r', 'w': 'A'}
tbl = s.maketrans(tt)               # {104: 'r', 119: 'A'} создает таблицу преобразования символов для метода str.translate()
x = s.translate(tbl)                # rello Aorld From PYTHON транслирование строки в соответствии с таблицой

tbl = s.maketrans('hw', 'rA', 'PN') # rello Aorld From YTHO оздает таблицу замены(что меняем, на что, что исключить)
x = s.translate(tbl)

x = '{0}, {1}, {2}'.format('a', 'b', 'c')      # 'a, b, c'   str.format(*args, **kwargs)
x = '{}, {}, {}'.format('a', 'b', 'c')         # 'a, b, c'
x = '{2}, {1}, {0}'.format(*'abc')             # 'c, b, a'
x = '{name}, {age}'.format(name='Tom', age=33) # Tom, 33
x = '{:^30}'.format('centered')                # '           centered           '
str.format_map(mapping)                        # mapping - подкласс словаря dict, аналог format()

x = s.encode("utf-8", "strict")                # b'hello world From PYTHON' байтовая версия строки

# === РАЗДЕЛЕНИЕ И ОБЪЕДИНЕНИЕ СТРОК
x = s.split('')                     # ['hello', 'world', 'From', 'PYTHON'] разбивает строку на подстроки пробелом
x = s.split('o')                    # ['hell', ' w', 'rld Fr', 'm PYTHON'] разделителем 'o'

x = ' '.join(l)                     # hello world From PYTHON соединит в строку через пробел

x = s.rsplit(sep=None, maxsplit=-1) # ['hello', 'world', 'From', 'PYTHON'] разделение справа по пробелу безлимитно
x = s.rsplit(sep=None, maxsplit=1)  # ['hello world From', 'PYTHON'] максимум 1 разделение
x = s.rsplit(sep='l', maxsplit=1)   # ['hello wor', 'd From PYTHON']  разделитель 'l' только 1 раз

x = n.splitlines()                  # ['hello world', 'From PYTHON']делит текст по символу '\n'
x = n.splitlines(True)              # ['hello world\n', 'From PYTHON'] если True - разрывы строк не будут вырезаться

x = s.partition('l')                # ('he', 'l', 'lo world From PYTHON') делит по первому разделителю слева (до, разд, после)
x = s.rpartition('l')               # ('hello wor', 'l', 'd From PYTHON') делит по первому разделителю справа (до, разд, после)

x = s.find('o', 2, 20)              # 4 наименьший индекс совпадения слева (искать, начало, конец)
x = s.rfind('o', 2, 20)             # 14 наименьший индекс совпадения справа (искать, начало, конец)

x = s.index('wor', 2, 20)           # 6 индекс первого совпадения начала подстроки начиная слева
x = s.rindex('wor', 2, 20)          # 6 индекс первого совпадения начала подстроки начиная справа

x = s.count('l', 0, 5)              # 2 считает количество 'l' с 0 по 5 символ
x =  len(s)                         # 23 считает количество символовв строке

x = s.startswith('hell', 0, 20)     # True строка начинается с (строка, начало, конец)
x = s.startswith('world', 6, 20)    # True строка начинается с (строка, начало, конец)
x = s.endswith('PYTHON', 6, 23)     # True строка заканчивается на (строка, начало, конец)

# === ПРОВЕРКА СТРОК
x = i.isalnum()                   # True состоит из цифр и/или букв
x = i.isdecimal()                 # True является десятичным
x = f.isdecimal()                 # False является десятичным
x = i.isdigit()                   # True состоит только из цифр
x = f.isdigit()                   # False состоит только из цифр

x = i.isnumeric()                 # True в строке только числовые символы
x = f.isnumeric()                 # False в строке только числовые символы

x = iden.isidentifier()           # True является допустимым идентификатором для функций, классов, переменных и тп

x = s.isalpha()                   # False состоит только из букв
x = iden.isalpha()                # True состоит только из букв

x = iden.isascii()                # True все символы являются символами ASCII
x = i.isascii()                   # True все символы являются символами ASCII
x = sp.isascii()                  # True все символы являются символами ASCII
x = rus.isascii()                 # False все символы являются символами ASCII

x = sp.isspace()                  # True есть только пробелы и если есть хотя бы один пробел

x = s.isprintable()               # True доступно для печати
x = i.isprintable()               # True доступно для печати
x = sp.isprintable()              # True доступно для печати

x = upper.isupper()               # True все слова имеют верхний регистр символов
x = lower.islower()               # True все слова имеют нижний регистр символов
x = title.istitle()               # True первая буква каждого слова заглавная  и только первая




# ===== Срезы
a[5:10:2]                                   # a[start:stop:step]

# ===== f-STRING, r-STRING
name = 'Ivan'
age = 34
x = f'My name is {name}, age:{age}'         # My name is Ivan, age:34
x = r'some string \n'                       # some string \n    чистая строка без обработки интерпритатором


# === КОДИРОВАНИЕ И ДЕКОДИРОВАНИЕ
# По умолчанию encoding в str.encode() и в bytes.decode() установлен в UTF-8

x = 'hello world'          # utf-8 by default in Python 3

x.encode('ascii')  # b'hello world'
x.encode('utf-16') # b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00'
x.encode('utf-32') # b'\xff\xfe\x00\x00h\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00 \x00\x00\x00w\x00\x00\x00o\x00\x00\x00r\x00\x00\x00l\x00\x00\x00d\x00\x00\x00'
x.encode('cp1252') # b'hello world'

# === Модуль string - содержит ascii символы по группам. 
# Любой ascii символ - максимум один байт.
# Всего кодировка ASCII содержит 128 символов:
# от 0 до 31 	    Контрольные и неотображаемые символы
# от 32 до 64 	    Знаки пунктуации, символы, числа и пробел
# от 65 до 90 	    Буквы английского алфавита в верхнем регистре
# от 91 до 96 	    Дополнительные графемы, такие как [ и \
# от 97 до 122 	    Буквы английского алфавита в нижнем регистре
# от 123 до 126 	Дополнительные графемы, такие как { и |
# 127 	            Контрольный неотображаемый символ (DEL)

import string

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace


# === изменение представления объекта
ascii('a')              # 'a'       представление объекта в ASCII, экранирует не входящие в эту таблицу символы
bin(100)                # 0b1100100 двоичное представление целого числа
oct(100)                # 0o144     восьмиричное представление целого числа
hex(100)                # 0x64      шестнадцатиричное представление целого числа

# === конструкторы классов

# = int() - вернет целое число
int('1000')                   # 1000 <class 'int'>

# = str() - вернет строкуchr(65)
str(1000)                     # 1000 <class 'str'>

# = bytes() - вернет байтовый объект
bytes('1', 'utf-8')           # b'1'
bytes('1', 'utf-16')          # b'\xff\xfe1\x00'
bytes('1', 'utf-32')          # b'\xff\xfe\x00\x001\x00\x00\x00'

bytes('a', 'utf-8')           # b'a'
bytes('a', 'utf-16')          # b'\xff\xfea\x00'
bytes('a', 'utf-32')          # b'\xff\xfe\x00\x00a\x00\x00\x00'
b'\xff\xfe\x00\x00a\x00\x00\x00'.decode('utf-32')  # конвертирует байты в символ

x  = 'hello'.encode('utf-16') # b'\xff\xfeh\x00e\x00l\x00l\x00o\x00' кодируем в байты utf-16
print(type(x))                # <class 'bytes'>
x.decode('utf-16')            # hello декодируем байты в строку utf-8

# === конвертация
chr(65)                       # A конвертирует число в символ юникод
ord('A')                      # 65 конвертирует символ в число



# === Модуль unicodedata - содержит unicode символы 
# Базовые элементы — это символы(кодовые точки) типа U+0041 - латинская A
# utf-8   - от 1 до 4 байт на символ
# utf-16  - от 2 до 4 байт на символ
# utf-32  - 4 байта на символ

import unicodedata
Все операции ввода-вывода осуществляют в байтах, пока вы не сообщите системе кодировку для преобразования этих данных в текст.

https://www.youtube.com/watch?v=_inWIREh9jc
unicodedata.name("€")           # 'EURO SIGN'
unicodedata.lookup("EURO SIGN") # '€'

