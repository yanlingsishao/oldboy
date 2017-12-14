#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-27 17:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : threading_lession3.py
# @Software: PyCharm

import threading
from time import ctime,sleep
import time

def ListenMusic(name):

        print ("Begin listening to %s. %s" %(name,ctime()))
        sleep(3)
        print("end listening %s"%ctime())

def RecordBlog(title):

        print ("Begin recording the %s! %s" %(title,ctime()))
        sleep(5)
        print('end recording %s'%ctime())


threads = []


t1 = threading.Thread(target=ListenMusic,args=('水手',))
t2 = threading.Thread(target=RecordBlog,args=('python线程',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    #t2.setDaemon(True)
    for t in threads:
        #t.setDaemon(True) #注意:一定在start之前设置
        t.start()
        print(threading.activeCount())
        #t.join()
    #t.join()
    #t.setDaemon(True)
    #print(threading.activeCount())
    #t2.join()########考虑这三种join位置下的结果？
    while threading.activeCount() == 1:
        print ("all over %s" %ctime())

