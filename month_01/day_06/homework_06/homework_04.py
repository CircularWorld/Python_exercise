'''
4. 将列表中的数字累减
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    提示：初始为第一个元素
'''
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
result = list02[0]
for num in list02:
    result -= num
print(result)
