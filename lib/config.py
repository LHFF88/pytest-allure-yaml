"""
对configparser的二次封装
提供一个全局的configparser的实例对象
"""
from configparser import RawConfigParser
import os
CONFIG = RawConfigParser()
CONFIG.read(
    os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        ), "config", "config.ini"
    ), encoding="utf-8"
)
