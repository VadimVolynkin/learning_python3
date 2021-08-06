# ================================================================================================================
# КОМПОЗИЦИЯ
# ================================================================================================================
ОТ СЕБЯ: Композиция - создание внутри объекта-контейнера(составной объект, композит) объекта другого класса(компонент).
Объект-компонент существует внутри неймспейса объекта-композита. Если композит удаляется, то компонент тоже перестает существовать - это отличие композиции от агрегации.
Композиция - это как конструктор - из частей собираем нужный функционал.

# ДЛЯ ЧЕГО ЭТО НУЖНО
Композиция позволяет повторно использовать код, добавляя объекты к другим объектам, в отличие от наследования интерфейса и реализации других классов. Композицию часто удобнее использовать чем наследование. Наследование реализации приводит к сильному зацеплению (coupling — прим. пер.) между классами - это усложняет изменение кода.
При композиции составной класс не наследует интерфейс класса компонента, но может использовать его реализацию. Композиционные отношения между двумя классами считаются слабосвязанными. Это обеспечивает лучшую адаптируемость к изменениям. Выбирая между наследованием и композицией решение для композиции обычно является наиболее гибким.

Композиция также позволяет избежать ненужного смешивания функционала: мухи (инструменты) — отдельно, котлеты (бизнес-модели) — отдельно.


# ===== КОГДА ПРИМЕНЯТЬ ==========================================================================================
Композиция использует реализацию класса компонента.
Используйте композицию вместо наследования:

- для создания компонентов, которые могут повторно использоваться несколькими классами в ваших приложениях.

- для реализации групп поведений и политик, которые можно применять взаимозаменяемо к другим классам для настройки их поведения.

- чтобы включить изменения поведения во время выполнения, не затрагивая существующие классы.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================

# Класс создает объекты с данныи и методами для вычисления зарплаты(компонент)
class Salary:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


# Класс создает объекты-композиты, которые создают внутри себя объект класса Salary(компонент)
class Employee:

    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)           # ЭТО КОМПОЗИЦИЯ

    def total_salary(self):
        print(self.obj_salary.annual_salary())         # использование реализации компонента


emp = Employee('Ivan', 33, 100000, 500000)
emp.total_salary()                                     # 1700000