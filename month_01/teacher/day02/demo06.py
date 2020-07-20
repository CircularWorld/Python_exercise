"""
    类型转换
        结果 = 数据类型(待转换数据)
"""
# 案例：计算明年年龄
# str_age = input("请输入你的年龄：")
# int_age = int(str_age) + 1
# print("明年你" + str(int_age))

# str --> int
number01 = int("18") # 18
# float -(截断删除)-> int
number02 = int(1.9) # 1
print(number02)

# int --> str
str01 = str(18)# "18"
# float --> str
str02 = str(1.5) #"1.5"

# int --> float
float01 = float(18) # 18.0
# str --> str
float02 = float("1.5") # 1.5

# 注意：
# 字符串转换为其他类型时,必须长得像目标类型.
# str --> ?
number03 = int("18我你") # 不像整数ValueError
# number03 = int("18.5") # 不像整数ValueError
# float03 = float("1.5a")

# 如果希望使用win快捷键
# 先 ctrl + alt   再 按win快捷键