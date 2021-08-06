# ===== Download Fake SQL DATA =======================================================================
# https://github.com/lerocha/chinook-database
# https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

https://python-scripts.com/random-data



from random import *
from string import *


import os.path

fake_data = []
for _ in range(1000):
    FirstName = ''.join(choice(ascii_letters) for _ in range(10))
    LastName = ''.join(choice(ascii_letters) for _ in range(10))
    Email = ''.join(choice(ascii_letters) for _ in range(5)) + '@' + ''.join(choice(ascii_letters) for _ in range(5)) + '.com'
    Age = randint(1956, 2020)

print(fake_data[10])


"""

CREATE TABLE customers
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(30),
    LastName CHARACTER VARYING(30),
    Email CHARACTER VARYING(30),
    Age INTEGER
);

"""









