"""
6.  自定义算法实现下列功能
    list01 = [3,9,34,26,5,6,7,8,9,6]
    在list01中找出最小值
    对liest01进行降序排列
    删除list01中大于10的元素
    删除list01中重复的元素
    体会编程思想
"""
list01 = [3, 9, 34, 26, 5, 6, 7, 8, 9, 6]


class MyNum:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num} ,"

    def __lt__(self, other):
        return self.num < other.num

    def __gt__(self, other):
        if type(other) == MyNum:
            return self.num > other.num
        else:
            return self.num > other

    def __eq__(self, other):
        return self.num == other.num


list01 = [
    MyNum(3),
    MyNum(9),
    MyNum(34),
    MyNum(26),
    MyNum(6),
    MyNum(7),
    MyNum(8),
    MyNum(9),
    MyNum(6)
]


def get_min_item():
    min_item = list01[0]
    for item in list01:
        if min_item > item:
            min_item = item
    return min_item


def sort_list_by_decrease():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] < list01[c]:
                list01[r], list01[c] = list01[c], list01[r]


def del_gt_10():
    for r in range(len(list01) - 1, -1, -1):
        if list01[r] > 10:
            del list01[r]

def del_repeat_num():
    for r in range(len(list01) - 1, 0, -1):
        for c in range(r):
            if list01[r] == list01[c]:
                del list01[r]
                break

def print_all_list():
    for item in list01:
        print(item, end='')


print(list01[0])
print(get_min_item().__dict__)
sort_list_by_decrease()
# del_gt_10()
del_repeat_num()
print_all_list()
