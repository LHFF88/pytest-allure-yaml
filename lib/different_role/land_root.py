"""
思路
从ini文件获取数据,发送登陆请求
获取返回的token
return token
"""
import requests
from lib.config import CONFIG
from jsonpath import jsonpath
from lib.logger import Logger
import hashlib
import time


class HttpClientLandRoot(object):
    def __init__(self, host=None, port=None, protocol=None, path=None, method=None,
                 username_key=None, username=None, password_key=None, password=None):
        # 初始化不传参时从配置文件中读取配置项
        self.post = None
        self.host = host if host else CONFIG["server_A"]["host"]
        self.port = port if port else CONFIG["server_A"]["port"]
        self.protocol = protocol if protocol else CONFIG["server_A"]["protocol"]
        self.path = path if path else CONFIG["land_root"]["path"]
        self.method = method if method else CONFIG["land_root"]["method"]
        self.username_key = username_key if username_key else CONFIG["land_root"]["username_key"]
        self.username = username if username else CONFIG["land_root"]["username"]
        self.password_key = password_key if password_key else CONFIG["land_root"]["password_key"]
        self.password = password if password else CONFIG["land_root"]["password"]
        self.client = requests.Session()
        self.logger = Logger()

    def password_md5(self):
        password_MD5 = self.password
        try:
            if password_MD5:
                new_md5 = str(password_MD5)
                # print("md5为"+new_md5)
                MD5 = hashlib.md5(new_md5.encode("utf-8")).hexdigest()
                self.password_md5_md5 = MD5
                return self.password_md5_md5

        except:
            print("未传password")

    def request(self):
        url = self.protocol + "://" + self.host + ":" + self.port + self.path
        print("登录账号： " + self.username)
        print("登录密码： " + self.password_md5())
        # 打印日志
        self.logger.info(f"url: {url}")
        # 登陆参数传递(账号,密码,时间戳可能会改)
        log_In = {self.username_key: self.username, self.password_key: self.password_md5_md5,
                  "timestamp": int(time.time() * 1000)}
        # 发起登陆请求(账号,密码,时间戳)
        r = self.client.request(url=url, method=self.method,
                                json=log_In)
        self.logger.debug(f"responseBody: {r.text}")
        return r

    # 根据请求的json中的accessToken获取token
    def get_token(self):
        get_json = jsonpath(self.request().json(), "$..accessToken")
        return get_json

    # 传递时间戳
    def timestamp(self, kwargs):
        # 添加时间戳
        timestamp = jsonpath(kwargs, "$..timestamp")

        try:
            if kwargs['apis'][0]['data']['json']['timestamp'] is None:
                timestamp = int(time.time() * 1000)
                kwargs["apis"][0]['data']['json']['timestamp'] = timestamp
            return kwargs
        except:
            print("未传timestamp")