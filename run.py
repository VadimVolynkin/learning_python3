
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

