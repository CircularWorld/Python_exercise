'''
在终端中录入4个同学身高,打印最高的值.
算法：
170 160 180 165
假设第一个就是最大值
使用假设的和第二个进行比较, 发现更大的就替换假设的
使用假设的和第三个进行比较, 发现更大的就替换假设的
使用假设的和第四个进行比较, 发现更大的就替换假设的
最后，假设的就是最大的.
'''
height_1 = int(input('height_1 = '))
height_2 = int(input('height_2 = '))
height_3 = int(input('height_3 = '))
height_4 = int(input('height_4 = '))

max = height_1
# if max < height_2:
#     max = height_2
# if max < height_3:
#     max = height_3
# if max < height_4:
#     max = height_4
# print(max)

height_all = [height_1,height_2,height_3,height_4]
for m in height_all:
    if max < m:
        max = m
print(m)


