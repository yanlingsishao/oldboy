#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年5月9日
@author: WangQiyuan

'''
import pickle
import hashlib
import time
import os,sys



class Manager:
    "父类"
    def create_md5(self):
        m = hashlib.md5()
        m.update(str(time.time()).encode('utf-8'))
        return m.hexdigest()

    def inspect_num(self,dic):
        while True:
            input_num = input("请输入序号:")
            if not input_num or not input_num.isdigit():
                continue
            input_num = int(input_num)
            if input_num not in dic.keys():
                continue
            if input_num == 6:
                return None
            return input_num

    def test_file_isnone(self,dir):
        '''测试文件是否为空'''
        name = self.get_name(dir)
        return name

    def find_id1(self,dir,name,arg,onlyidname):
        '''dir:目录名

           '''
        x = Manager().get_name(dir)
        for i in x:
            if i == None:
                continue
            if i.__dict__[arg]==name:
                return i.__dict__[onlyidname]

        return []

    def find_id(self,dir,name,onlyidname):
        '''dir:目录名

           '''
        x = Manager().get_name(dir)
        for i in x:
            if i == None:
                continue
            if i.__dict__["name"]==name:
                return i.__dict__[onlyidname]

        return []

    def get_name1(self,dir,file):
        if os.path.isdir(dir) == False:
            os.mkdir(dir)
        if os.path.isfile('db\{}\{}.db'.format(dir,file)) == False:
            if sys.platform in ["win32","windows"]:
                os.system("type nul > db\{}\{}.db".format(dir,file))
                return []
        else:
            with open('db\{}\{}.db'.format(dir,file),'rb') as f:
                try:
                    files = pickle.load(f)
                    return files
                except EOFError as e:
                    return []

    def get_name(self,dir):
        if os.path.isfile(dir) == False:
            if sys.platform in ["win32","windows"]:
                os.system("type nul > {}".format(dir))
                return []
        else:
            try:
                with open(r'{}'.format(dir),'rb') as f:
                    files = pickle.load(f)
                    return files
            except EOFError as e:
                return [None,None]

    def save(self,dir,obj):
        isnonefile = self.get_name(dir)
        isnonefile.append(obj)
        with open(dir,'wb') as f:
            pickle.dump(isnonefile,f)

    def save_db(self,dir,obj,all_obj_list):
        #isnonefile = self.get_name(dir, file)#所有数据
        index_value = all_obj_list.index(obj)
        all_obj_list[index_value]=obj
        with open(dir,'wb') as f:
            pickle.dump(all_obj_list,f)



    def del_obj(self,dir,delname):
        course_obj_list = self.get_name(dir)
        for i in course_obj_list:
            if i.name == delname:
                l = course_obj_list.index(i)
                course_obj_list.pop(l)
            else:
                continue
        print(course_obj_list)
        os.system("type nul > {}".format(dir))
        for k in course_obj_list:
                k.save(dir,k)




# from Cses.conf import settings
# x = Manager().get_name(settings.ADMIN_DB_DIR)
# print(x)