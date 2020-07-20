unit_price = float(input('请输入单价: '))
amount = int(input('请输入数量：'))
money = float(input('请输入支付金额：'))
return_money = money - amount * unit_price
if return_money > 0:
    print('找您%.2f元' % return_money)
elif return_money < 0:
    print('请在支付%.2f元' % -return_money)
else:
    print("欢迎光临")
