#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-27 17:58
# @Author  : Jerry Wang
# @Site    : 
# @File    : threading_lession5.py
# @Software: PyCharm

import threading,time
start = time.asctime()
def add():
    num = 0
    for i in range(1000000):
        num += i

    print(num)


def mul():
    num = 1
    for i in range(1,1000000):
        num += i

    print(num)

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=mul)

i = []
i.append(t1)
i.append(t2)

for t in i:

    t.start()1

for t in i:

    t.join()

print("time%s"%(time.asctime()-start))
