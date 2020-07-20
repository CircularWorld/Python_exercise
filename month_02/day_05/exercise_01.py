"""

"""

import re

s = """Hello
北京
"""
l = re.findall("\w+", s, flags=re.ASCII)
l = re.split("\\n", s, flags=re.ASCII)
l = re.findall(".+", s, flags=re.S)
l = re.sub("[a-z]+", "你好", s, flags=re.IGNORECASE)
l = re.finditer("^\w+", s, flags=re.MULTILINE)
# for data in l:
#     print(data.group())
# l = re.match("[A-Za-z]*",s).group()
s = 'Speake hello'
l = re.search("[A-Z](?P<name>[a-z]*)",s).group("name")
# l = re.match("\S[a-z]*",s).group()

print(l)
