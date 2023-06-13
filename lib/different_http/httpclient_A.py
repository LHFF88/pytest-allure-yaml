"""
对requests模块的二次封装
目的： 提供简单，固定的接口
要求： 使用session机制
"""
import requests
from lib.config import CONFIG
from lib.logger import Logger


class HTTPClient_A(object):
    def __init__(self, host=None, port=None, protocol=None):
        # 初始化不传参时从配置文件中读取配置项
        self.host = host if host else CONFIG["server_A"]["host"]
        self.port = port if port else CONFIG["server_A"]["port"]
        self.protocol = protocol if protocol else CONFIG["server_A"]["protocol"]
        self.client = requests.Session()
        self.logger = Logger()

    def request(self, path, **kwargs):
        url = self.protocol + "://" + self.host + ":" + self.port + path
        print("URL为:" + str(url))
        self.logger.info(f"url: {url}")
        # 把需要data中的某个数据,空格去掉
        # kwargs = cancel_blank(kwargs, 'content')
        r = self.client.request(url=url, **kwargs)
        self.logger.debug(f"responseBody: {r.text}")
        return r

    def set_headers(self, headers):
        self.client.headers.update(headers)

    def __del__(self):
        self.client.close()
