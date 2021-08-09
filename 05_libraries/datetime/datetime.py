https://docs-python.ru/standart-library/modul-datetime-python/metody-ekzempljara-ditetime-datetime/


"""
Относительное время(naive) 
Не имеет информации о временной зоне (timezone).
Никогда не пересекает границ программы, не сохраняется в базе данных и не передается по сети.
Используется для: измерения временных интервалов, общения с пользователем и так далее.
Большинство используемых в небрежно составленной программе времен - относительные. И это далеко не всегда корректно.
По умолчанию объект datetime.datetime и datetime.time создаются как относительное время, то есть без временной зоны.
datetime.now()
datetime.utcnow()

Абсолютное время(aware)
Обладает временной зоной, которая вдобавок не пустая. В английском для таких времен применяют термин aware - осведомленный.
Когда пишем время в базу данных или пересылаем с одной машины на другую следует пользоваться абсолютным временем, а еще лучше приводить время к Гринвичу (так называемому UTC), знаяя таймзону из него легко получить локальное время. 
UTC не имеет летнего времени. Операции с абсолютными временами безопасны, даже если они относятся к разным временным зонам - Питон всё учитывает.

Временные зоны
Смещения относительно времени по Гринвичу.
Объекты datetime и time могут принимать необязательный парамер по имени tzinfo, который None или экземпляр класса, унаследованный от базового абстрактного класса tzinfo.
"""


# =====================================================================
# DATETIME 
# =====================================================================
Типы datetime.date, datetime.time, datetime.datetime и datetime.timezone вляются хешируемыми(могут быть ключами словаря), поддерживают сериализацию pickle.

Объекты даты и времени могут быть:

# Осведомленные
Представляют определенный момент времени, который нельзя интерпретировать по другому.
Могут найти себя относительно других осведомленных объектов.
Содержат атрибут tzinfo - в нем хранится инфа о смещении времени от UTC, имени часового пояса и действии летнего времени.

# Наивные
Не имеют достаточно информации о времени в конкретном месте. 
Могут представлять: UTC, местное время или время в другом часовом поясе - это зависит от программы
Наивные объекты модуля datetime обрабатываются многими методами объекта datetime.datetime() как локальное время, поэтому предпочтительно использовать осведомленные объекты.


# =====================================================================
# DATETIME.DATETIME
# =====================================================================
dt = datetime.datetime(
    year, month, day, 
    hour=0, minute=0, second=0, microsecond=0, 
    tzinfo=None, *, fold=0)

# создание объекта datetime
date = datetime.datetime(2021, 3, 25)                # 2021-03-25 00:00:00
dt   = datetime.datetime(2021, 3, 25, 13, 45)        # 2021-03-25 13:45:00

# datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
d = datetime.date(2005, 7, 14)                      # 2005-07-14         объект даты (с отсечением времени)
t = datetime.time(12, 30)                           # 12:30:00
c = datetime.combine(d, t)                          # 2005-07-14 12:30:00
dt = datetime(2005, 7, 14, 12, 30)                  # 2005-07-14 12:30:00

# текущая локальная дата и время с tzinfo=None
datetime.datetime.today()                            # 2021-08-07 13:56:59.104110

# текущая локальная дата и время при tz=None
# tz может быть datetime.tzinfo или zoneinfo
datetime.datetime.now(tz=None)                       # 2021-08-07 13:57:26.349301

# текущая дата и время UTC 
datetime.datetime.utcnow()                           # 2021-08-07 10:58:14.661047       # наивный объект с tzinfo=None
datetime.datetime.now(datetime.timezone.utc)         # 2021-08-07 11:07:10.534944+00:00 # осведомленный объект

# из timestamp POSIX
datetime.datetime.fromtimestamp(time.time())         # 2021-08-07 14:10:30.637100

# дата и время UTC из 
datetime.datetime.utcfromtimestamp(time.time())      # 2021-08-07 11:13:36.877296       # наивный объект с tz=None

# из datetime.date + datetime.time 
date = datetime.date.today()
time = datetime.time(23, 55)
datetime.datetime.combine(date, time)                # 2021-08-07 23:55:00

