# import time
# class Open:
#     def __init__(self,filepath,mode='r',encode='utf-8'):
#         self.f=open(filepath,mode=mode,encoding=encode)
#
#     def write(self,line):
#         self.f.write(line)
#
#
#     def __getattr__(self, item):
#         return getattr(self.f,item)
#
#     def __del__(self):
#         print('----->del')
#         self.f.close()
#
#     def __enter__(self):
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#
#
# with Open('egon.txt','w') as f:
#     f.write('egontest\n')
#     f.write('egontest\n')
#     f.write('egontest\n')
#     f.write('egontest\n')
#     f.write('egontest\n')


















class Open:
    def __init__(self,filepath,mode,encode='utf-8'):
        self.f=open(filepath,mode=mode,encoding=encode)
        self.filepath=filepath
        self.mode=mode
        self.encoding=encode

    def write(self,line):
        print('write')
        self.f.write(line)

    def __getattr__(self, item):
        return getattr(self.f,item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        return True

with Open('aaaaa.txt','w') as write_file: #write_file=Open('aaaaa.txt','w')
    write_file.write('123123123123123\n')
    write_file.write('123123123123123\n')
    print(sssssssssssssss)
    write_file.write('123123123123123\n')







