# ================================================================================================================
# STATE
# ================================================================================================================
# поведенческий паттерн 
# Позволяет менять поведение объекта в зависимости от его состония, как если бы измениля его класс
# Например, объект Документ может принимать три состояния: Черновик, Модерация или Опубликован. В зависимости от состояния метод опубликовать будет обрабатываться по разному(передаваться модератору, публиковаться, ничего не делать)

# Паттерн Состояние часто используют в Python для превращения в объекты громоздких стейт-машин, построенных на операторах switch

# ===== Как работает
Программа может находиться в одном из нескольких состояний, которые всё время сменяют друг друга.
Набор этих состояний, а также переходов между ними, предопределён и конечен.
Программа в разных состояниях по разному реагирует на одни и теже события, как если бы изменился класс объекта

Паттерн Состояние предлагает создать отдельные классы для каждого состояния, в котором может пребывать объект, а затем вынести туда поведения, соответствующие этим состояниям.
Объект будет содержать только ссылку на один из объектов-состояний и делегировать ему работу, зависящую от состояния.
Конкретные состояния могут знать друг о друге и инициировать переходы от одного состояния к другому.

# ===== Когда применять
Когда есть объект, поведение которого меняется в зависимости от состояния, типов состояний много, и их код часто меняется.

Когда код класса содержит множество условных операторов, которые выбирают поведения в зависимости от текущих значений полей класса.

Когда вы сознательно используете табличную машину состояний, построенную на условных операторах, но вынуждены мириться с дублированием кода для похожих состояний и переходов.



# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod


# Контекст определяет интерфейс для клиентов
# Контекст хранит ссылку на экземпляр подкласса Состояния, который отображает текущее состояние Контекста
class Context:

    # Ссылка на текущее состояние Контекста
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    # Контекст позволяет изменять объект Состояния во время выполнения
    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    # Контекст делегирует часть своего поведения текущему объекту Состояния
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


# Базовый класс Состояния объявляет методы, которые должны реализовать все Конкретные Состояния
# Базовый класс Состояния предоставляет обратную ссылку на объект Контекст, связанный с Состоянием
# Эта обратная ссылка может использоваться Состояниями для передачи Контекста другому Состоянию
class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


# Конкретные Состояния реализуют различные модели поведения, связанные с состоянием Контекста
class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


# Клиентский код
if __name__ == "__main__":
    
    # создаем контекст и передаем в него состояние
    context = Context(ConcreteStateA())

    # выполняем запросы соответствующие этому состоянию
    context.request1() 
    context.request2()