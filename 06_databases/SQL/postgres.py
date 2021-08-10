
# TODO Управление транзакциями в PostgreSQL
https://pythonru.com/biblioteki/tranzakcii-postgres-v-python


# https://www.postgresqltutorial.com/
# https://khashtamov.com/ru/postgresql-python-psycopg2/
# https://eax.me/tag/postgresql/
# OpenStreetMap https://eax.me/postgis/
# PgBouncers https://eax.me/pgbouncer/
# https://eax.me/postgresql-replication/


import psycopg2


https://ru.wikipedia.org/wiki/PostgreSQL

# TODO drop db if exist and createdb
высокопроизводительные и надёжные механизмы транзакций и репликации;
один из встроенных языков - питон.
поддерживает наследрвание
PostGIS;
JSON с возможностью их индексации
PostgreSQL поддерживает одновременную модификацию БД несколькими пользователями с помощью механизма Multiversion Concurrency Control (MVCC). Благодаря этому соблюдаются требования ACID и практически отпадает нужда в блокировках чтения.



в PostgreSQL вообще не допускается синтаксис UTF-8.Поддержка Юникода (UTF-8) 
PostgreSQL различает регистр. Строки в запросах должны в точности совпадать с полями в базе данных.
Максимальный размер поля 	1 Гбайт
Максимум полей в записи 	250—1600, в зависимости от типов полей


# ===============================================================================================
# CREATE DATABASE
# ===============================================================================================
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

con = psycopg2.connect(
    dbname='postgres',
    user=self.user_name,
    host='',
    password=self.password
    )

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)        # <-- ADD THIS LINE
cur = con.cursor()

# Use the psycopg2.sql module instead of string concatenation
# in order to avoid sql injection attacs.
cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(self.db_name))
    )


# ===============================================================================================
# CONNECT TO DATABASE
# ===============================================================================================

# вариант1 с автозакрытием коннекта и курсора
from contextlib import closing

with closing(psycopg2.connect(
    dbname='base1',
    user='user1',
    password='mypass',
    host='localhost',
    port=5432
)) as conn:
    with conn.cursor() as cur:


# вариант2 без контекстного менеджера
conn = psycopg2.connect(
    dbname='base1',
    user='user1',
    password='mypass',
    host='localhost',
    port=5432
    )

cur = conn.cursor()

cursor.close()
conn.close()         # если не используется with closing

# ===============================================================================================
# CREATE TABLE
# ===============================================================================================
cur.execute("""CREATE TABLE allusers (
    id SERIAL PRIMARY KEY,
    login VARCHAR(64),
    password VARCHAR(64)
    )""")
conn.commit()

# ===============================================================================================
# INSERT INTO
# ===============================================================================================
cur.execute("INSERT INTO users (login, password) VALUES (%s, %s)", ("eax", "456"))
conn.commit()

try:
    # безопасная передача аргументов через кортеж
    sql = "INSERT INTO users (login, password) VALUES (%s, %s)", ("eax", "456")
    cur.execute(sql)
except psycopg2.OperationalError as e:
    print("Error: ", e)
else:
    conn.commit()

# безопасная передача аргументов через словарь
cursor.execute('SELECT * FROM engine_airport WHERE city_code = %(city_code)s', {'city_code': 'ALA'})
# ===============================================================================================
# UPDATE
# ===============================================================================================
cur.execute("UPDATE users SET password = %(password)s WHERE login = %(login)s", {"login":"eax", "password":"789"})
conn.commit()


# ===============================================================================================
# DELETE FROM
# ===============================================================================================
cur.execute("DELETE FROM users WHERE id = %s", (2,))
conn.commit()


# ===============================================================================================
# SELECT
# ===============================================================================================
"""
cursor.fetchone()                  # возвращает 1 строку
cursor.fetchall()                  # возвращает список всех строк
cursor.fetchmany(size=5)           # возвращает заданное количество строк
"""
from contextlib import closing
from psycopg2.extras import DictCursor

with closing(psycopg2.connect(...)) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:    # cursor_factory=DictCursor -вернет словарь, иначе кортеж
        cursor.execute('SELECT * FROM airport LIMIT 5')

        for row in cur.fetchall():                            # сформирует полный список
            print(row)

        for row in cur:                                       # не формирует список, итерирует по одному
            print(row)


