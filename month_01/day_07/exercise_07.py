'''
dict_hobbies = {
"qtx": ["看书", "编码", "旅游"],
"lzmly": ["刷抖音", "看电影"],
"于谦": ["抽烟", "喝酒", "烫头"]
}
# 打印"于谦"的第二个爱好
# 打印qtx所有爱好(一行一个)
# 打印lzmly的爱好数量
# 打印所有人的所有爱好(一行一个)
'''
dict_hobbies = {
"qtx": ["看书", "编码", "旅游"],
"lzmly": ["刷抖音", "看电影"],
"于谦": ["抽烟", "喝酒", "烫头"]
}
print(f'"于谦"的第二个爱好{dict_hobbies["于谦"][1]}')
for hobbie in dict_hobbies["qtx"]:
    print(hobbie)
print(len(dict_hobbies["lzmly"]))

for name in dict_hobbies:
    for hobit in dict_hobbies[name]:
        print(hobit)













# print(f'"于谦"的第二个爱好{dict_hobbies["于谦"][1]}')
# for hobbies in dict_hobbies["qtx"]:
#     print(hobbies)
# print(f'lzmly的爱好数量{len(dict_hobbies["lzmly"])}')
# for list_hobits in dict_hobbies.values():
#     for hobit in list_hobits:
#         print(hobit)