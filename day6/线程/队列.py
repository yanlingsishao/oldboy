#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-29 15:43
# @Author  : Jerry Wang
# @Site    : 
# @File    : 队列.py
# @Software: PyCharm
import queue,random
import threading,time
queue_a = queue.Queue(10)
class Producer(threading.Thread):
    def run(self):
        while True:
            elem = random.randrange(100)
            queue_a.put(elem)
            print("Producer a elem {},Now size is {}".format(elem,queue_a.qsize()))
            time.sleep(random.random())

class Consumer(threading.Thread):
    def run(self):
        while True:
            elem = queue_a.get()
            queue_a.task_done()
            print("Consumer a elem {},Now size is {}".format(elem,queue_a.qsize()))
            time.sleep(random.random())

def main():
    for i in range(3):
        Producer().start()
    for i in range(2):
        Consumer().start()

if __name__ == '__main__':
    main()
