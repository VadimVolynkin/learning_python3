https://pythonworld.ru/moduli/modul-json.html

import json

# python dict
data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        }
    ]
}

# ===== Сериализация JSON =============================================================

# === from python object to json and write in file
json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

"""
skipkeys = True - ключи словаря не базового типа (str, unicode, int, long, float, bool, None) будут проигнорированы, вместо того, чтобы вызывать исключение TypeError.

ensure_ascii = True - все не-ASCII символы в выводе будут экранированы последовательностями \uXXXX, и результатом будет строка, содержащая только ASCII символы. Если ensure_ascii = False, строки запишутся как есть.

check_circular = False - проверка циклических ссылок будет пропущена, а такие ссылки будут вызывать OverflowError.

allow_nan = False - при попытке сериализовать значение с запятой, выходящее за допустимые пределы, будет вызываться ValueError (nan, inf, -inf) в строгом соответствии со спецификацией JSON, вместо того, чтобы использовать эквиваленты из JavaScript (NaN, Infinity, -Infinity).
"""

# === from python object to json_string
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])           # '["foo", {"bar": ["baz", null, 1.0, 2]}]'
json.dumps("\"foo\bar")                                       # "\"foo\bar"
json.dumps('\u1234')                                          # "\u1234"
json.dumps('\\')                                              # "\\"
json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)          # {"a": 0, "b": 0, "c": 0}

# ===== Десериализация JSON ===========================================================

# from json file to python object
json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

with open("data_file.json", "r", encoding = "utf-8") as read_file:
    data = json.load(read_file)                                       # <class 'dict'>

"""
object_hook - опциональная функция, которая применяется к результату декодирования объекта (dict). Использоваться будет значение, возвращаемое этой функцией, а не полученный словарь.

object_pairs_hook - опциональная функция, которая применяется к результату декодирования объекта с определённой последовательностью пар ключ/значение. Будет использован результат, возвращаемый функцией, вместо исходного словаря. Если задан так же object_hook, то приоритет отдаётся object_pairs_hook.

parse_float, если определён, будет вызван для каждого значения JSON с плавающей точкой. По умолчанию, это эквивалентно float(num_str).

parse_int, если определён, будет вызван для строки JSON с числовым значением. По умолчанию эквивалентно int(num_str).

parse_constant, если определён, будет вызван для следующих строк: "-Infinity", "Infinity", "NaN". Может быть использовано для возбуждения исключений при обнаружении ошибочных чисел JSON.

Если не удастся десериализовать JSON, будет возбуждено исключение ValueError.
"""

# from json string to python object
json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')          # ['foo', {'bar': ['baz', None, 1.0, 2]}]   <class 'list'>
json.loads('"\\"foo\\bar"')                                   # '"foo\x08ar'                              <class 'str'>

# Расширяемый кодировщик JSON для структур данных Python
Класс json.JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)


# ===== Get JSON data from response =====================================================
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)






