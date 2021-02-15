
# https://www.youtube.com/watch?v=HGOBQPFzWKo    1:37
https://pythonworld.ru/moduli/modul-itertools.html

from itertools import (
    product, permutations, combinations, combinations_with_replacement, accumulate, groupby,
    count, cycle, repeat
    )

# product - перебирает все комбинации значений
# a = [1, 2, 3]
# b = [4, 5, 6]

# prod = product(a, b)
# print(list(prod))

# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# permutations - перестановки - перебирает все варианты последовательностей 1 списка
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))


# combinations - второй аргумент устанавливает длину кортежа.
a = [1, 2, 3, 4]
comb = combinations(a, 3)
print(list(comb))

comb_wr = combinations_with_replacement(a, 3)
print(list(comb_wr))


# accumulate - суммирует значения и результат прибавляет к следующему значению
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))


# groupby - группировка по любому признаку, значению
a = [1, 2, 3, 4]
def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3) # раскидает список по вариантам True, False
for key, value in group_obj:               # результат функции True или False - ключ
    print(key, list(value))


# count
for i in count(10):
    sleep(1)
    print(i)


# cycle
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in cycle(a):
    sleep(1)
    print(i)


# repeat
for i in repeat(1):
    sleep(1)
    print(i)