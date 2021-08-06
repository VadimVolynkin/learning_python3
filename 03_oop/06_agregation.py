# ================================================================================================================
# АГРЕГАЦИЯ
# ================================================================================================================
ОТ СЕБЯ: Агрегация - принятие объектом-контейнером уже ранее созданного объекта. 
По сути агрегация используется везде, где объект принимает объект.
Созданный объект не принадлежит неймспейсу контейнера, поэтому после удаления контейнера не перестает существовать - это основное отличие от композиции.

# Класс создает объекты с данныи и методами для вычисления зарплаты
class Salary:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


# Класс создает объекты-контейнеры, которые принимают уже ранее созданный объект класса Salary
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary                       # ЭТО АГРЕГАЦИЯ

    def total_salary(self):
        print(self.obj_salary.annual_salary())



# создание объекта-зарплаты с данными
# этот объект продолжит существовать если удалить объект emp ниже
salary_emp = Salary(100000, 500000)                    

# создание объкта конейнера, принимающего объект-зарплаты
emp = Employee('Ivan', 33, salary_emp)                 
emp.total_salary()                                     # 1700000