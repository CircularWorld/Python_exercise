'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R   r%4 = 0
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：LCIRETOESIIGEDHN
'''
def convert(s, numRows):
    if numRows < 2:  return s
    res = ["" for __ in range(numRows)]
    i ,flag = 0,-1
    for c in s:
        res[i]+=c
        if i == 0 or i == numRows-1: flag = -flag
        i +=flag
    return ''.join(res)



str01 = "LEETCODEISHIRING"
str02 = "LEEEDTCOHTENISEODIRIHENG"
print(convert(str01, 3))
# print(convert(str02, 4))


