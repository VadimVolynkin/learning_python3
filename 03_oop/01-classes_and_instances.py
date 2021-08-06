# ============================================================================================
# АТРИБУТЫ КЛАССОВ И ОБЪЕКТОВ
# ============================================================================================
Атрибуты - это методы и свойства. 
Бывают публичными, защищенными и приватными(подробнее см. в наследовании).
Могут принадлежать классу или экземпляру класса.
При совпадении имен атрибута класса и экземпляра приоритет отдается атрибуту экземпляра.


# ===== АТРИБУТЫ КЛАССА(атрибуты данных класса)
Публичные атрибуты класса доступны в любом экземпляре - общие для всех.
Попытка изменить атрибут класса в его экземпляре создаст атрибут экземпляра. Если удалить этот атрибут экземпляра, то при вызове значение будет получено из одноименного атрибута класса. Таким образом операции над атрибутом в экземпляре не влияют на атрибут класса.


# ===== АТРИБУТЫ ЭКЗЕМПЛЯРА
Атрибуты объекта принадлежат только этому конкретному объекту.
Свойства и методы, созданные внутри экземпляров, являются динамическими: можно изменять, удалять.
Методы экземпляра - это функции класса, вызываемые с использованием точечной нотации. Принимают self.
Методы экземпляра могут получить доступ к классу через атрибут self.__class__ - они могут изменять состояние как экземпляра объекта, так и самого класса.


# ===== Порядок поиска атрибута у объекта
Если находит - возвращает, если нет следующий:

1. __getattribute__          # поиск в объекте(метод ищет значение в obj.__dict__)
2. свойство data descriptor  # поиск в дескрипторе(дескрипторы определены в классе)
3. __dict__                  # поиск в словаре объекта
4. raise AttributeError      # если у объекта нет такого атрибута
5. __getattr__               # поиск атрибута в классе (срабатывает если на любом этапе был получен AttributeError)


# ===== Варианты доступа к атрибутам

obj.__setattr__("name", value)    # установить или изменить
setattr(obj, 'name', value) 
obj.name = value

obj.__getattribute__("name")      # получить, если нет атрибута - вернет AttributeError
obj.name                          # точечная нотация
getattr(obj, 'name', 'default')   # функция, если нет атрибута - вернет default
hasattr(obj, 'name')              # проверка наличия атрибута, функция вернет True or False

obj.__delattr__("name")           # метод удалит атр экземпляра, если нет или это атр класса - AttributeError
del obj.name                      # удалит атр экземпляра, если его нет или это атр класса - AttributeError
delattr(obj, 'name')              # функция удалит атр экземпляра, а если его нет или это атр класса - AttributeError


# ===== ПРИМЕР КЛАССА =======================================================================================

class MyClass:

    # атрибут класса
    some_class_attr = 'Hello World'

    # конструктор с атрибутами для экземпляров
    def __init__(self, x, y):
        self.x = x
        self.y = y


# создаем экземпляр
obj = MyClass(10, 25)

# функция, которую далее добавим к экземпляру
def say_goodbuy_x(self):
    print('goodbuy ')

# функция(метод) принадлежит только этому объекту
obj.say_goodbuy_x = say_goodbuy_x

# просмотр словаря объекта
print(obj.__dict__)        # {'x': 10, 'y': 25}

# все атрибуты и методы доступные объекту(его собственные + из класса)
print(dir(obj))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'some_class_attr', 'x', 'y']

# просмотр словаря класса
print(MyClass.__dict__)
{'__module__': '__main__', 'some_class_attr': 'Hello World', '__init__': <function MyClass.__init__ at 0x7fa5641e4dc0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}

# просмотр всех атрибутов и методов класса
print(dir(MyClass))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'some_class_attr']


# ================================================================================================================
# ОПИСАНИЕ АТРИБУТОВ НАСЛЕДУЕМЫХ ОТ САМОГО БАЗОВОГО КЛАССА object
# ================================================================================================================
__class__                  # <class '__main__.MyClass'> ссылка на класс
__new__()                  # создает новый экземпляр
__init__()                 # конструктор класса, передает аргументы экземпляру, созданному в __new__()
__init_subclass__          # конструктор класса. Применяется исключительно к будущим подклассам класса.

dir(obj)                   # список всех атрибутов и методов
__dict__                   # словарь собственных атрибутов

obj.__hash__()             # 8728784686517 хеш экземпляра
obj.__sizeof__()           # 32            размер экземпляра
obj.__doc__                # строка документирования

obj.__str__()              # <__main__.MyClass object at 0x7fc872f57b50>   печатное строковое представление экземпляра
obj.__repr__()             # <__main__.MyClass object at 0x7fc872f57b50>   строковое представление экземпляра для dev

