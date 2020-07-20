'''
7. 赌大小游戏
    玩家的身家初始10000，实现下列效果：
        少侠请下注: 30000
        超出了你的身家，请重新投注。
        少侠请下注: 8000
        你摇出了5点,庄家摇出了3点
        恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
        少侠请下注: 18000
        你摇出了6点,庄家摇出了6点
        打平了，少侠，在来一局？
        少侠请下注: 18000
        你摇出了4点,庄家摇出了6点
        少侠,你输了，身家还剩 0
        哈哈哈，少侠你已经破产，无资格进行游戏
'''
import random

property = 10000
while property:
    bet_num = input('少侠请下注:')
    if bet_num.isdigit() and int(bet_num) > property:
        print("超出了你的身家，请重新投注。")
        continue
    bet_num = int(bet_num)
    you_dice = random.randint(1, 6)
    dealer_dice = random.randint(1, 6)
    print('''你摇出了%d点,庄家摇出了%d点''' % (you_dice, dealer_dice))
    if you_dice > dealer_dice:
        property += bet_num
        print('恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩%d' % property)
    elif you_dice == dealer_dice:
        print('''打平了，少侠，在来一局？''')
    else:
        property -= bet_num
        print('少侠,你输了，身家还剩 %d' % property)
else:
    print("""哈哈哈，少侠你已经破产，无资格进行游戏""")
