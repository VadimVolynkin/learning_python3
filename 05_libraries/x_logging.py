# pipenv install logging_tree               # показывает дерево логгеров
# graylog, kibana                           # хранение логов

# ============================================

# https://docs.python.org/3/library/logging.html#logrecord-attributes

# LogRecord
# https://habr.com/ru/post/513966/

# https://python-scripts.com/logging-python
# https://www.youtube.com/watch?v=nAK-Tpc3NMI



# ====== УРОВНИ ЛОГИРОВАНИЯ =====================================================================================


# === CRITICAL
Exception with traceback Все пропало...Здесь система падает. Редко используется.

# === ERROR
Logical Error. Ошибка логики, не работает или работает неправильно.

# === WARNING
Тревожный звоночек. Еще не ошибка, пока все работает, но странным образом.

# === INFO
Информация к сведению: программа запущена, этап 1 пройден успешно, программа закончила работу и тп.

# === DEBUG
Отладочная информация. Пишет все что происходит.

# ===========================================================================================

# === LOGGERS
Корзина для логов, далее обработчик HANDLERS их как то обрабатывает или не обрабатывает. У логера может быть несколько хендлеров(один обрабатывает Error и пишет в файл, другой WARNING и шлет mail).
Логер может обрабатывать сообщения определенного уровня. Сообщения с уровнем ниже будут проигнорированы.
У каждого логера есть имя - обычно это имя модуля в общей структуре пакетов. По нему можно производить настройку логера.

# === FILTERS
Дополнительная фильтрация логов. Фильтры могут менять уровень сообщений. Это шаг после проверки базового уровня журналирования, но до передачи журнального сообщения обработчикам. мы также можем вставить новые атрибуты в методе filter

# === HANDLERS
Обработчик лог сообщений. Может записать в файл, отправить на email, отправить в консоль и тп.
Имеет уровни.

# stdout in console. Обычно только важные ошибки.
'class': 'logging.StreamHandler',
'stream': 'ext://sys.stdout',

# in file
'class':'logging.FileHandler',
'filename': 'sample.log'

MemoryHandler          # собирает сообщения в лист и отправляет пачками в другой хендлер
BufferingHandler       # собирает сообщения в лист и периодически удаляет

QueueHandler           # пишет в очередь. Очередь нужно создать самому.
QueueListener          # читает из очереди и отправляет в другой хендлер

NullHandler            # ничего не делает

WatchedFileHandler

Rotatinghandler

# === FORMATTERS
Форматирует сообщения нужным нам образом. Можем добавить сюда время, пользователя, хостнейм компа и тп.

============================

# TODO LogRecord


# TODO LoggerAdapter


# ====== ПРОСТОЕ ЛОГИРОВАНИЕ =====================================================================================
import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

# create logger
loger = logging.getLogger(__name__)

# instances of logRecord
loger.exception("exception massage")
loger.debug("This is a debug message")
loger.info("DB was crated")
loger.warning("warning message")
loger.error("An error has happened!")
loger.critical("critical error message")


try:
    some_code()
except Exception:
    loger.exception('Some bad situation')


# ====== ЛОГИРОВАНИЕ С КОНФИГОМ JSON =====================================================================================
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,                          # отключает встроенное логирование
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',                                  # хендлер имеет свой уровень
            'formatter': 'standard',
            'class':'logging.FileHandler',
            'filename': 'sample.log'
        },
        'stdout': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {                                                   # root logger = empty string
            'handlers': ['file', 'stdout'],                     # этот логер выводит на 2 хендлера
            'level': 'DEBUG',
            'propagate': True,                                  # распространить выше по уровню пакетов
        }
    },
}


logging.config.dictConfig(LOGGING_CONFIG)

if __name__ == "__main__":
    log = logging.getLogger(__name__)

    log.exception("exception massage")
    log.critical("critical massage")
    log.error('some value: %s', value)
    log.warning("warning massage")
    log.info("info hello world")
    log.debug("debug massage")







