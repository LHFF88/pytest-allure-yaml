from base_api import BaseApi


class Download:
    def download(self):
        req = {
            "url": "127.0.0.1/download",
            "method": "GET",
            "headers": {},
            "params": {
                "contractId": 2947403075747869536,
                "downloadItems": ["NORMAL"],
                "needCompressForOneFile": False
            },
        }
        res = BaseApi().requests_http(req).content  # 注意“.content"获取返回内容
        # with open("F:/response.zip", "wb") as f:
        with open("F:/response.pdf", "wb") as f:
            f.write(res)
        return res


if __name__ == '__main__':
    Download().download()
