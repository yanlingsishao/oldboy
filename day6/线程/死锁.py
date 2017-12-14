#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-29 15:26
# @Author  : Jerry Wang
# @Site    : 
# @File    : 死锁.py
# @Software: PyCharm
import threading,time
mutex_a = threading.Lock()
mutex_b = threading.Lock()


class MyThread(threading.Thread):
    def task_a(self):
        if mutex_a.acquire():
            print("thread {} get mutex a ".format(self.name))
            time.sleep(1)
            if mutex_b.acquire():
                print("thread {} get mutex b ".format(self.name))
                mutex_b.release()

            mutex_a.release()


    def task_b(self):

        if mutex_b.acquire():
            print("thread {} get mutex a ".format(self.name))
            time.sleep(1)
            if mutex_a.acquire():

                print("thread {} get mutex b ".format(self.name))

                mutex_a.release()
            mutex_b.release()



    def run(self):
        self.task_a()
        self.task_b()


def main():
    print("Start main threading")

    threads = [MyThread() for i in range(2)]

    for t in threads:
        t.start()

    print("End Main threading")

main()