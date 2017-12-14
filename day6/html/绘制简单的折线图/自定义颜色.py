#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-6 17:13
# @Author  : Jerry Wang
# @Site    : 
# @File    : 自定义颜色.py
# @Software: PyCharm
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# 要修改数据点的颜色，可向 scatter() 传递参数 c
plt.scatter(x_values,y_values,c="red",edgecolors="none",s=40)
plt.axis([0,1100,0,1100000])
plt.show()