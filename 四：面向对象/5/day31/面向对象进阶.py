class Bar:
    pass
class Foo(Bar):
    pass

obj=Foo()


# print(isinstance(obj,Foo))
#
#
# x=[]
# print(isinstance(x,list))

print(Foo.__bases__)

print(issubclass(Foo,Bar))