

# class Foo(metaclass=type):
#     x=1
#     def run(self):
#         print('running')
#
#
# # type('Foo',(object,),{'x':1,'run':run})




# class Mymeta(type):
#      def __init__(self,class_name,class_bases,class_dic):
#          # print(self)
#          # print(class_name)
#          # print(class_bases)
#          # print(class_dic)
#          for key in class_dic:
#             if not callable(class_dic[key]):continue
#             if not class_dic[key].__doc__:
#                 raise TypeError('小子，你没写注释，赶紧去写')
#
#          # type.__init__(self,class_name,class_bases,class_dic)
# class Foo(metaclass=Mymeta):
#     x=1
#     def run(self):
#         'run function'
#         print('running')

# Foo=Mymeta('Foo',(object,),{'x':1,'run':run})

# print(Foo.__dict__)












class Mymeta(type):
     def __init__(self,class_name,class_bases,class_dic):
            pass
     def __call__(self, *args, **kwargs):
        # print(self)
        obj=self.__new__(self)
        self.__init__(obj,*args,**kwargs) #obj.name='egon'
        return obj
class Foo(metaclass=Mymeta):
    x=1
    def __init__(self,name):
        self.name=name #obj.name='egon'
    def run(self):
        'run function'
        print('running')
# print(Foo.__dict__)

f=Foo('egon')

print(f)

print(f.name)









