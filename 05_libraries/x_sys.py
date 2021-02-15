# С его помощью можно взаимодействовать с интерпретатором, используя разные функции.

# https://pythonru.com/osnovy/modul-sys-v-python

import sys

a = 50
print(sys.platform)                                 # linux
print(sys.copyright)                                # Copyright of Python interpreter
print(sys.version)                                  # 3.8.5 (default, Aug 12 2020, 01:05:14) [GCC 7.5.0]
print(sys.stdout.write('String 1 \n'))              # String 1  10
print(sys.stderr.write('String 2 \n'))              # String 2  10
print(sys.getsizeof(a))                             # 28 bytes in variable
print(sys.argv)                          # all args in CMD['/home/vadim/PycharmProjects/python_beazley/05_libraries/sys.py']
print(sys.path)                          # ['/home/vadim/PycharmProjects/python_beazley/05_libraries', '/home/vadim/PycharmProjects/python_beazley/.venv/lib/python38.zip', '/home/vadim/PycharmProjects/python_beazley/.venv/lib/python3.8', '/home/vadim/PycharmProjects/pyt


# sys.maxsize
# sys.exit




















