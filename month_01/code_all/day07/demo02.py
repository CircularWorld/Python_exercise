"""
    自定义排序算法
    练习:exercise03
"""
# 核心思想：
# 确定第一个元素是最大值
# 确定第二个元素是最大值
# ...
# 确定第倒数第二个元素是最大值

# 步骤：
# 1.取出前几个数据(不要最后一个)
# 2.与后面元素进行比较
# 3.发现更xx则交换(取出的   比较的)
list01 = [43, 15, 5, 67, 87, 9]
def sort_list(list_num):
    """
    对数字列表升序
    :param list_num: 需要排序的列表
    """
    for r in range(len(list_num) - 1):  # 0   1
        for c in range(r + 1, len(list_num)):
            if list_num[r] > list_num[c]:
                list_num[r], list_num[c] = list_num[c], list_num[r]
sort_list(list01)
print(list01)