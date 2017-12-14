#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 11:32
# @Author  : Jerry Wang
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

import urllib.request
import urllib.parse

url = "https://www.52touzi.cn/customer/login"

value = {"username":"15010583665","password":"wqy5715211995"}
data = urllib.parse.urlencode(value).encode(encoding="utf-8")
get_url = url,"?",data
print(get_url)
request = urllib.request.Request(get_url)
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))