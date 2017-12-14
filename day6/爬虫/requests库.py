#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-1 14:42
# @Author  : Jerry Wang
# @Site    : 
# @File    : requests库.py
# @Software: PyCharm
import requests
# r = requests.get("http://cuiqingcai.com")
# print(type(r))
# print(r.status_code)
# print(r.encoding)
# print(r.cookies)


# 基于GET请求
# payload = {"key1":"value1", 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get",params=payload)
# print(r.url)

# json解析
# files = {'file': open('a.json', 'rb')}
# r =requests.get("http://httpbin.org/get",data=files)
# print(r.text)
# print(r.json())


# 基于POST请求
# payload = {"key1":"value1","key2":"value2"}
# r = requests.post("http://httpbin.org/post",data=payload)#传参
# print(r.text)

# url = 'http://httpbin.org/post'
# files = {'file': open('a.txt', 'rb')}
# r = requests.post(url, files=files)
# print (r.text)


# Cookies
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print (r.text)


# SSL证书验证
# r = requests.get("https://kyfw.12306.cn/otn/",verify=False)
# print(r.text)


proxies = {
  "https": "http://10.10.1.10:3128"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print (r.text)
