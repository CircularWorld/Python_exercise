# -- 定义函数, 删除列表中价格大于1w的商品
# -- (选做)
# 定义函数, 删除列表中商品名称相同的商品(不使用其他容器, 自定义算法)

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
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]
# -- 定义函数, 删除列表中价格大于1w的商品
def del_commodity_price_gt_1w():
    for r in range(len(list_commodity_infos)-1,-1,-1):
        if list_commodity_infos[r].price >10000:
            del list_commodity_infos[r]

def del_commodity_same_name():
    for r in range(len(list_commodity_infos) - 1, 0, -1):
        for c in range(r):
            if list_commodity_infos[r].name == list_commodity_infos[c].name:
                del  list_commodity_infos[r]
                break

def print_single_commodity_info(item):
    print(item.cid, item.name, item.price)

def print_all_commodity_infos():
    for item in list_commodity_infos:
        print_single_commodity_info(item)


# print_all_commodity_infos()
del_commodity_same_name()
print_all_commodity_infos()
# del_commodity_price_gt_2w()
# print_all_commodity_infos()