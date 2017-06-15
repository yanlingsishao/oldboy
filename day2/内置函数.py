#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# print(abs(-22))#取绝对值
# >>>22
#
# print(all([1,2,'']))#所有为真即为真，0，空，none为false
# >>>False
#
# print(any([1,2,''])) #只要有一个为真，即为真
# >>>True
#
# print(bin(20)) #10进制转二进制
# >>>0b100
#
# 这三种全返回False，其他的都是True
# print(bool())
# print(bool(None))
# print(bool(0))
#
# print(bytes("你好","utf-8"))#字符转字节
# >>>b'\xe4\xbd\xa0\xe5\xa5\xbd'  6个字节
# print(bytes("你好","utf-8").decode("utf-8"))#解码
# print(bytes("你好","gbk"))
# >>>b'\xc4\xe3\xba\xc3'   1个字符两个字节
# print(bytes("你好","gbk").decode("gbk"))
#
# print(chr(46))#ascli码对应位置，输出对应ascli码
# print(ord("a"))#ascli码，输出scli码对应位置
#
# print(dir("chr"))#打印某一个对象的方法
#
# print(divmod(10,3))#取余
#
# dic={"name":"alex"}
# print(str(dic))

# 可hash的数据类型即不可变的数据类型，不可hash的数据类型即可变的数据类型
# hash特性，得出来的值长度是不变的，值不可反推
# name="alex"
# print(hash(name))

#　print(help(all))#打印方法帮助

# name = "哈哈哈哈哈哈哈哈哈"
# print(globals())
# print(__file__)
#
# l=[1,20,3,50,-5,16]#最大值
# print(max(l))

# print(pow(3,3))#3**3
# print(pow(3,3,3))#3**3%3

#repr()#终端调用repr

# l=[1,4,3,5]
# print(list(reversed(l)))#反转，仅处理，不保存

# print(round(3.5))#四舍五入

# print(set("hello"))

# l="hello"#切片
# s=slice(3,5)
# print(l[s])


# l=[3,2,1,5,7]排序，不同类型不能比较
# print(sorted(l))
# people = [
#     {"name":"alex","age":1000},
#     {"name":"wupeiqi","age":10000},
#     {"name":"zhazha","age":9000},
#     {"name":"wangqiyuan","age":18}
# ]
# name_dic = {"way":500,"wangqiyuan":1000,"hsd":10}
# print(sorted(people,key=lambda dic:dic["age"]))
# print(sorted(name_dic,key=lambda key:name_dic[key]))
# print(sorted(zip(name_dic.values(),name_dic.keys())))

# l=[1,1,3,45,6]
# print(sum(l))#求和

# type 判断数据类型

# vars
# def test():
#     msg="房间爱到了房间哦·1"
#     print(locals())
#     print(vars())
# test()
# print(vars(int))

# __import__()
module_name="test"
m=__import__(module_name)