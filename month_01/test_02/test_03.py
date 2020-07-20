"""
定义函数，判断二维数字列表中是否存在某个数字
输入：二维列表、11
输出：True
"""


def bool_num_in_two_dimensional_list(double_list, target):
    for list_item in double_list:
        if target in list_item:
            return True
    return False


list_01 = [[1, 23], [4, 5, 6], [88, 9, 5]]
print(bool_num_in_two_dimensional_list(list_01,5))
