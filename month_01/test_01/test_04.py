'''

4.需求：一个小球从100m高度落下,每次弹回原高度一半.
   	         计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)  13 次
-- 全过程总共移动多少米?
步骤：使用while循环模拟小球弹起过程，计算结果。
'''
distance = height = 100
count = 0
while height / 2 > 0.01:
    height /= 2
    distance += height * 2
    count += 1
print(f'小球弹了{count}次，总移动{distance:.2f}米')
