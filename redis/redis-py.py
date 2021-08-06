# https://redis-py.readthedocs.io/en/stable/

# ==================================================================================
# REDIS-PY(Клиентская библиотека Python Redis)
# ==================================================================================
# Инкапсулирует ТСР соединение с redis-server, сериализует команды по протоколу Redis (RESP) и отправляет в виде байтов на сервер
# Парсит чистый ответ назад в объект Python в виде байтов, int, или даже datetime.datetime.

pipenv install redis

import redis

# экземпляр редис
# db - номер базы данных, можно создать несколько
r = redis.Redis(host='localhost', port=6379, db=0)


# ===== КЛЮЧИ
redis-py требует передачи ему ключей типа: bytes, str, int или float. Любой из типов нужно сначала сконвертровать в str.
Перед отправкой на сервер последние 3 типа будут конвертированы в байты.


# ===== КОНВЕЙЕРЫ
# Позволяет сократить число двусторонних транзакций(считать или записывать данные сервера Redis). 
# Если вызвать r.hmset() 3 раза, то для этого потребуется повторная операция для каждой строки.
# С конвейером все команды буферизируются в клиентской части pipe.hmset(). 
# Поэтому 3 ответа True вернулись вместе после вызова pipe.execute().
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)           # добавляет операции в pipe
    pipe.execute()                      # выполняет pipe
# [True, True, True]


# ===== ТРАНЗАКЦИИ
# все что между multi и execute будет выполнено или ничего
pipe.multi()
pipe.hincrby(itemid, "quantity", -1)
pipe.hincrby(itemid, "npurchased", 1)
pipe.execute()


# ===== ОПТИМИСТИЧЕСКАЯ БЛОКИРОВКА(optimistic locking)
# вызов функции .watch() ищет изменения в данных, которые записываются в течение удержания блокировки
# если в это время происходит конфликт, вызываемая функция повторяет весь процесс заново
pipe.watch(itemid)


# ===== СРОК ДЕЙСТВИЯ КЛЮЧА

r.setex("name", timedelta(minutes=1), value="bob")  # установка в секундах или объект timedelta
r.psetex("name", time=500, value="bob")             # установка в милисекундах или объект timedelta

r.expire("name", timedelta(seconds=3))              # установка нового таймаута на ключ в секундах или timedelta
r.expireat("name", unixtimeformat)                  # установка нового таймаута на ключ в юникс формате или datetime

r.pexpire("name", 500)                              # установка нового таймаута на ключ в милисекундах или timedelta
r.pexpireat("name", unixtimeformat)                 # установка нового таймаута на ключ в юникс формате или datetime

r.ttl("name")                                       # Срок годности (time to live) в секундах
r.pttl("name")                                      # Срок годности (time to live) в милисекундах

r.persist("name")                                   # удаляет срок действия - делает вечным

# ===== СНЕПШОТИНГ БД
r.bgsave()                                          # вернет True
r.lastsave()                                        # datetime.datetime(2019, 3, 10, 22, 4, 2) дата последнего снепшота
r.save()                                            # синхронное (блокирующее) сохранение



# ===== HASH
r.hset("mykey", "field1", "value1")                 # в питоне это {"mykey": {"field1": "value1"}}



# ===== ШИФРОВАНИЕ
# конфиденциальные данные перед записью в редис можно шифровать с помощью либы cryptography
# данные сначала нужно сериализовать в строку


# ===== СЕРИАЛИЗАЦИЯ
# для сериализации удобно использовать json или yaml
import json
import yaml  # pipenv install PyYAML
r.set(484272, json.dumps(restaurant_484272))
r.set(484272, yaml.dump(restaurant_484272))


