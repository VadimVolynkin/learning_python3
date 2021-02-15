# https://docs-python.ru/standart-library/paket-multiprocessing-python/funktsija-process-modulja-multiprocessing/

# ==============================================================================================
# Методы объекта Process
# Объект Process() запускает вызываемый объект target на исполнение в отдельном процессе/ядре процессора
# Имеет эквиваленты всех методов объекта Thread().
# ==============================================================================================

import multiprocessing

# Конструктор всегда следует вызывать с ключевыми аргументами
proc = multiprocessing.Process(
    group=None,                 # не используется - всегда должен быть None; существует для совместимости с threading.Thread()
    target=None,                # вызываемый методом Process.run() объект (функция)
    name=None,                  # имя процесса
    args=(),                    # кортеж аргументов для target
    kwargs={},                  # словарь аргументов для target
    *,
    daemon=None                 # демонизация процесса. Если daemon=None (по умолчанию), флаг будет = флагу проц. создателя.
    )

"""
Существует 2 способа запустить действие:
- Передать вызываемый объект (функцию) target в конструктор.
- Переопределить метод Process.run() или __init__() в подклассе. Другие методы переопределять нельзя.

Методы Process.start(), Process.join(), Process.is_alive(), Process.terminate() и Process.exitcode должны вызываться только процессом, создавшим этот объект процесса.
"""

Process.run()
# вызывает функцию target с args и kwargs

Process.start()
# запускает экземпляр Process в отдельном процессе/ядре процессора

Process.join(timeout)
# timeout=None (по умолчанию). Выполнение программы будет заблокировано, пока созданные процессы не завершаться.
# Если timeout > 0, то процесс блокируется не более чем на величину секунд timeout.
# Метод возвращает None, если его процесс завершается или если время ожидания метода истекает.

Process.name
# имя процесса - строка для идентификации. Имя может быть любым и даже одинаковым с другими процессами.

Process.is_alive()
# является ли процесс живым. Является живым с момента вызова Process.start() и до завершения порожденного дочернего процесса.

Process.daemon
# флаг демона процесса. Должен быть установлен перед вызовом Process.start()
# Начальное значение наследуется от процесса создателя. Демоническому процессу не разрешается создавать дочерние процессы.
# Когда процесс завершается, он пытается завершить все свои демонические дочерние процессы.

Process.pid
# возвращает идентификатор процесса или None если процесс еще не порожден

Process.exitcode
# код выхода порожденного процесса или None, если процесс еще не завершен.

Process.authkey
# ключ аутентификации процесса

Process.sentinel
# дескриптор объекта завершенного процесса

Process.terminate()
# завершает процесс

Process.kill()
# делает то же, что и Process.terminate()

Process.close()
# освобождает все связанные ресурсы с объектом Process
















