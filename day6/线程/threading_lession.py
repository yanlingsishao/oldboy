#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 16:14
# @Author  : Jerry Wang
# @Site    : 
# @File    : threading_lession.py
# @Software: PyCharm
import threading#线程
import time

def Hi(name):
    print("hi,%s"%name)
    time.sleep(3)
if __name__ == "__main__":
    t1 = threading.Thread(target=Hi,args=(10,))
    t1.start()

    t2 = threading.Thread(target=Hi,args=(9,))
    t2.start()

    t1.join()
    t2.join()
    # print("ending")

