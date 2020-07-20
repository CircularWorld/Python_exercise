"""
练习1: 创建字典,遍历字典,打印索引/键/值
练习2: 创建列表,将列表中大于10的数字,设置为0
"""
dict_value = {'a': 'A',
              'b': 'B',
              'c': 'C',
              'd': 'D'}
for i, eletment in enumerate(dict_value.items()):
    print(i, eletment)

list_num = [1.9, 88, 6, 43, 98, 66, 7]
for i, num in enumerate(list_num):
    if num > 10:
        list_num[i] = 0
print(list_num)