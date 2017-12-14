#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan


'''

import manager
import actions
import auth
from logger import MyLogger
import huabei


CONFIG_FILE = '..\\data\\user_info\\config.cfg'
USER_INFO = "..\\data\\user_info\\"

ALL_USERRULE_DIC={"common":[1,2,6,7,8,10,11],
         "huabei":[1,2,3,4,5,6,7,8,11],
         "overdue":[1,2,4,5,6,7,8,11],
         "lockuser":[11]
         }

def func_oper():
    huabei_operation = {
        1:(user_deposit,"存款"),
        2:(user_draw,"取款"),
        3:(huabei.borrow_,"借款"),
        4:(huabei.repayment,"还款"),
        5:(huabei.show_borrow_info,"花呗账单"),
        6:(manager.query_balance,"查询余额"),
        7:(change_pass,"修改密码"),
        8:(transfer,"转账"),
        #9:("","账单打印"),
        10:(huabei.huabei_update,"升级花呗会员"),
        11:(False,"退出登录"),

    }
    return huabei_operation

#——————————用户登录——————————————————————

# str="fadsf"
# def login_use(username,userstatus):
#     if userstatus == "common":
#         msg_huabei = '''
#                 您好,{}:
#                     您是{}用户，您有以下权限:
#                         1、存款
#                         2、取款
#                         3、查询余额
#                         4、修改密码
#                         5、转账
#                         6、退出登录
#
#                     '''.format(username,userstatus)
#         return msg_huabei
#     elif userstatus == "huabei":
#         msg_huabei = '''
#                 您好,{}:
#                     您是{}用户，您有以下权限:
#                     '''.format(username,userstatus,)
#         return msg_huabei
#     elif userstatus == "overdue":
#         msg_huabei = '''
#                 您好,{}:
#                     您是{}用户，您有以下权限:
#                         1、存款
#                         2、取款
#                         3、还款
#                         4、花呗账单
#                         5、查询余额
#                         6、修改密码
#                         7、转账
#                         8、账单打印
#                         9、退出登录
#                     '''.format(username, userstatus)
#         return msg_huabei
#     else:
#             sg_huabei = '''
#                     您好,{}:
#                         您是{}用户，您有以下权限:
#                             你已被锁定
#                         '''


def login_begin_user():#用户登录
    while True:
        username = input("请输入开户名:").strip()
        ret = manager.isnot_username(username)
        if ret == True:
            print("用户验证正确")
            MyLogger.info("用户【{}】验证正确".format(username))
            return username
        elif ret == False:
            print("用户验证错误")
            MyLogger.warning("用户【{}】验证失败".format(username))
            continue

def login_begin_cardid(user):#银行卡号输入
    while True:
        cardid = input("请输入银行卡号:").strip()
        ret=manager.isnot_card(user,cardid)
        if ret == True:
            print("卡号验证正确")
            MyLogger.info("卡号【{}】验证正确".format(cardid))
            return ret
        elif ret == False:
            print("卡号验证错误")
            MyLogger.warning("卡号【{}】验证失败".format(cardid))
            continue

def login_begin_pass(username):#密码登录验证
    while True:
        passwd = input("请输入密码:").strip()
        true_pass=manager.isnot_passwd(username,passwd)#验证密码
        if true_pass == False:
            continue
        else:
            return true_pass


#-----------------用户功能区-----------------------------

#存款，规则:每次最多100张,每张100元

def user_deposit_rule(addmon):
    int_addmon=int(addmon)
    if int_addmon > 10000:
        print("您充值的钱过多，单次最多一百张100元人民币，")
        return False
    elif int_addmon%100 == 0:
        print("ok,开始存款")
        return int_addmon
    else:
        print("未识别的人民币")
        return False


#存款
@auth.auth_common_permissions
def user_deposit(user):
    while True:
        addmon=input("请输入要存取的钱：")
        addmon1=user_deposit_rule(addmon)
        if addmon1 == False:
            continue
        else:
            now_balance=float(manager.get_user_onevalue(user,"balance"))#获取现在的余额.int类型
            str_user_info=manager.change_user_info(user,"balance",str(now_balance+addmon1))#改变balance对应的值
            print("充值成功")
            manager.query_balance(user, value="balance")
            return str_user_info

# 取款，规则：仅支持以下取款数额，最高每日不超过5万。
def user_draw_rule(draw_num):#取款规则
    # 100,200,500,1000,1500,3000
    draw_num_list=[100, 200, 500, 1000, 1500,3000]
    if draw_num in draw_num_list:
        return draw_num
    else:
        print("抱歉，未识别的取款额，请重新取款")

#取款，value：取款额
@auth.auth_common_permissions
def user_draw(user):
    while True:
        print("您好，可以取100, 200, 500, 1000, 1500, 3000")
        value=float(input("请输入取款额:"))
        draw_num=user_draw_rule(value)
        if draw_num == None:
            return draw_num
        now_balance = float(manager.get_user_onevalue(user, "balance"))
        if draw_num <= now_balance:
            str_user_info = manager.change_user_info(user, "balance", str(now_balance - draw_num))
            manager.query_balance(user, value="balance")
            return str_user_info
        else:
            print("余额不足！！您当前的余额为{}元".format(now_balance))

