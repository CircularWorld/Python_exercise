f = open('dict.txt','r')
import re
args_list = []
for line in f:
    pattern = '(?P<word>^\w*)\s*(?P<mean>.*)'
    res  = re.findall(pattern,line)
    # print(res)
    args_list.extend(res)
    print(args_list)
print(args_list)