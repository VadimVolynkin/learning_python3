# ================================================================================================================
# OBSERVER(Издатель-Подписчик, Слушатель, Наблюдатель)
# ================================================================================================================
# поведенческий паттерн 
# Цель Наблюдателя — обеспечить динамическую одностороннюю связь, в которой одни объекты косвенно зависят от других.
# Наблюдатель создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события в других объектах.
# Наблюдатель передаёт запрос одновременно всем заинтересованным получателям.

# ===== Как работает
Издатели - объекты, которые содержат важное или интересное для других состояние.
Подписчики - остальные объекты, которые хотят отслеживать изменения этого состояния.

Объект-издатель хранит в себе список ссылок на объекты подписчиков.
Издатель не ведет список подписки самостоятельно.
Издатель предоставляет методы, с помощью которых подписчики могут добавлять или убирать себя из списка.
Можно создать общий интерфейс с методами подписки и отписки для всех издателей.

Когда в издателе происходит событие, он проходит по списку подписчиков и оповещает их, вызывая определённый метод объектов-подписчиков.
Издателю безразлично, какой класс имеет подписчик - все они должны следовать общему интерфейсу и иметь единый метод оповещения.

# ===== Когда применять
Когда после изменения состояния одного объекта требуется что-то сделать в других, но заранее не извесно, какие именно объекты должны отреагировать.

Когда одни объекты должны наблюдать за другими, но только в определённых случаях.

Часто встречается в Python коде там, где применяется событийная модель отношений между компонентами. 

# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

# Интферфейс издателя объявляет набор методов для управлениями подписчиками
class Subject(ABC):
    
    # Присоединяет наблюдателя к издателю
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    # Отсоединяет наблюдателя от издателя
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    # Уведомляет всех наблюдателей о событии
    @abstractmethod
    def notify(self) -> None:
        pass


# Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его изменениях
class ConcreteSubject(Subject):

    
    _state: int = None                             # состояние Издателя, необходимое всем подписчикам              
    _observers: List[Observer] = []                # список подписчиков(может классифицироваться по типу события и т.д.)

    # добавляет подписчика
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    # удаляет подписчика
    def detach(self, observer: Observer) -> None:
        print("Subject: Removed an observer.")
        self._observers.remove(observer)

    
    # запуск обновления в каждом подписчике
    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    # Обычно логика подписки – только часть того, что делает Издатель.
    # Издатели часто содержат бизнес-логику, которая меняет состояние и запускат метод уведомления подписчиков
    def some_business_logic(self) -> None:

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()



# Интерфейс Наблюдателя объявляет метод уведомления, который издатели используют для оповещения подписчиков
class Observer(ABC):

    # Получить обновление от субъекта
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass



# Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому они прикреплены
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


# Клиентский код
if __name__ == "__main__":

    # создаем издателя
    subject = ConcreteSubject()                           

    # создаем наблюдателя_а и подписываем его
    observer_a = ConcreteObserverA()                     
    subject.attach(observer_a)                   # Subject: Attached an observer.                 

    # создаем наблюдателя_б и подписываем его
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)                   # Subject: Attached an observer.

    # выполняет бизнес-логику(она изменит состояние и вызовет обновление у подписчиков)
    subject.some_business_logic()                # Subject: My state has just changed...Notifying observers...           
    subject.some_business_logic()                # Subject: My state has just changed...Notifying observers... 

    # наблюдатель_а отписывается
    subject.detach(observer_a)                   # Subject: Removed an observer.
































