#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="logger.log",
#     filemode="w",
#     format="%(asctime)s [line%(lineno)s] %(message)s [%(levelname)s]",
#
#
# )
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# logging.log(10,'log') #如果level=40,则只有logging.critical和loggin.error的日志会被打印
#
# -----------------------------------------logger
def logger():
    logger=logging.getLogger()#logger对象

    fh=logging.FileHandler("test_log")#向文件发送日志
    ch=logging.StreamHandler()#向屏幕发送日志
    #两者需要格式fm
    fm=logging.Formatter("%(asctime)s %(message)s")

    fh.setFormatter(fm)
    ch.setFormatter(fm)

    logger.addHandler(fh)
    logger.addHandler(ch)
    #logger.setLevel("DEBUG")
    return logger
# -------------------------------------------------
ff=logger()
ff.setLevel("DEBUG")
ff.debug("hello")
ff.info('info')
ff.warning('warning')
ff.error('error')
ff.critical('critical')

# import requests
# r=requests.get(url="http://www.baidu.com")
# print(r.status_code)
# r = requests.get(url="http://www.52touzi.cn",params={'wd':'python'})
# print(r.url)
# print(r.text)

