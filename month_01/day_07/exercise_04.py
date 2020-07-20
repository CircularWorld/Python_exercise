# 商品字典
dict_commodity_infos = {
1001: {"name": "屠龙刀", "price": 10000},
1002: {"name": "倚天剑", "price": 10000},
1003: {"name": "金箍棒", "price": 52100},
1004: {"name": "口罩", "price": 20},
1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
{"cid": 1001, "count": 1},
{"cid": 1002, "count": 3},
{"cid": 1005, "count": 2},
]

# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.
for cid,info in dict_commodity_infos.items():
    print(f'商品编号:{cid} 商品名称:{info["name"]} 商品单价:{info["price"]}')
    # print(item.items())
# 2. 打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
for order in list_orders:
    print(f'商品编号:{order["cid"]} 购买数量:{order["count"]}')

# 3. 打印商品单价小于2万的商品信息
# 格式：商品编号xx,商品名称xx,商品单价xx.

for cid,info in dict_commodity_infos.items():
    if info["price"] <20000:
        print(f'商品编号:{cid} 商品名称:{info["name"]} 商品单价:{info["price"]}')


# 4. 打印所有订单中的商品信息,
# 格式：商品名称xx,商品单价:xx,数量xx.

for order in list_orders:
    name = dict_commodity_infos[order["cid"]]["name"]
    price = dict_commodity_infos[order["cid"]]["price"]
    print(f'商品名称 {name},商品单价:{price},数量{order["count"]}')
    # print(f'商品编号:{order["cid"]} 购买数量:{order["count"]}')
# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
max_order = list_orders[0]
for i in range(1,len(list_orders)):
    if max_order["count"] < list_orders[i]["count"]:
        max_order = list_orders[i]
print(f"查找数量最多的订单:{max_order['cid']}")
'''
排序核心思想
确定第一个元素是最大值
确定第二个元素是最大值
确定第三个元素是最大值
．．．
确定倒第二个元素是最大值
'''
'''
方法
1.取出前几个数据(不要最后一个)
2.与后面元素进行比较
3.发现更xx则交换(取出的   比较的)
'''
for r in range(len(list_orders)-1):#取值
    for c in range(r+1,len(list_orders)):#
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r]["count"],list_orders[c]["count"] = list_orders[c]["count"],list_orders[r]["count"]
print(list_orders)