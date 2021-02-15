# https://docs.mongodb.com/drivers/python/
# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://www.youtube.com/watch?v=rE_bJl2GAY8
https://www.youtube.com/playlist?list=PL0lO_mIqDDFXcxN3fRjc-EOWZLqW8dLVV


mongoengine
motor
pymongo



# TODO select, update, delete, insert
# TODO drop db if exist and createdb
# TODO Indexing
# TODO transaction
# TODO docker https://phoenixnap.com/kb/docker-mongodb
# TODO import export
# TODO create drop...



"""

В MongoDB документ представляет собой просто JSON-подобный двоичный формат сериализации, называемый BSON или Binary-JSON, и имеет максимальный размер 16 мегабайт.

MongoDB также предоставляет спецификацию GridFS в случае необходимости хранить файлы, размер которых превышает установленное ограничение.

высокую масштабируемость за счет эффективного масштабирования по горизонтали за счет разделения данных и размещения их на нескольких компьютерах.

не поддерживает отношения между сохраненными данными. Из-за этого трудно выполнять транзакции ACID, которые обеспечивают согласованность.

MongoDB является более подходящим, чем реляционная база данных, - это когда формат данных является гибким и не имеет отношений.

не подходит использовать MongoDB, если нам нужно соблюдать свойства ACID.



mongodb://127.0.0.1:27017









типов данных, таких как Date и Binary Data
"""


# импортируем pymongo
import pymongo
from pymongo.mongo_client import MongoClient

# соединяемся с сервером базы данных
# (по умолчанию подключение осуществляется на localhost:27017)
conn = pymongo.Connection()

# подключаемся к другому серверу, на другой порт
conn = pymongo.Connection('localhost', 27017)

# выбираем базу данных
db = conn.mydb

# БД можно выбрать и так
db = conn['mydb']

# выбираем коллекцию документов
coll = db.mycoll
coll = db['mycoll']

# осуществляем добавление документа в коллекцию,
# который содержит поля name и surname - имя и фамилия
doc = {"name":"Иван", "surname":"Иванов"}
coll.save(doc)

# альтернативное добавление документа
coll.save({"name":"Петр", "surname":"Петров"})

# выводим все документы из коллекции coll
for men in coll.find():
    print men

# выводим фамилии людей с именем Петр
for men in coll.find({"name": "Петр"})
    print men["surname"]

# подсчет количества людей с именем Петр
print coll.find({"name": "Петр"}).count()

# добавляем ко всем документам новое поле sex - пол
coll.update({}, {"$set":{"sex": "мужской"}})

# всем Петрам делаем фамилию Новосельцев и возраст 25 лет
coll.update({"name": "Петр"}, {"surname": "Новосельцев", "age": 25})

# увеличиваем всем Петрам возраст на 5 лет
coll.update({"name": "Петр"}, {"$inc": {"age": 5}})

# сбрасываем у всех документов поле name
coll.update({}, {"$unset": {"name": 1}})

# удаляем людей с возрастом более 20 лет
# другие условия $gt - больше, $lt - меньше,
# $lte - меньше или равно, $gte - больше или равно, $ne - не равно
coll.remove({"age": {"$gt": 20}})

# удаляем все документы коллекции
coll.remove({})











