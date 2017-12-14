#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-5 14:07
# @Author  : Jerry Wang
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import logging, os, pickle, sys, uuid

frame = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(frame)


# from conf import setting
#
# def sys_logging(content,levelname):
#     '''
#     程序记录日志函数
#     :param content: 日志的内容
#     :param levelname: 日志的等级
#     :return: none
#     '''
#     _filename = os.path.join(setting.log_dir,"log_sys.log")
#     log = logging.getLogger(_filename)
#     logging.basicConfig(filename=_filename,level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#     if levelname == 'debug':
#         logging.debug(content)
#     elif levelname == 'info':
#         logging.info(content)
#     elif levelname == 'warning':
#         logging.warning(content)
#     elif levelname == 'error':
#         logging.error(content)
#     elif levelname == 'critical':
#         logging.critical(content)

def show(msg, msg_type):
    '''
    程序不同信息打印的字体颜色
    :param msg: 打印信息
    :param msg_type: 打印信息的类型
    :return: none
    '''
    if msg_type == "info":
        show_msg = "\033[1;35m%s\033[0m" % msg
    elif msg_type == "error":
        show_msg = "\033[1;31m%s\033[0m" % msg
    elif msg_type == "msg":
        show_msg = "\033[1;37m%s\033[0m" % msg
    else:
        show_msg = "\033[1;32m%s\033[0m" % msg
    print(show_msg)