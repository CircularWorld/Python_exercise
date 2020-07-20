import copy
list01 = [
    ["烤鸭", "豆汁"],
    ["火锅", "兔头"],
    ["麻花", "包子"],
]
list02 = list01
list03 = list01[:]
list04 = copy.deepcopy(list01)

list04[0] = ["全聚德", "大董"]
print(list04)
print(list01)

list03[0][1] = ["全聚德", "大董"]
print(list03)
print(list01)

# 提示：看看切片原理
list02[0][:] = ["全聚德", "大董"]
print(list02)
print(list01)