
https://webdevblog.ru/porozhdajushhie-shablony-v-python/

https://webdevblog.ru/realizaciya-shablona-singleton-v-python/
# ================================================================================================================
# СТРУКТУРНЫЕ
# ================================================================================================================
# Нарушает принцип единственной ответственности класса.
# Гарантирует наличие единственного экземпляра класса(например доступ к базе).
# Предоставляет глобальную точку доступа. Одиночка гарантирует, что никакой другой код не заменит созданный экземпляр класса.
# Паттерн можно реализовать через базовый класс, декоратор, метакласс.


# ===== Как это работает
# скрывает конструктор
# предоставляет публичный метод для получения экземпляра, если экземпляра нет
# если уже есть - возвращает его


# ================================================================================================================
# НАИВНЫЙ ОДИНОЧКА(НЕБЕЗОПАСНЫЙ В МНОГОПОТОКЕ
# ================================================================================================================
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)   # вызывает родительский класс
            cls._instances[cls] = instance                 # кладет в словарь

        return cls._instances[cls]      # {<class '__main__.Singleton'>: <__main__.Singleton object at 0x7f5697ce1760>}

# какой то класс с логикой
# При создании объекта вызывает метод __call__ родительского класса - тот создаст или вернет объект
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print('I`am Singleton')

# клиентский код
if __name__ == '__main__':
    # создадим 2 объекта
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)                   # True   это один и тот же объект


# ================================================================================================================
# МНОГОПОТОЧНЫЙ ОДИНОЧКА
# ================================================================================================================
from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()                                       # создаем объект блокировки


    def __call__(cls, *args, **kwargs):

        with cls._lock:                                        # здесь доступ к объекту блокируется

            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)   # вызывает родительский класс
                cls._instances[cls] = instance                 # кладет в словарь

        return cls._instances[cls]      # {<class '__main__.Singleton'>: <__main__.Singleton object at 0x7f5697ce1760>}


# какой то класс с логикой
# При создании объекта вызывает метод __call__ родительского класса - тот создаст или вернет объект
class Singleton(metaclass=SingletonMeta):
    value: str = None

    # этот метод и переменная value только для теста
    def __init__(self, value: str) -> None:
        self.value = value


    def some_business_logic(self):
        print('I`am Singleton')


# задача для треда 
def test_singleton(value: str) -> None:
    singleton = Singleton(value)               # создать экземпляр синглтона
    print(singleton.value)                     # показать значение


# клиентский код
if __name__ == '__main__':

    # создадим 2 потока с разными параметрами
    th1 = Thread(target=test_singleton, args=("FOO",)) 
    th2 = Thread(target=test_singleton, args=("BAR",))
    th1.start()        # FOO  поток1 первым создал этот экзепляр
    th2.start()        # FOO  поток2 не смог создать экземпляр с BAR - был блок на вызов метода класса 


































