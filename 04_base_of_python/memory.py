





""" АЛЛОКАТОР ===================================================================

    Арена — большой непрерывный кусок памяти (обычно 256 килобайт), содержит несколько страниц виртуальной памяти операционной системы. В арене могут быть пулы с разными размерами блоков. Если used-пула нет, тогда берется empty-пул. Если и empty-пулов нет, то запрашивается новая арена.

    Пул — одна страница виртуальной памяти (обычно 4 килобайта). Каждый пул предназначен для хранения блоков одинакового размера. Каждый пул может быть в одном из трех состояний — used, full и empty. Каждый пул содержит список свободных и занятых блоков.

    Блок — маленький кусочек памяти, используемый для хранения одного объекта. Они могут быть размером 8, 16, 24, 32 …. 512 байт.



    счетчик ссылок - если сссылок 0 - удаляет.
    сборщик мусора (garbage collector) - смотрит, доступны ли объекты из основного кода на Python. Если нет - удаляет.

"""











