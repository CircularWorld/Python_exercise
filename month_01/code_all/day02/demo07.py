"""
    算数运算符 +  -  *  幂运算**
            小数商/   整数商//    余数%
"""
number01 = 5
number02 = 2
#
print(number01 + number02)  # 7
# 因为字符串与数字不能拼接，所以将数字转换为字符串
print("结果是:" + str(number01 + number02))  # 7

# 5 的 2次方 5 * 5  -->  25
print(number01 ** number02)

print(number01 / number02)  # 5 / 2 --> 2.5
print(number01 % number02)  # 5 % 2 --> 1
print(number01 // number02)  # 5 // 2 --> 2
