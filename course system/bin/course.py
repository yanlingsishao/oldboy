#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-01 13:42
# @Author  : Jerry Wang
# @Site    : 
# @File    : course.py
# @Software: PyCharm


import sys,os

#程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    a =main.Run()
    a.interactive()

