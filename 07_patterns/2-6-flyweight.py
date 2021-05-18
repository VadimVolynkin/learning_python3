# ================================================================================================================
# FLYWEIGHT(Легковес, Приспособленец, Кэш)
# ================================================================================================================
# Структурный паттерн проектирования
# Экономит память, разделяя общее состояние объектов между собой, вместо хранения одинаковых данных в каждом объекте.
# кеширует одинаковые данные, используемые в разных объектах


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
import json
from typing import Dict

# Легковес создает объекты-легковесы
class Flyweight():

    # При создании объекта Легковес принимает разделяемое состояния для нескольких реальных бизнес-объектов
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    # Метод принимает уникальное состояние для конкретного объекта и выполняет какуюто логику с шаред + уник
    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


# Фабрика Легковесов отвечает за создание и управление объектами-Легковесами
# Когда клиент запрашивает легковес, фабрика либо возвращает существующий экземпляр, либо создает новый
class FlyweightFactory():

    _flyweights: Dict[str, Flyweight] = {}                             # словарь для объектов-легковесов

    # конструктор принимает список начальных шаред данных для создания легковесов
    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)   # добавит в словарь хеш состояния: объект-легковес

    # генерирует хеш строки Легковеса из состояния
    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    # Возвращает существующий Легковес с заданным состоянием или создает новый
    # принимает общее состояние
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
 
        key = self.get_key(shared_state)                               # генерация хеш-ключа общего состояния

        if not self._flyweights.get(key):                              # если в словаре легковесов нет такого ключа
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)            # создаем легковес и добавляем его в словарь 
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]                                   # возвращает объект-легковес

    # показывает легковесы
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


# добавление нового объекта в базу
def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")

    # получение ссылки на объект из словаря или создание
    flyweight = factory.get_flyweight([brand, model, color])           

    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает его методам легковеса.
    # принимает уник данные (номер машины и владельца)
    # вывод общего состояния + уникальное
    flyweight.operation([plates, owner])


if __name__ == "__main__":

    # === создание объекта фабрики
    # Клиентский код обычно создает кучу предварительно заполненных легковесов на этапе инициализации приложения.
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])
    
    # === вывод списка легковесов
    # factory.list_flyweights()


    # === добавление повторяющегося объекта с "BMW", "M5", "red"
    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    # Client: Adding a car to database.
    # FlyweightFactory: Reusing existing flyweight.
    # Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["CL234IR", "James Doe"]) state.


    # === добавление нового объекта
    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")
    # Client: Adding a car to database.
    # FlyweightFactory: Can't find a flyweight, creating new one.
    # Flyweight: Displaying shared (["BMW", "X1", "red"]) and unique (["CL234IR", "James Doe"]) state.


    print("\n")

    # === вывод списка шаред легковесов
    factory.list_flyweights()


    # === получаем объект с шаред данными и выполняем его метод с передачей уникальных данных
    x = factory.get_flyweight(["BMW", "M5", "red"])     # <__main__.Flyweight object at 0x7ff6d911fb20>
    print(x.__dict__)                                   # {'_shared_state': ['BMW', 'M5', 'red']}
    x.operation(['12344', 'ivan'])                      # Flyweight: Displaying shared (["BMW", "M5", "red"]) and unique (["12344", "ivan"]) state.















