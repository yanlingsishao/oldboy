#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
bar = [lambda x: i + x for i in range(10)]
val = bar[1](100)
print(val)