"""
6. (选做)2048 游戏核心算法
# 全局变量
list_merge = [2, 0, 2, 0]

# (1)定义零元素向后移动的函数　zero_to_end()
     思想：从后向前判断，如果是0则删除,在末尾追加.
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]

# (2)定义合并函数　merge()
    核心思想：零元素后移，判断是否相邻相同。如果是则合并.
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
"""
import random


class Game2048:
    def __init__(self):
        pass


# 全局变量

list_merge = [0, 0, 0, 0]

def random_set_2_places_in_box():
    """
    在列表内随机生成两个添加数字的位置
    """
    while True:
        place_01 = random.randint(0,len(list_merge)-1)
        place_02 = random.randint(0,len(list_merge)-1)
        if place_01 != place_02:
            random_set_value_in_place(place_01)
            random_set_value_in_place(place_02)
            break

def random_set_value_in_place(place):
    """
    随机产生一个数字2 or 4　在位置上
    :param place: 列表位置索引
    """
    list_merge[place] = random.choice((2, 4))


def zero_to_end():
    """
    零元素向后移动
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    """
    合并相邻相同的元素
    """
    zero_to_end()
    for r in range(len(list_merge) - 1):
        # for c in range(r+1,len(list_merge)): 24816
        if list_merge[r] == list_merge[r + 1]:
            list_merge[r] *= 2
            del list_merge[r + 1]
            list_merge.append(0)
            # list_merge[r + 1] = 0
            # zero_to_end()

random_set_2_places_in_box()
print(list_merge)
zero_to_end()
print(list_merge)
merge()
print(list_merge)
