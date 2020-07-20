"""
    古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""
def calculate_weight(liang_amount):
    """
    计算重量
    :param liang_amount:输入要转化重量
    :return: 返回 斤和两元组
    """
    jin = liang_amount // 16
    liang = liang_amount % 16
    return jin,liang
