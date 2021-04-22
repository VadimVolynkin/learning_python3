# ================================================================================================================
# BUILDER
# ================================================================================================================
# Порождающий паттерн
# Позволяет создавать сложные объекты пошагово
# Один и тот же код строительства позволяет получать разные представления объектов- нужно вызвать нужные методы.
# Избавляет от необходимости  передавать в конструктор множество ненужных параметров(если делать своего рода конфиг)
# Избавляет от необходимости создавать множество подклассов продуктов(если делать через подклассы)
# Строители могут создавать совершенно разные продукты с разным интерфейсом, которые не имеют общего предка.
# Строитель может быть построен в виде Моста: директор будет играть роль абстракции, а строители — реализации.

# ===== Как это работает
# Строитель выносит процесс конструирования объекта за пределы его класса. 
# Строитель создает базовый пустой объект, а затем применяет к нему свои методы строительства, которые меняют объект до нужного состояния и отдает уже готовый результат продукта. 
# Потом строитель очищает результат и он готов к работе над новым объектом.

# Можно создать несколько строителей. Каждый будет иметь собственную реализацию тех же этапов создания продукта. Это позволит создавать совершенно другие объекты, используя те же методы. Все эти методы(этапы, шаги строительства) должны работать через общий интерфейс Строителя.

# Строитель не позволяет посторонним объектам иметь доступ к конструируемому объекту, пока тот не будет полностью готов. Это предохраняет клиентский код от получения незаконченных «битых» объектов.

# ===== Когда использовать
# Кргда продукты достаточно сложны и требуют обширной конфигурации.
# Когда избавиться от «телескопического конструктора»(конфиг из множества параметров).
# Когда код должен создавать разные представления какого-то объекта. Например, деревянные и железобетонные дома. Этапы теже, но особенности реализации(материалы) разные.
# Когда нужно собирать сложные составные объекты, например, деревья Компоновщика.

# ===== Как создать строителя
# Класс Строителя имеет 1 метод создающий продукт(начальный объект - болванка)
# и несколько методов настройки продукта(доделывание его частей). В процессе создания их часто вызывают цепочкой.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
# Строитель - это по сути инструкция по созданию частей объекта, его доработка.
# Интерфейс Строителя объявляет создающие методы для различных частей объектов Продуктов.   

    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder1(Builder):
# Несколько строителей могут создавать разные продукты при тех же шагах строительства.
# Строитель возвращает продукт только после выполнения всех шагов.

    def __init__(self):                      # при создании конкретного строителя reset() создает пустой объект продукта 
        self.reset()                         # для использования его в дальнейшей сборке


    def reset(self):
        self._product = Product1()           # создает пустой объект продукта


    # Конкретные строители предоставляют свои реализации методов создания частей продукта 
    # Разные типы строителей могут создавать разные продукты с разными интерфейсами

    # после возвращения конечного результата клиенту, экземпляр
    # строителя должен быть готов к началу производства следующего продукта
    # обычной практикой является вызов метода сброса в конце тела метода 

    @property
    def product(self):
        product = self._product    # кладет результат в product
        self.reset()               # обнуляет результат в _product
        return product

    def produce_part_a(self):
        self._product.add('PartA1')

    def produce_part_b(self):
        self._product.add('PartB1')

    def produce_part_c(self):
        self._product.add('PartC1')


class Product1:
    # результаты различных строителей могут не всегда следовать одному и тому же интерфейсу

    def __init__(self):
        self.parts = []                 # пустой список для частей продукта     

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")



class Director:
    # Директор необязателен, так как клиент может напрямую управлять строителями.
    # Директор задает порядок шагов строительства через общий интерфейс, а Стротель их выполняет. Директор не знает тип получаемого продукта.
    # Директор полезен, если есть несколько способов конструирования продуктов, отличающихся порядком или шагами конструирования.

    def __init__(self):
        self._builder = None

    # Метод возвращает строителя
    @property
    def builder(self):
        return self._builder

    # Метод кладет строителя в _builder
    @builder.setter
    def builder(self, builder):
        # Директор работает с любым экземпляром строителя, который передаётся ему клиентским кодом. 
        # Таким образом, клиентский код может изменить конечный тип вновь собираемого продукта.
        self._builder = builder

    # Директор может создать (строит строитель) несколько вариаций продукта, используя одинаковые шаги построения.
    # Методы ниже производят максимальную и полную версию продукта
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':

    director = Director()                    # создаёт объект-директор
    builder = ConcreteBuilder1()             # создаёт объект-строитель
    director.builder = builder               # передает конкретного строителя директору


    print("Standard basic product: ")
    director.build_minimal_viable_product()  # директор создаст минимальную версию продукта
    builder.product.list_parts()             # строитель покажет список готовых частей

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Здесь пример использования Строителя без Директора - прямой вызов методов.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()








































