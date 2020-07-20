"""
定义函数，返回字符串中第一个不重复的字符。
输入：ABCACDBEFD
输出：E
"""


def get_first_value_nonredundant_in_strings(str_input):
    """
    返回字符串中第一个不重复的字符
    :param str_input: 字符串
    :return: 第一个不重复的字符
    """
    # for r in range(len(str_input)):
    #     if str_input.count(str_input[r]) == 1: #利用字符串count函数计数
    #         return str_input[r]   ＃遍历字符串返回第一个出现次数为一的元素
    for r in range(len(str_input)):
        for c in range(len(str_input)):
            if r != c and str_input[r] == str_input[c]:
                break
            elif c == len(str_input) - 1:
                return str_input[r]


str_input = "aaaDebDe"
print(get_first_value_nonredundant_in_strings(str_input))
