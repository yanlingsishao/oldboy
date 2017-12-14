print('api包的init文件')
__all__=['x','y','policy','versions']
from . import policy
x=1
y=2
# policy=123123123123
# versions='123123123'


# import policy#以test.py的sys.path为准

#绝对导入
# from glance.api import policy
# from glance.api import versions

#相对导入
#
# from . import policy,versions
#
# from ..cmd.manage import main


# C:\Users\Administrator\PycharmProjects\py_fullstack_s4\day35\包\glance\api