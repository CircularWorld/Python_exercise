'''
10~60 个位不是　３，５，８的　和
'''

total_num = 0
for count in range(10, 61):
    unit = count % 10
    if unit== 3 or unit == 5 or unit == 8:
        continue
    print(count)
    total_num += count
print(total_num)
