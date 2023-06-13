"""
对logging模块的二次封装
目的：提供一个在框架的其它地方拿来即用的一个日志记录器对象
返回一个日志记录器
1. 定义一个Logger一个类，实例化会返回一个日志记录器对象
2. 日志文件存放在项目根目录下的log目录中
3. 每天对应一个日志文件
"""
import logging
import os
import time
from lib.config import CONFIG


class Logger(object):
    __instance = None

    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        # 准备工作
        # 获取项目的根目录的绝对路径
        current_path = os.path.abspath(__file__)
        root_path = os.path.dirname(os.path.dirname(current_path))
        log_path = os.path.join(root_path, "log")
        # 日志文件名称
        log_name = "log_" + time.strftime("%Y_%m_%d") + ".log"

        # 创建一个日志记录器
        logger = logging.getLogger(CONFIG["logger"]["name"])
        logger.setLevel(logging.DEBUG)

        # 创建日志处理器
        fh = logging.FileHandler(filename=os.path.join(log_path, log_name),
                                 encoding="utf8")
        fh_level = CONFIG["logger"]["fh_level"].upper()
        fh.setLevel(getattr(logging, fh_level))

        sh = logging.StreamHandler()
        sh_level = CONFIG["logger"]["sh_level"].upper()
        sh.setLevel(getattr(logging, sh_level))

        # 创建格式器
        fm = logging.Formatter(fmt=CONFIG["logger"]["format"],
                               datefmt=CONFIG["logger"]["datefmt"])

        fh.setFormatter(fm)
        sh.setFormatter(fm)

        logger.addHandler(fh)
        logger.addHandler(sh)

        cls.__instance = logger
        # 返回日志记录器
        return logger


if __name__ == '__main__':
    Logger()
