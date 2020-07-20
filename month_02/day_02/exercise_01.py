#!/usr/bin/python3

result = 1
list_num = []
for num in range(1,100,2):
        list_num.append(num)
        result *=num
print(result)
print(list_num)
