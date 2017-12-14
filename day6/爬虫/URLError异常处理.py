#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-1 11:20
# @Author  : Jerry Wang
# @Site    : 
# @File    : URLError异常处理.py
# @Software: PyCharm

import urllib.request

data = urllib.request.Request('http://blog.csdn.net/cqcreffff')

# URLError
# try:
#     urllib.request.urlopen(data)
# except urllib.request.URLError as e:
#     print(e.reason)
#
# try:
#     urllib.request.urlopen(data)
# except urllib.request.HTTPError as e:
#     print (e.code)
# except urllib.request.URLError as e:
#     print(e.reason)
# else:
#     print("ok")



try:
    urllib.request.urlopen(data)

except urllib.request.URLError as e:
    if hasattr(e,"reason"):
        print(e.reason)
else:
    print("ok")
