class Cat:
    """Строка документации класса"""

    name = 'bob'                    # атрибут класса - доступен каждому экземпляру
    emp_count = 0                   # счетчик созданных объектов

    def __init__(self, color):      # color - атрибут экземпляра, получаемый при создании
        self.color = color          # self - ссылка на объект в памяти
        Cat.emp_count += 1          # увеличит счетчик созданных объектов на 1

    def print_name(self):           # функция в классе, метод в экземпляре
        print(self.name)