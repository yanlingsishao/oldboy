#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
class F1:
    pass

class S1(F1):
    def show(self):
        print("S1.show")


class S2(F1):
    def show(self):
        print("S2.show")


class Func(F1):
    print(F1.show())


s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)