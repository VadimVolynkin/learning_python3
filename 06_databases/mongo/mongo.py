# https://docs.mongodb.com/drivers/python/
# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://www.youtube.com/watch?v=rE_bJl2GAY8
https://www.youtube.com/playlist?list=PL0lO_mIqDDFXcxN3fRjc-EOWZLqW8dLVV


pymongo
mongoengine
motor




# TODO select, update, delete, insert
# TODO drop db if exist and createdb
# TODO Indexing
# TODO transaction
# TODO docker https://phoenixnap.com/kb/docker-mongodb
# TODO import export
# TODO create drop...



"""

Монго хорошо подходит для данных, коорые не нужно структурировать и связывать.
Хрант данные в BSON - бинарный json.

Кластер - содержит БД. Кластеров может быть несколько для повышения отказоустойчивости.

БД - содержит коллекции

Коллекции - как таблицы в sql, но без структуры. 
Коллекции содержат объекты-документы. 

Документы - строка данных в json - по аналогии со строкой в sql. 
Каждый документ имеет уникальный uuid по аналогии с pk в sql.


# ===== Создание кластера
https://cloud.mongodb.com/v2/5d012375553855335a9c0b62#clusters

# строка коннекта
mongodb+srv://user_express:<password>@cluster0.eycxr.mongodb.net/test



В MongoDB документ представляет собой просто JSON-подобный двоичный формат сериализации, называемый BSON или Binary-JSON, и имеет максимальный размер 16 мегабайт.

MongoDB также предоставляет спецификацию GridFS в случае необходимости хранить файлы, размер которых превышает установленное ограничение.

высокую масштабируемость за счет эффективного масштабирования по горизонтали за счет разделения данных и размещения их на нескольких компьютерах.

не поддерживает отношения между сохраненными данными. Из-за этого трудно выполнять транзакции ACID, которые обеспечивают согласованность.

MongoDB является более подходящим, чем реляционная база данных, - это когда формат данных является гибким и не имеет отношений.

не подходит использовать MongoDB, если нам нужно соблюдать свойства ACID.




"""



# ===================================================================
# СОЗДАНИЕ КОННЕКТА
# ===================================================================
from pymongo import MongoClient
import pymongo

# ===== Создание клиента с подключением к докер контейнеру
client = MongoClient('mongodb://localhost', 27017,
                    username='root',
                    password='example')

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")


# ===== Создание клиента с подключением Mongo atlas
# pipenv install pymongo[srv]

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://user_express:PASSWD@cluster0.eycxr.mongodb.net/test"

# set a 5-second connection timeout
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")


# ===================================================================
# CREATE NEW (INSERT)
# ===================================================================
# создание БД
db = client.testdata
# создание коллекции
coll = db.users

# === данные для записи
# _id - явно задает id иначе монго сгенерит его в виде 6135f403b2bc1798b1ae83b0
# post = {'name': 'test name'}
post = {'_id': 1, 'name': 'test name2'}
post_list = [
    {
        '_id': 5, 
        'name': 'test name5',
        'time': datetime.datetime.now(),
        'status': True,
        'flags': [1, 2, 3]

    },
    {
        '_id': 6,
        'name': 'test name6',
        'time': datetime.datetime.now()
    }
]



# === insert_one(document, bypass_document_validation=False, session=None)
# bypass_document_validation - разрешает запись без проверки документа
# inserted_id - номер поста
post_id = coll.insert_one(post).inserted_id

# === insert_many(documents, ordered=True, bypass_document_validation=False, session=None)
post_ids = coll.insert_many(post_list).inserted_ids
print(post_ids)

# === добавляем ко всем документам новое поле sex - пол
coll.update({}, {"$set":{"newfield": "some text"}})


# ===================================================================
# READ (FIND)
# ===================================================================

# === find(filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False, cursor_type=CursorType.NON_TAILABLE, sort=None, allow_partial_results=False, oplog_replay=False, modifiers=None, batch_size=0, manipulate=True, collation=None, hint=None, max_scan=None, max_time_ms=None, max=None, min=None, return_key=False, show_record_id=False, snapshot=False, comment=None, session=None, allow_disk_use=None)

# все записи коллекции
coll.find()

# посчитать количество записей коллекции всего и по значению
coll.count_documents({})
coll.count_documents({'name': 'ivan'})

# посчитать количество коллекций
client.list_database_names()

# поиск по ключу
# limit(3) - ограничит поиск 3 результатами
# sort('name', -1) - сортирует по полю name по убыванию
# skip пропустит первые найденные
query = {'status': True}
coll.find(query).limit(3).sort('name', -1)
coll.find(query).skip(3).sort('name', -1)

