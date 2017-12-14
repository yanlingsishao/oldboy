#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 17:21
# @Author  : Jerry Wang
# @Site    : 
# @File    : threading_lession2.py
# @Software: PyCharm

import time
import threading

def music():
    print("listen to music %s" % (time.asctime()))  #1
    time.sleep(3)
    print("listen to music %s" % (time.asctime()))  #2

def game():
    print("play game %s"%(time.asctime()))          #1
    time.sleep(5)
    print("play game %s" % (time.asctime()))

if __name__ == "__main__":
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)
    t1.start()
    t2.start()
    #t1.join()
    t2.join()
    print("ending")