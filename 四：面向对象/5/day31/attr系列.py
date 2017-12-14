#__setattr__,__getattr__,__delattr__,


# class Foo:
#     def __init__(self,x):
#         self.name=x
#     #
#     def __setattr__(self, key, value):
#         # if not isinstance(value,str):
#         #     raise TypeError('must be str')
#         # print('----setattr---key:%s,value:%s' %(key,value))
#         # print(type(key))
#         # print(type(value))
#         # self.key=value
#         # setattr(self,key_str,value) #self.key_attribute=value
#         self.__dict__[key]=value
#
#     def __delattr__(self, item):
#         print('delattr:%s' %item)
#         print(type(item))
#         # delattr(self,item)
#         # del self.item
#         self.__dict__.pop(item)







# f1=Foo('egon') #f1.name='egon'

# f1.age=18


# print(f1.__dict__)
# print(f1.name)
# print(f1.age)

# print(f1.__dict__)
# del f1.age
# print(f1.__dict__)
# print(f1.age)










class Foo:
    def __init__(self,x):
        self.name=x

    #属性不存在的情况下才会触发
    def __getattr__(self, item):
        print('getattr-->%s %s' %(item,type(item)))


f=Foo('egon')
# print(f.name)

print(f.xxxxxxx)


