#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月16日
@author: WangQiyuan

'''
# {1,2,3,1}
# 或
# 定义可变集合set
set_test=set('hello')
print(set_test)
# >>>{'l', 'o', 'e', 'h'}
# 改为不可变集合frozenset
f_set_test=frozenset(set_test)
print(f_set_test)
# >>>frozenset({'l', 'e', 'h', 'o'})