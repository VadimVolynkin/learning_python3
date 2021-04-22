# ================================================================================================================
# PROTOTYPE
# ================================================================================================================
# Порождающий паттерн
# Позволяет копировать объекты со всем его содержимым(методы, атрибуты)
# Позволяет создавать объекты из объектов, а не из класса.


# ===== Как работает
# Создает общий для всех объектов интерфейс - метод clone(). 
# Он создает новый объект этого же класса, копирует в него значение всех полей и отдает его.


# ===== Когда применять
# Когда код не должен зависеть от классов копируемых объектов.
# Когда есть много подклассов с разными начальными значениями полей, их можно заменить на набор прототипов для производства из них новых объектов.


# ================================================================================================================
# Концептуальный пример
# ================================================================================================================
import copy


class SomeComponent:
    def __init__(self, name, age, somelist):
        self.name = name
        self.age = age
        self.somelist = somelist

    def __copy__(self):                                       # метод создает неглубокую копию списка
        somelist = copy.copy(self.somelist)                   

        new = self.__class__(self.name, self.age, somelist)   # создает новый объект с тем же конфигом
        new.__dict__.update(self.__dict__)                    # кладет словарь прототипа в словарь нового объекта
        return new

    def __deepcopy__(self, memo={}):
        somelist = copy.deepcopy(self.somelist)               # создает глубокую копию списка

        new = self.__class__(self.name, self.age, somelist)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)     # создает глубокую копию словаря прототипа
        return new



if __name__ == '__main__':

    name = 'Ivan'
    age = 30
    somelist = [1,2,3,4,5]

    # создадим объект-прототип 
    prototype_a = SomeComponent(name, age, somelist)
    print(prototype_a.__dict__)                         # {'name': 'Ivan', 'age': 30, 'somelist': [1, 2, 3, 4, 5]}


    # создадим простую копию прототипа
    new_a = prototype_a.__copy__()
    print(new_a.__dict__)                               # {'name': 'Ivan', 'age': 30, 'somelist': [1, 2, 3, 4, 5]}


    # неглубокая копия создает просто ссылки на старый объект 
    print(id(prototype_a.somelist))                     # 94291695696544  
    print(id(new_a.somelist))                           # 94291695696544   это тот же объект


    # изменение в одном - изменяет значение во втором
    new_a.somelist[0] = 55
    print(prototype_a.somelist)                         # [55, 2, 3, 4, 5]
    print(new_a.somelist)                               # [55, 2, 3, 4, 5]
    

    # создадим объект глубокого копирования и повторим проверку
    new_deep_a = prototype_a.__deepcopy__()

    print(id(prototype_a.somelist))                     # 140460665903424
    print(id(new_deep_a.somelist))                      # 140460643391296   теперь это разные объекты
    

    # изменение в одном - НЕ изменяет значение во втором
    new_deep_a.somelist[0] = 999
    print(prototype_a.somelist)                         # [55, 2, 3, 4, 5]
    print(new_deep_a.somelist)                          # [999, 2, 3, 4, 5]




# ================================================================================================================
# КОПИЯ ЧЕРЕЗ DEEPCOPY
# ================================================================================================================
# copy.deepcopy() создает полную глубокую копию объекта с приватными полями

class ProtoB:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


proto_b = ProtoB("Ivan", 40)
deep_copy_b = copy.deepcopy(proto_b)

proto_b._ProtoB__name = 'Igor'

print(proto_b.__dict__)                            # {'_ProtoB__name': 'Igor', '_ProtoB__age': 40}
print(deep_copy_b.__dict__)                        # {'_ProtoB__name': 'Ivan', '_ProtoB__age': 40}




















