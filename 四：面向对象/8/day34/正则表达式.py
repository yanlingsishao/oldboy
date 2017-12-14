

# 正则：对字符串的模糊匹配

# key：元字符（有特殊功能的字符）



import re

#   re.findall(pattern, string,) # 找到所有的匹配元素，返回列表


#元字符介绍

# . :匹配除\n以外的任意符号

#print(re.findall("a.+d","abcd"))


# ^:从字符串开始位置匹配

# $：从字符串结尾匹配

# print(re.findall("^yuan","yuandashj342jhg234"))
# print(re.findall("yuan$","yuandashj342jhg234yuan"))

# * + ?  {} ：重复

#print(re.findall("[0-9]{4}","af5324jh523hgj34gkhg53453"))


#贪婪匹配
print(re.findall("\d+","af5324jh523hgj34gkhg53453"))

#非贪婪匹配

# print(re.findall("\d+?","af5324jh523hgj34gkhg53453"))
# print(re.findall("(abc\d)*?","af5324jh523hgj34gkhg53453"))

# 字符集 []: 起一个或者的意思

# print(re.findall("a[bc]d","hasdabdjhacd"))

#注意: * ,+.等元字符都是普通符号， - ^ \

# print(re.findall("[0-9]+","dashj342jhg234"))
# print(re.findall("[a-z]+","dashj342jhg234"))
#
# print(re.findall("[^\d]+","d2a2fhj87fgj"))


# ()：分组

# print(re.findall("(ad)+","addd"))
# print(re.findall("(ad)+yuan","adddyuangfsdui"))

# print(re.findall("(?:ad)+yuan","adadyuangfsdui"))
# print(re.findall("(?:\d)+yuan","adad678423yuang4234fsdui"))

#命名分组

#ret8=re.search(r"(?P<A>\w+)\\aticles\\(?P<id>\d{4})",r"yuan\aticles\1234")
#ret8=re.search(r"a\\nb",r"a\nb")
#print(ret8)

# print(ret8.group("id"))
# print(ret8.group("A"))


# # |  :或
#
# print(re.findall("www\.(?:oldboy|baidu)\.com","www.oldboy.com"))

# \:转义

# 1 后面加一个元字符使其变成普通符号 \.  \*
# 2 将一些普通符号变成特殊符号 比如 \d \w

# print(re.findall("\d+\.?\d*\*\d+\.?\d*","-2*6+7*45+1.456*3-8/4"))
# print(re.findall("\w","$da@s4 234"))
# print(re.findall("a\sb","a badf"))

# print(re.findall("\\bI","hello I am LIA"))
# print(re.findall(r"\dI","hello 654I am LIA"))

# print(re.findall(r"c\\l","abc\l"))


#  re的方法


# re.findall()


# s=re.finditer("\d+","ad324das32")
# print(s)
#
# print(next(s).group())
# print(next(s).group())


# "(3+7*2+27+7+(4/2+1))+3"

# search;只匹配第一个结果

# ret=re.search("\d+","djksf34asd3")
# print(ret.group())
#
# #match:只在字符串开始的位置匹配
# ret=re.match("\d+","423djksf34asd3")
# print(ret.group())

#split 分割
# s2=re.split("\d+","fhd3245jskf54skf453sd",2)
# print(s2)
#
# ret3=re.split("l","hello yuan")
# print(ret3)
#
# #sub: 替换
#
# ret4=re.sub("\d+","A","hello 234jkhh23",1)
# print(ret4)
#
# ret4=re.subn("\d+","A","hello 234jkhh23")
# print(ret4)


#compile: 编译方法
# c=re.compile("\d+")
#
# ret5=c.findall("hello32world53") #== re.findall("\d+","hello32world53")
# print(ret5)


#计算："1 - 2 * ( (60-30*2+-96) - (-4*3)/ (16-3*2) )"

# s1="1+-2++5"
#
# def addsub(s):
#     pass
#
# def muldiv(s): #(60-30*2+-96)
#     pass
#     return (60-60+-96)
#
# def f(s):
#     s.replace("+-","-")
#
#
# while re.search("\([^()]+\)", s):
#     res = re.search("\([^()]+\)", s) #(60-30*2+-96)
#     res=muldiv(res)
#     ret=addsub(res)
# else:
#     res = muldiv(res)
#     ret = addsub(res)








s="2"


print(res.group())













