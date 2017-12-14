#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import re
#select name,age from staff_table where age > 22
directory = ["staff_id", "name", "age", "phone", "dept", "enroll-date"]


def auto_increment():
    ii = []
    list_data=list_db()
    for i in range(len(list_data)):
        if list_data[i][0] == None:
            ii.append(None)
        else:
            ii.append(list_data[i][0])
    if ii == []:
        return 1
    else:
        c = int(max(ii))
        c += 1
        return c




def list_db():
    with open("permissions_info", encoding="utf-8") as f:
        list=[]
        for line in f:
            li_line=line.split(",")
            li_line[5]=li_line[5].strip('\n')
            # tu_line=tuple(li_line)
            list.append(li_line)
        return list
            #x="select name,age from permissions_info where age > 22"".format()

#查询功能
def fetch():
    while True:
        data = input("请输入sql语句:(q:返回上一页)")
        #list=list_db()
        data_num = data.split(" ")
        if data == "q":
            break
        if data == ("select name,age from permissions_info where age > {}".format(data_num[7])):
            with open("permissions_info", encoding="utf-8") as f:
                list1 = []
                for line in f:
                    li_line = line.split(",")
                    li_line[5] = li_line[5].strip('\n')
                    n = li_line[1]
                    a = int(li_line[2])
                    g = [n,a]
                    if a > int(data_num[7]):
                        list1.append(g)
                for i in list1:
                    print(i)
                print("sql查到{}条符合的数据".format(len(list1)))
        elif data == ("select * from permissions_info where dept = {}".format(data_num[7])):
            with open("permissions_info", encoding="utf-8") as li:
                list2 = []
                for line in li:
                    li_line = line.split(",")
                    li_line[5] = li_line[5].strip('\n')
                    d = li_line[4]
                    if d == data_num[7]:
                        list2.append(li_line)
                for i in list2:
                    print(i)
                print("sql查到{}条符合的数据".format(len(list2)))
        elif data == ("select * from permissions_info where enroll_date like {}".format(data_num[7])):
            suggestions = []#
            collection = []
            list2 = []#最终
            pattern = '.*'.join(data_num[7])
            regex = re.compile(pattern)
            with open("permissions_info", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    list_line=line.split(",")
                    list_line[5] = list_line[5].strip('\n')
                    collection.append(list_line[5])
                    match = regex.search(list_line[5])
                    if match:
                        suggestions.append(list_line[5])
                        if list_line[5] in suggestions:
                            list2.append(list_line)
                #print(suggestions)
                for i in list2:
                    print(i)
        else:
            print("grammar mistakes error")


#fetch("select * from permissions_info where enroll_date like 2015")


#验证是否存在手机号
def isphone(value):
    with open("permissions_info",encoding="utf-8") as f:
        list3 = []
        for line in f:
            li_line = line.split(",")
            li_line[5] = li_line[5].strip('\n')
            p = li_line[3]
            list3.append(p)
        #print(list3)
        if value in list3:
            return False
        else:
            return list3




#添加功能
def add():
    while True:
        all_info=input('''格式:name,age,phone,dept,enroll-date
请输入添加语句:''')
        list_all_info=all_info.split(",")
        phone_list=isphone(list_all_info[2])
        if phone_list == False:
            print("phone repeat error")
        else:
            with open("permissions_info", "a", encoding="utf-8") as f:
                f.write("\n{},{}".format(auto_increment(),all_info))




# list.index()
# def count_elements(*args):
#     x = 0
#     kk=input("请输入查询字段:")
#     index_num=directory.index(kk)
#     for i in range(len(list_db())):
#         list = (list_db()[i][index_num]).count(*args)
#         x+=list
#     return x

#删除
def del_user():
    id = input("请输入要删除的staff_id:")
    with open("permissions_info", encoding="utf-8") as f:
        lines = f.readlines()
    with open("permissions_info","w", encoding="utf-8") as f_w:
        for line in lines:
            list_line=line.split(",")
            if list_line[0] == id:
                continue
            f_w.write(line)


#更改操作
def change_useinfo():
    data = input("请输入sql语句:")
    data_num = data.split(" ")
    if data == ('''3{}'''.format(data_num[5],data_num[9])):
        with open("permissions_info", encoding="utf-8") as f:
            lines = f.readlines()
        with open("permissions_info", "w", encoding="utf-8") as f_w:
            for line in lines:#line str
                list_line = line.split(",")#list_line list
                if list_line[4] != data_num[9]:
                    f_w.write(line)
                    continue
                elif list_line[4] == data_num[9]:
                    list_line[4] = data_num[5]
                    str_line=",".join(list_line)
                    f_w.write(str_line)
                    continue



                # else:
                #     continue
                    #f_w.write(line)
#1,zhahza,111,18323,HRR,2016-01-23
# change_useinfo('''UPDATE staff_table SET dept = HRR WHERE dept = HR''')

# fetch("select name,age from permissions_info where age > 22")
def login_db():
    msg_overdue = '''
            1、查询
            2、更改
            3、增加
            4、删除
            5、退出
               '''
    dic_login_atm={
        "1":fetch,
        "2":change_useinfo,
        "3":add,
        "4":del_user,
        "5":exit
    }
    while True:
        print("欢迎来到db manager".center(50, "*"))
        print(msg_overdue)
        choice = input("请输入您的操作：")
        if choice not in dic_login_atm.keys(): continue
        res = dic_login_atm[choice]()

if __name__ == "__main__":
    begin = login_db()
