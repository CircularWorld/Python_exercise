"""
增加新功能 ->验证权限
def 函数装饰器名称(func):
   def 内嵌函数(*args, **kwargs):
       需要添加的新功能
       return func(*args, **kwargs)
return内嵌函数
"""

def check_permission(func):
    def wapper(*args, **kwargs):
        print("验证权限", func.__name__)
        return func(*args, **kwargs)

    return wapper

@check_permission
def insert(data):
    print("插入成功",data)
    return 'ok'


@check_permission
def delete(id):
    print("删除成功",id)
    return 'yes'


res = insert("10条")
print(res)
res= delete(1)
print(res)
