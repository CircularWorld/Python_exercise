"""
    python 高级
        装饰器 - 拦截
        导入模块/包
            方式:
                import 模块名 -- 本质就是通过变量(模块名)访问其他模块
                from 模块名 import 成员 -- 本质是将其他模块导到当前作用域中
            是否成功唯一标准:
                导入路径 + sys.path = 真实路径
                sys.path 是列表,存放所有导入搜索路径.
                根目录:主模块所在文件夹
                主模块:第一次运行的文件
        异常处理
            适用性:针对运行时的逻辑错误(数据范围),不是语法错误.
            现象:不断向上返回,不再向下执行.
            价值:保障程序可以按照既定流程处理
            语法:
                try:
                    可能出错的代码
                except 错误类型:
                    处理逻辑
        生成器
            惰性/延迟操作
                循环一次,计算一次,返回一个
                不建立容器存储所有数据

            生成器函数
                适用性:函数返回多个结果
                语法:
                    def 函数名():
                        ...
                        yield 数据

                    for item in 函数名():
                        print(item)
            生成器表达式
                语法:
                    (item for item in 可迭代对象)

"""
list01 = [4, 45, 5, 6, 7]
for item in list01:
    print(item)

# iterator = list01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#     except StopIteration:
#         break


# 外函数负责接收旧功能
# 内函数负责包裹新旧功能
# 闭包:逻辑连续(从一次接收到多次包裹)
def verif_permissions(func):
    def wrapper(*args, **kwargs):  # 合并insert(1,2, p3=3,p4=4)传入的信息
        print("验证权限")
        return func(*args, **kwargs)  # 拆后与旧功能对应

    return wrapper


@verif_permissions(10)  # 一次接收
def insert(p1, p2, p3, p4):
    print(p1, p2, p3, p4)


# 多次包裹
insert(1, 2, p3=3, p4=4)  # 调用的是内部函数
insert(1, 2, p3=3, p4=4)
insert(1, 2, p3=3, p4=4)
