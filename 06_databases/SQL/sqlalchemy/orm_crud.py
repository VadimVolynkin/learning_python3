from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, or_, and_, not_, asc, desc, distinct
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime

# =========================================================================================================================
# SQLAlchemy ORM
# =========================================================================================================================
# ORM построен на базе Core
# declarative_base() - создание декларированного класса - это оболочка над маппером и MetaData
# Маппер соотносит подкласс с таблицей, а MetaData сохраняет всю информацию о базе данных и ее таблицах. 
# Управляет каталогом классов и таблиц.


# ===== СОЗДАЕМ ОБЪЕКТ Engine
# объект Engine отвечает за взаимодействие с базой данных. Состоит из двух элементов: диалекта и пула соединений.
# Диалект отвечает за обработку SQL-инструкций, выполнение, обработку результатов и так далее.
# Пул соединений — это способ кэширования соединений в памяти - это позволяет использовать их повторно(повышение произодительности). 

# подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI. 
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")

# подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI 
# engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")

# подключение к серверу SQLite на localhost 
engine = create_engine('sqlite:///sqlite3.db')

# === атрибуты create_engine()
# echo	           # True - будет сохранять логи SQL в стандартный вывод. По умолчанию = False.
# pool_size	       # количество соединений для пула. По умолчанию — 5
# max_overflow	   # количество соединений вне pool_size. По умолчанию — 10
# encoding	       # кодировка SQLAlchemy. По умолчанию — UTF-8. Не влияет на кодировку базы данных.
# isolation_level	 # степень изоляции 1 транзакции. Разные базы данных поддерживают разные уровни.

# ===== СОЗДАЕМ КОННЕКТ
engine.connect()


# =============================================================================================
# СОЗДАНИЕ БД
# =============================================================================================

# ===== создание декларотивного базового класса
# создаст в модели атрибуты - поля таблиц
Base = declarative_base()

# ===== создание модели
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    # Добавление ключей и ограничений
    __table_args__ = (
    ForeignKeyConstraint(['id'], ['users.id']),    # внешний ключ на users.id   
    Index('name_age_index' 'name', 'age'),         # составной индекс  
    )

# создание бд
Base.metadata.create_all(engine)

# удаление БД
Base.metadata.drop_all(engine)

# =============================================================================================
# CREATE
# =============================================================================================

# создание сессии
session = Session(bind=engine)

# готовим контент для записи
p1 = Person(name = 'vadim', age = 35)
p2 = Person(name = 'dmitriy', age = 23)
p3 = Person(name = 'dmitriy', age = 33)
p4 = Person(name = 'pavel', age = 55)
p5 = Person(name = 'denis', age = 66)

# добавление объектов в сессию(подготовка объектов к записи)
session.add(p1)
session.add_all([p1, p2, p3, p4, p5])

# запись в БД - следующие операции будут выполняться в новой транзакции
session.commit()


# =============================================================================================
# READ
# =============================================================================================

# создание сессии
session = Session(bind=engine)

# === all()
# вернет список

# получить все колонки из Person
q = session.query(Person).all()
for p in q:
    print(p.id, p.name)

# получить определенные колонки из Person
q = session.query(Person.id, Person.age).all()
for p in q:
    print(p.id, p.age)

# === count()
q = session.query(Person).count()
print(q)    # 3

# === first() - вернет первый результат или None
q = session.query(Person).first()
print(q.name)

# === get() - вернет экземпляр с соответствующим id или None
q = session.query(Person).get(1)
print(q.name)

# === filter()
# аналог WHERE. Принимает колонку, оператор и значение.
# фильтр вернет список
# несколько фильтров объединяются через AND
# можно использовать and_(), or_() и not_()

# несколько фильтров
q = session.query(Person).filter(Person.name == 'dmitriy', Person.age >= 30)

# ilike - регистр неважен, like - регистр важен
q = session.query(Person).filter(Person.name.ilike("dm%"))

# between - в промежутке от и до
q = session.query(Person).filter(Person.age.between(20, 50))

# вернет все с именем на dm + все с age = 55
q = session.query(Person).filter(or_(
    Person.name.ilike("dm%"),
    Person.age == 55
))

# === limit()
q = session.query(Person).limit(2)

# === offset()
q = session.query(Person).limit(2).offset(2)

# === order_by() - сортировка по возрастанию и убыванию
q = session.query(Person).order_by(Person.age)
q = session.query(Person).order_by(desc(Person.age))

# === join()
q = session.query(Customer).join(Table2).join(Table3)

# === outerjoin() - создает LEFT OUTER JOIN
q = session.query(Customer).outerjoin(Table2)

# === group_by()

# === having()

# === distinct()
q = session.query(Person).filter(Person.name == 'dmitriy').distinct()


# результат
for p in q:
    print(p.id, p.name, p.age)


# =============================================================================================
# UPDATE
# =============================================================================================

# создание сессии
session = Session(bind=engine)

# === получаем 1 объект для изменения
i = session.query(Person).get(5)

# меняем параметр, добавляем в сессию, комитим
i.age = 69
session.add(i)
session.commit()

# === для изменения сразу нескольких записей
session.query(Person).filter(Person.name.ilike("d%")).update({"age": 99}, synchronize_session='fetch')
session.commit()

# результат
q = session.query(Person)
for p in q:
    print(p.id, p.name, p.age)


# =============================================================================================
# DElETE
# =============================================================================================

# создание сессии
session = Session(bind=engine)

# === для удаления 1 объекта - получаем 1 объект, удаляем в сессии, комитим
i = session.query(Person).filter(Person.age == 55).one()
session.delete(i)
session.commit()


# === для удаления нескольких
session.query(Person).filter(Person.name.ilike("d%")).delete(synchronize_session='fetch')
session.commit()


# результат
q = session.query(Person)
for p in q:
    print(p.id, p.name, p.age)



# =========================================================================================================================
# Один-ко-многим
# =========================================================================================================================


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book")                           # добавляет атрибут books классу Author для доступа к связанным данным(a.books)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))  # устанавливает отношение один-ко-многим между моделями Author и Book
    author = relationship("Author")                        # добавляет атрибут author классу Book для доступа к связанным данным(b.author)



# =========================================================================================================================
# Один-к-одному
# =========================================================================================================================
# uselist=False в функции relationship() - единственное отличие от один-ко-многим

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    doj = Column(Date(), nullable=False)
    dl = relationship('DriverLicense', backref='person', uselist=False)


class DriverLicense(Base):
    __tablename__ = 'driverlicense'
    id = Column(Integer(), primary_key=True)
    license_number = Column(String(255), nullable=False)
    renewed_on = Column(Date(), nullable=False)
    expiry_date = Column(Date(), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'))


# =========================================================================================================================
# Многие-ко-многим
# =========================================================================================================================

# создается связующая таблица и затем соединяется с моделью с помощью secondary в relationship() в любой из основных таблиц
# связующая таблица может хранить дополнительные данные
class Author_Book(Base):
    __tablename__ = 'author_book'
    id = Column(Integer, primary_key=True)
    author_id =  Column(Integer(), ForeignKey("authors.id"))                  # внешний ключ на таблицу авторов
    book_id =  Column(Integer(), ForeignKey("books.id"))                      # внешний ключ на таблицу книг
    extra_data = Column(String(100))                                          # какие то дополнительные данные

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Author_Book", backref='author')                     # связывание с промежуточной таблицей


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)    
    authors = relationship("Author_Book", backref="book")                     # связывание с промежуточной таблицей

