'''
6. 计算梯形面积
    在终端中获取上底,下底和高
    输出面积
    公式：(上底 + 下底) 乘以 高 除以 2
'''

top = float(input('请输入梯形上底：'))
bootom = float(input('请输入梯形下底：'))
height = float(input('请输入梯形高：'))
Trapezoid_area = (top + bootom) * height / 2
del top, bootom, height
print('梯形面积为' + str(Trapezoid_area))