# из строки ISO 
datetime.datetime.fromisoformat('2011-11-04')                      # 2011-11-04 00:00:00
datetime.datetime.fromisoformat('2011-11-04T00:05:23')             # 2011-11-04 00:05:23
datetime.datetime.fromisoformat('2011-11-04T00:05:23+04:00')       # 2011-11-04 00:05:23+04:00

# из календарной даты ISO
dt = datetime.datetime.now()
dt.isocalendar()                                      # datetime.IsoCalendarDate(year=2021, week=31, weekday=6)
dt2 = datetime.datetime(2021, 9, 30)
datetime.datetime.isocalendar(dt2)                    # datetime.IsoCalendarDate(year=2021, week=39, weekday=4)

# парсит из какой то строки в соответствии с форматом
date_str = 'Fri, 24 Apr 2021 16:22:54 +0000'
format = '%a, %d %b %Y %H:%M:%S +0000'
datetime.datetime.strptime(date_str, format)          # 2021-04-24 16:22:54

# вычисление времени с помощью timedelta
tdelta = datetime.timedelta(hours=3)                  # 3:00:00                    создаем делту 3 часа
dt = datetime.datetime.now()                          # 2021-08-07 15:08:09.790242 получаем текущее время
dt + tdelta                                           # 2021-08-07 18:08:09.790242

# вычисление разницы между двумя datetime
# вернет объект timedelta
dt1 = datetime.datetime.now()                         # <class 'datetime.datetime'>
dt2 = dt1 + datetime.timedelta(hours=3)               # <class 'datetime.datetime'>
delta_dt = dt2 - dt1                                  # 3:00:00 <class 'datetime.timedelta'>

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

# string formating
dt = datetime.datetime.now()
dt_strf = dt.strftime('%B, %d, %Y')                                          # January, 15, 2021
dt_strp = datetime.datetime.strptime('January, 15, 2021', '%B, %d, %Y')      # 2021-01-15 00:00:00
print(repr(dt_strp))                                                         # datetime.datetime(2021, 1, 15, 0, 0)


# =====================================================================
# DATETIME.TIME
# =====================================================================
# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) не зависит от даты.
t = datetime.time(dt)                               # 11:40:03.886649
ct = datetime.ctime(dt)                             # Thu Jan 14 11:40:03 2021
t2 = datetime.time(13, 35, 55)                      # 13:35:55           объект времени (с отсечением даты)
print(t2.hour, t2.minute, t2.second)                # 13 35 55


# =====================================================================
# DATETIME.DATE
# =====================================================================
date = datetime.date(year, month, day)              # создает объект
today = datetime.date.today()                       # 2021-01-15 дата сегодня

# делает объект из timestamp
sec = time.time()                                   # 1588657177.4476178
datetime.date.fromtimestamp(sec)                    # datetime.date(2020, 5, 5)

# делает объект из строки даты
date.fromisoformat('2021-12-06')                    # 2021-12-06

# делает строку из объекта datetime или данных
datetime.date(2021, 12, 4).isoformat()              # '2021-12-04'
date.__str__()                                      # '2021-12-04'

# возвращает строку, представляющую дату
datetime.date(2021, 12, 4).ctime()                  # 'Sat Dec  4 00:00:00 2021'

# делает дату из переданных значений datetime.date.fromisocalendar(year, week, day)
datetime.date.fromisocalendar(2020, 4, 2)           # 2020-01-21

# меняет атрибуты даты на переданные значения date.replace(year=self.year, month=self.month, day=self.day)
date = datetime.date.today()                        # 2021-08-08
date.replace(month=7, day=26)                       # 2021-07-26

# возвращает объект структуры времени time.struct_time
date.timetuple()
# time.struct_time(tm_year=2020, tm_mon=5, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=126, tm_isdst=-1)

# григорианский порядковый номер даты, где 1 января 1 года имеет порядковый номер 1                     
date.toordinal()                                    # 737550

# возвращает день недели в виде целого числа, где понедельник равен 0, а воскресенье - 6
date.weekday()                                      # 1

# возвращает день недели в виде целого числа, где понедельник равен 0, а воскресенье - 6
date.isoweekday()                                   # 2

