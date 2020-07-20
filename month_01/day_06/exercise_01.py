
list_area = []
while True:
    area = input("请输入疫情地区：")
    if area:
        list_area.append(area)
    else:
        break
print(list_area)
str_area = '_'.join(list_area)
print(str_area)