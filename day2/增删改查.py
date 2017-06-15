#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
def add():
    pass
def delete():
    pass
def change():
    pass
def fetch():
    data = input("请输入你的数据:").strip()
    print("这是查询功能")
    print("用户查找数据是:",data)
    backend_data="backend %s"%data
    ret=[]
    with open("haproxy.conf","r",encoding="utf-8") as read_f:
        tag=False
        for read_line in read_f:#
            if read_line.strip() == backend_data:#
                tag=True
                continue
            if tag and read_line.startswith("backend"):
                   break
            if tag:
                print(read_line,end="")
                ret.append(read_line)
    return ret
def Exit():
    print("程序退出")
    exit()
def Main():
    msg = '''
欢迎来到我的世界：
        1:增加
        2:删除
        3:修改
        4:查找
        5:退出
        '''
    msg_dic = {
        "1":add,
        "2":delete,
        "3":change,
        "4":fetch,
        "5":Exit,
    }
    while True:
        print(msg)
        choice = input("请输入你的选项：").strip()
        if choice not in msg_dic.keys(): continue
        res=msg_dic[choice]()

if __name__ == "__main__":
    Main()

