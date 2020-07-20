"""
5. list01 = [6,2,3,4,5,6,7,3,2,4,8]
    定义函数,删除列表中重复元素.(不使用其他容器,自定义算法)
"""
def del_list_repeat_value(target):
    for r in range(len(target)-1,0,-1):
        for c in range(r):
            if target[r] == target[c]:
                del target[r]
                break

list01 = [6, 2, 3, 4, 5, 6, 7, 3, 2, 4, 8]
del_list_repeat_value(list01)
print(list01)