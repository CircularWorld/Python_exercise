"""
"水仙花数":各位数字幂次方和等于该数本身
定义函数，根据位数计算水仙花数
输入：3
输出：[153, 370, 371, 407]
"""


def get_narcissistic_number(count):
    list_narcissistic_number = []
    # for num in range(10 ** (count - 1), 10 ** count):
    #     if (num // 100) ** 3 + (num % 100 // 10) ** 3 + (num % 100 % 10) ** 3 == num:
    #         list_narcissistic_number.append(num)
    list_narcissistic_number = [num for num in range(10 ** (count - 1), 10 ** count) if (num // 100) ** 3 + (num % 100 // 10) ** 3 + (num % 100 % 10) ** 3 == num]
    return list_narcissistic_number


print(get_narcissistic_number(3))