"""
Метод execute вторым аргументом принимает коллекцию (кортеж, список и т.д.) или словарь. При формировании запроса необходимо помнить, что:

Плейсхолдеры в строке запроса должны быть %s, даже если тип передаваемого значения отличается от строки, всю работу берёт на себя psycopg2.

Не нужно обрамлять строки в одинарные кавычки.

Если в запросе присутствует знак %, то его необходимо писать как %%.
"""


# using sql module
from psycopg2 import sql

with psycopg2.connect() as conn:
    with conn.cursor() as cursor:
        columns = ('country_name_ru', 'airport_name_ru', 'city_code')

        stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.Identifier('airport')
        )
        cursor.execute(stmt)

        for row in cursor:
            print(row)

# ===============================================================================================
# TRANSACTIONS
# ===============================================================================================
"""
По умолчанию транзакция создаётся до выполнения первого запроса к БД, и все последующие запросы выполняются в контексте этой транзакции. Завершить транзакцию можно несколькими способами:

conn.close()                        # закроет соединение
del conn                            # удалит соединение
conn.commit() или conn.rollback()   # сделать коммит или откатить

autocommit для connection класса    # если атомарные опреации не нужны. коммитит каждый вызов execute
"""
with psycopg2.connect() as conn:
    conn.autocommit = True                      # коммитит каждый вызов execute
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users")
        conn.commit()                           # коммит
        conn.rollback()                         # откат

# ====== Python DB-API =======================================================================
"""
connect(                           # устанавливает соединение с базой
    host=hostname,
    user=username,
    password=password,
    dbname=database,
    port=port
    )
cursor()                           # объект который делает запросы и получает их результаты


# get data
cursor.fetchone()                  # возвращает 1 строку - кортеж или None, если запрос пустой
cursor.fetchall()                  # возвращает список всех строк
cursor.fetchmany(size=5)           # возвращает заданное количество строк

# query to db ========================================================

= cursor.execute(query)
Метод позволяет делать только один запрос за раз, при попытке сделать несколько через точку с запятой будет ошибка.

= cursor.executescript('''
 insert into Artist values (Null, 'A Aagrh!');
 insert into Artist values (Null, 'A Aagrh-2!');
''')
Метод позволяет делать только один запрос за раз.
Удобно использовать, если запросы сохранены в переменной или файле.

= cursor.executemany(query, collection)
collection = [
    ('A Aagrh!',),
    ('A Aagrh!-2',),
]



# transactions =======================================================

= conn.commit()
Если мы не читаем, а вносим изменения в базу - необходимо сохранить транзакцию

= conn.rollback()

# close operations ===================================================
= cursor.close()
= conn.close()
= del conn

"""




"""


====================================================================================
POSTGRESQL
====================================================================================
https://habr.com/ru/post/340460/
https://www.youtube.com/watch?v=-5_U5liPNTU


индекс - дополнительная структура данных(не SQL)
отделены от таблицы
информация о них - в системном каталоге
важна последовательность в запросе и индексе, иначе не будет работать

=== использование при поиске

= условие
where [operator] [value]

= при сортировке
order by [field] [asc|desc]

= при сортировке по условию GIST
order by [field] [operator] [value] [asc]

=== использование при сортировке
эффективно с limit
случайный доступ к данным с диска


=== минусы индексов
малая селнетивность - малая выборка(50/50)
хранение
долгий расчет - долгая вставка
высокая фрагментация индекса - долгая выборка
create index concurrently - не блокирует таблицу в процессе создания (конкурентное создание индекса)
неиспользуемые индексы - мониторинг(есть спецзапрос для этого)
индексы дубликаты

=== index types
Seq Index - простая последовательность

Index Scan  вынос колонки поиска из таблицы

Index Only Scan - пример (where c < 10). Можно еще результат отсортировать (order by asc), но в этом случае мы получи случайное тение таблицы, так как порядок в индексе будет уже не совпадать с порядком в таблице.

B-Tree - позволяет ускорить чтение индекса

GIST, GIN, SP-GIST - произвольные деревья

Bitmap Index Scan - сортируем Index Scan + строим в памяти Bitmap Index + читаем таблицу

функциональный индекс - immutable
===================================

"""