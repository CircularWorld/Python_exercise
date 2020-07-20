'''
4. 将列表中的数字累乘
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   结果：806400
'''
product_num = 1
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
for num in list02:
    product_num *= num
print(product_num)