# поиск по ключу
query = {'status': True}
coll.find(query)

# поиск по ключу выводом только указанных полей
# _id: 0 позволяет скрыть _id, чтобы скрыть остальные - нужно их не указывать
query = {'status': True}
coll.find(query, {'_id': 0, 'status': 1})

# поиск по ключу со значением начинащимся с буквы а или буквы после а по алфавиту
query = {'name': {'$gt': 'a'}}
coll.find(query)

# поиск по решулярным выражениям
# ищет слово начинаюзееся с text, * или . означает любые символы
query = {'name': {'$regex': 'text*'}}
query = {'name': {'$regex': 'text.'}}
coll.find(query)


# === find_one(filter=None, *args, **kwargs)

# вернет первую запись в коллеции
coll.find_one()

# вернет первую запись найденную по значению
query = {'name': 'text'}
coll.find_one(query)


# ===================================================================
# UPDATE
# ===================================================================
current = {'name': 'test3'}
new_data = {'$set': {'name': 'newtest3'}}

# ищет 1 документ по ключ-значение и меняет значение
coll.update_one(current, new_data)

# ищет все документы по ключ-значение и меняет в них значения
coll.update_many(current, new_data)

# инкремент
# найдет документ с ид = 1 и сделает инкремент поля balance
current = {'_id': 1}
new_data = {'$inc': {'balance': 100}}
coll.update_one(current, new_data)

# удаляет из списка flags элемент с индексом 0
# в pop нужно использовать индексы
current = {'_id': 1}
new_data = {'$pop': {'flags': 0}}
coll.update_one(current, new_data)

# удаляет из списка flags элемент с значением 0
# в pull нужно использовать значение
current = {'_id': 1}
new_data = {'$pull': 1}
coll.update_one(current, new_data)


# ===================================================================
# DELETE(DROP)
# ===================================================================

# удалить коллекцию
coll.drop()

# удалить 1 запись
coll.delete_one({'_id': 0})

# удалит все записи коллекции
# deleted_count - покажет сколько удалил
coll.delete_many({}).deleted_count

# удалит все записи с name = test
res = coll.delete_many({'name': 'test'})

# удалит все записи с name, в которых используется new
coll.delete_many({'name': {'$regex': 'new'}})


# ===================================================================
# ИНДЕКСЫ
# ===================================================================
# в 1 коллекцию нельзя добавить более 60 индексов
# поле id - индекс по умолчанию


from itertools import count

# создание данных для примера
for i in count(0, 1):
    data = {
        'id': i,
        'login': f'name{i}',
        'password': f'passw{i}',
        'time': datetime.datetime.now(),
    }
    coll.insert_one(data)
    print(f"{i}: данные записаны")


# создание индекса с обратным порядком
coll.create_index([('login', pymongo.DESCENDING)])

# создание индекса с по алфавиту с уникальным значением логина, иначе ошибка
coll.create_index([('login', pymongo.ASCENDING)], unique=True)

# покажет все индексы - сейчас их 2: _id_ и login_-1
print(coll.index_information())
# {'_id_': {'v': 2, 'key': [('_id', 1)]}, 'login_-1': {'v': 2, 'key': [('login', -1)]}}

# удаление индекса login_-1
coll.drop_index('login_-1')
# {'_id_': {'v': 2, 'key': [('_id', 1)]}}


# ===================================================================
# ТРАНЗАКЦИИ
# ===================================================================
# Транзакции монго работают на уровне документа.
# Монго поддерживает многодокументные транзакции в пределах replicaSet
# Распределенные транзакции.


# ===================================================================
# ОПЕРАТОРЫ
# ===================================================================

# меньше чем, больше чем
coll.find({"price": {"$lt": 1000}})
coll.find({"price": {"$gt": 1000}})

# больше или равно, меньше или равно
coll.find({"price": {"$gte": 1000}})
coll.find({"price": {"$lte": 1000}})

# равно - неравно
coll.find({"price": {"$eq": 1000}})
coll.find({"price": {"$ne": 1000}})

# все товары с ценой 5, 10, 15
# все товары у коорых цена не  5, 10, 15
coll.find({"price": {"$in": [5, 10, 15]}})
coll.find({"price": {"$nin": [5, 10, 15]}})

# найдет все с ценой меньше 500 или распродажа=True
coll.find({'$or': [{'price': {'$lt': 500}}, {'sales': True}]})

# найдет все с ценой меньше 500 и распродажа=True
coll.find({'$and': [{'price': {'$lt': 500}}, {'sales': True}]})

# ищет документы в которых есть это поле
coll.find({'sales': {'$exists': True}})











