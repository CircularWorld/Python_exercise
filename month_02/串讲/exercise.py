import re

#验证手机号手否符合规则

# s= '小明的电话：15137073885'
# pattern = r'\b1\d{10}\b'
# res = re.search(pattern,s)
# print(res.group())

#匹配单词边界
# str1 = 'this is book'
# patten = r'\b[a-z]+\s[a-z]+\s[a-z]+\b'
# res = re.search(patten,str1)
# print(res.group())

#匹配0~100之间的数字

# str1 = '86'#100 1 10
# patten = r'0|\b[1-9]\d{0,1}\b|100'
# res = re.search(patten,str1)
# print(res.group())

# str1 = '<h1>hello world!</h1>'
# pattern = r'<(\w+)>.+</\1>'
# res = re.search(pattern,str1)
# print(res.group())


# str3 = '<a><b>nihao</b></a>'
# pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.*</(?P=key2)></(?P=key1)>'
# res = re.match(pattern,str3)
# print(res.group())

# str3 = '<a><b>nihao</b></a>'
# pattern = '<(?P<key1>.+)><(?P<key2>.+)>\w+</(?P=key2)></(?P=key1)>'
# res = re.search(pattern,str3)
# print(type(res.group()))

# str1 = '/milllll'
# pattern = '^/mil$'
# res = re.search(pattern,str1)
# print(res.group())


# str1 = 'this is a number 123-2345-67'
# pattern =r'(.+?)(\d+-\d+-\d+)'
# res = re.search(pattern,str1)
# print(res.group(1))

# 目标字符串
s = """Hello
北京
"""
# # 让正则表达式只能匹配ascii码（英文符号）

pattern = '\w+$'
res = re.findall(pattern,s,flags= re.M)
print(res)