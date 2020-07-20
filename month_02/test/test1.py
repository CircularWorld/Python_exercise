# 给你一个 n*m 的二维数组，
# 每行元素保证递增，
# 每列元素保证递增，
# 试问如何找到某个数字，或者判断这个数字不存在。

# def search_number(list_N_M,num):
#     if list_N_M[0][0] <= num <= list_N_M[-1][-1]:
#         for i in range(len(list_N_M)-1):
#             if num <= list_N_M[i][-1] and num in list_N_M[i]:
#                 return True
#         return False
#     else:
#         return False
matrix = [
    [2, 4, 6, 9],
    [13, 15, 17, 19],
    [24, 26, 27, 28]
]


def search(matrix, num):
    row = len(matrix)
    col = len(matrix[0])
    i = row - 1
    j = 0
    res = False
    # matrix[i][j]
    while True:
        if i < 0 or j == col:
            break
        if matrix[i][j] > num:
            # 如果 左下角元素大于目标  上移
            i -= 1
        elif matrix[i][j] < num:
            # 如果 左下角元素小于目标  右移
            j += 1
        elif matrix[i][j] == num:
            res = True
            break
    return res


print(search(matrix, 24))

list_N_M = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
]
num = int(input("请输入数字"))
print(search_number(list_N_M, num))
