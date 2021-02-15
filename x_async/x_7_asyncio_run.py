import asyncio
"""
asyncio - фреймворк, он выполняет задачу создания событийных циклов.

1. Создаем корутины(логику программы) async def some_coroutine()
2. Оборачиваем корутины в экземпляры класса Task  task1 = asyncio.create_task(some_coroutine())
3. Ставим экземпляры Task в очередь на выполнение. await asyncio.gather(task1, task2)
4. Запускаем событийный цикл, дожидаемся выполнения и закрываем цикл asyncio.run(main())
"""



# =========================================================================================================
# EVENT LOOP
# =========================================================================================================

async def myCoroutine():
    while True:
        await asyncio.sleep(1)
        print('hello')


async def secondCoroutine():
    while True:
        await asyncio.sleep(2)
        print('world')

loop = asyncio.get_event_loop()                             # create loop

try:
    asyncio.ensure_future(myCoroutine())                    # create future an object
    asyncio.ensure_future(secondCoroutine())
    loop.run_forever()                                      # run loop nonstop
except KeyboardInterrupt:
    pass
finally:
    print('Closing Loop')
    loop.close()                                            # close loop



# =========================================================================================================
# TASK: EXAMPLE 1
# =========================================================================================================
import asyncio
import time

async def myTask():
    time.sleep(1)                                  # not async - will be wait before run next task
    print('hello')
    for task in asyncio.all_tasks():               # cancel all panding task. Only the first task will be completed.
        task.cancel()

async def taskGenerator():
    for i in range(5):
        asyncio.create_task(myTask())              # create from coroutine task object
        # pending = asyncio.all_tasks()            # show pending tasks
        # print(pending)


asyncio.run(taskGenerator())                       # create loop, run and close
# print('All tasks were completed')


# =========================================================================================================
# TASK: EXAMPLE 2
# =========================================================================================================
import asyncio
import time

async def myTask(number):
    time.sleep(1)                                  # not async - will be wait before run next task
    return number * 2


async def main(coros):
    for futures in asyncio.as_completed(coros):     # iter coros
        print(await futures)                        # print future as it will be completed


coros = [myTask(i) for i in range(3)]               # create list of coroutines
print(coros) # [<coroutine object myTask at 0x7f89dcfe6840>, <coroutine object myTask at 0x7f89d99f0640>, .....]

loop = asyncio.get_event_loop()                     # create loop
loop.run_until_complete(main(coros))                # run loop until comlete a list of coros (1 loop)
print('All tasks were completed')
loop.close()                                        # close loop

# =========================================================================================================
# TODO SYNCHRONIZATION: LOCKS and QUEUES
# =========================================================================================================


https://www.youtube.com/watch?v=HLc9TopRPII&list=PLzUGFf4GhXBLEQsoOfLzhH6JKybt8I5Ec&index=6


















