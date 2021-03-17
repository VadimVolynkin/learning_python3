# https://www.youtube.com/watch?v=4haMUvUxUJI
# https://www.youtube.com/watch?v=ZAEnVbkzLE4
# https://habr.com/ru/post/149077/


import socket

server = socket.socket(                          # сокет - сервер, который отвечает за отправку и принятие сообщений
    socket.AF_INET,                              # семья адресов сокета - inet - интернет адреса
    socket.SOCK_STREAM                           # протоколы взаимодействия с сокетом. SOCK_STREAM - TCP/IP протокол
)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # переиспользовать порт без таймаута после закрытия

server.bind(('127.0.0.1', 1236))                 # даем серверу адрес и порт
server.listen()                                  # может принимать входящие подключения


users = []                                       # список юзеров

def start_server():
    while True:
        # разделяет запрос на адрес и собственный сокет
        user_socket, address = server.accept()       # принимает входящие подключения

        # # передаем сообщение в бинарном коде
        user_socket.send('You are connected'.encode('utf-8'))

        # добавляем текущего юзера в список всех юзеров
        users.append(user_socket)



if __name__ == '__main__':
    start_server()










