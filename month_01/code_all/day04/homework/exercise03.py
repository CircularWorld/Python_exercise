"""
    商品优惠
    打折策略：如果vip客户，消费小于500,享受85折
                        否则享受8折
            否则，消费大于800,享受9折
                 否则原价
    根据账户类型和消费金额，计算折扣.
"""
def calculate_discount(vip,money):
    """
    计算购买商品折扣
    :param vip: vip信息
    :param money:消费金额
    :return:折扣
    """
    if vip == 'vip':
        return 0.85 if money < 500 else 0.8
    return 0.9  if money > 800 else 1

account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))
print(calculate_discount(account_type,money))