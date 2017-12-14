#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-4 18:24
# @Author  : Jerry Wang
# @Site    : 
# @File    : 解决死锁.py
# @Software: PyCharm
import time

import threading

class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance
        self.lock = threading.RLock()

    def withdraw(self, amount):

        with self.lock:
            self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount


    def drawcash(self, amount):#lock.acquire中嵌套lock.acquire的场景

        with self.lock:
            interest=0.05
            count=amount+amount*interest

            self.withdraw(count)


def transfer(_from, to, amount):

    #锁不可以加在这里 因为其他的其它线程执行的其它方法在不加锁的情况下数据同样是不安全的
     _from.withdraw(amount)

     to.deposit(amount)



alex = Account('alex',1000)
yuan = Account('yuan',1000)

t1=threading.Thread(target = transfer, args = (alex,yuan, 100))
t1.start()

t2=threading.Thread(target = transfer, args = (yuan,alex, 200))
t2.start()

t1.join()
t2.join()
print('>>>',alex.balance)
print('>>>',yuan.balance)