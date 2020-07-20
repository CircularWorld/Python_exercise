"""
返回列表中所有数字的个位
方式1:传统思想
定义函数,创建列表,循环计算每个元素的个位,存入列表
方式2:生成器思想
定义函数,循环计算每个元素的个位,通过yield返回
体会:惰性操作/延迟操作/推算数据
"""



def get_num_list():
    return [num % 10 for num in list01]


def get_num_list_generator():
    for num in list01:
        yield (num % 10)

list01 = [54, 55, 36, 67, 28, 69, 90]
# list02 = get_num_list()
# print(list02)

result = get_num_list_generator()
print(result)
for item in result:
    print(item,end ='')
# print(list03)
