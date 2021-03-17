

# =====================================================================================================
# Синхронизация потоков при помощи threading.Timer().
# Создает таймер, который будет запускать функцию function по прошествии interval секунд. 
# Является подклассом threading.Thread() и, как таковой, также служит примером создания пользовательских потоков.
# =====================================================================================================


import threading

timer = threading.Timer(
  interval,                   # интервал запуска вызываемого объекта (функции)
  function,                   # вызываемый объект (функция)
  args=None,
  kwargs=None
  )


Timer.cancel()
# Останавливает таймер и отменяет выполнение действия таймера, если таймер все еще находится в стадии ожидания. 


def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()



# =====================================================================================================
# Пример threading.Timer().
# =====================================================================================================

import threading, time

def delayed():
    th_name = threading.current_thread().name
    print(f'Th:{th_name} Worker запущен')


# Создание и запуск потоков таймеров
t1 = threading.Timer(5, delayed)
t1.name = 'Timer-1'
t2 = threading.Timer(5, delayed)
t2.name = 'Timer-2'

print('Запуск таймеров')
t1.start()
t2.start()

# отмена второго потока-таймера через 0.2 сек после его старта (до его срабатывания)
print(f'Ожидание перед завершением {t2.name}')
time.sleep(0.2)
print(f'Завершение {t2.name}')
t2.cancel()

print('Все Выполнено')
























