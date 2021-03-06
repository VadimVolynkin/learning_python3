# ================================================================================================================
# АДАПТЕР 
# ================================================================================================================
# Адаптер — это структурный паттерн
# Позволяет наладить работу объектов с несовместимыми интерфейсами - предоставляет классу альтернативный интерфейс
# Используется для конвертации одних типов данных в другие. Например JSON, XML. Может быть двусторонним.
# Позволяет объединить работу нескольких подклассов с доработкой их общей функциональности до требуемой.


# ================================================================================================================
# АДАПТЕР ОБЪЕКТОВ ЧЕРЕЗ КОМПОЗИЦИЮ
# ================================================================================================================
# Эта реализация использует композицию: объект адаптера при создании принимает адаптируемый объект
# Целевой класс с совместимым с клиентом интерфейсом
class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


# Класс с доп логикой с несовместимым с клиентом интерфейсом(другое название метода и неверный возвращаемый результат)
class Adaptee:

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


# Класс Адаптер наследуется от целевого класса
# Переопределяет у себя его метод - он вызывает метод адаптируемого объекта с обработкой его результата.
# Объект Адаптера при создании принимает адаптируемый объект, либо принимает его в параметре своего метода
class Adapter(Target):

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    # вызов метода Адаптера через понятный интерфейс Target
    print(target.request(), end="")


if __name__ == "__main__":
    adaptee = Adaptee()                                           # создаем объект адаптируемого класса
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")   # Adaptee: .eetpadA eht fo roivaheb laicepS

    adapter = Adapter(adaptee)                                    # создаем объект адаптера(принимает адаптируемый объект)
    client_code(adapter)                                          # Adapter: (TRANSLATED) Special behavior of the Adaptee.


# ================================================================================================================
# АДАПТЕР КЛАССОВ ЧЕРЕЗ НАСЛЕДОВАНИЕ
# ================================================================================================================
# Эта реализация базируется на наследовании: адаптер наследует оба интерфейса: целевой и адаптируемый.

# Целевой класс с совместимым с клиентом интерфейсом
class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


# Класс с доп логикой с несовместимым с клиентом интерфейсом(другое название метода и неверный возвращаемый результат)
class Adaptee:

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


# Класс Адаптер наследует оба класса: целевой и адаптируемый
# Переопределяет у себя метод целевого класса: вызывает cвой метод унаследованный из неадаптированного класса с обработкой его результата.
class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    # вызов метода Адаптера через понятный интерфейс Target
    print(target.request(), end="")


if __name__ == "__main__":
    adapter = Adapter()                                # создаем объект адаптера
    client_code(adapter)                               # Adapter: (TRANSLATED) Special behavior of the Adaptee.









