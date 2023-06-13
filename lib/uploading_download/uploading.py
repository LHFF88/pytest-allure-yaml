from lib.file_uploading.base_api import BaseApi

class Createbyfile:
    def createbyfile(self):
        req = {
                    "url": "127.0.0.1/createbyfile",
                    "method": "POST",
                    "headers": {},
                    "files": {"file": ("", open(r"F:\pdf_file.pdf", "rb"), "pdf")},
                    "data": {
                        "title": "接口发起的文档",
                        "fileType": "pdf"
                    }
        }
        res = BaseApi().requests_http(req)
        assert res.status_code == 200
        res_json = res.json()
        # return res_json["result"]["documentId"]

