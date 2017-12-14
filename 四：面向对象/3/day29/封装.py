# class A:
#     __x=1 #_A__x
#     def __test(self): #_A__test
#         print('from A')
#
#
# # print(A.__x)
# # print(A._A__x)
# # a=A()
# # print(a._A__x)
#
# # print(A.__dict__)
#
# # print(A.__dict__)
# A._A__test(123)
#
# a=A()
# a._A__test()

#__名字，这种语法，只在定义的时候才会有变形的效果，如果类或者对象已经产生了，就不会有变形效果

# class B:
#     pass
#
# # B.__x=1
# # print(B.__dict__)
# # print(B.__x)
#
# b=B()
# b.__x=1
# print(b.__dict__)
# print(b.__x)


#
# class A:
#     def fa(self):
#         print('from A')
#     def test(self):
#         self.fa()
#
#
# class B(A):
#     def fa(self):
#         print('from B')
#
#
# b=B()
# b.test() #b.test-->B--->A b.fa()




# class A:
#     def __init__(self):
#         self.__x=1
#
#     def tell(self):
#         print(self.__x)
#
#
# a=A()
# print(a.__dict__)
# # print(a.__x)
#
# a.tell()











#在定义阶段就会变形
class A:
    def __fa(self): #_A__fa
        print('from A')
    def test(self):
        self.__fa() #self._A__fa()


class B(A):
    def __fa(self): #_B__fa
        print('from B')


b=B()
b.test() #b._A__fa()




