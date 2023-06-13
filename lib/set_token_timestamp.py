import time

from lib.different_role.land_root import HttpClientLandRoot


# 设置root的token
def set_token_timestamp(kwargs):
    # 获取token
    token_value = HttpClientLandRoot().get_token()

    # 设置token
    token_all = {"Authorization": "Jztdata " + token_value[0]}
    if kwargs["apis"][0]['data']['headers'] is None:
        kwargs["apis"][0]['data']['headers'] = token_all

    # 设置时间戳
    if kwargs['apis'][0]['data']['json']['timestamp'] is None:
        timestamp = int(time.time() * 1000)
        kwargs["apis"][0]['data']['json']['timestamp'] = timestamp
    return kwargs

