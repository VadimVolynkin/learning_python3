https://pythonworld.ru/moduli/modul-time.html


time.altzone - смещение DST часового пояса в секундах к западу от нулевого меридиана. Если часовой пояс находится восточнее, смещение отрицательно.
print(time.altzone)                  # -10800

time.asctime([t]) - преобразовывает кортеж или struct_time в строку вида "Thu Sep 27 16:42:37 2012". Если аргумент не указан, используется текущее время.
print(time.asctime())                # Mon Jan 18 13:47:39 2021   its right time

time.daylight - не 0, если определено, зимнее время или летнее (DST).
print(time.daylight)                 # 0

time.ctime([сек]) - преобразует время, выраженное в секундах с начала эпохи в строку вида "Thu Sep 27 16:42:37 2012".

time.gmtime([сек]) - преобразует время, выраженное в секундах с начала эпохи в struct_time, где DST флаг всегда равен нулю.
print(time.gmtime(1620000000))       # time.struct_time(tm_year=2021, tm_mon=5, tm_mday=3, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=123, tm_isdst=0)

time.localtime([сек]) - как gmtime, но с DST флагом.

time.mktime(t) - преобразует кортеж или struct_time в число секунд с начала эпохи. Обратна функции time.localtime.

time.sleep(сек) - приостановить выполнение программы на заданное количество секунд.

time.strftime(формат, [t]) - преобразует кортеж или struct_time в строку по формату:

time.strptime(строка [, формат]) - разбор строки, представляющей время в соответствии с форматом. Возвращаемое значение struct_time. Формат по умолчанию: "%a %b %d %H:%M:%S %Y".

Класс time.struct_time - тип последовательности значения времени. Имеет интерфейс кортежа. Можно обращаться по индексу или по имени.

time.time() - время, выраженное в секундах с начала эпохи.

time.timezone - смещение местного часового пояса в секундах к западу от нулевого меридиана. Если часовой пояс находится восточнее, смещение отрицательно.
print(time.timezone)              # -10800

time.tzname - кортеж из двух строк: первая - имя DST часового пояса, второй - имя местного часового пояса.
print(time.tzname)                # ('MSK', 'MSK')







