"""
对pymysql的二次封装
提供两个接口：
    select     查询
    execute    插入，删除，修改
"""
import pymysql
from lib.config import CONFIG
from lib.logger import Logger


class MySQLClient(object):
    logger = Logger()

    def __init__(self, host=None, user=None, password=None, db=None, port=None):
        # 如果实例化的时候不传参，则从配置文件中读取参数值
        self.host = host if host is not None else CONFIG["database_A"]["host"]
        self.user = user if user is not None else CONFIG["database_A"]["user"]
        self.password = password if password is not None else CONFIG["database_A"]["password"]
        self.db = db if db is not None else CONFIG["database_A"]["db"]
        self.port = port if port is not None else int(CONFIG["database_A"]["port"])

    def select(self, sql):
        with pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db,
                             port=self.port,
                             cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                ret = cursor.execute(sql)
                self.logger.debug(sql)
                self.logger.debug(ret)
                return ret

    def execute(self, sqls):
        """提供insert, update, delete操作的接口，支持事务功能"""
        with pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db,
                             port=self.port,
                             cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                try:

                    cursor.execute(sqls)
                    self.logger.debug(sqls)
                except Exception:
                    connection.rollback()  # 清除缓存中的修改，让所有的sql语句都失效
                else:
                    connection.commit()  # 所有的sql语句都没有异常时，将缓存中的修改提交到数据库中
