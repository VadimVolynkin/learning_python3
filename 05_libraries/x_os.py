https://pythonru.com/osnovy/rabota-s-fajlami-v-python-s-pomoshhju-modulja-os

# os.name - имя операционной системы. Доступные варианты: 'posix', 'nt', 'mac', 'os2', 'ce', 'java'.
print(os.name)                 # posix

os.uname() - информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.
print(os.uname())              # posix.uname_result(sysname='Linux', nodename='luna', release='5.4.0-60-generic', version='#67~18.04.1-Ubuntu SMP Tue Jan 5 22:01:05 UTC 2021', machine='x86_64')

os.environ - словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
print(os.environ)

os.getlogin() - имя пользователя, вошедшего в терминал (Unix).
print(os.getlogin())           # vadim

os.getpid() - текущий id процесса.
print(os.getpid())             # 11547

os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True) - проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
print(os.access(path='/home/vadim/PycharmProjects/python_beazley/', mode=777))  # False

os.chdir(path) - смена текущей директории.

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).

os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True) - меняет id владельца и группы (Unix).

os.getcwd() - текущая рабочая директория.

os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True) - создаёт жёсткую ссылку.

os.listdir(path=".") - список файлов и директорий в папке.

os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. OSError, если директория существует.

os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию, создавая при этом промежуточные директории.

os.remove(path, *, dir_fd=None) - удаляет путь к файлу.

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает файл или директорию из src в dst.

os.renames(old, new) - переименовывает old в new, создавая промежуточные директории.

os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None) - переименовывает из src в dst с принудительной заменой.

os.rmdir(path, *, dir_fd=None) - удаляет пустую директорию.

os.removedirs(path) - удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.

os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None) - создаёт символическую ссылку на объект.

os.sync() - записывает все данные на диск (Unix).

os.truncate(path, length) - обрезает файл до длины length.

os.utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True) - модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).

os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).

os.system(command) - исполняет системную команду, возвращает код её завершения (в случае успеха 0).

os.urandom(n) - n случайных байт. Возможно использование этой функции в криптографических целях.
print(os.urandom(10))                # b'\xebC\x96XY\x00\xad\x9f\xf0&'

=============================================================================================

os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.

os.path.abspath(path) - возвращает нормализованный абсолютный путь.
print(os.path.abspath('/home/vadim/PycharmProjects/'))      # /home/vadim/PycharmProjects

os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
print(os.path.basename('/home/vadim/PycharmProjects/python_beazley/mymodule'))     # mymodule

os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
вернет общую часть пути с нескольких урлов(самую длинную)

os.path.dirname(path) - возвращает имя директории пути path.
print(os.path.dirname('/home/vadim/PycharmProjects/fgfref'))    # /home/vadim/PycharmProjects

os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.

os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.

os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.

os.path.getatime(path) - время последнего доступа к файлу, в секундах.
print(os.path.getatime('/home/vadim/PycharmProjects/python_beazley/run_c.py'))      # 1610963369.9786153

os.path.getmtime(path) - время последнего изменения файла, в секундах.
print(os.path.getctime('/home/vadim/PycharmProjects/python_beazley/run_c.py'))      # 1610963482.764496

os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).

os.path.getsize(path) - размер файла в байтах.

os.path.isabs(path) - является ли путь абсолютным.

os.path.isfile(path) - является ли путь файлом.

os.path.isdir(path) - является ли путь директорией.

os.path.islink(path) - является ли путь символической ссылкой.

os.path.ismount(path) - является ли путь точкой монтирования.

os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
print(os.path.join('/home/vadim/', 'somepth/123'))      # /home/vadim/somepth/123

os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).

os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.

os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).

os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).

os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.

os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.

os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.

os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).

os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.

os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.

























