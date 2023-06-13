import json
import allure
import pytest
from jsonpath import jsonpath
from lib.get_yaml import read_testcase_yaml
from lib.set_token_timestamp import set_token_timestamp   # 导入不同角色
from lib.different_http.httpclient_A import HTTPClient_A  # 配置不同的url
from lib.logger import Logger
from lib.different_db.mysqlclient_A import MySQLClient


class TestCaseCommon(object):
    # 根据路径更新yaml文件
    yaml_data = read_testcase_yaml("/yaml_data/user_yaml/saveUser.yaml")

    # 接口名称"会在allure的功能显示
    @allure.feature("测试接口")
    # yaml_data数据传递给"kwargs",ids拿到yaml文件中具体的name名称,在运行中显示
    @pytest.mark.parametrize("kwargs", yaml_data,
                             ids=[i['apis'][0].get("name") for i in yaml_data])
    def test_method(self, kwargs, my_fixture):
        # 添加token和时间戳
        kwargs = set_token_timestamp(kwargs)  # 设置请求token(可以设置不同角色)
        # 在yaml文件中添加时间戳
        # 打印
        print("yaml传输的值" + str(kwargs))
        # 实例化日志记录器对象
        self.logger = Logger()
        self.logger.info("\n" + "测试用例开始执行".center(120, "="))
        # 实例化HTTPClient,用于发送请求
        self.http_client = HTTPClient_A()
        # 实例化MySQLClient客户端
        self.mysql_client = MySQLClient()

        args_dict = {}
        # 对数据（当前用例）中的所有接口进行调用,所有接口存放在一个列表当中，遍历一次处理每个接口的调用和断言
        apis = kwargs.get("apis", "")
        for api in apis:
            # 将api转换很json字符串
            api = json.dumps(api)
            """
            将api字符串使用args_dict字典进行格式化
            类似于"%(name)s % {"name": "tom"}" 这样tom就会被替换到name当中
            args_dict = {},会在set_args传入形成字典,对yaml中的"%(asn_code)s" % {asn_code: xxx}的方式进行传递
            %这种方式只有在字符串的情况下,才能进行传递,所以要转化
            """
            # 将api字符串使用args_dict字典进行格式化
            api = api % args_dict
            # 将api字符串转换成json格式的数据
            api = json.loads(api)
            # print("业务流接口" + str(api))

            # 调用接口（发送HTTP请求）
            r = self.http_client.request(**api.get('data'))
            print("响应数值信息: " + str(r.json()))
            print("status: " + str(r.status_code))
            # print("code: " + str(jsonpath(r.json(), "$..code")[0]))
            # 处理断言部分
            for item in api.get("assert", ""):
                # HTTP状态码断言
                if item["type"] == "status":
                    assert (r.status_code == item["expect"])
                # 关键业务信息断言
                elif item["type"] == "sys":
                    current_value = jsonpath(r.json(), "$.." + item['name'])
                    if current_value:
                        assert (current_value[0] == item["expect"])
                # 数据库断言
                elif item["type"] == "db":
                    ret = self.mysql_client.select(item["sql"])
                    print("aaaaaaaaaaaaaaaaa" + str(ret))
                    if ret:
                        assert (ret == item["expect"])

            # 处理接口之间的数据关联， 见后续接口要用到的字段值保存到字典当中
            for item in api.get("set_args", ""):
                self.logger.info("set_args")
                current_value = jsonpath(r.json(), f"$..{item.get('name')}")
                if current_value:
                    args_dict[item.get("key")] = current_value[0]
