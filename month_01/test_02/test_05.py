"""
5.质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
    定义函数，获取指定范围内的所有质数。
输入：2,20
输出：[2, 3, 5, 7, 11, 13, 17, 19]
"""


def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    if number < 2: return False
    return True

def get_prime_number_in_range(star_num, end_num):
    return [num for num in range(star_num, end_num+1) if is_prime_number(num)]

print(get_prime_number_in_range(2, 20))
