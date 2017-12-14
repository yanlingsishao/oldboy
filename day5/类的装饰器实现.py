#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
def wrapper(fn):
    def deso():

        print("我被封装了，现在执行了")
        x = fn()
        return x
    return deso

@wrapper   #>>>>Foo=deso(Foo)
class Foo:
    print("我是主程序")
    pass

x = Foo()



