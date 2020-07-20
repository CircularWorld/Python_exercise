import random
num = random.randint(1,100)
count =0
print(num)
while count <3:
    count +=1
    user_num = input('请输入一个数：')
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num ==num:
            print('恭喜')
            break
        elif user_num < num:
            print('猜小了')
        else:
            print('猜大了')
    else:
        print('输入有误请输入１～１００之间的整数')
else:
    print('游戏失败')

# import random
# num = random.randint(1,100)
# count = 0
# print(num)
# while count <3:
#     user_num = 50
#     if user_num ==num:
#         print('恭喜')
#         break
#     elif user_num < num:
#         print('猜小了')
#         user_num = (max -50)/2
#         max = user_num
#     else:
#         print('猜大了')
# else:
#     print('输入有误请输入１～１００之间的整数')