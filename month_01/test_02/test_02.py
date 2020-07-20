"""
定义函数，删除列表中所有重复的元素(重复元素只保留一个)。
输入：[4,35,7,64,7,35]
输出：[4, 35, 7, 64]
"""


def del_repet_value_in_list(target):
    """
    删除列表中所有重复的元素
    """
    for r in range(len(target) - 1, 0, -1):  # 从后向前取元素，
        for c in range(r):  # 和　索引ｒ　之前的　元素　比较
            if target[r] == target[c]:
                del target[r]  # 倒序删除
                break\t


list_01 = [7, 7, 7, 64, 7, 35]
# set_01 = set(list_input)
# print(set_01)
del_repet_value_in_list(list_01)
print(list_01)
