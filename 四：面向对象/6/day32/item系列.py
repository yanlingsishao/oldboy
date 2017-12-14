#把对象操作属性模拟成字典的格式
class Foo:
    def __init__(self,name):
        self.name=name
    def __setattr__(self, key, value):
        print('setattr===>')
    def __getitem__(self, item):
        # print('getitem',item)
        return self.__dict__[item]
    def __setitem__(self, key, value):
        print('setitem-----<')
        self.__dict__[key]=value
    def __delitem__(self, key):
        self.__dict__.pop(key)
        # self.__dict__.pop(key)
    # def __delattr__(self, item):
    #     print('del obj.key时,我执行')
    #     self.__dict__.pop(item)

f=Foo('egon')
f.name='egonlin'
f['name']='egonlinhai'
# print(f.name)
# f.name='egonlin'
# f['age']=18
# print(f.__dict__)
#
# del f['age'] #del f.age
# print(f.__dict__)

# print(f['name'])