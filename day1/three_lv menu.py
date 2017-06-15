#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan
'''

dic = {
    '山西省':{'晋城市':['高平县','泽州县','沁水县'],'长治市':['长子县']},
    '河北省': {'保定市': ['雄县']},
}



e = list(dic['山西省'].keys())
f = list(dic['河北省'].keys())
e1 = list(dic["山西省"]["晋城市"])
e2 = list(dic["山西省"]["长治市"])
f1 = list(dic['河北省']["保定市"])
n = 0

def province_inf(province):

    y = list(dic[province].keys())[0:]

    return y

province_inf("山西省")


while True:
    print("全国省份：")
    for i in enumerate(dic):
        index = i[0]
        P_list = i[1]
        print(P_list)
    x = input("please input your Province:")

    if x == '山西省':
        print (e[0],e[1])
        if n == 0:
            while True:
                C1 = input("please input your City（x:返回上级，q：退出）:")
                if C1 == '晋城市':
                    print (e1[0],e1[1],e1[2])
                elif C1 == '长治市':
                    print (e2[0])
                elif C1 == 'q':
                    n = 1
                    break
                elif C1 == 'x':
                    break
                else:
                    print("没有查询到此城市，继续输入")
        if n == 1:
            break
        else:
            continue

    elif x == '河北省':
        print (f[0])
        if n == 0:
            while True:
                C2 = input("please input your City:")
                if C2 == "保定市":
                    print (f1[0])
                elif C2 == 'q':
                    n = 1
                    break
                elif C2 == 'x':
                    break
                else:
                    print("没有查询到此城市，继续输入")
        if n == 1:
            break
        else:
            continue

    elif x == 'q':
        break
    else:
        print("数据库未查出该省，退出输入q，查询请重新输入")

#
