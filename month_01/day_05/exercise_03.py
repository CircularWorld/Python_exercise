# list_area = ['北京','上海','深圳']
# list_add =  [1,2,3]
# list_total = [4000,5000,6000,]
# print(list_area[1])
# print(list_add[:2])
# print(list_total[1:])
#
# '''
# # 修改疫情地区列表最后一个元素 "sc"
# # 修改新增人数列表前两个元素　0
# # 修改现存人数列表后两个元素 26 17
# list_city = ["香港", "内蒙古", "四川"]
# list_new_people = [6, 0, 0]
# list_now_people = [51, 25, 16]
# '''
# list_city = ["香港", "内蒙古", "四川"]
# list_new_people = [6, 0, 0]
# list_now_people = [51, 25, 16]
#
# list_city[-1] = 'sc'
# print(list_city)
# list_new_people[:2] = '00'
# print(list_new_people)
# list_now_people[-2:] = [26,17]
# print(list_now_people)



'''
# 练习:



list_city = ["香港", "内蒙古", "四川"]
list_new_people = [6, 0, 0]
list_now_people = [51, 25, 16]'''

list_city = ["香港", "内蒙古", "四川"]
list_new_people = [1, 2, 3]
list_now_people = [51, 25, 16]
# 打印疫情地区列表所有元素(一行一个)
for city in list_city:
    print(city)
# 倒序打印新增人数列表(一行一个)
for i in range(len(list_new_people)-1,-1,-1):
    print(list_new_people[i])
# 将现存人数列表所有元素设置为0
for i in range(len(list_now_people)):
    list_now_people[i] = 0
print(list_now_people)

# 删除疫情地区列表中间元素
# 删除新增人数列表前两个元素
# 删除现存人数列表后两个元素
list_city = ["香港", "内蒙古", "四川"]
list_new_people = [1, 2, 3]
list_now_people = [51, 25, 16]

del list_city[len(list_city)//2]
print(list_city)

del list_new_people[:2]
print(list_new_people)

del list_now_people[1:]
print(list_now_people)