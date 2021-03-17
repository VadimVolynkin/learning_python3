# изменяемый тип данных, упорядочен по индексам, допускает неуникальные значения
# представляет собой список ссылок на объекты
# вес - 40 байт

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

###### Методы =====================================================
list.copy()                     # создаст новый объект списка с ссылками на теже объекты. Если объекты мутабельны, то изменение в 1 списке изменит второй список.
newlist = copy.deepcopy(mylist) # создаст новый объект списка с новыми объектами-копиями
list1.extend(list2)             # предназначен для сложения списков
list.append(x)                  # позволяет добавлять элемент в конец списка

list.reverse()                  # меняет порядок элементов в списке на противоположный
list.sort()                     # сортирует список

list.insert(i, x)               # служит для добавления элемента на указанную позицию( i – позиция, x – элемент)
list.count(x)                   # посчитает количество элементов x в списке
list.index(x)                   # вернет позицию первого найденного элемента x в списке

list.remove(x)                  # удаляет элемент из списка (только первое вхождение)
list.pop(i)                     # вернет и удалит элемент из позиции i, либо последний
list.clear()                    # предназначен для удаления всех элементов (после этой операции список становится пустым [])


elements = [3, 56, 23, 99, 102, 44, 6]
cars = ['audi', 'bmw', 'volvo', 'opel']
###### Генераторы =======================================================
c = [c * 3 for c in elements]
nums = [i for i in range(1, 15)]

###### Сортировка по убыванию ===========================================
elements.sort(reverse = True)

###### Перевести в строку ===============================================
elements_to_str = ', '.join(elements)

import json
list_to_str = json.dumps(elements)
print(type(list_to_str))

###### Перевести в словарь ==============================================
to_dict_from_cars = {x: cars[x] for x in range(len(cars))}
print(to_dict_from_cars)

to_dict_from_2lists = dict(zip(lk, lv))
print(to_dict_from_2lists)

to_dict_from_generator = {lk[a]: lv[a] for a in range(len(lk))}
print(to_dict_from_generator)

to_dict_from_list_tuple = dict(lt)
print(to_dict_from_list_tuple)

to_dict_from_list_of_lists = dict(ll)
print(to_dict_from_list_of_lists)

enumerate_list_to_dict = dict(enumerate(cars))
print(enumerate_list_to_dict)

###### Перевести в JSON =================================================
import json
list_to_json = json.dumps(cars)
print(list_to_json)

###### Перевести к set (множеству) ======================================
print(set(elements))








