

import logging



import logging

#  debug  info  warning(默认) error critical


#1  congfig函数

# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s [%(lineno)s] %(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S",
#                     filename="logger",
#                     filemode="a"
#                     )


# logging.debug('debug message')
# num=1000
# logging.info('cost %s'%num)

# logging.warning('warning messagegfdsgsdfg') #
#
# logging.error('error message')
#
# logging.critical('critical message')


#配置两种方式： 1  congfig   2 logger




# 2 logger对象

def get_logger():

    logger=logging.getLogger()

    fh=logging.FileHandler("logger2")

    sh=logging.StreamHandler()

    logger.setLevel(logging.DEBUG)  #设定输出等级

    fm=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logger.addHandler(fh)

    logger.addHandler(sh)

    fh.setFormatter(fm)
    sh.setFormatter(fm)

    return logger

Logger=get_logger()

Logger.debug('logger debug message')
Logger.info('logger info message')
Logger.warning('logger warning message')
Logger.error('logger error message')
Logger.critical('logger critical message')










