'''
(选做) 老王很不幸,买了一箱有虫子(1只)的苹果
    虫子吃完一个苹果再吃另外一个苹果
    在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
    请打印没有被虫子吃过的苹果数量（整数,最小也是0）
'''
while True:
    sum_apple = input('请输入苹果数量:')
    if sum_apple.isdigit():
        sum_apple = int(sum_apple)

        time = float(input('请输入经过的时间h:'))
        if time >= 0:
            speed = float(input('请输入虫子吃的速度小时/个:'))
            if speed >= 0:
                remain_apple = 0 if time > sum_apple \
                    else int(sum_apple - time*speed)
                print('剩余%d个苹果' % remain_apple)
                break
            else:
                print('虫子速度输入错误')

        else:
            print('请输入正确的时间')
    else:
        print('请输入正确的数量')