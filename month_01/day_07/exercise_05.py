"""
列表推导式嵌套　
请排列出所有扑克牌(大小王不算,使用列表存储)
["红桃","黑桃","方片","梅花"]
["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
"""
list_type = ["红桃", "黑桃", "方片", "梅花"]
list_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

list_card = [(r,c) for r in list_type for c in list_num]
print(list_card)

# list_pattern = ["红桃", "黑桃", "方片", "梅花"]
# list_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#
# list_card = [(r, c) for r in list_pattern for c in list_num]
# print(list_card)
