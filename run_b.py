

# создадим 2 списка
list1 = [1,2,3]
list2 = [1,4,5]


list1 += list2                  # добавляет в первый список
print(list1)                    # [1, 2, 3, 1, 4, 5]

r = list1 + list2               # создаетновый список, объединения 2 списка
print(r)                        # [1, 2, 3, 1, 4, 5]


r = list1 * 2                   # создаст повторяющийся список
print(r)                        # [1, 2, 3, 1, 2, 3]