# возвращает именованный кортеж с тремя компонентами: год year, неделя week и день недели weekday
datetime.date(2021, 1, 4).isocalendar()             # datetime.IsoCalendarDate(year=2021, week=1, weekday=1)

# возвращает строку, представляющую дату по произвольному формату
date.strftime('%d/%m/%y')                           # '05/05/20'
date.strftime('%A %d. %B %Y')                       # 'Tuesday 05. May 2020'


# =====================================================================
# DATETIME.TIMEDELTA
# =====================================================================
# объект создает разницу во времени между датами
# аргументы могут положительными и отрицательными
# много приммеров https://docs-python.ru/standart-library/modul-datetime-python/primery-ispolzovanija-datetime-timedelta/
delta = datetime.timedelta(days=0, 
                           seconds=0, 
                           microseconds=0, 
                           milliseconds=0, 
                           minutes=0, 
                           hours=0, 
                           weeks=0)

# создание объекта и единственный метод total_seconds()
td1 = datetime.timedelta(15)                        # 15 days, 0:00:00
td2 = datetime.timedelta(days=10)                   # 10 days, 0:00:00
td3 = datetime.timedelta(hours=10)                  # 10:00:00
td1.total_seconds()                                 # 1296000.0

# Интервал между датами
date1 = datetime.datetime.now()
date2 = datetime.datetime(2021, 1, 1) 
delta = date2 - date1
delta.total_seconds()


def timedelta_to_hms(duration):
    # преобразование в часы, минуты и секунды
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds

def timedelta_to_dhms(duration):
    # преобразование в дни, часы, минуты и секунды
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds


# =====================================================================
# DATETIME.TZINFO
# =====================================================================
# абстрактный базовый класс, необходимо определить свой подкласс datetime.tzinfo для сбора информации о конкретном часовом поясе
# Созданный подкласс datetime.tzinfo будет передаваться конструкторам объектов datetime.datetime() и datetime.time()
# объект tzinfo поддерживает методы, вычисляющие время относительно переданного объекта даты или времени:
# - смещение местного времени от UTC
# - имя часового пояса
# - смещение DST
# tzinfo считается не очень хорошим решением. вместо него часто используется pytz

tzinfo = datetime.tzinfo()    # <datetime.tzinfo object at 0x7fade8bd5180>


# =====================================================================
# DATETIME.TIMEZONE
# =====================================================================
# Класс timezone() является подклассом datetime.tzinfo, каждый экземпляр которого представляет часовой пояс, определенный фиксированным смещением от UTC.
# Объекты этого класса не могут использоваться для представления информации о часовом поясе в местах, где разные смещение используются в разные дни года или когда были внесены исторические изменения в гражданское время.

# Всегда храните и работайте со временем в UTC.
# Если вам нужно сохранить оригинальные данные - пишите их отдельно. 
# Никогда не храните локальное время и tz - Time Zone.

# вернет фиксированное значение, указанное при создании экземпляра часового пояса
offset = datetime.timedelta(hours=3)
tz = datetime.timezone(offset, name='МСК')                     # создание произвольной таймзоны с +3 часа и именем МСК

dt = datetime.datetime.now(tz=tz)                              # создание объекта времени с таймзоной
dt.utcoffset()                                                 # 3:00:00  разница с UTC

# вернет имя созданной таймзоны
dt.tzname()                                                    # МСК

# летнее время
tz.dst(dt)                                                     # всегда возвращает None

# возвращает dt + offset
tz.fromutc(dt)                                                 # 2021-08-10 00:09:33.887893+03:00

# вернет часовой пояс UTC
print(tz.utc)                                                  # UTC


















# TODO datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).
# tzinfo показывает относительно переданного им объекта даты или времени:
# смещение местного времени от UTC
# имя часового пояса
# смещение на летнее время DST

# geopy
# https://fooobar.com/questions/128842/get-timezone-from-city-in-pythondjango
import geopy
timezone = geopy.timezone((lat, lng))        # return pytz timezone object <DstTzInfo 'Asia/Singapore' LMT+6:55:00 STD>



















