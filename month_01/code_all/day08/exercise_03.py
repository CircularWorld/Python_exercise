"""
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""
def change(unit_price,amount,money):
    result = money - unit_price * amount
    if result > 0:
        print('找您%.2f元' % return_money)
    elif result < 0:
        print('请在支付%.2f元' % -result)
    else:
        print("欢迎光临")
    return result
# 1. 获取数据
unit_price = float(input("请输入商品单价："))
amount = int(input("请输入购买的数量："))
money = float(input("请输入支付金额："))
result_money = change(unit_price,amount,money)
print("应该找回" + str(result_money))