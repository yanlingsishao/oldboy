#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
l=(3,32,32,"fdsa")
diedai_l=l.__iter__()
while True:
    try:
        print(diedai_l.__next__())
    except StopIteration:
        print('迭代完毕了,循环终止了')
        break
