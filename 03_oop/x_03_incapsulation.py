"""
https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3

=== PUBLIC, PROTECTED, PRIVATE METHODS ================================================================
some_attr – публичное свойство (public);
_some_attr – режим доступа protected (можно обращаться только внутри класса и во всех его дочерних классах)
__some_attr – режим доступа private (можно обращаться только внутри класса). Приватная переменная всегда создается с префиксом своего класса.

__setattr__(self, key, value) – автоматически вызывается при изменении свойства key класса;
__getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
__getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
__delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).

=== ГЕТТЕРЫ И СЕТТЕРЫ =================================================================================
1. передают значения между приватными атрибутами класса
2. проверяют корректность атрибутов

=== ОБЪЕКТ-СВОЙСТВО PROPERTY ==================================================================
1. Позволяет обращаться к методу как к обычному атрибуту без скобок () - удобней чем геттеры и сеттеры
2. вычисляется только 1 раз
3. передают значения между приватными атрибутами класса
4. проверяют корректность атрибутов

property(fget=None, fset=None, fdel=None, doc=None)

@property
def name_method

@name_method.setter
def name_method

@name_method.deleter
def name_method

=== ДЕСКРИПТОР ========================================================================================
1. Дескриптор - это обычный объект, представляющий значение атрибута, определяет как осуществляется доступ к аттрибутам объекта. Может определяться только на уровне класса. Может иметь методы __get__(), __set__() и __delete__().

2. Дескриптор является способом изменить то, что происходит, когда вы обращаетесть к аттрибуту объекта. Может выполнять проверку типа при присваивании значения атрибуту, обработать исключение или что то еще.

3. Имя атрибута в экземпляре должно отличаться от имени, используемого самим дескриптором ("_" + name). Если к классе есть дескрипторы и атрибуты с одинаковыми именами, то приоритет вызова будет отдан дескриптору.

4. Non data descriptor - дескритор у которого еть только метод __get__. Попытка переписать дескриптор удалит его и создаст простой атрибут.


"""
# ===========================================================================================
# PROTECTED and PRIVATE attrs and methods
# ===========================================================================================

class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

        self._name = name                 # protected _name - соглашение использовать только в классе и наследниках
        self._balance = balance
        self._passport = passport

        self.__name = name                # Инкапсуляция (private attr) _name - доступ только через метод
        self.__balance = balance
        self.__passport = passport


    def print_public_data(self):                                 # функция в классе - метод в экземпляре
        print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

    def __print_private_method_data(self):                       # приватный метод - доступ только внутри класса
        print(self.__name, self.__balance, self.__passport)      # вызов вне класса запрещен - ошибка

    def print_data_from_private_method(self):                    # использует приватный метод
        self.__print_private_method_data()


account1 = BankAccount('Bob', 10000, 374424747283645)

# account1.print_private_data()
# print(account1.__name)                              # доступ напрямую запрещен - ошибка
# account1.__print_private_method_data()              # доступ напрямую запрещен - ошибка
# account1.print_data_from_private_method()

# print(dir(account1))                                # все атрибуты и методы экземпляра
# print(account1._BankAccount__balance)               # так можно получить доступ к приватным атрибутам экземпляра
# account1._BankAccount__print_private_method_data()  # так можно получить доступ к приватным методам экземпляра


# ============================================================================================
# Getters and Setters
# ============================================================================================

class Point:
    WIDTH = 0
    # запрещает создание атрибутов кроме:
    #__slots__ = ["__x", "__y", "WIDTH"]


    def __init__(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Need to be a number')


    def __checkValue(x):
        """метод проверки атрибута на тип"""
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False


    def setCoords(self, x, y):
        """Сеттер проверяет атрибуты через приватный метод"""
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Value need to be a number!!!')


    def getCoords(self):
        """Геттер для получения приватных атрибутов"""
        return self.__x, self.__y

    #######################################################

    def __setattr__(self, key, value):
        """Метод запрещает установку и изменение атрибута"""
        if key == "WIDTH":
            raise AttributeError("WIDTH not allowed")
        else:
            # менять value можно только через __dict__
            self.__dict__[key] = value


    def __getattribute__(self, item):
        """Метод запрещает показ приватного атрибута"""
        if item == '_Point__z':
            raise ValueError('Private attribute')
        else:
            return object.__getattribute__(self, item)


    def __getattr__(self, item):
        """Срабатывает при обращении к несуществующему атрибуту"""
        print("__getattr__: "+item)


    def __delattr__(self, item):
        """Срабатывает при удалении атрибута"""
        print("__delattr__ :"+item)


# create instance
pt = Point('10', 20)

# pt.setCoords(30, 40)
# print(pt.getCoords())
# pt.WIDTH2 = 100
# del pt.WIDTH2


# ============================================================================================
# Property
# ============================================================================================
class PointProperty:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        """метод проверки атрибута на тип"""
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('bad data')

    @coordX.deleter
    def coordX(self):
        print('del')
        del self.__x

    # если не используется декоратор property
    # coordX = property(__getcoordX, __setcoordX, __delcoordX)

# ============================================================================================
# Descriptors
# ============================================================================================
class CoordValue:

    # создает имя дескриптора в момент создания экземпляра
    def __set_name__(self, owner, name):           # owner = class Point - владелец дескриптора(класс в котором он вызван)
        self.__name = name                         # __name = имя переменной экземпляра дескриптора

    def __get__(self, instance, owner):            # instance - ссылка на экземпляр класса, в котором вызван дескриптор
        return instance.__dict__[self.__name]

    # создает атрибут в экземпляре, в котором вызван дескриптор
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, obj):                     # obj имя дескриптора для удаления
        del obj.__dict__[self.__name]


class NoDataDescriptor:
    """Такой дескриптор может только получать данные"""
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "No Data Descriptor"


class PointDescriptor:

    # дескрипторы
    nodata = NoDataDescriptor()
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x                # self.coordX - вызов дескриптора, а не одноименного атрибута экземпляра класса
        self.coordY = y                # при совпадении имен приоритет отдается всегда дескриптору


d = PointDescriptor(1, 2)
print(pt.nodata)
# d.nodata = 'hello'                   # это удалит дескриптор nodata и создаст простой атрибут со строкой
# d = PointDescriptor()
# d.coordX = 10
# d.coordY = 30


# print(d.coordX, d.coordY)
# print(d.__dict__)
# print(d.__dir__())
