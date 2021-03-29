import logging

#实例化
logger = logging.getLogger('test_case')
#设置日志的级别，最低级别就是debug，
logger.setLevel(logging.DEBUG)
#设置日志的格式
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#写入到文件中的日志
fl = logging.FileHandler(filename='../log/test.log',mode='a',encoding='utf-8')
#设置写入日志文件中的日志格式
fl.setFormatter(format)

#输出到终端的日志信息
sl = logging.StreamHandler()
#设置输出的日志格式
sl.setFormatter(format)

logger.addHandler(fl)
logger.addHandler(sl)


# logger.debug("test")