"""解决pytest-html报告中文乱码问题，避免修改pytest-html/plugi.py源码"""
import pytest

from lib.different_db.mysqlclient_A import MySQLClient
from lib.different_http.httpclient_A import HTTPClient_A
def pytest_collection_modifyitems(items):
    # 解决pytest执行用例，标题有中文时显示编码不正确的问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# def pytest_collection_modifyitems(items) :
#     for item in items :
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode escape")


@pytest.fixture
def my_fixture(kwargs):
    # 实例化HTTPClient,用于发送请求
    http_client = HTTPClient_A()
    # 实例化MySQLClient客户端
    mysql_client = MySQLClient()

    # 1.处理setup部分
    execute_sql = kwargs["apis"][0]
    for item in execute_sql.get("setup", "") :
        if item.get("type") == "api" :
            http_client.request(**item.get("data"))
        elif item.get("type") == "db" :
            mysql_client.execute(item.get("sqls"))
    yield
    # 2.处理teardown部分
    for item in execute_sql.get("teardown", "") :

        if item.get("type") == "api" :
            http_client.request(**item.get("data"))
        elif item.get("type") == "db" :
            mysql_client.execute(item.get("sqls"))
