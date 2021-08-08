
https://docs-python.ru/standart-library/modul-datetime-python/metody-ekzempljara-ditetime-datetime/

import datetime
import time
import pytz

# =====================================================================
# DATETIME.TIME
# =====================================================================


# =====================================================================
# DATETIME.DATE
# =====================================================================


# =====================================================================
# DATETIME.TIMEDELTA
# =====================================================================



# =====================================================================
# DATETIME.TZINFO
# =====================================================================
# абстрактный базовый класс
tzinfo = datetime.tzinfo()    # <datetime.tzinfo object at 0x7fade8bd5180>

# Необходимо определить свой подкласс datetime.tzinfo для сбора информации о конкретном часовом поясе
# Созданный подкласс datetime.tzinfo будет передаваться конструкторам объектов datetime.datetime() и datetime.time()
# объект tzinfo поддерживает методы, вычисляющие относительно переданного объекта даты или времени:
# - смещение местного времени от UTC
# - имя часового пояса
# - смещение DST

# === .astimezone()

dt = datetime.datetime.now()
dt_with_tz = dt.astimezone()                       # получает таймзону из объекта времени   # <class 'datetime.datetime'>


# === .utcoffset() вернет таймзоны от UTC, как объект datetime.timedelta()
moscow_tz = pytz.timezone('Etc/GMT-3')
dt_with_tz = datetime.datetime.now(tz=moscow_tz)   # создадим объект с таймзоной
dt_with_tz.utcoffset()                             # 3:00:00

dt = datetime.datetime.now()                       # создадим объект времени без tz
dt.utcoffset()                                     # None



offset_moscow  = datetime.datetime.now(tz=pytz.timezone('Etc/GMT-3')).utcoffset()    # 3:00:00
offset_newyork = datetime.datetime.now(tz=pytz.timezone('Etc/GMT+4')).utcoffset()    # -1 day, 20:00:00
diff = offset_moscow - offset_newyork                                                # 7:00:00
rdiff = offset_newyork - offset_moscow                                               # -1 day, 17:00:00

# print(offset_moscow)
# print(offset_newyork)
# print(diff)
# print(rdiff)

# Москва на 7 часов опережает New York
# 2021-08-07 18:23:30.906096+03:00  |  Moscow
# 2021-08-07 11:23:30.935984-04:00  |  New York

# Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)




# вернет корректировку перехода на летнее время DST как объект datetime.timedelta()
# вернет None, если DST неизвестна


# tzinfo.dst(dt)


# =====================================================================
# ZONEINFO
# =====================================================================




# =====================================================================
# DATETIME.TIMEZONE
# =====================================================================
# Класс timezone() является подклассом datetime.tzinfo, каждый экземпляр которого представляет часовой пояс, определенный фиксированным смещением от UTC.
# Объекты этого класса не могут использоваться для представления информации о часовом поясе в местах, где разные смещение используются в разные дни года или когда были внесены исторические изменения в гражданское время.

# Всегда храните и работайте со временем в UTC.
# Если вам нужно сохранить оригинальные данные - пишите их отдельно. 
# Никогда не храните локальное время и tz - Time Zone.

# tz = datetime.timezone(offset, name=None)
# offset - объект datetime.timedelta(), разница между местным временем и UTC
# name=None - строка, название часового пояса

# offset = datetime.timedelta(hours=3)
# tz1 = datetime.timezone(offset, name='МСК')

# print(tz1)                         # МСК

# datetime.tzname()









