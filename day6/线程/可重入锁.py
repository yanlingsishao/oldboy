#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-29 15:31
# @Author  : Jerry Wang
# @Site    : 
# @File    : 可重入锁.py
# @Software: PyCharm
import time,threading

mutex = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(1):
            print("thread {} get mutex".format(self.name))
            time.sleep(1)
            mutex.acquire()
            mutex.release()
            mutex.release()


def main():
    print("Start main threading")

    threads = [MyThread() for i in range(2)]
    for t in threads:
        t.start()

    print("End Main threading")

main()