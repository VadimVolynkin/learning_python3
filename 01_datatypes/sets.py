set
frozenset

# изменяемый тип
# неупорядоченная уникализированная последовательность
# нет доступа по индексу
# вес - 48 байт

m = {1, 2, 3}
m2 = set([1,2,3])

['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']



add(x)
сlear()
remove()
discard()
pop()

isdisjoint()
issubset()
issuperset()

update()
union()

intersection()
intersection_update()

difference_update()
symmetric_difference()
symmetric_difference_update()

###### Пересечение =======================================================

list1 = ['Jotaro', 'Josuke', 'Koichi']
list2 = ['Jotaro', 'Koichi', 'Giorno']
lang_X = {'C++', 'Perl', 'PHP'}
lang_Y = {'Java', 'C#', 'PHP', 'Python'}

overlap = lang_X & lang_Y
overlap2 = lang_X.intersection(lang_Y)
print(overlap)



###### Объединение =======================================================
lang_Z = lang_X | lang_Y
lang_Z = lang_X.union(lang_Y)
print(lang_Z)


###### Разность множеств =======================================================
lang_Z = lang_X - lang_Y
lang_Z = lang_X.difference(lang_Y)
print(lang_Z)


###### Симметрическая разность =======================================================
lang_Z = lang_X ^ lang_Y
lang_Z = lang_X.symmetric_difference(lang_Y)
print(lang_Z)













