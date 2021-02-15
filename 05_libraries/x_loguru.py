# pipenv istall loguru

from loguru import logger


logger.add('debug.json', format='{time} {level} {message}', level='DEBUG', rotation='10 KB', compression='zip', serialize=True)


logger.debug('hello from debug')
logger.info('hello from info')
logger.warning('hello from warning')
logger.error('hello from error')
logger.critical('hello from critical')


# ===== DECORATOR ===================================================================

def divide(a, b):
    return a / b

@logger.catch
def main():
    divide(1, 0)

main()







