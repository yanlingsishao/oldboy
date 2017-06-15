#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import hashlib

def hash_m(value):#加密方法
    hash = hashlib.md5()
    hash.update(value.encode('utf-8'))
    hash=hash.hexdigest()
    return hash



#print(hash_m("123456"))




