import unittest


# Модульные тесты
class TestSplitFunction(unittest.TestCase):

    def setUp(self):
    # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
    # Выполнить завершающие действия (если необходимо)
        pass

    def testsimplestring(self):
        r = splitter.split(‘GOOG 100 490.50’)
        self.assertEqual(r,[‘GOOG’,’100’,’490.50’])

    def testtypeconvert(self):
        r = splitter.split(‘GOOG 100 490.50’,[str, int, float])
        self.assertEqual(r,[‘GOOG’, 100, 490.5])

    def testdelimiter(self):
        r = splitter.split(‘GOOG,100,490.50’,delimiter=’,’)
        self.assertEqual(r,[‘GOOG’,’100’,’490.50’])

# Запустить тестирование
if __name__ == ‘__main__’:
    unittest.main()




===============================================================================



import time

start_cpu = time.clock()
start_real= time.time()

инструкции
инструкции

end_cpu = time.clock()
end_real = time.time()
print('Действительное время в сек. %f '.format(end_real – start_real))
print('Процессорное время в сек. %f '.format(end_cpu - start_cpu))





===============================================================================


from timeit import timeit
timeit('math.sqrt(2.0)','import math')
















