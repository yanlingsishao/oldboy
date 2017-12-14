#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import json
class json_handle:
    def __init__(self,user):
        self.user = user


    def json_read(self):

        user = self.user
        #dic = {user:{"借款事项":{0:[0,0]}, "花呗额度": [3000], "花呗剩余额度": [3000], "用户还款": [0]}}
        with open("../data/huabei_data/huabei.json", encoding="utf-8") as f:
            json_readvalue=json.load(f)
            #json_user=json_readvalue.get(self.user)
            print("加载出文件完成...")
            return json_readvalue

    def json_write(self):
        user= self.user
        dic = {user:{"借款事项":[{0:0}], "花呗额度":3000,"花呗剩余额度":3000, "用户待还": [0]}}
        json_reads = json_handle.json_read
        print(json_reads)
        with open("../data/huabei_data/huabei.json","w") as f:
            json.dump({json_reads,dic})
        print("加载入文件完成...")

#def change_json(user,key):


# province_json = open("省市.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
# setting = json.load(province_json)
# province_json.close()

# json_user=json_handle("wangqiyuan")
# print(json_user.json_read())
json_user=json_handle("lisi")
json_user.json_write()