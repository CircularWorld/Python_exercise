"""
    Python核心2
        语句
        容器
"""

# def func01():
#     for r in range(5):  # 执行一次
#         for c in range(4):  # 执行多次
#             # continue # 跳过当次循环
#             # break 跳出1层循环
#             return  # 结束函数(跳出所有循环)

# 读取操作
import copy
list01 = [10, 20, 30]
list02 = list01  # 赋值:将list01存储的列表地址给list02
list03 = list01[:]  # 浅拷贝:将list01指向的列表复制一份
list04 = list01[::-1]  # 浅拷贝:通常,[30, 20, 10]

list05 = [
    [10,20,30]
]
# list06 = copy.deepcopy(list05) # 深拷贝:拷贝所有数据[10,20,30]
list06 = list05[:] # 浅拷贝:只拷贝一层
list05[0][1] = 100 # 修改第二层数据
print(list06[0][1]) # ?

# 写入操作
list01 = [10, 20, 30]
list01[0] = 100 # 将右侧数据地址赋值给列表元素
list01[1] = [200] # 将右侧数据地址赋值给列表元素
list01[2:] = [300,400] # 遍历右侧元素,赋值给列表元素
print(list01)