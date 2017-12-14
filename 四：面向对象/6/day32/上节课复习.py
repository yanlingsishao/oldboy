#基于继承来定制自己的数据类型
class List(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
    def append(self, p_object):
        ' 派生自己的append：加上类型检查'
        if not isinstance(p_object,int):
            raise TypeError('must be int')
        super().append(p_object)
    #
    @property
    def mid(self):
        '新增自己的属性'
        index=len(self)//2
        return self[index]

#
# l=List([1,2,3])
#
# print(l.mid)



#基于授权来定制自己的数据类型：

# class Open:
#     def __init__(self,filepath,mode,encode='utf-8'):
#         self.f=open(filepath,mode=mode,encoding=encode)
#         self.filepath=filepath
#         self.mode=mode
#         self.encoding=encode
#
#     def write(self,line):
#         print('write')
#         self.f.write(line)
#
#     def __getattr__(self, item):
#         return getattr(self.f,item)
#
#
# # f=Open('a.txt','w')
# # f.write('123123123123123\n')
# # print(f.seek)
# # f.close()
# #
# # f.write('111111\n')
#
#
#
# f=open('b.txt','w')
# f.write('bbbbbb\n')
# f.close()
# print(f)





# class Foo:
#     def test(self):
#         pass
#
# print(getattr(Foo,'test'))
#
# obj=Foo()
# print(getattr(obj,'test'))




class List:
    def __init__(self,x):
        self.seq=list(x)

    def append(self,value):
        if not isinstance(value,str):
            raise TypeError('must be str')
        self.seq.append(value)
    @property
    def mid(self):
        index=len(self.seq)//2
        return self.seq[index]
    def __getattr__(self, item):
        return getattr(self.seq,item)

    def __str__(self):
        return str(self.seq)

l=List([1,2,3])

l.append('1')

print(l.mid)
l.insert(0,123123123123123123123123123)
# print(l.seq)

print(l)




obj.name='egon'
del obj.name