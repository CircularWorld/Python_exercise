'''
10.(选做)彩票模拟器
    双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝球：1个,1--16之间（包含）
    提示：列表就是彩票(前六个元素就是红球)
        -- 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)
        -- 在终端中购买彩票(提示：号码已经存在,号码超过范围)
'''
import random
list_lottery_ticket = []
list_all_ticket = []
list_user_ticket = []
count = 0
while len(list_lottery_ticket) < 6:
    number = random.randint(1, 33)
    if number not in list_lottery_ticket:
        list_lottery_ticket.append(number)
        count += 1
list_lottery_ticket.append(random.randint(1, 16))
print(list_lottery_ticket)
list_all_ticket = [list_lottery_ticket]
count = 0
while count < 7:
    if count < 6:
        red_number = int(input(f'请输入第{count + 1}个红球:'))
        if red_number in range(1, 34)and red_number not in list_user_ticket:
            list_user_ticket.append(red_number)
            count += 1
    elif count == 6:
        bule_number = int(input(f'请输入蓝球:'))
        if bule_number in range(1, 17):
            list_user_ticket.append(bule_number)
            print(f"您的彩票号码{list_user_ticket}")
            if list_user_ticket in list_all_ticket:
                print("号码已经存在")
            exit()
    else:
        print("号码超过范围")
        break
