# ================================================================================================================
# MEDIATOR(Intermediary, Controller, Посредник)
# ================================================================================================================
# поведенческий паттерн 
# Посредник убирает прямую связь между компонентами(отправителями и получателями), заставляя их общаться через себя.
# Таким образом отправители и получатели становятся зависимыми от посредника. 


# ===== Как работает
Клиент вызывает метод компонента
Компонент делает что то и уведомляет посредника с передачей данных(отправитель - self, какие то данные).
Посредник анализирует данные - решает какому компоненту перенаправить запрос. Он определяет как компоненты взаимодействуют друг с другом.
Отправитель и полуатель ничего не знают друг о друге. 


# ===== Когда применять
Когда сложно менять некоторые классы из-за того, что они имеют множество хаотичных связей с другими классами.

Когда нельзя повторно использовать класс, поскольку он зависит от уймы других классов.

Когда приходится создавать множество подклассов компонентов, чтобы использовать одни и те же компоненты в разных контекстах.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC


# Интерфейс Посредника предоставляет метод, используемый компонентами для уведомления посредника о событиях 
# Посредник реагирует на события и передает исполнение другим компонентам
class Mediator(ABC):

    def notify(self, sender: object, event: str) -> None:
        pass

# Конкретный посредник может сам создавать компоненты и управлять ими
# Конкретный посредник знает как компоненты должны взаимодействовать между собой
# Конкретный посредник может обработать запрос сам
class ConcreteMediator(Mediator):

    # принимает 2 компонента
    # устанавливает им посредника - себя
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    # принимает объект отправителя и объект события
    # выполняет бизнес логику вызывая методы компонентов
    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()



# Базовый Компонент обеспечивает базовую функциональность хранения объекта-посредника внутри объекта-компонента
class BaseComponent:

    # при создании экземпляра назначает посредника 
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


# Конкретные Компоненты реализуют бизнес логику и уведомляют посредника
# Конкретные Компоненты не зависят от конкретных классов посредников
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


# Клиентский код
if __name__ == "__main__":

    # создаем компоненты и передаем их посреднику
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    # Компонент делает что то и уведомляет посредника с передачей сообщения
    # Посредник анализирует сообщение и вызывает методы компонента
    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()

