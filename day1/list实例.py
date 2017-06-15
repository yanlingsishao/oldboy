#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# list 类，列表
# 列表中的元素可以是，数字，字符串，列表，布尔值，所有的都能放进去
# 索引修改和删除
# 切片修改和删除
# 支持for循环，in操作
# 字符串转换为列表，每一个字符都成了列表的元素，数字不能循环，也不能转列表
li = [1,23,5,'fads',"你好",[1,23,78],"alex",True]
# li[1] = 23 #修改
# li[1:3]=22,12#修改
# del li[1:3]#删除
# del li[1]#删除
# print(li)
# x = li[5][1]#索引可以一直往里找
# s = 'fasdfdsafsadfas'
# x = list(s)
# print(s)
# >>>['f', 'a', 's', 'd', 'f', 'd', 's', 'a', 'f', 's', 'a', 'd', 'f', 'a', 's']



# 列表转换为字符串
# 当列表仅有字符串时，可以用join,或者for循环 str()
# lll = ['fads','fasd','fadsfa','fasd']
# x = ''.join(lll)
# print(x)



###################list类中的方法#######################
li = [11,22,33,44,22]
# 参数
# li.append(5)#追加列表元素
# >>>[11,22,33,44,5]

# li.clear()#清空列表
# >>>[]

# v = li.copy()#浅拷贝
# print(v)
# >>>[11, 22, 33, 44]

# v = li.count(22)#计算元素出现的次数
# print(v)
# >>>1

# li.extend([9898,"不得了"])扩展原列表，元素，可迭代对象
# print(li)
# >>>[11, 22, 33, 44, 9898, '不得了']

# v = li.index(22)#根据值获取当前索引位置
# print(v)
# >>>1

# li.insert(0,99)#在指定索引位置插入元素
# print(li)
# >>>[99, 11, 22, 33, 44, 22]


v = li.pop(3) #删除制定索引位置（默认是最后一个）的值，还可以获取该删除的值
print(v)
print(li)

# li.remove(33) #删除列表中的指定值
# print(li)
# >>>[11, 22, 44, 22]

# ps:pop,remove,del li[1],del li[2:8], clear

# li.reverse()#将当前列表进行翻转
# print(li)
# [22, 44, 33, 22, 11]

# li.sort()#从小到达排
# print(li)
# >>>[11, 22, 22, 33, 44]
# li.sort(reverse=True) #从小往大排
# print(li)
# >>>[44, 33, 22, 22, 11]
