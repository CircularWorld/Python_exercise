"""
使用列表推导式生成1--50之间能被3或者5整除的数字
使用列表推导式生成5 -- 100之间的数字平方
"""

list_num = [number for number in range(1, 50) if number % 3 == 0 or number % 5 == 0]
print(list_num)

list_number_square = [value ** 2 for value in range(5, 101)]
print(list_number_square)
