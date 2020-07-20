
# 练习1:使用迭代思想，打印元组中所有元素。
# 练习2:不使用for循环，打印字典中所有记录(键和值)
# tuple_num = (1,2,3,4,5,6,7)
# iter_num = tuple_num.__iter__()
# while True:
#     try:
#         print(iter_num.__next__(),end = " ")
#     except StopIteration:
#         break
dict_num = {1:"a",2:"b",3:'c'}
#获取可迭代对象
iterator = dict_num.items().__iter__()
while True:
    try:#获取下一个元素
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break