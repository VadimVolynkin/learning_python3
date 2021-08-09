# ==============================================================================================
# ОПРЕДЕЛЕНИЕ ТЕКУЩЕГО ВРЕМЕНИ В РАЗНЫХ ГОРОДАХ
# ОПРЕДЕЛЕНИЕ ВРЕМЕНИ В РАЗНЫХ ГОРОДАХ, КОГДА В ТАЙМЗОНЕ ХХХХ БУДЕТ ...
# ==============================================================================================

import pytz
import datetime

# КОНФИГ  ==================================
year, month, day, hour, minute, second, our_tz = 2021, 8, 7, 23, 0, 0, 'Etc/GMT-3'

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
    """Выводит текущее время в разных городах мира"""
    
    print('======== DATETIME NOW ===========================================')

    for k, v in mytimezones.items():
        print(datetime.datetime.now(tz=pytz.timezone(v)), ' | ', k)


def print_time_in_anytimezone_when_our(
        year, month, day, 
        hour, minute, second, 
        our_tz):
    """Выводит время в других таймзонах, 
    если в произвольной зоне our_tz сейчас ... 
    """

    # создание объекта времени в выбранной таймзоне
    anytime = datetime.datetime(
        year, month, day, hour, minute, second,
        tzinfo = pytz.timezone(our_tz))

    # вывод городов с их локальным временем на момент anytime
    print('======== Если у нас сейчас: ', anytime, ' =======================')
    for k, v in mytimezones.items():
        time_in_other_city = anytime.astimezone(tz=pytz.timezone(v))
        print(time_in_other_city, ' | ', k)


# RUN ==================================

def main():
    # === если в таймзоне ххх сейчас ..., то в других городах
    print_time_in_anytimezone_when_our(year, month, day, 
                                    hour, minute, second, our_tz)

    # === Текущее время в других городах
    # print_timezones_datetime_now(mytimezones)

main()
