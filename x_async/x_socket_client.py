import socket

# создаем экземпляр клиента
client = socket.socket(                          # сокет - клиент, который отвечает за отправку и принятие сообщений
    socket.AF_INET,                              # семья адресов сокета - inet - интернет адреса
    socket.SOCK_STREAM                           # протоколы взаимодействия с сокетом. SOCK_STREAM - TCP/IP протокол
)

client.connect(('127.0.0.1', 1236))              # коннектимся к адресу нашего сокет-сервера

while True:
    data = client.recv(2048)                     # получать данных в байтах
    print(data.decode('utf-8'))                  # раскодируем









