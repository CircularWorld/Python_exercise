'''
5. 在终端中循环录入年龄,如果录入空,则退出循环.
   最后打印平均年龄(总年龄除以人数)
'''
sum_age= 0
count =0
while True:
    age = input('请输入年龄：')
    if age:
        if age.isdigit():
            count += 1
            sum_age+=int(age)
        else:
            print('输入有误，请重新输入')
            continue
    else:
        break
print("平均年龄为: %.2f" % (sum_age/count))