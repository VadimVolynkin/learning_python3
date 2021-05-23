
from collections import Counter
from re import findall

with open('some.txt') as fp:
    # ищет только слова без знаков с переводом в нижний регистр
    # findall(что искать, где искать)
    words = findall(r'\w+', fp.read().lower())

cnt = Counter(words).most_common(10)
print(cnt)






