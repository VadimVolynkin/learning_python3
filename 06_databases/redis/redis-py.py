# https://redis-py.readthedocs.io/en/stable/

# ==================================================================================
# REDIS-PY(Клиентская библиотека Python Redis)
# ==================================================================================
# Инкапсулирует ТСР соединение с redis-server, сериализует команды по протоколу Redis (RESP) и отправляет в виде байтов на сервер
# Парсит чистый ответ назад в объект Python в виде байтов, int, или даже datetime.datetime.

pipenv install redis

import redis

Типы клиентов Редис:
redis.Redis()           # обратно совместимая со старыми версиями Redis с любыми наборами данных
redis.StrictRedis()     # пытается правильно применять типы данных

# создание клиента
# decode_responses=True избавит необходимости явно расшифровывать каждое значение из базы
# db - номер базы данных, можно создать несколько
r = redis.StrictRedis(
    host='localhost',
    port=6379,
    password='qwerty',
    charset="utf-8",
    decode_responses=True,
    db=0
)


# ==================================================================================
# ОПЕРАЦИИ С ТИПАМИ В REDIS-PY
# ==================================================================================





r.delete('key')                          # удаляет ключ



# ===== STRING =====================================================================

r.set('index', '1')                      # создать строковое значение
r.get('index')                           # получить значение - 1 <class 'str'>

r.incr('index')                          # увеличить строку на 1
r.decr('index')                          # уменьшить строку на 1

r.incrby('index', 3)                     # увеличить строку на 3
r.decrby('index', 5)                     # уменьшает строку на 5

r.mset({"name": "Bob", "age": "30"})     # установка нескольких ключей одной командой
r.mget("name", "age")                    # ['Bob', '30'] писок значений ключа, оба значения - строки

r.getset("index", 15)                    # устанавливает новое значение и возвращает старое


# ===== BIT ARRAY ============================================================================
# key - любой ключ
# номер бита
# булево значение. 1 или чтото = True, 0 = False

r.setbit('key', 1, 1)                   # установка трех битов
r.setbit('key', 2, 'somevalue')
r.setbit('key', 3, 0)

r.getbit('key', 3)                      # 0(0 = False = 0), вернет булево значение бита 3 в виде цифры

r.bitcount('key')                       # 2, подсчет offset c значением 1


# ===== LIST ============================================================================

r.lpush('my_list', 'A')                            # добавляет элемент в список слева
r.rpush('my_list', 'B')                            # добавить вторую строку в список справа
r.rpush('my_list', 'C')                            # добавить третью строку в список справа

r.lrange('my_list', 0, -1)                         # показать элементы с первого до последнего

r.lrem('my_list', 1, 'C')                          # удалить из списка 1 экземпляр, значение которого "C"
r.rpush('my_list', r.lpop('my_list'))              # вытащить первый элемент нашего списка и переместить его в конец

r.lpop('my_list')                                  # удалит элемент слева и вернет его значение
r.rpop('my_list')                                  # удалит элемент справа и вернет его значение

r.llen("my_list")                                  # вернет кол-во элементов в списке

r.blpop('my_list', 5)                              # блокирует LPOP вызов если список пуст, ждет 5 сек и возвращает(None)


# ===== SET ============================================================================

# Добавить элемент в set 1
r.sadd('my_set_1', 'Y')
print(f"my_set_1: {r.smembers('my_set_1')}")

# Добавить элемент в set 1
r.sadd('my_set_1', 'X')
print(f"my_set_1: {r.smembers('my_set_1')}")

# Добавить элемент в set 2
r.sadd('my_set_2', 'X')
print(f"my_set_2: {r.smembers('my_set_2')}")

# Добавить элемент в set 2
r.sadd('my_set_2', 'Z')
print(f"my_set2: {r.smembers('my_set_2')}")

# Объединение set 1 и set 2
print(f"sunion: {r.sunion('my_set_1', 'my_set_2')}")

# Пересечение set 1 и set 2
print(f"sinter: {r.sinter('my_set_1', 'my_set_2')}")


# ===== SORTED SET =====================================================================

# Создали отсортированный set с 3 значениями
r.zadd('top_songs_set', {'Never Change - Jay Z': 1,
                         'Rich Girl - Hall & Oats': 2,
                         'The Prayer - Griz': 3})
print(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}")

# Добавили элемент в set с конфликтующим значением
r.zadd('top_songs_set', {"Can't Figure it Out - Bishop Lamont": 3})
print(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}")

# Индекс сдвига значения
r.zincrby('top_songs_set', 3, 'Never Change - Jay Z')
print(f"top_songs_set: {r.zrange('top_songs_set', 0, -1)}")



# ===== HASH =====================================================================

record = {
    "name": "vadim",
    "age": 30,
    "city": "moscow"
}
r.hset('person', mapping=record)              # создает словарь в редисе
r.hmget('person', ('name', 'age'))            # ['vadim', '30']
r.hgetall('person')                           # {'name': 'vadim', 'age': '30', 'city': 'moscow'}



# ===== SET =====================================================================

r.sadd('my_set_1', 'Y')                # {'Y', 'X'} добавить элемент в set 1
r.sadd('my_set_1', 'X')       
res = r.smembers('my_set_1')

r.sadd('my_set_2', 'X')                # {'X', 'Z'} добавить элемент в set 2
r.sadd('my_set_2', 'Z')                          
res = r.smembers('my_set_2')

r.sunion('my_set_1', 'my_set_2')       # {'Z', 'X', 'Y'}, объединение set 1 и set 2
r.sinter('my_set_1', 'my_set_2')       # {'X'}, пересечение set 1 и set 2
r.sismember('my_set_1', 'Y')           # True, проверка наличия 'Y' в 'my_set_1'

r.spop('my_set_1')                     # вернет случайный элемент и удалит его
r.srandmember('my_set_1')              # вернет случайный элемент и не удалит его

r.sunionstore('newset', 'my_set_1', 'my_set_2')  # объединит 2 сета и создаст новый
r.sunionstore('newset', 'my_set_1')              # сделает копию сета

r.scard('my_set_1')                              # 2 - количество элементов


# ===== SORTED SET =====================================================================

r.zadd('hot_tours', {'tour1': 999, 'tour2': 222, 'tour3': 500})  # создает сортированный список             

r.zrange('hot_tours', 0, -1)                  # ['tour2', 'tour3', 'tour1'] сортирует от меньшего к большему
r.zrevrange('hot_tours', 0, -1)               # ['tour1', 'tour3', 'tour2'] сортирует от большего к меньшему

r.zrange('hot_tours', 0, -1, withscores=True) # [('tour2', 222.0), ('tour3', 500.0), ('tour1', 999.0)] сортирует от меньшего к большему

r.zrangebyscore('hot_tours', min=300, max=1000)# ['tour3', 'tour1'] сортирует промежуток по цене 

r.zrank('hot_tours', 'tour2')                  # 0 индекс элемента в отсортированном списке








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

# ===== ШИФРОВАНИЕ
# конфиденциальные данные перед записью в редис можно шифровать с помощью либы cryptography
# данные сначала нужно сериализовать в строку


# ===== СЕРИАЛИЗАЦИЯ
# для сериализации удобно использовать json или yaml
import json
import yaml  # pipenv install PyYAML
r.set(484272, json.dumps(restaurant_484272))
r.set(484272, yaml.dump(restaurant_484272))







# ===== HASH ==============================================================================

r.hset("mykey", "field1", "value1")                 # в питоне это {"mykey": {"field1": "value1"}}
