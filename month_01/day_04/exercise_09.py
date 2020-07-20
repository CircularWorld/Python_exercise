# total_num = 0
# for __ in range(5):
#     num = float(input('请输入数字：'))
#     total_num+=num
# print(total_num)

total_num =0
while True:
    num =input('请输入数字:')
    if num =='':
        break
    total_num += float(num)
print(total_num)