list01 = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]
'''
print(list01[0][2]) # 3
# 打印出5/9/12
# (每行一个)循环打印6, 7, 8, 9, 10
# (每行一个)循环打印15,14,13,12,11
# (每行一个)循环打印1,6,11
# (每行一个)循环打印14,9,4
# 以表格状打印每个元素(不要逗号)'''
print(list01[0][4]) # 5
print(list01[1][3]) # 9
print(list01[2][1]) # 12
for item in list01[1]:
    print(item, end = ' ')
for item in list01[2][::-1]:
    print(item)

for item in list01:
    print(item[0])

for item in list01[::-1]:
    print(item[-2])

for r in range(len(list01)):
    for c in range(len(list01[r])):
        print(list01[r][c], end = ' ')
        print('A',end ='')
    print()
