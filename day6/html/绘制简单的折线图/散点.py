#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-6 16:57
# @Author  : Jerry Wang
# @Site    : 
# @File    : 散点.py
# @Software: PyCharm
import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()

