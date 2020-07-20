import re
#验证手机号手否符合规则
#1.都是数字
#2.11位
#3.必须以1开头
#4.第二位是35678中的一位
# phoneStr = '13012345678'
# pattern = '1[35678]\d{9}'
# res = re.match(pattern,phoneStr)
# print(res.group())

#匹配单词边界
# str1 = 'this is book'
#以字母开始
#中间包含空字符
#is两边分别限定单词边界
# pattern = r'\w+\s\bis\b\s\w+'
# res = re.match(pattern,str1)
# print(res.group())

#匹配0~100之间的数字
#1. 0
#2. 100
#3. 1-99
# num = input('>>>')
# pattern = '0$|100$|[1-9]\d{0,1}$'
# res = re.match(pattern,num)
# print(res.group())

#
# str1 = '<h1>hello world!</h1>'
# pattern = r'^<h1>(.*)</h1>'
# res = re.match(pattern,str1)
# print(res.group())

#<xx><yy>xxxx</yy></xx>
#\1对第一个分组的引用   \2

# str2 = '<h1><span>hello world!</span></h1>'
# pattern = r'<(.+)><(.+)>.*</\2></\1>'
# res = re.match(pattern,str2)
# print(res.group())
#
# str3 = '<a><b>nihao</b></a>'
# pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.*</(?P=key2)></(?P=key1)>'
# res = re.match(pattern,str3)
# print(res.group())



# str1 = '/milllll'
# pattern = '^/mil$'
# res = re.match(pattern,str1)
# print(res.group())

str1 = 'this is a number 123-2345-67'
pattern = r'(.+)(\d+-\d+-\d+)'
res = re.match(pattern,str1)
print(res.group())

pattern2 = r'(.+?)(\d+-\d+-\d+)'
res2 = re.match(pattern2,str1)
print(res2.groups())