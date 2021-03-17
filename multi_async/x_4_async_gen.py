# https://www.youtube.com/watch?v=hOP9bKeDOHs&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=5

"""
# ===== Асинхронность на генераторах с помощью select =================================================
1. Закидываем генератор-сервер в список задач.
2. Берем из задач первый генератор-сервер, удаляем из задач, делаем с ним next(), получаем кортеж (причина, сокет),
закидываем его в словарь для чтения { сокет: генератор-сервер, ...}
3. При изменении в словаре to_read серверного сокета, по сокету закидываем генератор-сервер в список задач.
Удаляем его из списка задач, выполняется next() и принимается клиентский сокет, в список задач добавляется генератор-клиент.
4. Берем из задач первый генератор-клиент, удаляем из задач, делаем с ним next() отрабатывает клиентский код

"""
import socket
from select import select                            # выбирает готовые объекты

tasks = []                                           # список задач из генераторов

to_read = {}                                         # {'сокет5': 'генератор1', 'сокет6': 'генератор1', ...} для чтения
to_write = {}                                        # для записи


def server():
    """Генератор Клиент отдает кортеж"""

    server_socket = socket.socket(                   # сокет - сервер, который отвечает за отправку и принятие сообщений
        socket.AF_INET,                              # семья адресов сокета - inet - интернет адреса
        socket.SOCK_STREAM                           # протоколы взаимодействия с сокетом. SOCK_STREAM - TCP/IP протокол
    )
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # переиспользовать порт без таймаута после закрытия

    server_socket.bind(('127.0.0.1', 1236))                 # даем серверу адрес и порт
    server_socket.listen()                                  # может принимать входящие подключения

    while True:
        print('wait next server')
        yield ('read', server_socket)                       # вернем кортеж
        client_socket, addr = server_socket.accept()        # принимаем сокет и делаем кортеж(клиентский сокет, адрес)
        print('Connection from', addr)

        tasks.append(client(client_socket))                 # добавим генератор клиента в список задач
        print('Added client task', tasks)


def client(client_socket):
    """Генератор Клиент отдает кортеж"""

    while True:
        yield ('read', client_socket)                              # вернет кортеж для чтения
        request = client_socket.recv(4096)                         # читаем клиентский сокет

        if not request:
            break
        else:
            response = 'HelloWorlf\n'.encode()                     # если что то есть - готовим ответ клиенту
            yield ('write', client_socket)                         # вернет кортеж для записи
            client_socket.send(response)                           # отправит ответ клиенту

    client_socket.close()



def event_loop():
    while any([tasks, to_read, to_write]):                                    # пока что то есть
        # блок обработки словарей
        while not tasks:                                                      # пока нет задач (буфер-список пуст)
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])  # списки наполняются готовыми сокетами

            # получает по сокету генератор, удаляет пару из словаря и добавляет генератор в tasks
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        # блок сортировки задач в словари чтения и записи
        try:                                       # если есть задачи типа генератор
            task = tasks.pop(0)                    # берем первый генератор и удаляем его из списка задач
            reason, sock = next(task)              # делаем next - получаем кортеж (причина, сокет)
            print('Task after next', tasks)

            # сортируем задачи по причинам, добавляем в словари пары { сокет: генератор, ...}
            if reason == 'read':
                to_read[sock] = task

            if reason == 'write':
                to_write[sock] = task

            print('Added pairs', to_read)

        except StopIteration:                      # если задач нет - выходим из итерации
            print("Done")

        print('============== LOOP ==============')



tasks.append(server())                             # закидываем генератор-сервер в задачи
event_loop()


















