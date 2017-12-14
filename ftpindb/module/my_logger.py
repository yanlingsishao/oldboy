#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年7月27日
@author: WangQiyuan

'''
import logging

ATM_LOG="..\\logs\\all.logs"



def logger():
    logger=logging.getLogger()#logger对象
    fh=logging.FileHandler(ATM_LOG,encoding="utf-8")#向文件发送日志
    fm=logging.Formatter("%(asctime)s - %(name)s - %(message)s - [%(thread)d:%(process)d]")
    fh.setFormatter(fm)
    logger.addHandler(fh)
    return (fh,logger)


class MyLogger:
    def debug(msg):
        mylogger = logger()
        mylogger_fh = mylogger[0]
        mylogger_func = mylogger[1]
        mylogger_func.setLevel("DEBUG")
        mylogger_func.debug(('{} {}'.format("debug",msg)))
        mylogger_func.removeHandler(mylogger_fh)
    def error(msg):
        mylogger = logger()
        mylogger_fh = mylogger[0]
        mylogger_func = mylogger[1]
        mylogger_func.setLevel("ERROR")
        mylogger_func.error(('{} {}'.format("error",msg)))
        mylogger_func.removeHandler(mylogger_fh)
    def info(msg):
        mylogger = logger()
        mylogger_fh = mylogger[0]
        mylogger_func = mylogger[1]
        mylogger_func.setLevel("INFO")
        mylogger_func.info(('{} {}'.format("INFO",msg)))
        mylogger_func.removeHandler(mylogger_fh)
    def warning(msg):
        mylogger = logger()
        mylogger_fh = mylogger[0]
        mylogger_func = mylogger[1]
        mylogger_func.setLevel("WARNING")
        mylogger_func.debug(('{} {}'.format("warning",msg)))
        mylogger_func.removeHandler(mylogger_fh)


    # def error(msg):
    #     mylogger = logger()
    #     mylogger_fh = mylogger[0]
    #     mylogger_func = mylogger[1]
    #     mylogger_func.setLevel("DEBUG")
    #     mylogger_func.debug(('{} {}'.format("DEBUG", msg)))
    #     mylogger_func.removeHandler(mylogger_fh)




# def warning(self):
#     logger.warning('Warning {}'.format(self))
# def error(self):
#     logger.error('Error {}'.format(self))
# #
# jj={
#     "INFO":info,
#     "WARNING":warning,
#     "ERROR":error
# }


# logger.(jj.keys())(({} {}).format(jj.get()))