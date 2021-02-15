

"""
Функторы - объекты класса, которые можно выполянть как функции.
Для создания функтера нужно определить метод __call__


"""


class Counter:

    def __init__(self):
        self.__counter = 0   # счетчик вызова экземпляра класса

    def __call__(self, *args, **kwargs):
        """
        Этот функтер считает количество вызовов экземпляра
        Каждый экземпляр имеет свой независимый счетчик.
        """
        self.__counter +=1
        print(self.__counter)
        return self.__counter

# c1 = Counter()
# c2 = Counter()

class StripChars:
    def __init__(self, chars):
        self.__chars = chars                          # chars - рока символов дял удаления '/?:;!,.* '


    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):              # args[0] строка для удаления символов '. Hello world! '
            raise ValueError('Need to be string')
        return args[0].strip(self.__chars)


# s1 = StripChars('/?:;!,.* ')

# print(s1('. Hello world! '))







