#
# list_01 = [1,2,3,4]
# list_02 = ["a","b","c","d"]
# for a,b in zip(list_01,list_02):
#     pass
#     # print(a,b)

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 矩阵转置

list_num2 = [list(item) for item in zip(*list01)]
print(list_num2)