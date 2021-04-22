https://webdevblog.ru/shablon-fabrichnogo-metoda-i-ego-realizaciya-v-python/
https://refactoring.guru/ru/design-patterns/factory-method/python/example
http://www.managepy.ru/%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD-%D1%84%D0%B0%D0%B1%D1%80%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-factory-method-%D0%BD%D0%B0-python/
https://itnan.ru/post.php?c=1&p=463731
https://www.youtube.com/playlist?list=PLG7hNdgnQsvf0YIGZagE4qKat9MWC1BmK


# ================================================================================================================
# ФАБРИЧНЫЙ МЕТОД(Virtual Constructor)
# ================================================================================================================
# Порождающий паттерн
# Нужен для конкретных реализаций общего интерфейса.
# Часто используется в начале посроения архитектуры приложения. Потом он часто эволюционирует в абстрактную фабрику и другие более гибкие решения.

# ===== Как работает
Определяет общий интерфейс для создания объекта, но оставляет подклассам ­решение какой объект создать.

# ===== Как создать
1. Создать Абстрактный класс Продукта + Конкретные классы продукта
2. Создать Абстрактный класс Создателя с общим интерфейсом для создания объекта-продукта
3. Создать Конкретные классы Создателей - у каждого своя реализация конкретного продукта


# ===== Цель примененения, где применять
1 интерфейс - много реализаций
Замена сложного логического кода с if/elif/else для определений реализаций объекта
Позволяет избегать модификации существующего кода для поддержки новых требований и задач.
Позволяет разделить процесс создания от кода, который зависит от интерфейса объекта.


# +++
Позволяет избежать привязки к конкретным классам Продуктов
Позволяет выделить весь код по созданию продуктов в 1 место(класс, модуль, функцию)
Упрощает добавление новых продуктов и поддержку уже существующего кода

# ---
Использование паттерна может приводить к созданию больших параллельных иерархий классов, так как для каждого конретного продукта создается конкретная фабрика для его создания.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from abc import ABC, abstractmethod

# Абстрактный Продукт - определяет интерфейс Продуктов
# требует реализации абстрактных методов в наследниках
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретные Продукты предоставляют различные реализации интерфейса Абстрактного Продукта
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class ConcreteProductByDefault(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProductByDefault()}"



# Существует 2 варианта класса создателя:
# 1 - абстрактный класс(определяет интерфейс Создателей_ - требует реализации абстрактного метода factory_method в наследниках. Но может также содержать реализацию по умолчанию.
# 2 - конкретный класс - сам реализует создание конкретного продукта

# определяет метод some_operation для получения продукта
class Creator(ABC):
    # Абстрактный Фаб­ричный метод позволяет классу делегировать создание продуктов подклассам
    # Простой фабричный метод может обеспечить реализацию по умолчанию сам - ему наследники создатели не нужны
    # Фабричный метод может принимать параметры, например тип требуемого объекта
    # Обычно Создатель содержит бизнес-логику работы с объектами продуктов
    @abstractmethod
    def factory_method(self):
        pass
        # return 'ConcreteProductByDefault() - продукт по умолчанию, если делать вариант2'

    # Общий интерфейс создания объекта
    # вызовет фабричный метод уже в наследниках, чтобы получить их конкретную реализацию продукта
    # возврат строки с продуктом - по сути бзнес логика. Подклссы могут косвенно менять ее возвращая другой тип продукта.
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: {product.operation()}"


# Конкретные классы создателя
# переопределяют фабричный метод - каждый вернет свою реализацию конкретного продукта
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()
        
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()



# Клиентский код 
# принимает Конкретный объект создателя
# вызывает в нем бизнес логику some_operation, которая создаст объект, что то сним сделает и вернет результат.
def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    # эта функция запутит метод some_operation объекта Конкретного Создателя1
    # some_operation запустит factory_method Конкретного Создателя1, который возвращает Конкретный Продукт1
    client_code(ConcreteCreator1())



# ================================================================================================================
# ПРИМЕР 2
# ================================================================================================================
from abc import abstractmethod

class Factory:

    @abstractmethod
    def factory_method(self):
        pass

    def run(self):
        product = self.factory_method()
        return product


class ConcreteFactory1(Factory):
    def factory_method(self):
        print('ConcreteProduct1')


class ConcreteFactory2(Factory):
    def factory_method(self):
        print('ConcreteProduct2')


ConcreteFactory1().run()


# ================================================================================================================
# ПРИМЕР 3 - СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА ДЛЯ НЕСКОЛЬКИХ ОС
# ================================================================================================================
from abc import abstractmethod

# Абстрактная фабрика определяет интерфейс для конкретных фабрик
# Может создать любой объект для любой операционной системы
# 1 метод для каждого интерфейса 
class AbstractFactory():

    @abstractmethod
    def create_menu():
        pass

    @abstractmethod
    def create_window():
        pass


# Конкретные фабрики реализуют интерфейс
# каждая фабрика будет иметь столько методов - сколько существует интерфейсов(в примере 2)
# каждый интерфейс каждой фабрики вернет свой конкретный объект
class WinFactory():
    def create_menu(self):
        return 'WinMenu'

    def create_window(self):
        return 'WinWindow'


class LinuxFactory():
    def create_menu(self):
        return 'LinuxMenu'

    def create_window(self):
        return 'LinuxWindow'


# Запуск клиентского кода
# допустим приложение определило, что нужно создать интерфейс для Linux
os = LinuxFactory()               # создаем объект фабрики                      
menu = os.create_menu()           # создаем объекты интерфейса
window = os.create_window()
print(menu)                       # LinuxMenu
print(window)                     # LinuxWindow