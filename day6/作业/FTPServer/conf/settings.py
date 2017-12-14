#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-5 14:09
# @Author  : Jerry Wang
# @Site    : 
# @File    : settings.py
# @Software: PyCharm
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
user_home = "%s/home" % basedir
user_info = "%s/db" % basedir

HOST = "0.0.0.0"
PORT = 9999