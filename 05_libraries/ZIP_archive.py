https://docs-python.ru/standart-library/modul-zipfile-python/obekt-zipfile-modulja-zipfile/


# ================================================================================================================
# МОДУЛЬ ZipFile
# ================================================================================================================
# При записи файла, если размер файла заранее неизвестен, но может превышать 2 ГБ, то передайте force_zip64=True для поддержки больших файлов.
# Если размер файла известен заранее, то создавайте объект zipfile.ZipInfo() с установленным аргументом file_size и используйте его в качестве параметра имени.


# ================================================================================================================
# МЕТОДЫ ZipFile
# ================================================================================================================

# ===== ZipFile.close() =====================================================================       
# Закрыть файл архива 

with zipfile.ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')

# ===== ZipFile.getinfo() ===================================================================     
# Получить zipfile.ZipInfo() для определенного файла 


# ===== ZipFile.infolist() ==================================================================    
# возвращает список, содержащий объект zipfile.ZipInfo() для каждого члена архива 


# ===== ZipFile.namelist() ==================================================================   
# возвращает список членов архива по имени


# ===== ZipFile.open(name, mode='r', pwd=None, *, force_zip64=False)=========================
# предоставляет доступ к элементу архива в виде двоичного файлового объекта
# name - имя файла или объекта, может принимать объект zipfile.ZipInfo().
# mode - если включен:
# - 'r' (по умолчанию), только для чтения: : read(), readline(), readlines(), seek(), tell(), __iter__(), __next__().
# - 'w' вернет дескриптор для записи с методом write(). Попытка чтения или записи других файлов архиве вызовет ValueError
# pwd - это пароль для расшифровки зашифрованных ZIP-файлов


import zipfile

text = 'Это новый текстовый файл в архиве.'

# Добавим в архив 'test.zip' файл 'ReadMe.txt' с текстом внутри 'text'
with zipfile.ZipFile('test.zip', mode='a') as zf:
    with zf.open('ReadMe.txt', mode='w') as fp:
        fp.write(text.encode('utf-8'))

# смотрим результат добавления
with zipfile.ZipFile('test.zip') as zf:
    for name in zf.namelist():
        print(name)


# прочитаем добавленный файл прямо из архива, не извлекая его
with zipfile.ZipFile('test.zip') as zf:
    with zf.open('ReadMe.txt') as fp:
        text = fp.read()
        print(text.decode('utf-8'))


# ===== ZipFile.extract(member, path=None, pwd=None)=========================================
# извлекает 1 элемент архива member в текущий рабочий каталог
# member - полное имя или объект zipfile.ZipInfo(). Информация о его файле извлекается максимально точно.
# path  - другой каталог для извлечения.
# pwd - пароль для зашифрованных файлов.
# ZipFile.extract() возвращает созданный нормализованный путь (каталог или новый файл).

import zipfile, fnmatch, glob

# директория для извлечения
extract_dir = 'extract_dir'

# паттерн для извлечения файлов
file_pattern = '*-[0-9].sql'

with zipfile.ZipFile('test.zip') as zf:
    for file in zf.infolist():
        # выбираем файлы для извлечения по 'file_pattern'
        if fnmatch.fnmatch(file.filename, file_pattern):
            zf.extract(file.filename, extract_dir)

# выводим результат
for file in glob.glob(extract_dir + '/**', recursive=True):
    print(file)



# ===== ZipFile.extractall(path=None, members=None, pwd=None) ===============================
# извлекает все элементы архива в текущий рабочий каталог
# path указывает другой каталог для извлечения.
# members не обязателен и должен быть подмножеством списка, возвращаемого методом ZipFile.namelist().
# pwd - пароль для зашифрованных файлов.

import zipfile, glob

extract_dir = 'extract_dir'
with zipfile.ZipFile('test.zip') as zf:
    zf.extractall(extract_dir)

# смотрим результат
for file in glob.glob(extract_dir + '/**', recursive=True):
    print(file)


# ===== ZipFile.printdir() ==================================================================
# печатает оглавление архива в sys.stdout.

import zipfile, glob

with zipfile.ZipFile('test.zip') as zf:
    zf.printdir()


# ===== ZipFile.setpassword(pwd) ============================================================
# устанавливает pwd в качестве пароля по умолчанию для извлечения зашифрованных файлов.


