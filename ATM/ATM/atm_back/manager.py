#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
'''
#一、cfg操作功能，主要操作config.cfg文件进行增删改查
           -------------方法--------------
           1、get_option_old_value(username)                #获取option的value，username参数===账号名
           2、cfg_read(section="cardid")                    #获取所有的cfg的option，默认参数section
           3、del_one_option(option,section="cardid")       #删除cfg文件option  option参数===账号名
           4、add_one_option(option,value,section="cardid") #添加cfg文件option  option参数===账号名，value参数===银行卡号
           5、get_option_value()                            #获取新cordid
#二、 用户额度功能
           1、set_user_limit                                 #设定用户额度方法
           2、                                               #存款数量8000和存款次数大于10次（有5次存款大于2000），开启花呗功能
'''

import os
import configparser
import actions
import auth
from prettytable import PrettyTable







CONFIG_FILE = '..\\data\\user_info\\config.cfg'
USER_INFO = "..\\data\\user_info\\"



user_dic={
    "id":0,
    "CardID":1,
    "username":2,
    "passwd":3,
    "phone":4,
    "balance":5,
    "user_status":6,
    "user_huabei":7
}

# user_info目录下的文件操作
def change_user_info_file(filename):#value
    file=open(USER_INFO+filename,"w",encoding="utf-8")
    return file

#cfg操作 --------------------------------------------

def __cfg():
    cf = configparser.ConfigParser()
    cf.read(CONFIG_FILE, encoding='utf-8')
    secs = cf.sections()
    return (cf,secs)



#获取用户列表
def get_user_info(username):
    cf=__cfg()[0]
    str_user_info=cf[username][username]
    list_user_info=str_user_info.split(";")
    return list_user_info

#用户是否存在
#获取用户id
def get_user_value(value):#value即user_dic的key值
    user_value=user_dic.get(value)#获取行id
    return user_value#无key返回none

#改变用户信息
def change_user_info(username,value,new_value):#更改用户的任何信息
    #username:即用户名，value：即该用户某个表头，new_value:更改新的值
    user_list_id=get_user_value(value)
    cf=__cfg()[0]
    list_user_info=get_user_info(username)#用户列表
    list_user_info[user_list_id]=new_value#更改用户某个表头对应的值
    str_user_info=";".join(list_user_info)
    cf.set(username,username,str_user_info)
    cf.write(open(CONFIG_FILE, "w"))
    return str_user_info

def get_all_userlistheader(value):#获取某列的所有内容
    sesc=__cfg()[1]#获取所有section
    list_user_header=[]
    for se in sesc:
        list_user_info=get_user_info(se)
        list_user_header.append(list_user_info[user_dic.get(value)])
    return list_user_header

def get_user_onevalue(user,value):#获取用户的某个值 value参数就是user_dic字典里的key
    list_user_info=get_user_info(user)#获取用户列表
    value_id = get_user_value(value)#取出
    user_value=list_user_info[value_id]
    return user_value


def isnot_card(user,cardid):#验证用户银行卡号是否正确
    true_cardid=get_user_onevalue(user,"CardID")
    if cardid == true_cardid:
        return True
    else:
        return False

# def isnot_cardid(user,cardid,value="CardID"):#验证用户是否在库里
#     true_cardid = get_user_onevalue(user,value)
#     if cardid == true_cardid:
#         print("卡号验证正确")
#         return true_cardid
#     else:
#         print("卡号验证错误")
#         return False

def isnot_username(username):#验证用户是否在库里
    list_user=get_all_userlistheader("username")
    if username in list_user:
        return True
    else:
        return False

def isnot_phone(phone):#验证手机是否在库里
    list_user_phone = get_all_userlistheader("phone")
    if phone in list_user_phone:
        return True
    else:
        return False

def isnot_lock_username(user):
    userstatus=get_user_onevalue(user,"user_status")
    if userstatus == "lockuser":
        return True#是锁定返回True
    else:
        return False

#验证密码
def isnot_passwd(user,input_pass,value="passwd"):
    true_pass=get_user_onevalue(user,"passwd")
    md_pass=actions.hash_m(input_pass)
    if true_pass == md_pass:
        print("密码验证正确")
        return true_pass
    else:
        print("密码验证错误")
        return False

def get_list_int_userid(header):#获取int类型的header的列表，header只能是"id"或"CardID"
    list_int_userid = []
    list_str_user_id = get_all_userlistheader(header)#获取header列所有内容
    for num in list_str_user_id:#num即获取到的str的数字
        list_int_userid.append(int(num))#将num数字化
    return list_int_userid#返回int格式的id、cardid的列表

