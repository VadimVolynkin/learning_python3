# ================================================================================================================
# VISITOR
# ================================================================================================================
# поведенческий паттерн 
позволяет добавить новую операцию для целой иерархии классов, не изменяя код этих классов.



# ===== Как работает


# ===== Когда применять
Когда нужно выполнить какую-то операцию над всеми элементами сложной структуры объектов, например, деревом.

Когда над объектами сложной структуры объектов надо выполнять некоторые не связанные между собой операции, но вы не хотите «засорять» классы такими операциями.

Когда новое поведение имеет смысл только для некоторых классов из существующей иерархии.

Максимальную выгоду от паттерна Посетитель вы почувствуете, используя его со сложной структурой объектов, такой как дерево Компоновщика. В этом случае было бы полезно хранить некоторое промежуточное состояние алгоритма при выполнении методов посетителя над различными объектами структуры.

# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Интерфейс Компонента объявляет метод accept, принимающий посетителя
class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


# Конкретный Компонент должен реализовать метод accept
# Метод accept принимает посетителя и вызывает его метод, соответствующий классу компонента
class ConcreteComponentA(Component):

    # вызываем visitConcreteComponentA, чтобы посетитель знал с каким классом компонента он работает
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    # Конкретные Компоненты могут иметь особые методы, не объявленные в их базовом классе или интерфейсе
    # Посетитель может использовать эти методы, поскольку знает о конкретном классе компонента
    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"


class ConcreteComponentB(Component):
    
    # То же самое здесь: visitConcreteComponentB => ConcreteComponentB
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"



# Интерфейс Посетителя объявляет набор методов посещения, соответствующих классам компонентов
# Сигнатура метода позволяет посетителю определить конкретный класс компонента, с которым он работает
class Visitor(ABC):

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


# Конкретные Посетители реализуют несколько версий алгоритма, они могут работать со всеми классами конкретных компонентов
class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")



# Принимает список компонентов и посетителя
# Клиентский код может выполнять операции посетителя над любым набором элементов, не выясняя их конкретных классов
# Операция accept направляет вызов к соответствующей операции в объекте посетителя
def client_code(components: List[Component], visitor: Visitor) -> None:

    for component in components:
        component.accept(visitor)


if __name__ == "__main__":

    # создание списка компонентов
    components = [ConcreteComponentA(), ConcreteComponentB()]

    # создание посетителя1 и запуск
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    # создание посетителя2 и запуск
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)















