import redis
import time


r = redis.StrictRedis(
    host='localhost',
    port=6379,
    # password='qwerty',
    charset="utf-8",
    decode_responses=True
)


# r.set('ip_address', '127.0.0.0')
# r.set('timestamp', int(time.time()))
# r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11)')
# r.set('last_page_visited', 'home')



r.zadd('hot_tours', {'tour1': 999, 'tour2': 222, 'tour3': 500})                

res =r.zrank('hot_tours', 'tour2')       # 0 индекс элемента в отсортированном списке
# r.zrevrange('hot_tours', 0, -1)    # ['tour1', 'tour3', 'tour2'] сортирует от большего к меньшему
print(res)










