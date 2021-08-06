# ================================================================================================================================
# DBAPI-ДРАЙВЕРА
# ================================================================================================================================
# По умолчанию без доп. драйверов SQLAlchemy работает только с SQLite.

# MySQL	PyMySQL, MySQL-Connector, CyMySQL, MySQL-Python (по умолчанию)
# PostgreSQL	psycopg2 (по умолчанию), pg8000,
# Microsoft SQL Server	PyODBC (по умолчанию), pymssql
# Oracle	cx-Oracle (по умолчанию)
# Firebird	fdb (по умолчанию), kinterbasdb

# установка драйвера 
pipenv install psycopg2

# ================================================================================================================================
# ПОДГОТОВКА К ПОДКЛЮЧЕНИЮ
# ================================================================================================================================

# ===== СОЗДАНИЕ объекта Engine
# объект Engine отвечает за взаимодействие с базой данных. Состоит из двух элементов: диалекта и пула соединений.
# Диалект отвечает за обработку SQL-инструкций, выполнение, обработку результатов и так далее.
# Пул соединений — это способ кэширования соединений в памяти - это позволяет использовать их повторно(повышение произодительности). 

from sqlalchemy import create_engine

# Подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI. 
engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")

# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI 
engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")

# Подключение к серверу SQLite на localhost 
engine = create_engine('sqlite:///sqlite3.db')  # используя относительный путь
engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь

# ================================================================

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts", 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
# echo	           # True - будет сохранять логи SQL в стандартный вывод. По умолчанию = False.
# pool_size	       # количество соединений для пула. По умолчанию — 5
# max_overflow	   # количество соединений вне pool_size. По умолчанию — 10
# encoding	       # кодировка SQLAlchemy. По умолчанию — UTF-8. Не влияет на кодировку базы данных.
# isolation_level	 # степень изоляции 1 транзакции. Разные базы данных поддерживают разные уровни.

# получение соединения
engine.connect()



# ================================================================================================================================
# СОЗДАНИЕ БД
# ================================================================================================================================

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="1111")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
sql_create_database = 
# Создаем базу данных
cursor.execute('create database sqlalchemy_tuts')
# Закрываем соединение
cursor.close()
connection.close()



# ================================================================================================================================
# СОЗДАНИЕ ТАБЛИЦ
# ================================================================================================================================


from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime

# метадата - данные о таблицах БД
# используется для создания или удаления таблиц
metadata = MetaData()

blog = Table('blog', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(), nullable=False),
    Column('published', Boolean(), default=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

# ===== ограничения 
# primary_key      # True - первичный ключ таблицы. Для создания составного ключа, нужно установить True для каждой колонки.
# nullable	       # False = NOT NULL. по умолчанию True
# default	         # значение по умолчанию, если при вставке данных оно не было передано. Может быть функцией.
# onupdate       	 # значение по умолчанию, если ничего не было передано при обновлении записи. Может быть = default.
# unique	         # True - значение должно быть уникальным
# index	           # True создает индексируемую колонку. По умолчанию False
# auto_increment	 # Добавляет параметр auto_increment. по умолчанию = auto. значение основного ключа будет увеличиваться каждый раз при добавлении новой записи. Если нужно увеличить значение для каждого элемента составного ключа, то этот параметр нужно задать как True для всех колонок ключа. Для отключения поведения нужно установить значение False


# создает таблицы, если их нет 
metadata.create_all(engine)
# удаляет таблицы
metadata.drop_all()



# ================================================================================================================================
# Методы и атрибуты объекта ResultProxy
# ================================================================================================================================
# объект ResultProxy возвращается в результате выполнения запроса
r = conn.execute(query)

fetchone()	
Извлекает следующую запись из результата. Если других записей нет, то последующие вызовы вернут None

fetchmany(size=None)
Извлекает набор записей из результата. Если их нет, то последующие вызовы вернут None

fetchall()
Извлекает все записи из результата. Если записей нет, то вернется None

first()
Извлекает первую запись из результата и закрывает соединение. Это значит, что после вызова метода first() остальные записи в результате получить не выйдет, пока не будет отправлен новый запрос с помощью метода execute()

rowcount
Возвращает количество строк в результате

keys()
Возвращает список колонок из источника данных

scalar()
Возвращает первую колонку первой записи и закрывает соединение. Если результата нет, то возвращает None



# ================================================================================================================================
# CRUD
# ================================================================================================================================


# ===== CREATE 1 - метод insert() экземпляра Table
ins = customers.insert().values(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko'
)
# посмотреть SQL который будет сгенерирован
print(ins)

# создаем объект соединения
conn = engine.connect()

# выполняем инструкцию
# метод вернет объект типа ResultProxy
r = conn.execute(ins)

# первичный ключ вставденной записи
r.inserted_primary_key   


# ===== CREATE 2 - использование функции insert() из библиотеки sqlalchemy

from sqlalchemy import insert

ins = insert(customers).values(
    first_name = 'Valeriy',
    last_name = 'Golyshkin'
)
conn = engine.connect()
r = conn.execute(ins)

print(r.inserted_primary_key)


# ===== CREATE MANY - использование функции insert() из библиотеки sqlalchemy

from sqlalchemy import insert

conn = engine.connect()
ins = insert(customers)

r = conn.execute(ins, [
        {
            "first_name": "Vladimir", 
            "last_name": "Belousov", 
        },
        {
            "first_name": "Tatyana", 
            "last_name": "Khakimova", 
        }
    ])

print(r.rowcount)



# ===== READ 1 - метод select() экземпляра Table

from sqlalchemy import select

conn = engine.connect()

# запрос вернет все записи из таблицы customers
s = customers.select()
print(s)

# запрос может принимать список колонок з которых нужно получить данные
s = select([customers])

# выполнение запроса
r = conn.execute(s)

# fetchall() на объекте ResultProxy возвращает все записи
# fetchall() загружает все результаты в память сразу. В случае большого количества данных это не очень эффективно.
print(r.fetchall())


# ===== READ 2 с фильтром записей where()
# where() может быть несколько
# поддерживаются Побитовые операторы (&, | , ~) и Союзы (and_, or_, not_)

s = select([items]).where(
    items.c.cost_price > 20
)

print(s)
r = conn.execute(s)
print(r.fetchall())


# ===== UPDATE
from sqlalchemy import update

s = update(items).where(
    items.c.name == 'Water Bottle'
).values(
    selling_price = 30,
    quantity = 60,
)

print(s)
rs = conn.execute(s)



# ===== DELETE
from sqlalchemy import delete

s = delete(customers).where(
    customers.c.username.like('Vladim%')
)

print(s)
rs = conn.execute(s)
