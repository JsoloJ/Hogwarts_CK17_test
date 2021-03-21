import configparser
from test_api.util.log import logger

def config_func(section, option):
    # logger.info("读取配置文件")
    config = configparser.ConfigParser()
    config.read("../config/config.ini", encoding="utf-8")
    value = config.get(section, option)
    return value


# config_func('config','path')