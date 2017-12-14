#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-28 13:38
# @Author  : Jerry Wang
# @Site    : 
# @File    : Lock_lession.py
# @Software: PyCharm

# def gen_AB():
#     print('start')
#     yield 'A'
#     print('continue')
#     yield 'B'
#     print('end.')
#     yield 'C'
#     print("nima")
#
#
# res1 = [x * 3 for x in gen_AB()]
# print(res1)
# for i in res1:
#     print('-->', i)

import threading,time

class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name,"gotlockB",time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name,"gotlockA",time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()
if __name__=="__main__":

    lockA=threading.Lock()
    lockB=threading.Lock()
    threads=[]
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待线程结束，后面再讲