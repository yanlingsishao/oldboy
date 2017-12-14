#反射当前模块的属性
import sys

x=1111
class Foo:
    pass
def s1():
    print('s1')

def s2():
    print('s2')


# print(__name__)

this_module = sys.modules[__name__]
print(this_module)

print(hasattr(this_module, 's1'))
print(getattr(this_module, 's2'))
print(this_module.s2)
print(this_module.s1)