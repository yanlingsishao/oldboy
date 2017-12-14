#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-10-05 13:42
# @Author  : Jerry Wang
# @Site    : 
# @File    : uid.py
# @Software: PyCharm


import hashlib
import time

def create_md():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()