def exit_card():
    pass

# 管理接口——————————————————————————————
# 修改密码接口
def change_pass(username):
    #修改配置用户数据文件密码
    login_begin_pass(username)
    passwd=input("请输入新密码")
    hash_pass_m=actions.hash_m(passwd)#先加密要更改的密码
    manager.change_user_info(username,"passwd",hash_pass_m)
    print("请重新登录")

def get_all_fundic(userstatus):
    all_dic = {}
    COUNT = 1
    for i in sorted(func_oper().keys()):#i在key里
        if i in ALL_USERRULE_DIC.get(userstatus):
            huabei_oper = func_oper()  #
            h = huabei_oper.get(i)[0]  #
            all_dic[COUNT] = h
            COUNT +=1
    return all_dic


def get_rule_func(value,userstatus):
    all_dic= get_all_fundic(userstatus)
    func_rule=all_dic.get(value)
    return func_rule


def get_all_strdic(username,userstatus):
    ALL_DIC = {}
    COUNT = 1
    jj = '''
您好,{}:
您是{}用户，您有以下权限:'''.format(username, userstatus)
    print(jj)
    for i in sorted(func_oper().keys()):
        if i in ALL_USERRULE_DIC.get(userstatus):
            huabei_oper = func_oper()  #
            h = huabei_oper.get(i)[1]  #
            ALL_DIC[COUNT] = h
            print("      {}.{}".format(COUNT,h))
            COUNT +=1
    return ALL_DIC

def get_all_strdic_func(userstatus):
    ALL_DIC = {}
    COUNT = 1
    for i in sorted(func_oper().keys()):
        if i in ALL_USERRULE_DIC.get(userstatus):
            huabei_oper = func_oper()  #
            h = huabei_oper.get(i)[1]  #
            ALL_DIC[COUNT] = h
            COUNT +=1
    return ALL_DIC



#-------------转账功能----------------------------
def transfer_rule(user,otheruser):
    transfer_num = int(input("请输入转帐金额:"))
    otheruser_balance = float(manager.get_user_onevalue(otheruser, "balance"))#被转账人余额
    user_balance = float(manager.get_user_onevalue(user,"balance"))#转账的余额
    if user_balance >= transfer_num:#输入金额>=用户余额
        transfer_balnce = str(transfer_num + otheruser_balance)
        user_balance = str(user_balance - transfer_num)
        str_otuser_info = manager.change_user_info(otheruser, "balance", transfer_balnce)
        str_user_info = manager.change_user_info(user,"balance",user_balance)
        return (str_otuser_info,str_user_info)
    else:
        print("抱歉，余额不足")
        return False

def transfer_rule_two(user,otheruser):
    othuser_isnot=manager.isnot_username(otheruser)
    if othuser_isnot == True:
        user_isnot_lock = manager.isnot_lock_username(otheruser)
        if user_isnot_lock == True:
            print("抱歉，对方银行卡已锁定")
            MyLogger.info("对方银行卡已锁定")
            return False
        print("开户名校验成功")
        MyLogger.info("开户名校验成功")
        cardid = input("请输入您要转账的银行卡号：")
        cardid_isnot = manager.isnot_card(otheruser, cardid)  # 验证卡号
        if cardid_isnot == True:
            print("银行卡号校验成功")
            MyLogger.info("银行卡号校验成功")
            ret=transfer_rule(user,otheruser)
            return False
        else:
            print("银行卡号校验失败")
            MyLogger.warning("银行卡号校验失败")
            return False

def transfer(user):
    while True:
        otheruser=input("请输入您要转帐的对方开户名：")
        transfer_status=transfer_rule_two(user,otheruser)
        if transfer_status == False:
            int_info=input("返回用户菜单:q,其他：重新转账")
            if int_info == "q":
                return False
            else:
                continue
        else:
            print("开户名校验失败")
            MyLogger.warning("开户名校验失败")
            continue



# get_all_strdic("wangqiyuan","overdue")
# def get_all_dic(userstatus):
#     for i in sorted(func_oper().keys()):#遍历排序权限头
#         if  userstatus == "common" and i in common_list:
#             get_all_dic_1(i)
#             COUNT += 1
#         elif userstatus == "huabei" and i in huabei_list:
#             huabei_oper = func_oper()#
#             h = huabei_oper.get(i)[0]#
#             all_dic[count] = h
#             count+=1
#     return all_dic

# print(func_oper("wangqiyuan").keys())
# print(common_dic)
#             count+=1
#     return common_list
    # 1、存款
    # 2、取款
    # 3、借款
    # 4、还款
    # 5、花呗账单
    # 6、查询余额
    # 7、修改密码
    # 8、转账
    # 9、账单打印
    # 10、退出登录

