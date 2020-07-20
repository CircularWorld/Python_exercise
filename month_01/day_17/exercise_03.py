# 练习1:在列表中获取所有整数,并计算它的平方.
# 练习2:在列表中获取所有大于10的小数.
# 要求：使用列表推导式，生成器表达式完成.
# 通过调试，体会差异.

list01 = [1, 'asd', 1.1, 10.7, 20.6, 10, 20]

list_result1 = [item for item in list01 if type(item) == int]
print(list_result1)

list_result1_g = (item for item in list01 if type(item) == int)
for item in list_result1_g:
    print(item)

list_result2 = [item for item in list01 if type(item) == float and item > 10]
print(list_result2)

list_result2_g = (item for item in list01 if type(item) == float and item > 10)
for item in list_result2_g:
    print(item)