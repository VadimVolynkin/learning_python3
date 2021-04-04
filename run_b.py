


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































