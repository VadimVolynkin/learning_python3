"""
# ===== Асинхронность на колбэках с помощью selectors =================================================
selectors - более высокуровневая абстракция над select с вызовом коллбека.

1. Получаем объект селектор по дефолту
2. регистрируем серверный сокет в селектер
3. регистрируем клиентский сокет в селектер
4. Полуаем из селектора готовый для чтения объект(когда в нем что то меняется)
5. Передаем в связанную с объектом функцию связанный с объектом сокет
Если у сервера повляется входящее подключение - то accept_connection - принимаем клиентский сокет и регирстриуем его в селекторе.
Если на клиентском сокете что то появляется, то send_message

"""
import socket
import selectors


# Получаем объект селектор по дефолту
selector = selectors.DefaultSelector()     # <selectors.EpollSelector object at 0x7fb667911f10>

def server():
    # создаем сервер-сокет и сразу регистрируем его в selector
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # переиспользовать порт без таймаута после закрытия
    server_socket.bind(('127.0.0.1', 1236))
    server_socket.listen()

    # регистрируем: серверный сокет(файловый объект), событие(чтение), связанные данные(объект принятия коннекта)
    selector.register(fileobj=server_socket, events=selector._EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    """
    Сервер принимает входящее соединение
    """
    # разделяет коннект на клиентский сокет и кортеж(адрес, порт)
    client_socket, addr = server_socket.accept()                       # принимает входящее подключение
    print('Connection from ', addr)

    # регистрируем: клиентский сокет(файловый объект), событие(чтение), связанные данные(объект отправки сообщений)
    selector.register(fileobj=client_socket, events=selector._EVENT_READ, data=send_message)


def send_message(client_socket):
    """
    Отправляет ответ клиенту
    """
    request = client_socket.recv(4096)              # принимаем переданное сообщение серверу макс 4096 байт

    if request:                                     # если чтото есть
        response = 'Hello world\n'.encode()         # формируем ответ в байткоде
        client_socket.send(response)                # передаем клиенту ответ
    else:
        selector.unregister(client_socket)          # снимаем с регистрации клиентский сокет перед закрытием
        client_socket.close()                       # закрываем клиентский сокет, если нет запроса


def event_loop():

    while True:
        # получаем объекты готовые для чтения или записи
        events = selector.select()                  # key(obj SelectorKey), events(чтение или запись)
        # obj SelectorKey:
        # - fileobj
        # - events
        # - data
        for key, _ in events:
            callback = key.data                     # получаем функцию из поля дата
            callback(key.fileobj)                   # вызываем функцию эту с объектом сокета


if __name__ == '__main__':
    server()
    event_loop()







