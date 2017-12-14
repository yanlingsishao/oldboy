#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import requests, sys,json
import urllib3
import fileinput




host = 'http://toutiao-ali.juheapi.com'
path = '/toutiao/index'
method = 'GET'
appcode = '910e5ac5de3c4c5f9bc38c2a314755c3'
querys = 'type=type'
bodys = {}
url = "{}{}?{}".format(host,path,querys)
head = {"APPCODE":appcode}
xx = urllib3.HTTPConnectionPool(url)
xx.

try:
    r = requests.get(url)
    r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)

