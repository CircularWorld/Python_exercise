'''
11.
    (1).在终端中录入秒数,  80
       计算几分钟零几秒存入列表[分,秒]   [1,20]
'''
# sec = input('请输入秒数:')
# list_time = []
# if sec and sec.isdigit():
#     sec = int(sec)
#     list_time[:] =[sec//60,sec%60]
#     print(list_time)


'''
    (2).将第一步重复3次,将每个列表再存入列表
        请输入秒：80
        请输入秒：90
        请输入秒：100
        [[1, 20], [1, 30], [1, 40]]
'''
list_all_time = []
for __ in range(3):
    sec = input('请输入秒数:')
    list_time = []
    if sec and sec.isdigit():
        sec = int(sec)
        list_time =[sec//60,sec%60]
        # print(list_time)
        list_all_time.append(list_time)
print(list_all_time)
'''
    (3).打印第二步所有时间,一行一个,格式:x分零x秒
        1分零20秒
        1分零30秒
        1分零40秒
'''
for time in list_all_time:
    print(f'{time[0]}分零{time[1]}秒')