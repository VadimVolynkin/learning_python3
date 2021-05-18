# ================================================================================================================
# TEMPLATE METHOD
# ================================================================================================================
# поведенческий паттерн 
# Определяет скелет алгоритма, перекладывая ответственность за некоторые его шаги на подклассы.
# Паттерн позволяет подклассам переопределять шаги алгоритма, не меняя его общей структуры.


# ===== Как работает


# ===== Когда применять
Когда подклассы должны расширять базовый алгоритм, не меняя его структуры.

Когда у вас есть несколько классов, делающих одно и то же с незначительными отличиями. Если вы редактируете один класс, то приходится вносить такие же правки и в остальные классы.

Шаблонные методы можно встретить во многих библиотечных классах Python. Разработчики создают их, чтобы позволить клиентам легко и быстро расширять стандартный код при помощи наследования.

# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from abc import ABC, abstractmethod


# Абстрактный Класс определяет шаблонный метод - скелет алгоритма из вызовов (обычно) абстрактных примитивных операций
# Конкретные подклассы должны реализовать эти операции, но оставить сам шаблонный метод без изменений
class AbstractClass(ABC):

    # Шаблонный метод определяет скелет алгоритма
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()


    # Эти операции уже имеют реализации по умолчанию
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")


    # Эти операции должны быть реализованы в подклассах
    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    
    # Это Хуки - дополнительные точки расширения в некоторых критических местах алгоритма.
    # Подклассы могут переопределять их, но это не обязательно, поскольку у хуков уже есть стандартная (но пустая) реализация. 
    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


# Конкретные классы должны реализовать все абстрактные операции базового класса. 
# Они могут переопределить некоторые операции с реализацией по умолчанию.
class ConcreteClass1(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


# Обычно конкретные классы переопределяют только часть операций базового класса
class ConcreteClass2(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


# Клиентский код вызывает шаблонный метод для выполнения алгоритма. 
# Клиентский код не должен знать конкретный класс объекта, если он работает с ним через интерфейс его базового класса.
def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())