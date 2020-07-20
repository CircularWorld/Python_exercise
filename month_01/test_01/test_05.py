'''
5.需求：在终端中录入5个疫情省份的确诊人数，
              打印最大值、最小值、平均值.（使用内置函数实现）
	   步骤：循环获取信息，使用列表记录，使用内置函数计算。
'''
list_num = []
for __ in range(5):
    confirm_num = int(input("请输入确诊人数："))
    list_num.append(confirm_num)
print(list_num)
print('最多的有%d人' % max(list_num))
print('做少的有%d人' % min(list_num))
print("平均有%d人'" % (sum(list_num) / len(list_num)))
# print(sum(list_num) / len(list_num))
