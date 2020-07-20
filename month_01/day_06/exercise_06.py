'''
# 练习1：将两个列表，合并为一个字典
# 姓名列表["张无忌","赵敏","周芷若"]
# 房间列表[101,102,103]
# 练习2：颠倒练习1字典键值
'''
list_01 = ["张无忌", "赵敏", "周芷若","小昭"]
list_02 = [101, 102, 103,104]
# for i in range(len(list_01)):
#     dict_info[list_01[i]] = list_02[i]
dict_info = {list_01[i]:list_02[i] for i in range(len(list_01))}
print(dict_info)

# for key,value in dict_info.items():
#     dict_info_change[value] = key
# print(dict_info_change)
dict_info_change = {value:key for key, value in dict_info.items()}
print(dict_info_change)
