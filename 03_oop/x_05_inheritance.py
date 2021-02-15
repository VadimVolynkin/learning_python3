
"""
Любой класс Питона наследуется от базового класса object.
Отсутствие конструктора в наследнике вызывает конструктор в базовом классе Prop.

super().__init__(*args)
super позволяет обойти все родительские классы в определенном порядке только один раз (избавляет от возможной рекурсии), выбрать базовый класс.


вызовет метод базового класса, правильно перебрав вышестоящие классы и определив его. Передавать self в такой метод уже не нужно.

SomeClass.__mro__ определяет порядок наследования в классе. См. Линеаризация.

Приватные перемменные, определенные в базовом классе, будут иметь префикс имени базового класса, но будут находиться внутри пространства имен класса наследника-инициализатора. Для их использования вне класса можно создать  в базовом классе публичный геттер.

Переопределение метода - изменение его функционала внутри класса-наследника. Переопределять можно только частные методы. Частные методы определяются независимо в каждом классе.

Перегрузка методов - выполнение разного функционала в зависимсти от переданных данных.

Абстрактный метод - метод требующий обязательного переопределения в дочерних классах.



"""

class Point:
    def __init__(self, x = 10, y = 20):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.__x}, {self.__y}'

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Styles:
    def __init__(self):
        print('Constructor Styles')
        super().__init__()


class Pos:
    def __init__(self):
        print('Constructor Pos')
        super().__init__()


class Line2(Styles, Pos):
    def __init__(self, sp:Point, ep:Point, color = 'red', width = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()


    def draw(self):
        print(f'Draw line: {self._sp}, {self._ep}, {self._color}, {self._width}')


l = Line2(Point(2, 14), Point(20, 40), 'green', 5)

# =========================================================================

class Prop:
    # self - ссылка на создаваемый экземпляр класса Line или Rect из которого вызван
    # атрибуты конструктора принадлежат также экземпляру класса
    def __init__(self, sp:Point, ep:Point, color:str = 'red', width:int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width   # будет создана приватная переменная с префиксом этого класса _Prop__width внутри пространства имен класса-инициализатора.


    def getWidth(self):
        return self.__width


    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and \
            (isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        return False


    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")


class Line(Prop):
    def __init__(self, *args):
        print('Переопределенный конструктор Line')
        # super вызовет конструктор базового класса, правильно перебрав вышестоящие классы и определив его.
        super().__init__(*args)

    def drawLine(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}')

    def __setOneCoord(self, sp):
        if sp.isInt():
            self._sp = sp
        else:
            print("Координата должна быть целым числом")

    def __setTowCoord(self, sp, ep):
        if sp.isInt() and ep.isInt():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть целочисленными!")


    def setCoords(self, sp: Point, ep: Point = None):
        if ep == None:
            self.__setOneCoord(sp)
        else:
            self.__setTowCoord(sp, ep)


class Rect(Prop):

    def drawRect(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.__width}')



# l = Line(Point(1, 2), Point(10, 20))
# l.setCoords(Point(2.565), Point(20.443, 40))
# l.setCoords(Point(2.565, 30))

# print(l.getWidth())
# print(dir(l))
# l.drawLine()

# r = Rect(Point(1, 2), Point(10, 20))
# r.drawRect()












