# l=list([1,2,3])
#
# l.append(4)
# l.append('5')
# print(l)

# class List(list):
#     pass
#
# l1=List([1,2,3])
# print(l1)
# l1.append(4)
# print(l1)
# l1.append('5')
# print(l1)

#基于继承的原理，来定制自己的数据类型（继承标准类型）

# class List(list):
#     def append(self, p_object):
#         # print('--->',p_object)
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         # self.append(p_object)
#         super().append(p_object)
#     def insert(self, index, p_object):
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         # self.append(p_object)
#         super().insert(index,p_object)
#
# l=List([1,2,3])
# # print(l)
# # l.append(4)
# # print(l)
#
# # l.append('5')
# print(l)
# # l.insert(0,-1)
# l.insert(0,'-1123123213')
# print(l)







# def test(x:int,y:int)->int:
#     return x+y
# print(test.__annotations__)
#
# print(test(1,2))
# print(test(1,'3'))
#
# def test(x,y):
#     return x+y






#不能用继承,来实现open函数的功能
# f=open('a.txt','w')
# print(f)
# f.write('1111111')

#授权的方式实现定制自己的数据类型
import time


class Open:
    def __init__(self,filepath,m='r',encode='utf-8'):
        self.x=open(filepath,mode=m,encoding=encode)

        self.filepath=filepath
        self.mode=m
        self.encoding=encode

    def write(self,line):
        print('f自己的write',line)
        t=time.strftime('%Y-%m-%d %X')
        self.x.write('%s %s' %(t,line))

    def __getattr__(self, item):
        # print('=------>',item,type(item))
        return getattr(self.x,item)
#
# f=Open('b.txt','w')
# # print(f)
# f.write('111111\n')
# f.write('111111\n')
# f.write('111111\n')


f=Open('b.txt','r+')
# print(f.write)
print(f.read)


res=f.read() #self.x.read()
print(res)

print('=-=====>',f.read())
f.seek(0)
print(f.read())
# f.flush()
# f.close()


















