import logging
from logging import handlers
from case02.config.read_ini import log_level,log_file

def logger():
    #创建日志对象
    logger=logging.getLogger('logger')
    #设置日志等级
    if log_level==str(0):
        logger.setLevel(logging.INFO)
    elif log_level==str(1):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    if not logger.handlers:
        #日志切割，最大100M,最多50个
        file_handler=logging.handlers.RotatingFileHandler(log_file,mode='a',encoding='utf-8',
                                                          maxBytes=1024*1024*100,backupCount=50)
        file_handler.setLevel(logging.DEBUG)
        #创建控制台输出handler
        console_handler=logging.StreamHandler()
        #定义handler输出格式
        formatter=logging.Formatter('[%(asctime)s]-[%(filename)s line:%(lineno)d]- %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        #logger添加handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger

if __name__=='__main__':
    logger().info("info等级的日志")
    logger().debug('debug等级的信息')