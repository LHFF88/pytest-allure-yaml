aa = {'apis':
          [{'name': '后台用户管理 用户新增 通过性测试01', 'data':
              {'path': '/admin/add', 'method': 'post', 'headers':
                  {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJBcGl0ZXN0IiwiY3JlYXRlZCI6MTY3MDkwOTg5MTk2OCwiZXhwIjoxNjcwOTUzMDkxfQ.JpeRSv48_HLT6V-46jPlzPR9RFiR27rT_16N6TXjIZVK-PT1Qj7mZaMSZLOFob_9_9klkm8E__HVcCrfKfnYzA'},
               'json': {'username': '测试0001', 'password': '84086854434102de19fcd60b20238152', 'departmentId': 1, 'roleId': [2], 'type': 1}},
            'assert': [{'type': 'status', 'expect': 200}, {'type': 'sys', 'name': 'code', 'expect': 200}]}],
      'teardown': [{'type': 'db', 'sqls': ["DELETE FROM ums_admin WHERE username = '测试0001';"]}]}

# bb = aa.get('teardown')
# print(bb)

cc = {'apis': [{'name': '后台用户管理 用户新增 通过性测试01', 'data': {'path': '/admin/add', 'method': 'post', 'headers': {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJBcGl0ZXN0IiwiY3JlYXRlZCI6MTY3MDkxMDEzNjk4MCwiZXhwIjoxNjcwOTUzMzM2fQ.BGeGzRIbJm8M9RXUupl1z-VujsuzE7jdvAav3wkP90U33dJsJacgG4QFujVBqnOB21IduGOU2nHuGaw8dfbQMw'}, 'json': {'username': '测试0001', 'password': '84086854434102de19fcd60b20238152', 'departmentId': 1, 'roleId': [2], 'type': 1}}, 'assert': [{'type': 'status', 'expect': 200}, {'type': 'sys', 'name': 'code', 'expect': 200}]}], 'teardown': [{'type': 'db', 'sqls': ["DELETE FROM ums_admin WHERE username = '测试0001';"]}]}
dd = cc.get('teardown')
print(dd)