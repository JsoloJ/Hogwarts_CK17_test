import configparser
from test_api.util.log import logger

def config_read(section, option):
    # logger.info("读取配置文件")
    config = configparser.ConfigParser()
    config.read("../config/config.ini", encoding="utf-8")
    value = config.get(section, option)
    return value

def config_write(section,option,value):
    config = configparser.ConfigParser()
    config.read("../config/config.ini", encoding="utf-8")
    config.set(section,option,value)
    with open("../config/config.ini", "w",encoding="utf-8") as configfile:
        config.write(configfile)





# config_func('config','path')