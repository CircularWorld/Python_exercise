class Commodity:
    def __init__(self, cid, name="", price=""):
        self.cid = cid
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.cid == other.cid

    def __lt__(self, other):
        return self.price < other.price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]

print(list_commodity_infos.index(Commodity(1001)))

print(Commodity(1001) in list_commodity_infos)

list_commodity_infos.sort()
print(list_commodity_infos)
# print(max(list_commodity_infos).__dict__)
# list_commodity_infos.remove(Commodity(1003))
# print(list_commodity_infos)
