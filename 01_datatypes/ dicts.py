# изменяемый тип данных
# неупорядоченные наборы пар ключ-значение, номеров позиций в словарях нет
# объект словаря хранит лишь указатели, а не сами значения
# Ключ не меняется - hashable объект неизменяемого типа(строка, число, кортеж)
# вес - 48 байт

dir()   #show all methods ================================================
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

###### Методы Словаря =====================================================

mydict = {}                   # создает словарь
dict.clear()                  # очищает словарь
dict.copy()                   # возвращает неглубокую копию - новый объект со старыми значениями
dict.deepcopy()               # возвращает глубокую копию - новый объект с новыми значениями
dict.update([other])          # обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

classmethod dict.fromkeys(seq, value) # создает словарь с ключами из seq и значением value (по умолчанию None).

dict.items()                  # возвращает пары (ключ, значение).
dict.keys()                   # возвращает ключи в словаре.
dict.values()                 # возвращает значения в словаре.


dict.get(key, default)        # возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.setdefault(key, default) # возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).

dict.pop(key, default)        # удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem()                # удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.


###### Сортировка по ключу =====================================================
num_dict = {'b': 13, 'd': 30, 'e': -32, 'c': 93, 'a': 33}
sorted_by_key = {key: val for key, val in sorted(num_dict.items())}
print(sorted_by_key)

###### Сортировка по значению =====================================================
sorted_by_val = {key: val for key, val in sorted(num_dict.items(), key=lambda x:x[1])}
print(sorted_by_val)


sorted_by_val30 = {key: val for key, val in num_dict.items() if val >= 30}
print(sorted_by_val30)

###### dict to list =====================================================
lk = [x for x in a.keys()]
print(lk)
lv = [x for x in a.values()]
print(lv)
lt = [x for x in a.items()]
print(lt)

to_dict_from_generator = {lk[a]: lv[a] for a in range(len(lk))}
print('to_dict_from_generator :', to_dict_from_generator)

to_dict_from_2lists = dict(zip(lk, lv))
print('to_dict_from_2lists :', to_dict_from_2lists)

to_dict_from_list_tuple = dict(lt)
print('to_dict_from_tuple :', to_dict_from_list_tuple)


###### dict to json =====================================================
import json
myfile = open('my_json', 'w')
dict_to_json = json.dump(a, fp=myfile)
print(dict_to_json)


###### dict to string =====================================================
import json
dict_to_str = json.dumps(a)
print(dict_to_str)

print(str(a))


###### dicts generator =====================================================
hl = ['h', 'e', 'l', 'l', 'o']

d = {a: a ** 2 for a in range(7)}
d = {a: hl[a] for a in range(len(hl))}








