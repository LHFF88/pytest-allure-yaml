import yaml
import os


# 拿到绝对路径
absolute_path = (os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


# 读取测试用例
def read_testcase_yaml(yaml_fail: object) -> object:
    with open(absolute_path + yaml_fail, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 读取报告
def read_html(html_fail: object) -> object:
    with open(absolute_path + html_fail, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value