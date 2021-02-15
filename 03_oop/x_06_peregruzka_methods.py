


class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Need to be int number')

        self.__secs = secs % self.__DAY   # если передано больше суток, покажет остаток


    def getFormatTime(self):
        s = self.__secs % 60               # остаток в секундах
        m = (self.__secs // 60) % 60       # вычисляем кол-во минут и остаток в минутах
        h = (self.__secs // 3600) % 24     # вычисляем часы
        return(f'{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}')

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0' + str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        self.__secs += other.getSeconds()
        return self


    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Need to be Clock class')
        return self.__secs == other.getSeconds()


    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Need to be string')

        if item == 'hour':
            return (self.__secs // 3600) % 24

        elif item == 'min':
            return (self.__secs // 60) % 60

        elif item == 'sec':
            return self.__secs % 60

        return 'Wrong key'


    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Need to be string')

        if not isinstance(value, int):
            raise ValueError('Need to be int')

        s = self.__secs % 60               # остаток в секундах
        m = (self.__secs // 60) % 60       # вычисляем кол-во минут и остаток в минутах
        h = (self.__secs // 3600) % 24     # вычисляем часы

        if key == 'hour':
            self.__secs = s + 60 * m + value * 3600
        elif key == 'min':
            self.__secs = s + 60 * value + h * 3600
        elif key == 'sec':
            self.__secs = value + 60 * m + h * 3600




c1 = Clock(8000)
c2 = Clock(200)
c3 = Clock(200)
# c3 += c1 + c2
# print(c2 == c3)

c1['hour'] = 12
print(c1.getFormatTime())
print(c1['hour'], c1['min'], c1['sec'])








