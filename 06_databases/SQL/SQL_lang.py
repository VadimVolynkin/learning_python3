
https://www.w3schools.com/sql/sql_primarykey.asp
https://metanit.com/sql/tutorial/


# === SELECT
SELECT * FROM CUSTOMERS
SELECT CITY FROM MYTABLE
SELECT DISTINCT FROM CUSTOMERS

# === WHERE
SELECT * FROM Customers WHERE CITY = "BERLIN"
SELECT * FROM Customers WHERE NOT CITY = "BERLIN"
SELECT * FROM Customers WHERE CustomerID = 32
SELECT * FROM Customers WHERE CustomerID = 32 AND NAME = "VADIM"
SELECT * FROM Customers WHERE CustomerID = 32 OR CustomerID = 55

# === ORDER BY
SELECT * FROM Customers ORDER BY CITY
SELECT * FROM Customers ORDER BY COUNTRY, CITY

# === INSERT
INSERT INTO CUSTOMERS (NAME, AGE) VALUES (VADIM, 35)

# === UPDATE
UPDATE CUSTOMERS SET CITY = 'OSLO'
UPDATE CUSTOMERS SET CITY = 'OSLO' WHERE CITY = 'BERLIN'
UPDATE CUSTOMERS SET CITY = 'OSLO', COUNTRY = 'NORWAY' WHERE CustomerID = 32

# === DELETE
DELETE FROM CUSTOMERS WHERE COUNTRY = 'NORWAY'
DELETE FROM CUSTOMERS

# === NULL
SELECT * FROM Customers WHERE POSTALCODE IS NULL
SELECT * FROM Customers WHERE POSTALCODE IS NOT NULL

# === MIN
SELECT MIN(PRICE) FROM PRODUCTS

# === MAX
SELECT MAX(PRICE) FROM PRODUCTS

# === COUNT
SELECT COUNT(*) FROM PRODUCTS WHERE PRICE = 18

# === AVG
SELECT AVG(PRICE) FROM PRODUCTS

# === SUM
SELECT SUM(PRICE) FROM PRODUCTS

# === LIKE
SELECT * FROM Customers WHERE CITY LIKE 'a%'        STARTS A
SELECT * FROM Customers WHERE CITY LIKE '%a'        ENDS A
SELECT * FROM Customers WHERE CITY LIKE '%a%'       CONTAINS A
SELECT * FROM Customers WHERE CITY LIKE 'a%b'       STARTS A ENDS B
SELECT * FROM Customers WHERE CITY NOT LIKE 'a%'    NOT STARTS A

# === WILDCARDS
SELECT * FROM Customers WHERE CITY LIKE '_a%'       SECOND LETTER = a
SELECT * FROM Customers WHERE City LIKE '[acs]%'    FIRST LETTER STARTS a c s
SELECT * FROM Customers WHERE City LIKE '[^acf]%'   FIRST LETTER STARTS NOT a c f
SELECT * FROM Customers WHERE City LIKE '[a-f]%'    FIRST LETTER STARTS FROM a to f


# === IN
SELECT * FROM Customers WHERE Country IN ('Norway', 'France')
SELECT * FROM Customers WHERE Country NOT IN ('Norway', 'France')


# === BETWEEN
SELECT * FROM Products WHERE Price BETWEEN 10 AND 20
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20
SELECT * FROM Products WHERE ProductName BETWEEN 'Geitost' and 'Pavlova'


# === ALIAS
SELECT CustomerName, Address, PostalCode AS Pno FROM Customers
SELECT * FROM Customers AS Consumers


# === JOIN
SELECT * FROM Orders LEFT JOIN Customers ON Orders.CustomerID=Customers.CustomerID
SELECT * FROM Orders RIGHT JOIN Customers ON Orders.CustomerID=Customers.CustomerID
SELECT * FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID


# === GROUP BY
SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country
SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country ORDER BY COUNT(CustomerID) DESC


# === DATABASE
CREATE DATABASE testDB
DROP DATABASE testDB
CREATE TABLE Persons(PersonID int, LastName varchar(255))
DROP TABLE Persons
TRUNCATE TABLE Persons
ALTER TABLE Persons ADD Birthday DATE
ALTER TABLE Persons DROP COLUMN Birthday


# =================================================================================================================
# Этапы проетирования
# =================================================================================================================
# 1. Создание схемы базы данных.
# 2. Определение ограничений целостности

# = Концептуальное проетирование
построение семантической модели наиболее высокого уровня абтракции без привязки к типу БД и модели данных.
1. Описание информационных объектов и связей между ними
2. 1 таблица - 1 сущность

# === Восходящий подход
Все атрибуты группируем по сущностям, для которых затем создаются таблицы. Больше подходит для проектирования небольших баз данных с небольшим количеством атрибутов.

# === Нисходящий подход
Данный подход подразумевает выявление сущностей. Затем происходит анализ сущностей, выявляются связи между ними, а потом и атрибуты сущностей.

# =================================================================================================================
# Нормализация базы
# =================================================================================================================
# удаление избыточности данных (data redundancy)
# позволяет избежать нарушения целостности данных при их изменении, то есть избежать аномалий изменения (update anomaly)

В ненормализованной форме таблица может хранить информацию о двух и более сущностях. Может содержать повторяющиеся столбцы. Столбцы могут хранить повторяющиеся значения.
В нормализованной форме каждая таблица хранит информацию только об одной сущности.

в 99% нормализация - декомпозиция (разделение на несколько таблиц)

# === Первая нормальная форма (1NF)
1. в каждой клетке таблицы должно быть только 1 значение
2. таблицы не должны содержать повторяющихся строк.

# === Вторая нормальная форма (2NF)
1. есть первичный ключ
2. все атрибуты зависят от этого ключа целиком

# === Третья нормальная форма (3NF)
1. все атрибуты зависят только от первичного ключа.

# === форма Бойса-Кодда (BCNF)
1. Ключевые атрибуты не должны зависить от неключевых
Нормальная форма Бойса-Кодда (BCNF) является немного более строгой версией третьей нормальной формы.

# === Четвертая нормальная форма (4NF)
применяется для устранения многозначных зависимостей (multivalued dependencies) - таких зависимостей, где столбец с первичным ключом имеет связь один-ко-многим со столбцом, который не является ключом. Эта нормальная форма устраняет некорректные отношения многие-ко-многим.

# === Пятая нормальная форма (5NF)
устраняет нетривиальные зависимости(декомпозиция без потерь). разделяет таблицы на более малые таблицы для устранения избыточности данных. Разбиение идет до тех пор, пока нельзя будет воссоздать оригинальную таблицу путем объединения малых таблиц.

# === Шестая нормальная форма (domain key normal form / 6NF)
Каждое ограничение в связях между таблицами должно зависеть только от ограничений ключа и ограничений домена, где домен представляет набор допустимых значений для столбца. Эта форма предотвращает добавление недопустимых данных путем установки ограничения на уровне отношений между таблицами, но не на уровне таблиц или столбцов. Данная форма, как правило, не применима на уровне СУБД, в том числе и в SQL Server.













