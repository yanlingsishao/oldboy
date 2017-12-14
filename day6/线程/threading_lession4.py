#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-27 17:50
# @Author  : Jerry Wang
# @Site    : 
# @File    : threading_lession4.py
# @Software: PyCharm
# 线程的创建方式
import threading
import time
# 1
# def sayhi(num):
#     print("running on number:%s"%num)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi,args=(1,))   #生成一个线程实例
#     t2 = threading.Thread(target=sayhi,args=(2,))   #生成另一个线程实例
#     t1.start()  # 启动线程
#     t2.start()  # 启动另一个线程
#     print(t1.getName()) #获取线程名
#     print(t2.getName())

# 2
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on numbser:%s"%self.num)
        time.sleep(3)

if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
