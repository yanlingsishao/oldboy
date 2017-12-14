# class Foo:
#     def spam(self):
#         print('----->',self)
#
#
# # Foo.spam(123123)
#
# f1=Foo()
# f1.spam()


# class Foo:
#     @staticmethod
#     def spam(x,y,z):
#         print(x,y,z)
#
#
# # Foo.spam(1,2,3)
# f2=Foo()
# f2.spam(1,2,3)
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
    @staticmethod
    def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间
        t=time.localtime() #获取结构化的时间格式
        obj=Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
        return obj

    @staticmethod
    def tomorrow():#用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
# d1=Date(2017,1,13)
# # Date.test()
# print(d1.test)
# d1.test()


# d1=Date(2017,1,13)
# d2=Date(2017,1,14)
# date_now=Date.now()
# print(date_now)
# print(date_now.year)
# print(date_now.month)
# print(date_now.day)


# d1=Date.now()
# print(d1.year,d1.month,d1.day)
#
# d2=Date.tomorrow()
# print(d2.day)



#但凡是定义在类的内部，并且没有被任何装饰器修饰过的方法，都是绑定方法：有自动传值功能
d1=Date(1212,22,22)
print(d1.now)
print(Date.now)
# d1.now()  #now(d1)


#但凡是定义在类的内部，并且被staticmethod装饰器修饰过的方法，都是解除绑定的方法，实际上就函数：就没有自动传值功能了
d_n1=Date.now()
d_n2=d1.now()
print(d_n1.year,d_n1.month,d_n1.day)
print(d_n2.year,d_n2.month,d_n2.day)

