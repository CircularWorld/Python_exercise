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
3. 定义向左移动函数,改变list_map中的数据
   思路：将list_map每行赋值给list_merge
        调用合并函数(练习2)

4. 定义向右移动函数,改变list_map中的数据
   思路：将list_map每行,反转,赋值给list_merge
        调用合并函数
        将list_merge反转后赋值给list_map
"""
import random
# 全局变量
list_map = [
    [0, 0, 4, 4],
    [0,2, 8, 8],
    [4, 0,4, 0],
    [2, 2, 2, 2]
]

# def random_set_2_places_in_box():
#     """
#     在列表内随机生成两个添加数字的位置
#     """
#     while True:
#         place_01 = random.randint(0,len(list_merge)-1)
#         place_02 = random.randint(0,len(list_merge)-1)
#         if place_01 != place_02:
#             random_set_value_in_place(place_01)
#             random_set_value_in_place(place_02)
#             break
#
# def random_set_value_in_place(place):
#     """
#     随机产生一个数字2 or 4　在位置上
#     :param place: 列表位置索引
#     """
#     list_merge[place] = random.choice((2, 4))


def zero_to_end():
    """
    零元素向后移动
    """
    for list_merge in list_map:
        for i in range(len(list_merge) - 1, -1, -1):
            if list_merge[i] == 0:
                del list_merge[i]
                list_merge.append(0)


def merge():
    """
    合并相邻相同的元素
    """
    for list_merge in list_map:
        for r in range(len(list_merge) - 1):
            # for c in range(r+1,len(list_merge)): 24816
            if list_merge[r] == list_merge[r + 1]:
                list_merge[r] *= 2
                del list_merge[r + 1]
                list_merge.append(0)
                # list_merge[r + 1] = 0
                # zero_to_end()
# 3. 定义向左移动函数,改变list_map中的数据
#    思路：将list_map每行赋值给list_merge
#         调用合并函数(练习2)
def left_move():
    zero_to_end()
    merge()
"""
4. 定义向右移动函数,改变list_map中的数据
   思路：将list_map每行,反转,赋值给list_merge
        调用合并函数
        将list_merge反转后赋值给list_map
"""
def reverse_list_map():
    for i in range(len(list_map)):
        list_map[i].reverse()

def right_move():
    reverse_list_map()
    zero_to_end()
    merge()
    reverse_list_map()

def matrix_transpose():
    for r in range(len(list_map)):
        for c in range(r):
                list_map[r][c], list_map[c][r] = list_map[c][r], list_map[r][c]


    # list_map = [
    #     [0, 0, 4, 4],
    #     [0, 2, 8, 8],
    #     [4, 0, 4, 0],
    #     [2, 2, 2, 2]
    # ]

def up_move():
    matrix_transpose()
    left_move()
    matrix_transpose()

def down_move():
    matrix_transpose()
    right_move()
    matrix_transpose()

def print_list_map():
    for item in list_map:
        print(item)
    print("*****************")

print_list_map()
down_move()
print_list_map()

# matrix_transpose()
# print_list_map()
# up_move()
# print_list_map()
# right_move()
# print_list_map()
