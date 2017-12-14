
import ftpclient
#
# print(ftpclient)
# print(ftpclient.FtpClient)
# obj=ftpclient.FtpClient('192.168.1.3')
#
# print(obj)
# obj.test()



#
f1=ftpclient.FtpClient('192.168.1.1')
if hasattr(f1,'get'):
    func=getattr(f1,'get')
    func()
else:
    print('其他逻辑')