def since_the_growth(header):#某header列int自增长1，header只能是"id"或"CardID"
    list_int_userid=get_list_int_userid(header)
    max_user_id=max(list_int_userid)
    max_user_id+=1
    return max_user_id

def isnot_cfg_none():#cfg是否为空
    sec = __cfg()[1]
    if sec == None:
        return None
    else:
        return sec

def generate_cardid():#生成卡号
    cardid=since_the_growth("CardID")#生成出未处理过的卡号
    processed_cardid=str(cardid).rjust(16,"0")#生成处理过的16位卡号，
    return processed_cardid

def add_user_info(username,passwd,phonenum):#添加一个用户，生成卡号，id
    cf=__cfg()[0]
    sec = isnot_cfg_none()
    cf.add_section(username)
    if sec == None:
        user_id = 0
        user_cardid="0000000000000001"
    else:
        user_id = since_the_growth("id")
        user_cardid = generate_cardid()
    user_passwd = actions.hash_m(passwd)  # 加密密码
    cf.set(username, username, "{};{};{};{};{};0;common;0".format(user_id, user_cardid, username, user_passwd, phonenum))
    cf.write(open(CONFIG_FILE, "w"))

#def lock_user(username):

def fetch_single_user_info(username):#单用户列表
    #secs = __cfg()[1]  # 用户列表
    single_user_info = PrettyTable(["id", "CardID", "username", "phone","balance","user_status","user_huabei"])  # ！！！留了一个status
    single_user_info.align["ID"] = "l"
    single_user_info.padding_width = 1
    single_user_info_list=get_user_info(username)
    #print(single_user_info_list)
    del single_user_info_list[user_dic.get("passwd")]
    single_user_info.add_row(single_user_info_list)
    return single_user_info


def fetch_users():#列出用户列表，管理员功能
    cf=__cfg()[0]
    secs = __cfg()[1]#用户列表
    user_list = PrettyTable(["id", "CardID", "username", "phone","balance","user_status","user_huabei"])  # ！！！留了一个status
    user_list.align["ID"] = "l"
    user_list.padding_width = 1
    for se in secs:
        list_user_info=get_user_info(se)
        del list_user_info[user_dic.get("passwd")]
        user_list.add_row(list_user_info)
    print(user_list)
    return user_list

# def del_one_option(value):



def change_pass(user):#更改密码
    import account
    input_pass=input("请输入旧密码")
    true_pass = isnot_passwd(user,input_pass, value="passwd")
    new_pass=account.validate_pass()
    new_pass=actions.hash_m(new_pass)
    str_user_info=change_user_info(user,"passwd",new_pass)
    print("更改成功,请重新登录")
    return "已更改"


@auth.auth_common_permissions
def query_balance(user,value="balance"):
    now_balance=get_user_onevalue(user,value)
    print("当前余额为{}".format(now_balance))
    return now_balance



# #-----------------用户功能区-----------------------------
#
# #存款，规则:每次最多100张,每张100元
# def user_deposit_rule(addmon):
#     int_addmon=int(addmon)
#     if int_addmon > 10000:
#         print("您充值的钱过多，单次最多一百张100元人民币，")
#         return False
#     if 10000%int_addmon == 0 and 100 >=10000/int_addmon >= 1:
#         print("ok,开始存款")
#         return int_addmon
#     else:
#         print("未识别的人民币")
#         return False
#
# #存款
# def user_deposit(user):
#     while True:
#         addmon=input("请输入要存取的钱：")
#         addmon1=user_deposit_rule(addmon)
#         if addmon1 == False:
#             continue
#         else:
#             now_balance=int(get_user_onevalue(user,"balance"))#获取现在的余额.int类型
#             str_user_info=change_user_info(user,"balance",str(now_balance+addmon1))#改变balance对应的值
#             return str_user_info
#
#
# #取款，规则：仅支持以下取款数额，最高每日不超过5万。
# #100,200,500,1000,1500,3000
# #draw_num_list=[100, 200, 500, 1000, 1500,3000]
# def user_draw_rule(draw_num):#取款规则
#     draw_num_list=[100, 200, 500, 1000, 1500,3000]
#     if draw_num in draw_num_list:
#         return draw_num
#     else:
#         print("抱歉，未识别的取款额，请重新取款")
#
# def user_draw(user,value):#取款，value：取款额
#     draw_num=user_draw_rule(value)
#     if draw_num == None:
#         return draw_num
#     now_balance = int(get_user_onevalue(user, "balance"))
#     if draw_num <= now_balance:
#         str_user_info = change_user_info(user, "balance", str(now_balance - draw_num))
#         return str_user_info
#     else:
#         print("余额不足！！您当前的余额为{}元".format(now_balance))







