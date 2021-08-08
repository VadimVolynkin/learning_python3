# ==============================================================================================
# ОПРЕДЕЛЕНИЕ ТЕКУЩЕГО ВРЕМЕНИ В РАЗНЫХ ГОРОДАХ
# ОПРЕДЕЛЕНИЕ ВРЕМЕНИ В РАЗНЫХ ГОРОДАХ, КОГДА В ТАЙМЗОНЕ ХХХХ БУДЕТ ...
# ==============================================================================================

import pytz
import datetime

# КОНФИГ  ==================================
year, month, day, hour, minute, second = 2021, 8, 7, 23, 0, 0
our_tz = 'Etc/GMT-3'

mytimezones = {
    "Moscow": 'Etc/GMT-3',

    "Greece": "Etc/GMT-3",
    "Cyprus": 'Etc/GMT-3',

    "Montenegro": "Etc/GMT-2",
    "Berlin": "Etc/GMT-2",
    "Paris": "Etc/GMT-2",
    "London": "Etc/GMT-1",

    "Sharm El Sheikh": "Etc/GMT-2",

    "Phuket": "Etc/GMT-7",
    "Pattaya": "Etc/GMT-7",
    "Trat": "Etc/GMT-7",

    "Sidney": "Etc/GMT-10",

    "New York": "Etc/GMT+4",
    "Canada/Monreal": "Etc/GMT+4",
    "San-Francisco": "Etc/GMT+7",

}


# КОД  ==================================

def print_timezones_datetime_now(mytimezones):
    """
    Выводит текущее время в разных городах мира
    """
    print('======== DATETIME NOW ===========================================')

    for k, v in mytimezones.items():
        print(datetime.datetime.now(tz=pytz.timezone(v)), ' | ', k)


def get_our_datetime(year, month, day, hour, minute, second, our_tz):
    """Создает объект времени для 'нашей' таймзоны"""

    our_time = datetime.datetime(
        year, month, day, hour, minute, second, tzinfo=pytz.timezone(our_tz))

    return our_time


def get_other_local_time_if_our(
    year, month, day, hour, 
    minute, second, our_time, other_tz):

    """Сколько времени в другом часовом поясе если у нас """

    # создание объекта времени 'другой' таймзоны
    other_time = datetime.datetime(
        year, month, day, hour, minute, second, tzinfo=pytz.timezone(other_tz))

    # вычисление оффсетов таймзон
    our_offset = our_time.utcoffset()
    other_offset = other_time.utcoffset()

    # определение дельты таймзон
    delta = our_offset - other_offset
    other_local_time = our_time + delta
    other_local_time = other_local_time.replace(tzinfo=pytz.timezone(other_tz))

    return other_local_time


def print_time_in_other_timezone_if_our(mytimezones, our_time, our_tz):
    """Выводит время в разных городах мира, 
    когда в таймзоне our_tz время our_time"""

    print('=== IF IN ', our_tz, 'NOW ', our_time, '=== TIME IN OTHER CITY ===')

    # получение времени в таймзоне
    for k, v in mytimezones.items():
        time_in_other_city = get_other_local_time_if_our(
            year, month, day, hour, minute, second, our_time, other_tz=v)
        print(time_in_other_city, ' | ', k)


# RUN ==================================

def main():

    # === если в таймзоне ххх сейчас ..., то в других городах
    our_time = get_our_datetime(year, month, day, hour, minute, second, our_tz)
    print_time_in_other_timezone_if_our(mytimezones, our_time, our_tz)

    # === Текущее время в других городах
    # print_timezones_datetime_now(mytimezones)


main()
