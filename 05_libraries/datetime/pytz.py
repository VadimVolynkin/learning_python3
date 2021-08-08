# =====================================================================
# PYTZ
# =====================================================================
# модуль преобразует дату и время
# позволяет выполнять вычисления часовых поясов

import datetime
import pytz
from pprint import pprint

# ===== TIMEZONES ===============================================================


# === GMT

# === Etc/GMT-7
Etc/GMT-7 = UTC+7

# === UTC
Всемирное координированное время. UTC - это таймзона без перехода на летнее время и без каких бы то ни было изменений в прошлом. 
Всегда храните и работайте со временем в UTC.
Из UTC можно конвертировать время в локальное для любого часового пояса.

# === DST
летнее время

# ===================================================================================================================

# ===== ВСЕ ВРЕМЕННЫЕ ЗОНЫ PYTZ
all_pytz_timezones = pytz.all_timezones                # ['Africa/Abidjan', 'Africa/Accra', ...]
all_pytz_timezones_set = pytz.all_timezones_set        # LazySet({'EST5EDT', 'America/Nipigon', 'Pacific/Rarotonga', ...})


# ===== ОБЩИЕ ЧАСОВЫЕ ПОЯСА
common_timezone = pytz.common_timezones                # ['Africa/Abidjan', 'Africa/Accra', ...]
common_timezone_set = pytz.common_timezones_set        # LazySet({'Europe/Kiev', 'Canada/Eastern', ...})


# ===== ОБЪЕКТ ТАЙМЗОНЫ

# создание объектов таймзоны
utc = pytz.utc                                         # получение UTC
moscow_tz = pytz.timezone('Europe/Moscow')             # получение таймзоны

print(moscow_tz.zone)                                  # Europe/Moscow

# получение текущего времени в таймзоне
print(datetime.datetime.now(tz=utc))                   # 2021-08-07 08:31:09.881518+00:00
print(datetime.datetime.now(tz=moscow_tz))             # 2021-08-07 11:31:09.881619+03:00


# ===== ВСЕ ИМЕНА СТРАН
for k, v in pytz.country_names.items():
    print(k, ' = ', v)                                 # RU  =  Russia