obj.__subclasshook__()     # NotImplemented
obj.__weakref__            # None   слабые ссылки

__eq__                     # ниже блок операций сравнения: равно, неравно, больше...
__ne__                     # операции вернут bool
__gt__
__ge__
__le__
__lt__

__format__                 # используется функцией format (а также методом format у строк)
__module__                 # __main__   имя модуля в котором определен класс
__reduce__
__reduce_ex__



# ================================================================================================================
# ПОЛЕЗНЫЕ ФУНКЦИИ ДЛЯ РАБОТЫ С КЛАССАМИ И ОБЪЕКТАМИ
# ================================================================================================================

type(obj)                               # <class '__main__.MyClass'>  показывает класс экземпляра
isinstance(obj, MyClass)                # True  является ли объект экземпляром класса
issubclass(MyClass, object)             # True  является ли класс подклассом



# ================================================================================================================
# CONSTRUCTOR and DESTRUTOR(правильнее финализатор)
# ================================================================================================================
ЭКЗЕМПЛЯР КЛАССА - объект. 
Создается двумя методами __new__(cls, *args, **kwargs) и __init__(class_obj, *args, **kwargs)
При количестве ссылок = 0 объект удаляется - сборшик мусора вызывает __del__

# === Конструктор __init__(self)
Вызывается в момент создания экземпляра.

# === Деструктор __del__(self)
Вызывается в момент уничтожения экзмемпляра. 
В него можно прописать свою логику, необходимую в случае удаления объекта. Например, отправить уведомление.

class Point:

    # конструктор
    def __init__(self, x, y):Когда этот магический метод не определен, то вызывается специальный метод __len__()
        self.x = x
        self.y = y
        print('Создан объект ' + self.__str__())       # Создан объект <__main__.Point object at 0x7f8a358a7310>

    # деструктор
    def __del__(self):
        print('Удален объект ' + self.__str__())       # Удален объект <__main__.Point object at 0x7f47dcc49310>


pt = Point(5, 10)              # создаем объект
print(pt.__dict__)             # {'x': 5, 'y': 10}
del pt                         # уменьшит счетчик ссылок на объект на 1, если будет 0 - объект удаляется.


# ================================================================================================================
# METHOD, CLASSMETHOD, STATICMETHOD
# ================================================================================================================

# === Обычный метод
Функция, принимающая self - ссылку на экземпляр класса.
Может работать с данными и методами экземпляра класса.
Попытка вызова из класса без передачи экземпляра - TypeError.

# === @classmethod 
Метод оперирует классом как объектом, принимает cls - ссылку на класс. Вызов MyClass.some_classmethod().
Имеет доступ к атрибутам класса и статическим методам класса.
Не имеет доступа к экземплярам.
Может быть вызван относительно экземпляра obj.some_classmethod().
Часто используется для создания экземпляров класса, принимая данные требующие предварительной обработки перед __init__().

# === @staticmethod 
Обычная функция, определенная в классе из соображений тиматичности.
Не принимает ни self, ни cls, поэтому не имеет доступа ни к классу, ни к его экземплярам.
Метод может быть вызван из экземпляра obj.some_staticmethod() и из класса MyClass.some_staticmethod().
Cтатические методы могут использоваться для валидации данных перед созданием экземпляров класса, для обеспечения различных способов создания новых экземпляров.
Статический метод можно переопределить в экземпляре, присвоив ему новую функцию.

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    # обычный метод
    # self - ссылка на экземпляр  <__main__.Date object at 0x7fcee6847f40>
    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'

    # метод класса
    # # cls - ссылка на класс <class '__main__.Date'>
    # делает из строки с датой кортеж для __init__()
    # создаст экземпляр и вернет его
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)                           # cls = Date
        return date1

    
    # статический метод 
    # проверяет строку с датой на валидность(здесь проверка даты в учебных целях, не полная)
    # вернет bool
    @staticmethod
    def is_date_valid(date_as_string):
        if date_as_string.count('.') == 2:                          # проверяет разделители
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 3999       # проверяет диапазон

    
# с помощтю classmethod создать экземпляр Date можно так:
date1 = Date.from_string('30.12.2020')
date1.string_to_db()

# далее используем staticmethod для проверки валидности даты
# список строк с датами
dates = [
    '30.12.2020', 
    '30-12-2020'
    ]

for string_date in dates:
    # проверяем валидность строки с датой
    if Date.is_date_valid(string_date):
        # если все нормально, то создаем экземпляр
        date = Date.from_string(string_date)
        # далее делаем, что-то с экземпляром
        string_to_db = date.string_to_db()
        print(string_to_db)
    else: 
        print(f'Неправильная дата или формат строки с датой') 

