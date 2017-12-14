# m=input("请输入你要导入的模块：")

# m1=__import__(m)
# print(m1)
# print(m1.time())



#推荐使用方法
import importlib
t=importlib.import_module('time')
print(t.time())