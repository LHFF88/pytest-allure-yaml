"""
对requests模块的二次封装
目的： 提供简单，固定的接口
要求： 使用session机制
"""

import requests
from lib.config import CONFIG
from lib.logger import Logger


class HTTPClient_B(object):
    def __init__(self, host=None, port=None, protocol=None):
        # 初始化不传参时从配置文件中读取配置项
        self.host = host if host else CONFIG["server_B"]["host"]
        self.port = port if port else CONFIG["server_B"]["port"]
        self.protocol = protocol if protocol else CONFIG["server_B"]["protocol"]
        self.client = requests.Session()
        self.logger = Logger()

    def request_B(self, path, **kwargs):
        url = self.protocol + "://" + self.host + ":" + self.port + path
        self.logger.info(f"url: {url}")
        r = self.client.request(url=url, **kwargs)
        self.logger.debug(f"responseBody: {r.text}")
        return r

    def set_headers(self, headers):
        self.client.headers.update(headers)

    def __del__(self):
        self.client.close()
