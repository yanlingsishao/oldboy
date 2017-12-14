#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-29 14:00
# @Author  : Jerry Wang
# @Site    : 
# @File    : fabfile.py
# @Software: PyCharm
#from gevent import monkey;monkey.patch_all()
import gevent
def eat(name):
    print('%s eat 1' %name)
    gevent.sleep(2)
    print('%s eat 2' %name)

def play(name):
    print('%s play 1' %name)
    gevent.sleep(1)
    print('%s play 2' %name)


g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,name='egon')
g1.join()
g2.join()
#或者gevent.joinall([g1,g2])
print('主')