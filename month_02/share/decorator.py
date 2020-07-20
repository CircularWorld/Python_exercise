'''
外部嵌套作用域
闭包
装饰器
内部函数返回值是旧函数的返回值
'''
def print_func_name(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper

@print_func_name
def func01():
    print("func01执行了")


func01()
func01()
func01()