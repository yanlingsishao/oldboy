import sys
def add():
    print('add')

def change():
    print('change')

def search():
    print('search')


def delete():
    print('delete')

this_module=sys.modules[__name__]
while True:
    cmd=input('>>：').strip()
    if not cmd:continue
    if hasattr(this_module,cmd):
        func=getattr(this_module,cmd)
        func()
    # if cmd in func_dic: #hasattr()
    #     func=func_dic.get(cmd) #func=getattr()
    #     func()



#
# func_dic={
#     'add':add,
#     'change':change,
#     'search':search,
#     'delete':delete
# }

#
# while True:
#     cmd=input('>>：').strip()
#     if not cmd:continue
#     if cmd in func_dic: #hasattr()
#         func=func_dic.get(cmd) #func=getattr()
#         func()



#
# class Foo:
#     x=1
#     def __init__(self,name):
#         self.name=name
#
#
#     def walk(self):
#         print('walking......')
# f=Foo('egon')






# Foo.__dict__={'x':1,'walk':....}

# 'x' in Foo.__dict__ #hasattr(Foo,'x')
# Foo.__dict__['x'] #getattr(Foo,'x')

# print(Foo.x) #'x' in Foo.__dict__








