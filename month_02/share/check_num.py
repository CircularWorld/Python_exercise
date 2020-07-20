"""
装饰器 判断函数接收的参数是整数

isinstance(对象, 类型)
返回指定对象是否是某个类的对象。
issubclass(类型，类型)
返回指定类型是否属于某个类型。
type(对象)返回类型
"""
# def requires_ints(func):
#     def wapper(*args,**kwargs):
#         # 先得到传入参数
#         kwargs_values = [i for i in kwargs.values()]
#         for num in list(args)+kwargs_values:
#             #判断一个对象是否是某个类的对象
#             # if not isinstance(num,int):
#             if type(num) != int:
#                 raise TypeError(func.__name__+'传入参数不是整数')
#         return func(*args,**kwargs)
#
#     return wapper
#
# @requires_ints
# def set_age(num):
#     age = num
#     return age
#
#
# print(set_age(3.3))

def check_num(func):
    def wapper(*args,**kwargs):
        #添加新功能
        kwargs_list =[i for i in kwargs.values()]
        for num in list(args)+kwargs_list:
            # if type(num)!=int:
            if not isinstance(num,int):
                raise TypeError(func.__name__+'传入参数不是整数')
        return func(*args,**kwargs)

    return wapper

@check_num
def set_age(num):
    age = num
    print(age)

set_age(3)


# res = check_num(set_age)
# res(3)
