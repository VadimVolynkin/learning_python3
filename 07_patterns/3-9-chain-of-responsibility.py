# ================================================================================================================
# CHAIN OF RESPONSIBILITY(CoR, Chain of Command, Цепочка обязанностей)
# ================================================================================================================
# поведенческий паттерн 
# Цепочка обязанностей передаёт запрос последовательно через цепочку потенциальных получателей.
# Каждый последующий обработчик решает, может ли он обработать запрос сам и если нет. Есть 4 варианта:
# 1. если нет - прерывание операции
# 2. если нет - передача следующему
# 3. если да - обработка и выход
# 4. если да - обработка и передача следующему


# ===== Когда применять
Когда программа должна обрабатывать разнообразные запросы несколькими способами, но заранее неизвестно, какие конкретно запросы будут приходить и какие обработчики для них понадобятся. Запросы будут передавать по цепи пытаясь найти обработчик, который сможет их обработать.

Когда важно, чтобы обработчики выполнялись один за другим в строгом порядке. Например процесс аутентификации, авторизации, выдача куки, кеширование и тп.

Когда набор объектов, способных обработать запрос, должен задаваться динамически. В любой момент можно добавить или убрать элемент в любом месте цепочки.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


# Интерфейс Обработчика объявляет метод set_next для построения цепочки обработчиков. 
# Интерфейс Обработчика объявляет метод handle для выполнения запроса.
class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


# Поведение цепочки по умолчанию может быть реализовано внутри базового класса обработчика.
class AbstractHandler(Handler):

    # переменная для следующего обработчика
    _next_handler: Handler = None                              

    # метод устанавливает следующий обработчик
    # метод вернет ссылку на следующий обработчик - 
    # это позволит связать обработчики в цепочку monkey.set_next(squirrel).set_next(dog)
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    # метод перенаправляет запрос следующему обработчику(если он есть)
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:                                  
            return self._next_handler.handle(request)

        return None



# Все Конкретные Обработчики либо обрабатывают запрос, либо передают его следующему обработчику в цепочке.
class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)              # перенаправит запрос следующему объекту


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)



# Обычно клиентский код приспособлен для работы с единственным обработчиком.
# В большинстве случаев клиенту даже неизвестно, что этот обработчик является частью цепочки.
def client_code(handler: Handler) -> None:

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":

    # создание конкретных обработчиков
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)                 # Chain: Monkey > Squirrel > Dog

    # Клиент должен иметь возможность отправлять запрос любому обработчику, а не только первому в цепочке.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
