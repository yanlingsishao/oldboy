#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-1 12:00
# @Author  : Jerry Wang
# @Site    : 
# @File    : 抓取段子.py
# @Software: PyCharm

import urllib
from urllib import request
page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)


def getHTML(url):
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url, headers=headers)
    return request.urlopen(req)


try:
    response = getHTML(url)
    import re

    content = response.read().decode('utf-8')
    pattern = re.compile('<img src=".*?alt=(.*?)>.*?<div class="content.*?<span>(.*?)</span>', re.S)
    items = re.findall(pattern, content)
    print(items)
    for item in items:
        print(item[0], item[1])
    #print(response.read().decode("utf-8"))

except urllib.request.URLError as e:
    if hasattr(e, 'code'):
        print(e.code())
    if hasattr(e, 'reason'):
        print(e.reason())
