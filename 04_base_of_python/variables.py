# Есть 4 области видимости в Питоне:
1. Local - локальная переменная функции. Доступны только в блоке программы. Переменные после отпработки блока кода уничтожаются, но если на них остается живая ссылка, то они будут существовать и дальше. Такую ссылку может сохранить вложенная функция. Функции построенные по такому принципу нужны для построения специализированных функций, т.е. являются фабриками функций. 
2. Enclosing(вмещающая)- локальная переменная функции для ее вложенной функции.
3. Global - область видимости модуля. Переменная доступная в любом месте программы.
4. Built-in - область видимости интерпретатора типа функций open, len и т.п. Они доступны везде, не требуют импорта.

https://docs-python.ru/tutorial/opredelenie-funktsij-python/operatory-global-nonlocal/
global a        связывает с глобальной перемменной. Так можно делать только в отсутствии соответствующих локальных переменных.
nonlocal x      связывет с внешней переменной  
оператор nonlocal используются только во вложенных функциях
Свободные переменные


https://docs-python.ru/tutorial/opredelenie-funktsij-python/oblast-vidimosti-peremennyh/
Если переменная используется в блоке кода, но не определена в нем, то такая переменная называется свободной. Свободные переменные разрешаются (смотрите "Правила разрешение имен в Python") не в ближайшем окружающем пространстве имен, а в глобальном пространстве имен.



# ================================================================================================================
# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ globals()
# ================================================================================================================
g = 100500

print(globals())

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4482bbbbb0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/vadim/PycharmProjects/python_beazley/run_b.py', '__cached__': None, 'g': 100500}


# ================================================================================================================
# ЛОКАЛЬНЫЕ ПЕРЕМЕННЫЕ locals()
# ================================================================================================================
# если вызвать в глобальной видимости, то locals() = globals()


# ===== locals() = globals() =================================================================
g = 100500

print(locals())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4482bbbbb0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/vadim/PycharmProjects/python_beazley/run_b.py', '__cached__': None, 'g': 100500}


# ===== locals() выведет локальные переменные функции foo ====================================
g = 100500

def foo():
    l = 42
    print(locals())

foo()                           
{'l': 42}

# ================================================================================================================
# ПЕРЕМЕННЫЕ ВСТРОЕННЫЕ В ИНТЕРПРЕТАТОР vars(builtins)
# ================================================================================================================
# vars(builtins) просто выводит переменные из интерпретатора. К локальной и глобальной области отношения не имеет.

g = 100500

import builtins

print(vars(builtins))
{'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'copyright': Copyright (c) 2001-2020 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}


# ================================================================================================================
# ПЕРЕМЕННЫЕ СРЕДЫ ОКРУЖЕНИЯ
# ================================================================================================================
# имеют приоритет над переменными по дефолту

import os

env_vars = os.environ
print(env_vars)

environ({'CLUTTER_IM_MODULE': 'xim', 'PIPENV_VENV_IN_PROJECT': '1', 'NVM_DIR': '/home/vadim/.nvm', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'LC_MEASUREMENT': 'ru_RU.UTF-8', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'LC_PAPER': 'ru_RU.UTF-8', 'LC_MONETARY': 'ru_RU.UTF-8', 'XDG_MENU_PREFIX': 'gnome-', 'LANG': 'en_US.UTF-8', 'DISPLAY': ':0', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'COLORTERM': 'truecolor', 'NVM_CD_FLAGS': '', 'USERNAME': 'vadim', 'CHROME_DESKTOP': 'code-url-handler.desktop', 'XDG_VTNR': '2', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '5346', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'S_COLORS': 'auto', 'LC_NAME': 'ru_RU.UTF-8', 'XDG_SESSION_ID': '2', 'USER': 'vadim', 'DESKTOP_SESSION': 'ubuntu', 'QT4_IM_MODULE': 'xim', 'TEXTDOMAINDIR': '/usr/share/locale/', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'PWD': '/home/vadim/PycharmProjects/python_beazley', 'HOME': '/home/vadim', 'VSCODE_GIT_ASKPASS_NODE': '/usr/share/code/code', 'TEXTDOMAIN': 'im-config', 'SSH_AGENT_PID': '2612', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.56.2', 'QT_ACCESSIBILITY': '1', 'XDG_SESSION_TYPE': 'x11', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'XDG_SESSION_DESKTOP': 'ubuntu', 'LC_ADDRESS': 'ru_RU.UTF-8', 'GJS_DEBUG_OUTPUT': 'stderr', 'LC_NUMERIC': 'ru_RU.UTF-8', 'GTK_MODULES': 'gail:atk-bridge', 'VSCODE_GIT_ASKPASS_MAIN': '/usr/share/code/resources/app/extensions/git/dist/askpass-main.js', 'WINDOWPATH': '2', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'QT_IM_MODULE': 'ibus', 'XMODIFIERS': '@im=ibus', 'IM_CONFIG_PHASE': '2', 'NVM_BIN': '/home/vadim/.nvm/versions/node/v14.8.0/bin', 'XDG_CURRENT_DESKTOP': 'Unity', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/code.desktop', 'SHLVL': '2', 'XDG_SEAT': 'seat0', 'VSCODE_GIT_IPC_HANDLE': '/run/user/1000/vscode-git-2270ec9cf6.sock', 'LC_TELEPHONE': 'ru_RU.UTF-8', 'GDK_BACKEND': 'x11', 'GDMSESSION': 'ubuntu', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'LOGNAME': 'vadim', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'GIT_ASKPASS': '/usr/share/code/resources/app/extensions/git/dist/askpass.sh', 'XDG_RUNTIME_DIR': '/run/user/1000', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'PATH': '/home/vadim/.local/bin:/home/vadim/.nvm/versions/node/v14.8.0/bin:/home/vadim/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'LC_IDENTIFICATION': 'ru_RU.UTF-8', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'SESSION_MANAGER': 'local/luna:@/tmp/.ICE-unix/2534,unix/luna:/tmp/.ICE-unix/2534', 'BREAKPAD_DUMP_LOCATION': '/home/vadim/.config/Code/exthost Crash Reports', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'GTK_IM_MODULE': 'ibus', 'LC_TIME': 'ru_RU.UTF-8', '_': '/usr/local/bin/python3.8'})







