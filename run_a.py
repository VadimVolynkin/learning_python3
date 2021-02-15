from psycopg2 import sql


columns = ('country_name_ru', 'airport_name_ru', 'city_code')

stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
    sql.SQL(',').join(map(sql.Identifier, columns)),
    sql.Identifier('airport')
    )



print(stmt)


Composed(
    [
        SQL('SELECT '),
        Composed([Identifier('country_name_ru'), (','), Identifier('airport_name_ru'), SQL(','), Identifier('city_code')]),
        SQL(' FROM '), Identifier('airport'), SQL(' LIMIT 5')])

















# class Cat:
#     __shared_attr = {
#         'breed': 'pers'
#     }

#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr   # присваевает экземплярам 1 атрибут-словарь для всех экземпляров


# a = Cat()
# b = Cat()



# print('a breed', a.breed)
# print('b breed', b.breed)

# b.breed = 'siam'

# print('a breed', a.breed)
# print('b breed', b.breed)
# print(b.__dict__)
# print(dir(b))



















# class Point:

#     def __init__(self, xyz):
#         self.xyz = list(xyz)

#     def show(self):
#         return tuple(self.xyz)

#     def set_xyz(self, x, y, z):
#         self.xyz[0] = x
#         self.xyz[1] = y
#         self.xyz[2] = z


# a = Point([5, 15, 25])
# print(a.show())
# a.set_xyz(10, 20, 30)
# print(a.xyz)
# print(a.show())



# class ABC:
#     xx = 100
#     yy = 200


#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def summa(self):
#         print(self.x + self.y)

#     def class_summa(self):
#         print(ABC.x + ABC.y)

#     def __del__(self):
#         print("Удаление экземпляра: " + self.__str__())




# a = ABC(77, 88)


# print(a.xx)




# print('int:', int().__sizeof__())         # int: 24
# print('float:', float().__sizeof__())     # float: 24
# print('str:', ''.__sizeof__())            # str: 49
# print('bool:',  False.__sizeof__())       # bool: 24
# print('list:', [].__sizeof__())           # list: 40
# print('dict:', {}.__sizeof__())           # dict: 48
# print('set:', {1, 2}.__sizeof__())        # set: 200
# print('tuple:', tuple().__sizeof__())     # tuple: 24
# print('None:', None.__sizeof__())         # None: 16












