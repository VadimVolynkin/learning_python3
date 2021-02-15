# неизменяемый тип данных, tuples упорядочены по позициям
# хранят указатели на другие объекты
# работают быстрее, чем списки
# весят меньше чем списки- 32 байта
# пустой кортеж - всегда только 1 в памяти(синглтон)

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


###### Методы =======================================================================

tuple.insert(i, x) – служит для добавления элемента на указанную позицию( i – позиция, x – элемент)
tuple.count(x) – посчитает количество элементов x в списке
tuple.index(x) – вернет позицию первого найденного элемента x в списке

###### Сортировка по убыванию =======================================================
cars_tuple = ('audi', 'bmw', 'volvo', 'opel', 'volvo')
elements = [3, 56, 23, 99, 102, 44, 6]

sorted_tuple = tuple(sorted(elements, reverse=True))

###### Перевести в строку =============================================================
elements_to_str = ', '.join(cars_tuple)

###### Перевести в словарь ==========================================================
cars_tuple_to_dict = {x : cars_tuple[x] for x in range(len(cars_tuple))}
print(cars_tuple_to_dict)

###### Перевести в список ==========================================================
list(cars_tuple)

###### Перевести к set (множеству) ==================================================
print(set(elements))

###### Перевести в JSON =============================================================
import json
list_to_json = json.dumps(cars)
print(list_to_json)






