"""
# ===== Асинхронность с простыми функциями с помощью select. Событийный цикл ==============================

select - функция для мониторинга готовности файловых объектов и сокетов, любых объектов с методом .fileno() - файловый номер.
Ждет наступления событий с объектами.

1. Создаем серверный сокет и закидыавем его в список для мониторинга.
2. При появлении у сервера входящего подключения, закидываем клиентский сокет в очередь для мониторинга
3. При появлении данных от клиента, вызываем функцию отправки ответа на клиентский сокет.
"""
import socket
from select import select


# список для мониторинга
to_monitor = []

# создаем сервер-сокет
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # переиспользовать порт без таймаута после закрытия
server_socket.bind(('127.0.0.1', 1236))                                # создается файл сокета
server_socket.listen()                                                 # может принимать входящие подключения


def accept_connection(server_socket):
    """
    Сервер принимает входящее соединение
    """
    # разделяет коннект на клиентский сокет и (клиентский адрес, порт)
    client_socket, addr = server_socket.accept()                       # входящий буфер ждет данные о новом подключении
    to_monitor.append(client_socket)                                   # добавляем клиента в список мониторинга
    print('Connection from ', addr)                                    # ('127.0.0.1', 47856) клиентский адрес



def send_message(client_socket):
    """
    Отправляет ответ клиенту
    """
    request = client_socket.recv(4096)              # ждет во входящем буфере данные клиента макс. 4096 байт

    if request:                                     # если что-то есть
        response = 'Hello world\n'.encode()         # формируем ответ в байткоде
        client_socket.send(response)                # send пишет ответ в буфер отправки клиенту
    else:
        client_socket.close()                       # если нет данных - закрываем клиентский сокет


def event_loop():

    while True:
        # select выбирает готовые объекты для чтения, записи, ошибки
        ready_to_read, _ , _ = select(to_monitor, [], [])                # чтение, запись, ошибки

        for sock in ready_to_read:                                       # если чтото есть в списке на чтение
            print(sock)
            if sock is server_socket:                                    # если объект списка является объектом сервера
                accept_connection(sock)                                  # принимаем входящий коннект
            else:
                send_message(sock)                                       # иначе это клиент, тогда шлем сообщение(принимает объект)


if __name__ == '__main__':
    to_monitor.append(server_socket)                                     # добавляем серверный сокет в список
    event_loop()












