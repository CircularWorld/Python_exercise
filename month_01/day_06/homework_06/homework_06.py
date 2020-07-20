'''
6. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   结果:[63, 227, 3127]
   提示：将数字转换为字符串进行处理
'''
list03 = [135, 63, 227, 675, 470, 733, 3127]
# for i in range(len(list03)):
#     list03[i] = str(list03[i])
list03 = [str(list03[i]) for i in range(len(list03))]
print(list03)
list_result = [int(item) for item in list03 if item[-2] not in '378']
# for item in list03:
#     if item[-2] not in '378':
#         list_result.append(item)
print(list_result)