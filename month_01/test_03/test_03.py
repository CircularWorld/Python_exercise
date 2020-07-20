"""二分查找
定义函数，在有序数字列表中找到目标值，并返回其索引。
如果目标值不在列表中，返回它可以按顺序插入的索引。
输入：[1,2,6,8,9]  8
输出：3

输入：[1,2,6,8,9]  5
输出：2"""

def get_index_in_orderly_num_list(list_orderly_num,target_num):
    for num_index in range(len(list_orderly_num)):
        if list_orderly_num[num_index] >= target_num:
            return num_index

list_num = [1,2,6,8,97]
print(get_index_in_orderly_num_list(list_num,4))

