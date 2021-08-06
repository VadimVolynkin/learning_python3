"""
ИНКАПСУЛЯЦИЯ - объединение данных и методов работы с этими данными в один объект, позволяя скрыть детали реализации объекта от пользователя.
Инкапсуляция нужна для сокрытия атрибутов и методов, а также избегания конфликтов имен между экземплярами базовых и производных классов. Сокрытия в питоне нет. Можно снизить заметность переопределив __dir__().
Частные атрибуты и методы класса - имена в классе вида __Foo автоматически меняются на _Classname__Foo. Частные методы предотвращают переопределение в классах-наследниках.

some_attr – публичное свойство (public)
_some_attr – режим доступа protected (можно обращаться только внутри класса и во всех его дочерних классах)
__some_attr – режим доступа private (можно обращаться только внутри класса). Приватная переменная всегда создается с префиксом своего класса. Для ее использования вне класса можно создать в базовом классе публичный геттер.

ПОЛИМОРФИЗМ - это возможность использования экземпляра без учета его фактического типа(возможность работать с разными объектами единым образом).
Питон знает к какому классу относится объект и выбирает для него соответствующий метод при обращении к одинаковому имени метода.

НАСЛЕДОВАНИЕ - это механизм создания новых классов, призванный настроить или изменить поведение существующего класса.

КОМПОЗИЦИЯ - создание внутри класса объекта другого класса.

МЕТОД ЭКЗЕМПЛЯРА – это функция, оперирующая экземпляром класса, который передается ей в первом аргументе.

@classmethod - оперирует классом как объектом. Передает cls первым аргументом. Может быть вызван относительно экземпляра.

@staticmethod - это обычная функция, в пространстве имен класса. Нет self - не оперирует экземплярами, но может быть вызвана относительно экземпляра.
Обычно статические методы используются для обеспечения различных способов создания новых экземпляров.

@property - cвойства экземпляра класса - тип атрибута, который вычисляется только 1 раз(по сути функция), но обращение к нему происходит без () - как к простому атрибуту.
Свойства могут перехватывать операции по изменению и удалению атрибута @name_attr.setter или @name_attr.deleter.

Переопределение метода - изменение его функционала внутри класса-наследника. Переопределять можно только частные методы. Частные методы определяются независимо в каждом классе.

Перегрузка методов - выполнение разного функционала в зависимсти от переданных данных.

СВЯЗАННЫЙ МЕТОД - объект, напоминающий подготовленную к вызову функцию без ().

ЭКЗЕМПЛЯР КЛАССА - объект. Создается двумя методами __new__(cls, *args, **kwargs) и __init__(class_obj, *args, **kwargs)
При количестве ссылок = 0 объект удаляется.

ДЕСКРИПТОР - это обычный объект, представляющий значение атрибута. Может иметь методы __get__(), __set__() и __delete__()
Может выполнять проверку типа при присваивании значения атрибуту, обработать исключение или что то еще.
Дескриптор может определяться только на уровне класса.
Имя атрибута в экземпляре должно отличаться от имени, используемого самим дескриптором ("_" + name)
Дескрипторы определяют как осуществляется доступ к аттрибутам объекта. Дескриптор является способом изменить то, что происходит, когда вы обращаетесть к аттрибуту объекта.
Дескриптор - это обычный объект, представляющий значение атрибута. Может иметь методы __get__(), __set__() и __delete__()

АБСТРАКТНЫЕ БАЗОВЫЕ КЛАССЫ реализуют механизм организации объектов в иерархии, позволяющий утверждать о наличии требуемых методов. Абстрактный класс не может использоваться для создания экземпляров, но определяет, какие свойства и методы должны быть реализованы в подклассах.
from abc import ABCMeta, abstractmethod, abstractproperty
FooAbstrsact.register(SomeClass)

МЕТАКЛАСС – это объект, который знает, как создавать классы и управлять ими.
Одно из основных применений метаклассов - проверка и сбор информации об определениях классов.
Метаклассы могут менять поведение классов.
Метакласс определяется как "класс класса". Любой класс, экземпляры которого являются сами классы, является метаклассом.

ДЕКОРАТОР КЛАССА – это функция, которая принимает и возвращает класс.


__class__ в экземпляре хранит ссылку на свой класс
__dict__ экземпляра хранит словарь атрибутов и методов экземпляра
obj.__setattr__("name", value)
obj.__delattr__("name")
obj.__getattribute__("name")


__dict__ класса хранит ссылки на методы
__bases__ класса хранит ссылки на родительские классы в виде кортежа
__getattr__()   поиск метода класса
__slots__       ограничивает выбор имен атрибутов. Экземпляры класса смогут иметь атрибуты только с указанными именами.



































