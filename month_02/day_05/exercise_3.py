import re
# s= '18701883070'
# l = re.findall("1[35678]\d{9}",s)
# print(l)
#
# str1 = 'this is book'
#
# print(re.search(r"^\w+\s\bis\b\s\w+",str1).group())
# s= 'asd 10'
# print(re.search(r"\b0\b|\b100\b|\b[1-9]\d{0,1}\b", s).group())

str1 = '<h1><span>hello world!<span><h1>'
pattern = r'<(.+)><(.+)>.*<\2><\1>'

res = re.match(pattern,str1)
print(res.group())