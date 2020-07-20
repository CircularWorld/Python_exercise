'''
8. 在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有省份名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in
'''
list_area = []
while True:
    province = input('请输入疫情地区（空字符串停止）:')
    if province:
        if province not in list_area:
            list_area.append(province)
        else:
            print('此省已存在')
    else:
        break
# print(list_area)
for area in list_area[::-1]:
    print(area)
