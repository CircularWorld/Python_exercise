confirm_people = int(input('请输入确诊人数：'))
cure_people = int(input('请输入治愈人数:'))
cure_ratio = confirm_people / cure_people
print('治愈比例' + str(cure_ratio * 100) + '%')
