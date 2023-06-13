import time

from jsonpath import jsonpath

def timestamp_data(kwargs):
    t = int(time.time())  # 拿到毫秒级的时间戳
    t = int(round(t*1000))
    expire = t + int(10000)
    if kwargs['apis'][0]['data']['timestamp'] is None:
        kwargs['apis'][0]['data']['timestamp'] = t
    if kwargs['apis'][0]['data']['issueTime'] is None:
        kwargs['apis'][0]['data']['issueTime'] = t
    if kwargs['apis'][0]['data']['expireTime'] is None:
        kwargs['apis'][0]['data']['expireTime'] = expire
    return kwargs
