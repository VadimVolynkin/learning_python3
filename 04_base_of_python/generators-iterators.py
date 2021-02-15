http://toly.github.io/blog/2014/03/05/advanced-design-patterns-in-python/

List comprehensions

# ===== ГЕНЕРАТОРЫ СПИСКОВ =======================================================================================
Генератор списков заключен в квадратные скобки, таким образом, видно что список производится сразу используется обычный итератор, выходное выражение и опциональное условие.

Результирующий список вычисляется и сохраняется в память сразу. Это не проблема для небольших списков, наподобие приведенных выше, или даже списков на порядок больших. Но иногда это может быть неэффективно.

a = [x**2 for x in range(10) if x%2 != 0]
print(a)     # вернет список


# ===== ВЫРАЖЕНИЯ-ГЕНЕРАТОРЫ =====================================================================================
Выражения-генераторы  не хранят в памяти все значения сразу, а генерируют их по мере необходимости, то есть, при проходе к следующему значению. Это избавляет снижает размер занимаемой памяти в больших последовательностях.
В выражении -генераторе нельзя определить число эдементов через len(b) или или получить доступ к отдельному элементу по индексу b[5].
Генератор – это итератор, элементы которого можно перебирать (итерировать) только один раз.

b = (x**2 for x in range(10) if x%2 != 0)
print(b)          # <generator object <genexpr> at 0x0000020E8F429C80>
print(len(b))     # TypeError: object of type 'generator' has no len()
print(b[5])       # TypeError: 'generator' object is not subscriptable
c = list(b)       # make list

# генератор можно итерировать через for
for x in b:
    print(x)


# ===== СОЗДАНИЕ СВОЕГО ГЕНЕРАТОРА ==========================================================================
Генератор – это функция, которая воспроизводит последовательность значений и может использоваться при выполнении итераций.
Слово yield объявляет объект-генератор. У генератора может быть несколько yield.
Объект-генератор выполняет функцию, когда вызывается метод __next__(). Метод работает пока не будет встречена инструкция yield, которая остановит выполнение функции, вернет результат, вернет контроль выполнения потока. При следуюзем вызове next() функция вернет следующий объект последовательности.

def foo(x):
    while 1:
        print(x)
        yield x
        x += 1

c = foo(5)
c.__next__()
c.__next__()


# TODO Сопрограммы и выражения yield ==========================================================
yield может также использоваться как выражение, стоящее справа от оператора присваивания
Закрыть поток входных данных можно вызовом метода close()


# ===== ПРЕОБРАЗОВАНИЕ В ИТЕРАТОР ==============================================================================
Итератор – это объект, который поддерживает функцию next() для перехода к следующему элементу коллекции.
Итерируемый объект – это объект, который позволяет поочередно обойти свои элементы и может быть преобразован к итератору.
Дойдя до конца списка, итератор it не может вернуться в начало и перебрать список еще раз.
Итерируемые типы: множества, списки, кортежи и строки.

a = [1,2,3]
it = iter(a)

print(next(it))
print(next(it))

# ===== СОЗДАНИЕ СВОЕГО КЛАССА ИТЕРАТОРА ==========================================================================

class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit               # max num

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration            # end of iteration

        self.__num += 1
        return self.__num


it = MyIter(10)

for i in it:
    print(i)







