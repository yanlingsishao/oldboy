#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
# 字典
# key：value
# 布尔值列表字典不能作为key，报错，value什么都行
# 无序，可迭代

dic = {
    "fasd":"fads",
    "k1":"fdasfads"
}
# x = dic.values()
# x = dic.keys()
# x = dic.items()
# print(x)

# j = dic.fromkeys(['fds','fasd'],123)#传一个序列，创建字典，并且指定统一的值
# print(j)

# v = dic["fasd"]
# print(v)
# >>>fads
# v = dic.get("fafdsd")  get根据key取value，如果没有key，默认取none
# print(v)
# >>>None

# v = dic.pop("k1") # pop可以移除值，可以获取删除的值
# print(v,dic)


# v = dic.popitem()#随机删
# print(v)

# v = dic.setdefault("k1","123")#如果key存在，获取原来的值，如果key不存在，更新可以的值并获取新的值
# print(v)

# dic.update({"k2":"fdagfsds"})#update更新,如果没有key，就增加一个字典元素，如果有，就更新为新值
# dic.update(k1="fda",fasd="fasfdad")
# print(dic)