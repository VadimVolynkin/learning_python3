http://pythonicway.com/education/basics/36-design-patterns-python

https://webdevblog.ru/porozhdajushhie-shablony-v-python/
http://toly.github.io/blog/2014/03/05/advanced-design-patterns-in-python/

# ===== НАБЛЮДАТЕЛЬ ====================================================================
class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.observers = set()

    def __del__(self):
        for ob in self.observers:
            ob.close()
        del self.observers

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def withdraw(self, amt):
        self.balance -= amt
        self.notify()



import weakref
class AccountObserver(object):

    def __init__(self, theaccount):
        self.accountref = weakref.ref(theaccount) # Создаст слабую ссылку
        theaccount.register(self)

    def __del__(self):
        acc = self.accountref()                   # Вернет объект счета
        if acc:                                   # Прекратить наблюдение, если существует
            acc.unregister(self)

    def update(self):
        print(f"Баланс: {self.accountref().balance}")

    def close(self):
        print("Наблюдение за счетом окончено")

# Пример создания
a = Account("Дейв",1000.00)
a_ob = AccountObserver(a)
a_ob.update()


# ===== МОНОСОСТОЯНИЕ ====================================================================

class Cat:
    __shared_attr = {
        'breed': 'pers'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr   # присваевает экземплярам 1 атрибут-словарь для всех экземпляров


a = Cat()
b = Cat()
# print('a breed', a.breed)
# print('b breed', b.breed)

# b.breed = 'siam'

# print('a breed', a.breed)
# print('b breed', b.breed)


# ===== СИНГЛТОН ====================================================================

class SingltonVar1:
    """
    При попытке создать несколько экземпляров класса, новый объект не будет создан,
    переменным будут присвоены ссылки на один и тот же объект.

    Такую реализацию Сингтона можно обойти через наследование и перегрузку метода.
    """
    __instance = None

    def __new__(cls, *args, **kwargs):                                 # cls ссылается на класс SingltonVar1
        """Метод выполняется перед созданием экземпляра класса"""

        # если __instance не равно SingltonVar1
        if not isinstance(cls.__instance, cls):

            # 1. создаем экземпляр класса - вызываем метод __new__ базового класса
            # 2. присваеваем ссылку на него атрибуту класса __instance
            cls.__instance = super(SingltonVar1, cls).__new__(cls)
        else:
            print('Экземпляр класса SingltonVar1 уже создан')

s = SingltonVar1()
s2 = SingltonVar1()









