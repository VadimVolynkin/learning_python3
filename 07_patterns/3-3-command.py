# ================================================================================================================
# COMMAND(Действие, Транзакция, Action, Команда)
# ================================================================================================================
# поведенческий паттерн 
# Команда устанавливает косвенную одностороннюю связь от отправителей к получателям.
# Позволяет заворачивать запросы или простые операции в отдельные объекты. Это позволяет откладывать выполнение команд, выстраивать их в очереди, а также хранить историю и делать отмену.

# Объекты команд часто подаются в обработчики событий элементов GUI. Практически любая реализация отмены использует принципа команд.

# ===== Как работает


# ===== Когда применять

# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod


# Интерфейс Команды объявляет метод для выполнения команд
class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


# Некоторые команды способны выполнять простые операции самостоятельно
class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


# Некоторые команды делегируют более сложные операции другим объектам-получателям
# Команды могут принимать один или несколько объектов-получателей вместе с любыми данными о контексте через конструктор
class ComplexCommand(Command):

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    # Команды могут делегировать выполнение любым методам получателя
    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


# Получатели содержат бизнес-логику
# Получатели умеют выполнять все виды операций, связанных с выполнением запроса
# Любой класс может выступать Получателем
class Receiver:

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


# Отправитель связан с одной или несколькими командами
# Отправитель отправляет запрос команде
class Invoker:

    # аргументы для хранения команд
    _on_start = None
    _on_finish = None

    # Инициализация команд
    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    # Отправитель не зависит от классов конкретных команд и получателей
    # Отправитель передаёт запрос получателю косвенно, выполняя команду
    def do_something_important(self) -> None:

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):    # является ли _on_start командой
            self._on_start.execute()               # выполняет метод команды 

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# Клиентский код может параметризовать отправителя любыми командами
if __name__ == "__main__":

    invoker = Invoker()                                      # создание отправителя
    invoker.set_on_start(SimpleCommand("Say Hi!"))           # инициализация простой команды(выполнит действие сама)

    receiver = Receiver()                                    # создание получателя
    invoker.set_on_finish(
        ComplexCommand(receiver, "Send email", "Save report")# инициализация сложной (передаст выполнение получателю)
        )

    invoker.do_something_important()                         # выполнит метод с командами















