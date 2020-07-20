# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


# --1.定义函数,打印所有商品信息,
# --格式：商品编号xx,商品名称xx,商品单价xx.
# --
def print_commodity_infos():
    """
    打印所有商品信息
    """
    for item in list_commodity_infos:
        print(f'商品编号{item["cid"]},商品名称{item["name"]},商品单价{item["price"]}.')


# --2.定义函数,打印商品单价小于2万的商品信息
# --
def print_commodity_infos_lt_2w():
    """
    打印商品单价小于2万的商品信息
    """
    for item in list_commodity_infos:
        if item["price"] < 20000:
            print(f'商品编号{item["cid"]},商品名称{item["name"]},商品单价{item["price"]}.')
# --3.定义函数,打印所有订单中的商品信息,
# --格式：商品名称xx,商品单价:xx,数量xx.
# --
def print_in_order_commodity_infos():
    """
    打印所有订单中的商品信息,
    """
    for order in list_orders:
        cid = order["cid"]
        for commodity_info in list_commodity_infos:
            if cid in commodity_info.values():
                # print('A',commodity_info.values())
                print(f"商品名称:{commodity_info['name']},商品单价:{commodity_info['price']},数量{order['count']}.")
                break #找到对应商品后跳出循环
print_in_order_commodity_infos()
# --4.定义函数,查找最贵的商品(使用自定义算法,不使用内置函数)
def get_most_expensive_commodity():
    """
    得到最贵的商品信息
    :return: 商品字典信息
    """
    most_commodity = list_commodity_infos[0]
    for i in range(1,len(list_commodity_infos)):
        if most_commodity["price"] < list_commodity_infos[i]["price"]:
            most_commodity = list_commodity_infos[i]
    return most_commodity

print(get_most_expensive_commodity())

# --
# --5.定义函数,根据单价对商品列表升序排列

def sort_commodity_by_increase():
    """
    根据价格对商品升序排列
    """
    for r in range(len(list_commodity_infos)-1):
        for c in range(r+1,len(list_commodity_infos)):
            if list_commodity_infos[r]["price"] > list_commodity_infos[c]["price"]:
                    list_commodity_infos[r],list_commodity_infos[c] = list_commodity_infos[c],list_commodity_infos[r]

sort_commodity_by_increase()
print(list_commodity_infos)
