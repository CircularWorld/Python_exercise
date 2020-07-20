'''
4. 在终端中循环录入5个人的年龄,
   最后打印平均年龄(总年龄除以人数)
'''
sum_age= 0
for __ in range(5):
    age = input('请输入年龄：')
    if not age.isdigit():
        print('输入有误')
        exit()
    sum_age+=int(age)
print(f"平均年龄为: {sum_age}")