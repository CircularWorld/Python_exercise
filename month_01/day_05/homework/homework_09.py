'''
9. 在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
   （使用内置函数实现）
'''
list_center_num= []
for __ in  range(5):
    center_num = input('请输入确认人数：')
    if center_num and center_num.isdigit():
        list_center_num.append(int(center_num))
    else:
        print('请输入整数')
        exit()
print(list_center_num)
print(max(list_center_num))
print(min(list_center_num))
print(sum(list_center_num)/len(list_center_num))
