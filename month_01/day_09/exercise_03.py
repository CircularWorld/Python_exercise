"""
定义多个数值累乘
"""
def multiplicative(*args):
    result = 1
    print(args)
    for item in args:
        result *=item
    return result

list_01 = [1,2,34,5]
print(multiplicative(list_01))
print(multiplicative(1,2,3,4))