# ===== ZipFile.read(name, pwd=None) ========================================================
# возвращает байты прочитанный из файла в архиве с именем name.
# если метод сжатия отличен от ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2 или ZIP_LZMA, вызовет исключение NotImplementedError.
# name - может принимать в качестве имени файла объект zipfile.ZipInfo(). Архив должен быть открыт для чтения или добавления.
# pwd - пароль для зашифрованных файлов. Если указан, то переопределит пароль по умолчанию ZipFile.setpassword(). 

import zipfile

with zipfile.ZipFile('test.zip') as zf:
    for file in zf.infolist():
        if 'ReadMe' in file.filename:
            byte_text = zf.read(file)
            print(byte_text.decode('utf-8'))


# ===== ZipFile.testzip() ===================================================================
# читает все файлы в архиве и проверяет их CRC и заголовки файлов. 
# возвращает имя первого неверного/битого файла или если все "путем", то возвращает None.

import zipfile

with zipfile.ZipFile('test.zip') as zf:
    ok = zf.testzip()
    print('It`s OK!') if ok is None else print(f'{ok} is fail.')



# ===== ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None) =======
# добавляет файл с именем filename в архив
# filename - полное имя файла
# arcname - имя файла в архиве , по умолчанию arcname=filename без буквы диска и с удаленными начальными разделителями пути. 
# compress_type - переопределяет значение, заданное при создании экземпляра zipfile.ZipFile для добавления в архив элемента.
# compresslevel - переопределит конструктор. Архив должен быть открыт в режиме 'w', 'x' или 'a'.

import zipfile, os, glob

path = '/home/docs-python/script/'

# составим список добавляемых файлов в архив
file_dir = glob.glob(path+'**', recursive=True)

with zipfile.ZipFile('test.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        zf.write(file)

os.system('file test.zip')


# ===== ZipFile.writestr(zinfo_or_arcname, data, compress_type=None, compresslevel=None) ====
# записывает файл в архив
# zinfo_or_arcname - либо имя файла в архиве, либо объект ZipInfo. Если это объект ZipInfo, то необходимо указать аргумент data. Если это имя файла, то дата и время устанавливаются на текущую дату и время. Архив должен быть открыт в режиме 'w', 'x' или 'a'.
# data - данные (содержимое) файла str или bytes. Если данные str, то кодируется в UTF-8.
# compress_type - переопределяет значение параметра, заданное при создании экземпляра класса zipfile.ZipFile для добавления в архив нового элемента. По умолчанию конструктор zipfile.ZipInfo() устанавливает compress_type=zipfile.ZIP_STORED.
# compresslevel - переопределит конструктор

import zipfile

text = 'Это новый текстовый файл в архиве.'
filename = 'ReadMe.txt'

# добавляем текстовый файл в архив
with zipfile.ZipFile('test.zip', mode='a', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    zf.writestr(filename, text)

# прочитаем добавленный текстовый файл в архив
with zipfile.ZipFile('test.zip') as zf:
    byte_text = zf.read(filename)
    print(byte_text.decode('utf-8'))


# ================================================================================================================
# АТРИБУТЫ ZipFile
# ================================================================================================================


# ===== ZipFile.filename =====================================================================
# возвращает имя файла ZIP

import zipfile

with zipfile.ZipFile('test.zip') as zf:
    filename = zf.filename
    print(filename)

# ===== ZipFile.debug ========================================================================
# устанавливает уровень вывода отладочной информации. Уровень может быть от 0 (по умолчанию, без выходных данных) до 3-х (максимальный выходной). Отладочная информация записывается в sys.stdout.ZipFile.comment:

# ===== ZipFile.comment ======================================================================
# возвращает комментарий, связанный с файлом ZIP как объект байтов.
# При назначении комментария экземпляру класса zipfile.ZipFile, созданному в режиме 'w', 'x' или 'a', он должен быть не длиннее 65535 байт. Комментарии длиннее этого будут усечены.

import zipfile

# добавим комментарий к архиву для этого архив открываем в режиме mode='a'
comment = 'Комментарий к архиву'
with zipfile.ZipFile('test.zip', 'a') as zf:
    zf.comment = comment.encode('utf-8')

# теперь читаем комментарий
with zipfile.ZipFile('test.zip') as zf:
    text = zf.comment
    print(text.decode('utf-8'))