bytes
bytearray           От типа bytes отличается только тем, что является изменяемым. 
memoryview          https://docs-python.ru/tutorial/metody-tipa-memoryview-python/

Все операции ввода-вывода осуществляют в байтах, пока вы не сообщите системе кодировку для преобразования этих данных в текст.
# ================================================================================================================
# BYTES
# ================================================================================================================
# bytes неизменяемый тип
# bytearray изменяемый тип - это их единственное отличие
# методы у них одинаковые, поэтому они могут смешиваться не вызывая ошибок при обработке
# типы bytes и bytearray поддерживают теже методы, что и обычные строки, но принимают только байты

# Бит - 0 или 1. Базовая единица информации, которой оперируют вычислительные устройства.
# Байт = 8 бит 00000001 - минимальная единица хранения и обработки цифровой информации. Последовательность байт представляет собой какую-либо информацию (текст, картинку, мелодию...).
# Байт может хранить число от 0 до 255.
# Байты в Питоне - это строки. Обычно их записывают или читают из файла.
# Для хранения пикселя нужно 3 байта (255, 255, 255) 


['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 4 способа создать байтовую строку:
b'bytes'                                  # b'bytes'
bytes('bytes', encoding = 'utf-8')        # b'bytes'
'Байты'.encode('utf-8')                   # b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'  это кирилица в utf-8
bytes([50, 100, 76, 72, 41])              # b'2dLH)' список чисел от 0 до 255 и возвращает байты после функции chr.

# декодирование из байт в str
b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8')    # 'Байты'

# ===== Таблицы кодировки =======================================
utf-8               от 0 до 1 114 111()
ascii               от 0 до 127(7 бит)
chr(100)
Latin-1             базовая кодировка для Hypertext Transfer Protocol (HTTP) 
cp1252              вариант Latin-1 для Windows

list(b'\xf0\x9f\xa4\xa8')           [240, 159, 164, 168]


# одно и тоже число в разных системах счисления
int('11')                    # 11
int('11', base=10)           # 11 (десятичная система по умолчанию)
int('11', base=2)            # 3 двоичная
int('11', base=8)            # 9 восьмеричная
int('11', base=16)           # 17 шестнадцатеричная


0b11                         # 3 двоичный литерал
0o11                         # 9 восьмеричный литерал
0x11                         # 17 шестнадцатеричный литерал

# ================================================================================================================
# BYTEARRAY
# ================================================================================================================
# массив байт - изменяемый тип 

b = bytearray(b'hello world!')        # bytearray(b'hello world!')
b[0] = 105
print(b)                              # bytearray(b'iello world!')


# ================================================================================================================
# MEMORYVIEW - БУФЕР ОБМЕНА
# ================================================================================================================

"""
Объекты memoryview позволяют коду Python получать доступ к внутренним данным объекта, который поддерживает буферный протокол, без копирования.
Поддерживает срезы и индексирование.
Элемент в memoryview - атомарная единица памяти. Для простых типов, таких как bytes и bytearray, элемент - один байт.

""""
v = memoryview(b'abcefg')     # передаем строку байт
v[1]                          # 98 - это b
v[-1]                         # 103
v[1:4]                        # <memory at 0x7f3ddc9f4350>   срез возвращает объект
bytes(v[1:4])                 # b'bce'                       преобразование объекта memory в байты


memoryview.__eq__(exporter)
# сравнение memoryview и буфера обмена - вернет bool
# memoryview     объект памяти буфера обмена
# exporter       буфер обмена


memoryview.tobytes(order=None)
# вернет данные из буфера обмена как строку байтов bytestring - аналог bytes() в представлении памяти
# memoryview     объект памяти буфера обмена
# order=None     как преобразовывать данные

m = memoryview(b"abc")       # объект буфера обмена с байтовой строкой 
m.tobytes()                  # b'abc'    строка байт


memoryview.hex()
# вернет строку, содержащую 2 шестнадцатеричные цифры для каждого байта в буфере

m = memoryview(b"abc")
m.hex()                      # '616263'


memoryview.tolist()
# вернет данные буфера обмена в виде списка элементов буфера

memoryview(b'abc').tolist()  # [97, 98, 99]


memoryview.toreadonly()
# вернет версию буфера обмена только для чтения, исходный объект памяти не изменится

m = memoryview(bytearray(b'abc'))
mm = m.toreadonly()          # новый объект только для чтения     
mm.tolist()                  # [89, 98, 99] вывод
mm[0] = 42                   # TypeError: cannot modify read-only memory


memoryview.release()
# освободит базовый буфер, открытый объектом memoryview
# метод удобен для удаления ограничений и освобождения любых зависших ресурсов

m = memoryview(b'abc')
m.release()                  # любая дальнейшая операция над представлением вызывает ValueError 


memoryview.cast(format[, shape])
# приведет memoryview к новому формату format или форме shape
import array
a = array.array('l', [1,2,3])
x = memoryview(a)
x.format                     # 'l'
y = x.cast('B')
y.format                     # 'B'


memoryview.obj
# атрибут только для чтения, представляет основной объект обзора памяти

b  = bytearray(b'xyz')       # объект массива из байтовой строки
m = memoryview(b)            # объект в буфере
m.obj is b                   # True


memoryview.nbytes
# атрибут только для чтения. Показывает количество пространства в байтах, которое массив будет использовать в непрерывном представлении
import array
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)

len(m)                       # 5
m.nbytes                     # 20
y = m[::2]
len(y)                       # 3
y.nbytes                     # 12
len(y.tobytes())             # 12


memoryview.readonly
# атрибут только для чтения. Указывает, доступна ли память только для чтения. Возвращает bool

m = memoryview(bytearray(b'abc'))
mm = m.toreadonly()
mm.readonly                  # True


memoryview.format
# атрибут только для чтения. Вернет строку с форматом в стиле модуля struct для каждого элемента в представлении

import struct
buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
x = memoryview(buf)
x.format                     # 'B'


memoryview.itemsize
# атрибут только для чтения, вернет int размер в байтах для каждого элемента memoryview
import array, struct
m = memoryview(array.array('H', [32000, 32001, 32002]))
m.itemsize                   # 2


memoryview.ndim
# атрибут только для чтения, вернет int - сколько измерений многомерного массива представляет память

import array
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
m.ndim                       # 1


memoryview.shape
# атрибут только для чтения, вернет кортеж целых чисел длины ndim, дающий форму памяти в виде N-мерного массива

import array
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
x.shape                      # (96,)


memoryview.strides
# атрибут только для чтения, вернет кортеж целых чисел длины ndim, дающий размер в байтах для доступа к каждому элементу для каждого измерения массива.

import array
a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
x.strides                    # (1,)


memoryview.suboffsets
# атрибут только для чтения, вернет кортеж
# Используется внутри для массивов в стиле PIL. Значение носит исключительно информационный характер

import struct
buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
x = memoryview(buf)
x.suboffsets                 # ()


import struct
buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
x = memoryview(buf)
x.c_contiguous               # True - является ли память смежной с языком С
x.f_contiguous               # True - является ли память смежной с языком Fortran
x.contiguous                 # True - является ли память смежной с языками C и Fortran