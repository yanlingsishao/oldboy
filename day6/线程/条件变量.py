#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-29 15:39
# @Author  : Jerry Wang
# @Site    : 
# @File    : 条件变量.py
# @Software: PyCharm
import time,threading
import random

queue = []

con = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) > 100:
                    con.wait()
                else:
                    elem = random.randrange(100)
                    queue.append(elem)
                    print("Producer a elem {}, Now size is {}".format(elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()


class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) < 0:
                    con.wait()
                else:
                    elem = queue.pop()
                    print("Consumer a elem {}. Now size is {}".format(elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()


def main():
    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()

main()