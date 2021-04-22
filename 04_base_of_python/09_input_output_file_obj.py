https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/
# ================================================================================================================
# ФАЙЛОВЫЕ ОБЪЕКТЫ 
# ================================================================================================================
file = open('foo.txt')                  
# создает файловый объект (По умолчанию только для чтения, в utf-8)
# возвращает поток(генератор строк из файла), можно итерироваться при помощи next().
# Варианты открытия файла:
# r - только для чтения(По умолчанию)
# w - только для записи (существующий файл с таким же именем будет удален)
# r+  для чтения и записи
# a - для добавления данных в конец
# b - добавление этого символа к чему то выше - открыть для ... в двоичном режиме. Следует использовать для всех файлов, которые не содержат текст.

file.close()          
# закрывает объект, освобождает все занятые ресурсы

file.flush()
# Освобождает внутренний буфер чтения и сбрасывает данные в файл
# вернет int количество буферизованных символов или байт

file.fileno()
# вернет int - файловый дескриптор

file.isatty()
# вернет True, если файл подключен/связан с терминальным устройством tty

file.read(size) 
# Если None или -1 - все содержимое файла будет прочитано и возвращено. В конце файла вернет пустую строку.
# Если int - читает не более size символов в текстовом режиме или size байтов в бинарном. Метод позволят читать большой файл частями.

file.readlines()
# читает построчно до конца файла EOF и возвращает список строк или байтовых объектов
list(file)
# тоже самое

file.readline(size=5) 
# При None или -1 - читает всю строку, пока не достигнет символ новой строки \n
# Читает не более size символов в строке за раз, пока не достигнет символ новой строки \n. Позволят читать длинные строки частями.

fp.tell()                
# текущее положение указателя

fp.seek(offset, whence) 
# (смещение указателя, относительно чего). whence = 0 - начало файла, 1 - текущая позиция, 2 - конец

file.truncate(size)
# Если size, файл усекается до этого размера. По умолчанию size равен текущей позиции указателя.

file.write(str)
# пишет строку. Строка может быть множеством строк, разделенных '\n', соединенных в одну.
# возвращает целое число - количество записанных байт. 
# Из-за буферизации, строка может не отображаться в файле, пока не будет вызван file.flush() или file.close().

file.writelines(sequence)
# Записать списка строк в файл без автодобавления '\n'


# ================================================================================================================
# ТИПЫ ОБРАБАТЫВАЕМЫХ ФАЙЛОВ
# ================================================================================================================

# === Текстовые файлы
fp = open('foo.txt')
fp = open('foo.txt', 'r')
fp = open('foo.txt', 'w')
type(fp)                  # <class '_io.TextIOWrapper'>   возвращает объект TextIOWrapper file


# === Буферизованные двоичные типы файлов
fp = open('foo.txt', 'rb')
fp = open('foo.txt', 'wb')
type(fp)                  # <class '_io.BufferedWriter'>  возвращает объект BufferedReader или объект BufferedWriter file.


# === Необработанный тип файлов Raw
# низкоуровневый строительный блок для двоичных и текстовых потоков
fp = open('abc.txt', 'rb', buffering=0)
type(fp)                  # <class '_io.FileIO'>




# ================================================================================================================
# ПРИМЕРЫ РАБОТЫ С ФАЙЛОВЫМ ОБЪЕКТОМ
# ================================================================================================================

# вариант записи 1: пишем построчно
# менеджер контекста with для открытия и закрытия файла. close() прописывать не нужно
text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']
with open('foo.txt', 'w') as fp:
    for line in text:
        fp.write(line + '\n')  # пишет строку  + '\n'       
        


# вариант записи 2: пишем все сразу
text = ['Строка №1', 'Строка №2', 'Строка №3', 'Строка №4', 'Строка №5']
# объединим список строк в одну строку с разделителем '\n'
write_string = '\n'.join(text)
print(write_string)
with open('foo.txt', 'w') as fp:
    fp.write(write_string) # пишет строку 1 раз
    fp.flush()             # после выполнения flush() данные из write_string физически запишутся в файл
    print(fp.fileno())     # 6 - файловый дескриптор
    print(fp.tell())       # 89 - текущее положение указателя


# вариант чтения 1: весь файл строка за строкой
with open('foo.txt', 'r') as fp:
    for line in fp:
        print(line, end='') # end= " предотвращает добавление дополнительной новой строки в печатаемый текст


# вариант чтения 2: по 15 байт если файл длинный
with open('foo.txt', 'r') as fp:
    chunk = fp.read(15)
    while chunk:
        print(chunk)
        chunk = fp.read(15)


# ================================================================================================================
# МЕТОДЫ УКАЗАТЕЛЯ ФАЙЛА
# ================================================================================================================


# Пример работы с методами
fp = open('workfile', 'rb+')
fp.write(b'0123456789abcdef')         # 16

# Перейти к 6-му байту в файле
fp.seek(5)                            # 5
fp.read(1)                            # b'5'

# Перейти к 3-му байту с конца
fp.seek(-3, 2)                        # 13
fp.read(1)                            # b'd'


# ================================================================================================================
# ПОТОКИ ВВОДА И ВЫВОДА sys.stdin и sys.stdout - ЭТО ФАЙЛЫ
# ================================================================================================================

# ===== чтение ввода пользователя ==
name = input('Введите свое имя :')        # примет строку. Может потребоваться преобразование, если нужен другой тип

# ===== вывод данных на экран ======
import sys
sys.stdout.write('Введите свое имя :')
name = sys.stdin.readline()
