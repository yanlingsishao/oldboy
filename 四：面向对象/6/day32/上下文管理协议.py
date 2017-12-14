# with open('a.txt','r') as f:
#     print('--=---->')
#     print(f.read())

# with open('a.txt', 'r'):
#     print('--=---->')


#
class Foo:
    def __enter__(self):
        print('=======================》enter')
        return 111111111111111

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print('exc_type',exc_type)
        print('exc_val',exc_val)
        print('exc_tb',exc_tb)
        return True


# with Foo(): #res=Foo().__enter__()
#     pass

with Foo() as obj: #res=Foo().__enter__() #obj=res
    print('with foo的自代码块',obj)
    raise NameError('名字没有定义')
    print('************************************')

print('1111111111111111111111111111111111111111')

