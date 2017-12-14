class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')
    def speak(self):
        raise AttributeError('子类必须实现这个方法')



class People(Animal):
    def run(self):
        print('人正在走')

    # def speak(self):
    #     print('说话')

class Pig(Animal):
    def run(self):
        print('pig is walking')
    def speak(self):
        print('哼哼哼')

peo1=People()
# peo1.run()
peo1.speak()

# peo1=People()
# pig1=Pig()
#
# peo1.run()
# pig1.run()















# class Interface:#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
#     def read(self): #定接口函数read
#         pass
#
#     def write(self): #定义接口函数write
#         pass
#
#
# class Txt(Interface): #文本，具体实现read和write
#     def read(self):
#         print('文本数据的读取方法')
#
#     def write(self):
#         print('文本数据的读取方法')
#
# class Sata(Interface): #磁盘，具体实现read和write
#     def read(self):
#         print('硬盘数据的读取方法')
#
#     def write(self):
#         print('硬盘数据的读取方法')
#
# class Process(Interface):
#     def read(self):
#         print('进程数据的读取方法')
#
#     def write(self):
#         print('进程数据的读取方法')
#
#
#
# t1=Txt()
# s1=Sata()
# p1=Process()
#
#
#
# t1.read()
# t1.write()
#
# s1.read()
# s1.write()
#
# p1.read()
# p1.write()









