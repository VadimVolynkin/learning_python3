import asyncio
import aiohttp
from time import time


def write_image(data):
    filename = 'images/file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)                                                 # эта запись синхронна


async def fetch_content(url, session):                                   # ассинхронные запросы на сервер
    """Корутина парсит картинки"""
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()                                     # чтение ответа - получаем картинку
        write_image(data)                                                # запись в файл в синхронном режиме



async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []                                                           # список задач

    async with aiohttp.ClientSession() as session:                       # запуск запросов должен быть в сессии
        for i in range(10):                                              # создание списка задач
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)                                     # планирование задач - передача распакованного списка

if __name__ == "__main__":
    asyncio.run(main())                                                  # создание цикла, его запуск и закрытие




