
"""
@classmethod - оперирует классом как объектом.Передает cls первым аргументом.
Работает только с методами и атрибутами этого класса.
Может быть вызван относительно экземпляра.

"""

class Static:
    """
    @staticmethod - это обычная функция(нет self), в пространстве имен класса.
    Не оперирует ни экземплярами, ни классами.
    Может быть вызван из экземпляра и из класса.
    Статический метод можно переопределить в экземпляре, присвоив ему новую функцию.
    """
    __count = 0

    def __init__(self):
        Static.__count +=1    # будет показывать количество созданных экземпляров

    @staticmethod
    def getCount():
        return Static.__count

    @staticmethod
    def summa(x, y):
        print(x + y)


print(type(Static.summa))


# pt = Static()

# def summa(x = 10, y = 5):
#     return x + y

# pt.getCount = summa

# print(Static.getCount())
# print(pt.getCount())







