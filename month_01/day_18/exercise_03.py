"""
练习:使用装饰器，为旧功能增加新功能(验证权限).
"""


# 验证权限
# def insert():
#     print("插入成功")
#
#
# def delete():
#     print("删除成功")
#
#
# insert()
# delete()
# """
# 练习:使用装饰器，为旧功能增加新功能(验证权限).
# """
def add_func(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper


# 验证权限
@add_func
def insert():
    print("插入成功")


def delete():
    print("删除成功")


insert()
delete()
