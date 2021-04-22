# ================================================================================================================
# DECORATOR
# ================================================================================================================
# структурный паттерн
# позволяет добавлять объектам новые поведения, помещая их в объекты-обёртки, не меняя их интерфейс
# поддерживает рекурсивную вложенность
# часто применяется в коде с потоками
# когда нельзя расширить обязанности объекта с помощью наследования


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================

# Базовый интерфейс Компонента
class Component():

    def operation(self) -> str:
        pass

# Конкретные Компоненты предоставляют реализации
class ConcreteComponent(Component):

    def operation(self) -> str:
        return "ConcreteComponent"



# Базовый Декоратор наследуется от Компонента и имеет тот же интерфейсу, что и другие компоненты
# Цель этого класса - определить интерфейс обёртки для всех конкретных декораторов
# Реализация кода обёртки по умолчанию может включать поле для хранения компонента и средства его инициализации
# Базовый декоратор делегирует все свои операции вложенному объекту компонента
class Decorator(Component):

    _component: Component = None                       # поле для хранения объекта компонента

    # конструктор принимает объект компонента
    def __init__(self, component: Component) -> None:
        self._component = component

    # возвращает объект компонента
    @property
    def component(self) -> str:
        return self._component

    # делегирует вызов методу объекта компонента
    def operation(self) -> str:
        return self._component.operation()



# Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат некоторым образом 
class ConcreteDecoratorA(Decorator):

    # вызов метода component, который вернет полученный объект компонента, затем вызов у него operation
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):

    # Декораторы могут выполнять своё поведение до или после вызова обёрнутого объекта
    def operation(self) -> str:
        print('some decorator code before')
        print(f"ConcreteDecoratorB({self.component.operation()})")
        print('some decorator code after')



# Клиентский код работает со всеми объектами, используя интерфейс Компонента
def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":

    # Клиентский код может поддерживать простые компоненты...
    simple = ConcreteComponent()                             # создаем простой объект конкретного компонента без декоратора
    client_code(simple)                                      # RESULT: ConcreteComponent
    print("\n")


    # Клиентский код может поддерживать декорированные компоненты...
    decorator1 = ConcreteDecoratorA(simple)                  # создадим декоратор и передадим ему простой объект
    client_code(decorator1)                                  # RESULT: ConcreteDecoratorA(ConcreteComponent)
    print("\n")


    # Клиентский код может поддерживать декорированные декораторы...
    decorator2 = ConcreteDecoratorB(decorator1)              # создадим декоратор и передадим ему декоратор
    client_code(decorator2)
    # some decoraor code before
    # ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
    # some decoraor code after