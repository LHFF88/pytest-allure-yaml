import requests


class BaseApi:
    @staticmethod
    def requests_http(req):
        # ** 解包
        result = requests.request(**req)
        return result

