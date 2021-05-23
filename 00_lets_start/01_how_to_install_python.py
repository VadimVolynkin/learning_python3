# ===== УСТАНОВКА НОВОЙ ВЕРСИИ ПИТОНА ИЗ ИСХОДНИКОВ ======================================================

# перед началом как обычно обновим apt
sudo apt update

# устанавливаем зависимости
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

# загрузка последней версии питона
sudo wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz

# Распакуйте архив - после его можно удалить
sudo tar -xf Python-3.9.5.tgz

# перейдите в папку Python 3.9.5
cd Python-3.9.5

# Выполните команды - повышает производительность при выполнении кода python
sudo ./configure
sudo ./configure —enable-optimizations

# чтобы скомпилировать и установить Python 3.9.5 установите количество процессорных ядер
sudo make -j 4

# чтобы установить двоичные файлы, выполните команду
sudo make altinstall

# текущая версия питона по умолчанию
python3 -V

# ===== УСТАНОВКА ВЕРСИИ ПО УМОЛЧАНИЮ ====================================================================
# обычно вызов питона 3 происходит в терминале через команду Bash: python3
# python3 выполняет выполняет ссылку /usr/bin/python3 на на нужную версию питона

# создание жесткой ссылки /usr/bin/python3
# ln опции файл_источник файл_ссылки
sudo ln /usr/local/bin/python3.9 /usr/bin/python3


# = ВОЗМОЖНЫЕ ПРОБЛЕМЫ
# При смене версии интерпретатора python3 с 3.6 на версию 3.9 была замечена ошибка - перестал открываться гном-терминал. Далее лечение:

# переходим, открываем
cd /usr/bin
sudo nano gnome-terminal

# меняем первую строку(прописываем конкретную версию питона с которой будет работать терминал)
#!/usr/bin/python3 на #!/usr/bin/python3.6


# ===== update-alternatives ==============================================================================
# можно использовть эту утилиту для создания списка версий и переключения между ними 

# сначала нужно добавить в утилиту нужные версии питона
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.9 2

# выбор версии по умолчанию
sudo update-alternatives --config python3


===============================================================================================
/lib/python3.9/site-packages$ ll
/lib/python3.6/site-packages$ ll





pipenv: /usr/local/bin/pipenv /home/vadim/.local/bin/pipenv


drwxr-xr-x  8 root root   4096 мая 23 15:18 site-packages/
/usr/local/lib/python3.9/site-packages/pip/_internal/cli/base_command.py
/usr/local/lib/python3.9/site-packages/pip/_internal/cli/main.py


drwxr-xr-x  5 root root  4096 мая 23 12:37 pip/



apt-get remove --purge pipenv








