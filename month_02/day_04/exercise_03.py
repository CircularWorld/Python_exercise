"""
在一个字符串文本中筛选出所有整数

"""
import re

s = "Alex:1998,Sunny:1997"

# print(re.sub(r"\W+","##",s,2))
# print(re.split(r"\W+",s))
pattern = r"(?P<name>\w+):(?P<year>\d+)" #[('Alex', '1998'), ('Sunny', '1997')]
# print(re.findall(pattern,s))
l = re.finditer(pattern,s)
for iu in l:
    #每次取出一个匹配内容对应的match对象
    print(iu.group("name")) # 获取match对应内容
    print(iu.group("year")) # 获取match对应内容
    print(iu.group(1)) # 获取match对应内容
    print(iu.group(2)) # 获取match对应内容



# str = "身高170,体重６０"




# print(re.findall("[1-9][0-9]*",str))
# print(re.findall("[0-9]+",str))
# print(re.findall("\d+",str))
# print(re.findall("wo+","woooo...w"))
# print(re.findall("[A-Z][A-Za-z]*","I Love You"))