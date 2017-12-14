# class Foo:
#     def bar(self):
#         pass
#     @classmethod #把一个方法绑定给类：类.绑定到类的方法(),会把类本身当做第一个参数自动传给绑定到类的方法
#     def test(cls,x):
#         print(cls,x) #拿掉一个类的内存地址后，就可以实例化或者引用类的属性了
#
#
# # print(Foo.bar)
# # print(Foo.test)
#
# Foo.test(123123)
#
# f=Foo()
# print(f.bar)
# print(f.test)
# print(Foo.test)
# f.test(1111)



import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    #
    # def test():
    #     print('from test')
    #
    @classmethod
    def now(cls): #用Date.now()的形式去产生实例,该实例用的是当前时间
        print(cls)
        t=time.localtime() #获取结构化的时间格式
        obj=cls(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
        return obj

    @classmethod
    def tomorrow(cls):#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return cls(t.tm_year,t.tm_mon,t.tm_mday)


class EuroDate(Date):
    def __str__(self):
        return '年:%s,月:%s,日:%s' %(self.year,self.month,self.day)

# e1=EuroDate.now()
# print(e1)


e1=EuroDate(1,1,1)
print(e1)














