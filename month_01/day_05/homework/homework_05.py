'''
5. 将列表中整数的个位不是5和3的数字存入另外一个列表
   list03 = [25, 63, 27, 75, 70, 83, 27]
   结果:[27, 70, 27]
'''
list03 = [25, 63, 27, 75, 70, 83, 27]
list_new = []
for num in list03:
    if num%10 ==5 or num%10 ==3:
        continue
    list_new.append(num)
print(list_new)