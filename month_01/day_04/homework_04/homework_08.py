'''
8. (选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/运算
'''
height = 100
total_distance = 100
count = 0
# 拿弹之后的高度比较，如果弹之后小于０．０１说明弹不起
while height / 2 > 0.01:
    count += 1
    height /= 2
    total_distance += height*2
# print('总共弹起%d次，全过程总共移动%.2f米' % (count,total_distance))
print(f'总共弹起{count}次，全过程总共移动{total_distance: .2f}米')
