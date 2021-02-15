https://www.youtube.com/watch?v=hj6Tgc4hEU0

# pipenv install maya

import datetime
import pytz


# pytz позволяет получить зону по имени
dt = datetime.datetime.now()                              # 2021-01-15 18:20:43.945110
dtu= datetime.datetime.utcnow()                           # 2021-01-15 15:20:43.945135
dtp= datetime.datetime.now(tz=pytz.UTC)                   # 2021-01-15 15:20:43.945143+00:00
dt_moscow = dt.astimezone(pytz.timezone('Europe/Moscow')) # 2021-01-15 18:20:43.945110+03:00

for tz in pytz.all_timezones:
    print(tz)


# string formating
dt = datetime.datetime.now()
dt_strf = dt.strftime('%B, %d, %Y')                                          # January, 15, 2021
dt_strp = datetime.datetime.strptime('January, 15, 2021', '%B, %d, %Y')      # 2021-01-15 00:00:00
print(repr(dt_strp))                                                         # datetime.datetime(2021, 1, 15, 0, 0)


# timedelta
td1 = datetime.timedelta(15)                        # 15 days, 0:00:00
td2 = datetime.timedelta(days=10)                   # 10 days, 0:00:00
td3 = datetime.timedelta(hours=10)                  # 10:00:00


# datetime.date(year, month, day) Неизменяемый объект
d = datetime.date(dt)                               # 2021-01-14
today = datetime.date.today()                       # 2021-01-15
birth_day = datetime.date(1986, 3, 25)              # 1986-03-25
day_live = today - birth_day                        # 12715 days, 0:00:00
before_15_days = today - td1                        # 2020-12-31
print(today.day, today.month, today.year, today.weekday()) # 15 1 2021 4


# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбинация даты и времени.
dt1 = datetime.datetime.now()                       # 2021-01-15 14:14:23.304584
dt2 = datetime.datetime.utcnow()                    # 2021-01-15 11:14:23.304592
dt3 = datetime.datetime(2019, 11, 23)               # 2019-11-23 00:00:00
before_10_days = dt1 - td2                          # 2021-01-05 15:04:20.994499
print(dt1.day, dt1.month, dt1.year, dt1.hour, dt1.minute) # 15 1 2021 15 15


# datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
d = datetime.date(2005, 7, 14)                      # 2005-07-14         объект даты (с отсечением времени)
t = datetime.time(12, 30)                           # 12:30:00
c = datetime.combine(d, t)                          # 2005-07-14 12:30:00
dt = datetime(2005, 7, 14, 12, 30)                  # 2005-07-14 12:30:00


# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) не зависит от даты.
t = datetime.time(dt)                               # 11:40:03.886649
ct = datetime.ctime(dt)                             # Thu Jan 14 11:40:03 2021
t2 = datetime.time(13, 35, 55)                      # 13:35:55           объект времени (с отсечением даты)
print(t2.hour, t2.minute, t2.second)                # 13 35 55


# datetime.timedelta  разница между двумя моментами времени, с точностью до микросекунд.
dd = datetime(2020, 7, 14)                          # 2020-07-14
dt = datetime.now()
three_hours = timedelta(hours=3)                    # 3:00:00
two_days = timedelta(2)                             # 2 days, 0:00:00
plus_two_days = date.today() + two_days             # 2021-01-16
difference_days = dt - dd                           # 184 days, 19:31:59.403805


# datetime.timetuple() - возвращает struct_time из datetime.
dt = datetime.now()                                 # create instance
tt = datetime.timetuple(dt)
# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=14, tm_hour=11, tm_min=42, tm_sec=48, tm_wday=3, tm_yday=14, tm_isdst=-1)


# datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
# datetime.toordinal() - количество дней, прошедших с 01.01.1970.
df = datetime.fromordinal(8000)                     # 0022-11-26 00:00:00
dt = datetime.toordinal(df)                         # 8000


# datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
# datetime.timestamp() - возвращает время в секундах с начала эпохи.
df = datetime.fromtimestamp(1200000000)             # 2008-01-11 00:20:00
dt = datetime.timestamp(df)                         # 1200000000.0


# datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
# datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
# datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
# datetime.isoformat(sep='T') - строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm", если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
dt = datetime(2005, 7, 14, 12, 30)                  # 2005-07-14 12:30:00
dw = datetime.weekday(dt)                           # 3
diw= datetime.isoweekday(dt)                        # 4
dic= datetime.isocalendar(dt)                       # (2005, 28, 4)
dif= datetime.isoformat(dt, sep='T')                # 2005-07-14T12:30:00


# datetime.replace(year, month, day, hour, minute, second, microsecond, tzinfo) - возвращает новый объект datetime с изменёнными атрибутами.
dr = datetime.replace(dt)                           # 2005-07-14 12:30:00


# datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
# datetime.strftime(format) - см. функцию strftime из модуля time.
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")           # 2006-11-21 16:30:00
now = datetime.now()
print(now.strftime("%Y-%m-%d"))                     # 2017-05-03
print(now.strftime("%d/%m/%Y"))                     # 03/05/2017
print(now.strftime("%d/%m/%y"))                     # 03/05/17
print(now.strftime("%d %B %Y (%A)"))                # 03 May 2017 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))               # 03/05/17 01:36



# TODO datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).
# tzinfo показывает относительно переданного им объекта даты или времени:
# смещение местного времени от UTC
# имя часового пояса
# смещение на летнее время DST

# geopy
# https://fooobar.com/questions/128842/get-timezone-from-city-in-pythondjango
import geopy
timezone = geopy.timezone((lat, lng))        # return pytz timezone object <DstTzInfo 'Asia/Singapore' LMT+6:55:00 STD>



"""
Относительное время(naive)
Никогда не пересекает границ программы, не сохраняется в базе данных и не передается по сети.
Используется для: измерения временных интервалов, общения с пользователем и так далее.
У относительного времени нет информации о временной зоне (timezone).
Большинство используемых в небрежно составленной программе времен - относительные. И это далеко не всегда корректно.

Абсолютное время(aware)
Обладает временной зоной, которая вдобавок не пустая. В английском для таких времен применяют термин aware - осведомленный.
Когда пишем время в базу данных или пересылаем с одной машины на другую следует пользоваться абсолютным временем, а еще лучше приводить время к Гринвичу (так называемому UTC). UTC не имеет летнего времени.
Операции с абсолютными временами безопасны, даже если они относятся к разным временным зонам - Питон всё учитывает.

По умолчанию объект datetime.datetime и datetime.time создаются как относительное время, то есть без временной зоны.
datetime.now()
datetime.utcnow()

Временные зоны
Смещения относительно времени по Гринвичу.
Объекты datetime и time могут принимать необязательный парамер по имени tzinfo, который None или экземпляр класса, унаследованный от базового абстрактного класса tzinfo.
"""




# TODO ====================================================================
# Berlin
# London
# Paris
# Cyprus
# Creece
# Montenegro

# Sharm-el-Sheih


# New York
# San-Francisco

# Canada

# Pattaya
# Phuket
# Trat

# Sidney


# ====================================================================
























