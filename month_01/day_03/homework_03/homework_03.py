'''
(3) 如果是vip客户,消费小于等于500,享受85折
                消费大于500,享受8折
    如果不是vip客户,消费大于等于800,享受9折
                  消费小于800,原价
    在终端中输入账户类型,消费金额,计算折扣.
'''
money  = float(input('消费金额为：'))
if money:
    vip = input('是否是ＶＩＰ(Y/N):')
    if vip == 'Y':
        discount = 0.85 if money <= 500 else 0.8
    elif vip == 'N':
        discount = 0.9 if money >= 900 else 1
    else:
        print('请选择是否为ｖｉｐ')
        exit()
    print('折扣为%d折' % (discount * 10))
else:
    print('价格输入有误')


