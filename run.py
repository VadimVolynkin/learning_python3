# как добавить метод в экземпляр
# как удалить метод из экземпляра
# 89===
class Cat:
    """Строка документации класса"""

    name = 'bob'                    # атрибут класса - доступен каждому экземпляру
    emp_count = 0                   # счетчик созданных объектов

    def __init__(self, color):      # color - атрибут экземпляра, получаемый при создании
        self.color = color          # self - ссылка на объект в памяти
        Cat.emp_count += 1          # увеличит счетчик созданных объектов на 1

    def print_name(self):           # функция в классе, метод в экземпляре
        print(self.name)

# создаем объекты
obj = Cat('white')
obj2 = Cat('red')
obj3 = Cat('green')

def print_hello(self):
    print('hello')

obj.age = 35
print(obj.__dict__)
print(dir(obj))

print(Cat.__name__)

# print(obj.__class__)
















