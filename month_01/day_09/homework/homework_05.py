"""
5.  --定义函数,将列表中奇数设置为1
    --定义函数,将列表中奇数删除
    测试数据:[3,7,5,6,7,8,9,13]
    结论:在列表中删除多个元素,倒序删除
"""

def set_odd_to_1(list_num):
    """
    将列表中奇数设置为1
    :param list_num: 传入数字列表
    """
    for i in range(len(list_num)):
        if list_num[i]%2:
            list_num[i] =1

def del_odd_in_list(list_num):
    """
    将列表中奇数删除
    :param list_num: 传入数字列表
    """
    for i in range(len(list_num)-1,-1,-1):
        if list_num[i]%2:
            del list_num[i]

# def del_odd_in_list_02(list_num):
#     for item in list_num:
#         if item%2 ==1:
#             list_num.remove(item)



list_num = [3,7,5,6,7,8,9,13]
set_odd_to_1(list_num)

del_odd_in_list(list_num)
print(list_num)