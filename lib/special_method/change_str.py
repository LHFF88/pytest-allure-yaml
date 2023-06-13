import json

from jsonpath import jsonpath

from lib.special_method.Single_change_double_quotes import DoubleQuoteDict


# 把需要data中的某个数据,用DoubleQuoteDict方法,由单引号转化成双引号
def changes_sign(api, name):
    if name in api['data']['data']:
        changes_value = jsonpath(api, "$.." + name)
        api['data']['data'][name] = DoubleQuoteDict(changes_value[0])
        return api
    return api


# 把需要data中的某个数据,用json.dumps方法,由单引号转化成双引号
def changes_str(api, name):
    if name in api['data']:
        changes_value = jsonpath(api, "$.." + name)
        api['data'][name] = json.dumps(changes_value[0])
        return api
    return api


# 把需要data中的某个数据,中的数据把双引号去掉shy双引号
def changes_cancel_syh(api, name):
    if name in api:
        api = api.replace('\"{', "{")
        api = api.replace('}\"', '}')
        return api
    return api


# request中把需要data中的某个数据,空格去掉
def cancel_blank(kwargs, name):
    if name in kwargs['data']:
        content = str(kwargs['data'][name])
        content = content.replace(': ', ":")
        content = content.replace('\'', "\"")
        content = content.replace(', ', ",")
        kwargs['data'][name] = content
        return kwargs
    return kwargs


if __name__ == '__main__':
    api = {'data': {'path': '/do/auth/request', 'method': 'post', 'data': {
        'sign': 'B0okGocfacmNbvZIq1yC+RjVOFNqju7Ip/B+fgKJlucUOtalH+JkjLp2ppM9LZTUznKMU2qSo44Ud6+lm7pjBi+jSMir6WSs7H1B4xQsDHsSaftBp6vrROEeMWEKGrhWmQK5hu8+8Bb9ra6IVz0Mqkipn7gtsKfAstey5H29lQ4=',
        'appId': '1591413300057473024', 'timestamp': '1669477212000',
        'content': {"expireTime": 1669477222000, "issueTime": 1669477212000,
                    "userInfo": {"name": "Test01", "phone": "13780612189", "uid": "370282199908237894"}}}},
           'assert': [{'type': 'status', 'expect': 200}, {'type': 'sys', 'name': 'code', 'expect': 200}]}

    name = 'content'
    aa = changes_sign(api, name)
    bb = changes_str(aa, name)
    print(type(bb))
    print(bb)
