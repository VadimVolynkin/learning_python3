
# ================================================================================================================
# FACADE
# ================================================================================================================
Фасад создает новый упрощенный интерфейс к сложной подсистеме. Дает клиенту нужные фичи и скрывает ненужные.
Фасад делегирует запросы клиентов соответствующим объектам внутри подсистемы, отвечает за управление их жизненным циклом.
Фасад не вносит новую функциональность.
Подсистема ничего не знает о существовании фасада.
Фасад можно сделать одиночкой.
Если область ответственности фасада начинает размываться - лучше сделать дополнительный фасад.
Несколько фасадов могут общаться между собой.


# ===== Когда применять
Когда нужно представить простой или урезанный интерфейс к сложной подсистеме.
Когда нужно разложить подсистему на отдельные слои(части).

# ================================================================================================================
# Концептуальный пример
# ================================================================================================================


class Facade:
    # Фасаду можно передать готовые объект подсистем или создать их в фасаде
    # Фасады могут работать с несколькими подсистемами одновременно
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    
    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)



# Подсистема может принимать запросы от фасада(лучший вариант) или/и клиента напрямую.
# Для Подсистемы Фасад – это ещё один клиент.
class Subsystem1:

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"



# Клиентский код принимает Фасад и вызывает его методы, содержащие вызов методов подсистем
# Клиент может даже не знать о существовании подсистем
def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


# Объекты подсистем могут быть созданы в клиентском коде или в самом Фасаде
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)






