import re

s = "Alex:1998,Sunny:1997"

pattern = r"(?P<name>\w+):(?P<year>\d+)"  # [('Alex', '1998'), ('Sunny', '1997')]
# 匹配目标开头
obj = re.match(pattern,s)
print(obj.group())
# 匹配目标字符串第一处符合规则的地方
print()
print()
print()
print()
obj = re.search(pattern, s)
print(obj.group())
# 获取匹配内容在目标字符串中的位置
print(obj.span())
# 捕获组组名和对应内容形成的字典
print(obj.groupdict())
