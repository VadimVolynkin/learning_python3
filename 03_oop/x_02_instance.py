"""
1. Экземпляру класса можно присвоить метод

"""

class Car():
    """
    Атрибуты класса влияют на атрибуты всех его экземпляров.
    """
    name = 'bmw'
    age = 30


a = getattr(Car, 'name', 100)
setattr(Car, 'x', 100)
b = getattr(Car, 'y', 200)
print(a, Car.x, b)

delattr(Car, 'x')
del Car.age

c1 = Car()
c2 = Car()
print(c2.name)


"""
Изменение атрибута класса в экземпляре отражается только на экземпляре и делает его атрибутом экземпляра.
Если удалить этот атрибут экземпляра, то при вызове значение будет получено из атрибута класса.
"""
print('=====================================')
c2.name = 'opel'
print(c2.__dict__)        #  атрибут экземпляра в дикте экземпляра
print(c2.name)
del c2.name
print(c2.name)            # значение получено их атрибута класса
print(c2.__dict__)

print(isinstance(c2, Car))


# ====== all attrs and methods in instances ============================================================
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# __class__                  # ссылка на свой класс

# dir(obj)                   # список атрибутов и методов экземпляра
# __dict__                   # словарь атрибутов экземпляра(из класса через init self.name = 'Bob', добавленные obj.age = 35)
# obj.__hash__()             # метод вернет хеш экземпляра
# obj.__sizeof__()           # метод вернет размер экземпляра
# obj.__doc__                # строка документирования

# obj.__str__()              # метод вернет печатное строковое представление экземпляра
# obj.__repr__()             # метод вернет оценочное строковое представление экземпляра

# obj.__subclasshook__()
# obj.__weakref__

# __eq__
# __ne__
# __format__
# __init__
# __init_subclass__
# __gt__
# __ge__
# __le__
# __lt__
# __module__
# __new__
# __reduce__
# __reduce_ex__

# obj.__setattr__("name", value)    # установить или изменить
# obj.name = value
# setattr(obj, 'name', value)       # функция

# obj.__getattribute__("name")      # получить, если нет атрибута - вернет AttributeError
# obj.name
# getattr(obj, 'name', 'default')   # функция, если нет атрибута - вернет default
# hasattr(obj, 'name')              # функция вернет True or False

# obj.__delattr__("name")           # метод удалит атр экземпляра, если нет или это атр класса - то AttributeError
# del obj.name                      # удалит атр экземпляра, если нет или это атр класса - то AttributeError
# delattr(obj, 'name')              # функция удалит атр экземпляра, если нет или это атр класса - то AttributeError

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


# ===========================================================================================
# МОНОСОСТОЯНИЕ -
# изменение любого атрибута в экземпляре меняет значение атрибута в классе и всех экземплярах
# ===========================================================================================


class Cat:
    __shared_attr = {
        'breed': 'pers'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr   # присваевает экземплярам 1 атрибут-словарь для всех экземпляров


a = Cat()
b = Cat()
print('a breed', a.breed)
print('b breed', b.breed)

b.breed = 'siam'

print('a breed', a.breed)
print('b breed', b.breed)

print(a.__dict__)


# ===========================================================================================
# TODO Скрыть атрибуты и методы в питоне можно с помощью accessify и его декораторов @protected and @private
# ===========================================================================================