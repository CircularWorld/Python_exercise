'''
3.需求：累加20 --90之间,个位不是2/3/6/7的整数和。
步骤：生成范围内的整数，计算个位数，根据逻辑累加数字。
'''

total_num = 0
for num in range(20, 90):
    if num % 10 not in [2, 3, 6, 7]:
        total_num += num
        # print(num)
print(total_num)
