# 2. 给你一个长度为n的数组，
# 其中只有一个数字出现了1次，
# 其他均出现2次，
# 问如何快速的找到这个数字。
# 字典?
list_num = [2,3,4,4,5,5,3,2,88]
# def get_number(list_num):
#     dict_num = dict()
#     for num in list_num:
#         if num in dict_num:
#             dict_num[num] +=1
#         else:
#             dict_num[num] = 1
#     for key,count in dict_num.items():
#         if count ==1:
#             return key

# def search_num(list_num):
#     list_num.sort()
#     for i in range(0,len(list_num)-1,2):
#         if list_num[i] != list_num[i+1]:
#             return list_num[i]
#     else:
#         return list_num[-1]

def search_num(list_num):

print(search_num(list_num))

