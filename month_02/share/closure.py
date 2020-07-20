"""
闭包
    字面意思: 封闭(保存外部函数)内存空间(栈帧)
    内部函数,可以在外部函数执行后,访问其变量

三要素：
-- 必须有一个内嵌函数。
-- 内嵌函数必须引用外部函数中变量。
-- 外部函数返回值必须是内嵌函数。

3.定义：是由函数及其相关的引用环境组合而成的实体。
4.优点：内部函数可以使用外部变量。
5.缺点：外部变量一直存在于内存中，不会在调用结束后释放，占用内存。
6.作用：实现python装饰器。
什么是装饰器和闭包
技术点分析

"""

def func1():
    a =10
    def func2():
        nonlocal a
        a+=1
        print(a)

    return func2

res = func1()
res()
res()
res()
res()



# def func1():
#     a = 10 #
#
#     def func2():
#         nonlocal a
#         a +=1
#         print(a)
#
#     return func2
# result= func1()
#
# result()
# result()
# result()
