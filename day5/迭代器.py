#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# class Foo:
#     def __init__(self,a):
#        self.a = a
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         self.a += 1
#         return self.a
#
#
#
#
# for i in Foo(3):
#     print(i)


class Foo:
    def __init__(self,start,stop):
        self.num=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n=self.num
        self.num+=1
        return n

f=Foo(1,5)
from collections import Iterable,Iterator
print(isinstance(f,Iterator))

for i in Foo(1,5):
    print(i)