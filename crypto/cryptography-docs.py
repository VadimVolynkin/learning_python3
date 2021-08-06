import redis
import json
from cryptography.fernet import Fernet

r = redis.Redis(host='localhost', port=6379, db=0)

cipher = Fernet(Fernet.generate_key())

info = {
    "cardnum": 2211849528391929,
    "exp": [2020, 9],
    "cv2": 842,
}
 
# создает json строку из данных
# шифрует строку
# создает ключь базе
r.set("user:1000", cipher.encrypt(json.dumps(info).encode("utf-8")))


# шифрованные данные в базе редис
print(r.get("user:1000"))
# b'gAAAAABhDSnctQ-R96O8-p9adoRenGctMhGzTxULVP40nvNl2TP9LX9FHzLFIEoYVWJxu7Ug9OTi5eIzaWozlOW5Me_9aOzref9ricjzsDrM0qAts5EQBjSSW8qc6o2md772pDSE9tVdDodgsabT4yFqE1vobJP4jw=='

# получает данные из редиса
# расшифровывает в json строку
# десериализует в словарб питона
data = json.loads(cipher.decrypt(r.get("user:1000")))
print(data)         # {'cardnum': 2211849528391929, 'exp': [2020, 9], 'cv2': 842}
print(type(data))   # <class 'dict'>