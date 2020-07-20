"""
斐波那契数列：从第3项开始，每一项都等于前两项之和。
1, 1, 2, 3, 5, 8, 13, 21..
定义函数，根据长度获取斐波那契数列。
"""
import random


def get_list_fibonacci(count_num):
    """
    根据长度获取斐波那契数列
    :param count_num: 斐波那契数列长度
    :return: list_fibonacci　斐波那契数列
    """
    list_fibonacci = []
    if count_num >= 3:
        list_fibonacci = [1, 1]
        #for r in range(2, count_num):
            # list_fibonacci.append(list_fibonacci[r - 1] + list_fibonacci[r - 2])
        for __ in range(count_num-2):# 从第三项开始遍历添加
            list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2]) #最后两项相加微信元素
        return list_fibonacci

    if count_num in range(1, 3):
        for __ in range(count_num):
            list_fibonacci.append(1)
    return list_fibonacci


# print(get_list_fibonacci(random.randint(0, 9)))
print(get_list_fibonacci(8))
