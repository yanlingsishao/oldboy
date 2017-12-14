#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-6 14:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IP = "127.0.0.1"
PORT = 8080

ACCOUNT_PATH = os.path.join(BASE_DIR,"conf","accounts.cfg")