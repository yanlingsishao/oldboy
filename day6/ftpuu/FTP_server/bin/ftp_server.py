#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-6 14:13
# @Author  : Jerry Wang
# @Site    : 
# @File    : ftp_server.py
# @Software: PyCharm


import os,sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from module import main


if __name__ == "__main__":
    main.ArgvHandler()