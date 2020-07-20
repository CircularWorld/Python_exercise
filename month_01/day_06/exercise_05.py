'''
列表适合：存储单一维度的信息
疫情地区列表（地区）
字典适合：存储多个维度的信息
疫情信息(地区、新增人数、现有人数..)

练习1: 创建三个字典, 存储前三个地区疫情信息(地区, 新增, 现有, 累计, 治愈)
练习2: 为以上三个字典, 添加si亡信息
练习3: 删除第一个字典的新增人数,
练习4: 将第二个字典的新增人数设置为0,
练习5: 打印第三个字典信息:
格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
'''
'''
'''
# 练习1: 创建三个字典, 存储前三个地区疫情信息(地区, 新增, 现有, 累计, 治愈)
dict_infor_hongkong = {'region':'hongkong','add':6,'now':53,'add_up':1099,'cure':1042}
dict_infor_neimenggu = {'region':'neimenggu','add':0,'now':21,'add_up':235,'cure':213}
dict_infor_sichuan = {'region':'sichuan','add':1,'now':17,'add_up':578,'cure':558}
dict_infor_hongkong['dead'] = 4
dict_infor_neimenggu['dead'] = 1
dict_infor_sichuan['dead'] = 3

del dict_infor_hongkong['add']
print(dict_infor_hongkong)

dict_infor_neimenggu['add'] = 0
print(dict_infor_neimenggu)

print(dict_infor_sichuan)

# 格式: xx新增xx, 现有xx, 累计xx, 治愈xx, si亡xx
print(f"{dict_infor_sichuan['region']}新增{dict_infor_sichuan['add']},死亡{dict_infor_sichuan['dead']}")

dict_infor = {'上海':dict_infor_hongkong,'内蒙古':dict_infor_neimenggu}
print(dict_infor['上海'].values())