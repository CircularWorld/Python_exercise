class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]


def print_single_commodity(commodity):
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


# 1.定义函数,打印所有商品信息,
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)


# print_commodity_infos()

# 2.  定义函数,打印商品单价小于2万的商品信息
def print_commodity_infos_lt_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)

# print_commodity_infos_lt_2w()
# 3. 查找最贵的商品(使用自定义算法,不使用内置函数)
def get_max_price_commodity():
    max_commodity = list_commodity_infos[0]
    for i in range(1,len(list_commodity_infos)):
        if max_commodity.price < list_commodity_infos[i].price:
            max_commodity = list_commodity_infos[i]
    return max_commodity

max_commodity = get_max_price_commodity()
# print_single_commodity(max_commodity)
print(max_commodity.__dict__)
# 4. 根据单价对商品列表降序排列
def sort_decrease_by_price():
    for r in range(len(list_commodity_infos)-1):
        for c in range(r+1,len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r],list_commodity_infos[c] = list_commodity_infos[c],list_commodity_infos[r]

# sort_decrease_by_price()
# print_commodity_infos()
# 订单列表
class Order:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count

list_orders = [
    Order(1001,1),
    Order(1002,3),
    Order(1005,2),
]
# def print_order_commodity_infos():
#     for
