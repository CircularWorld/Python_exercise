"""
    选择语句
            if 条件1:
                满足条件1执行的语句

            if 条件2:
                满足条件2执行的语句
            else:
                不满足条件2执行的语句

        写法2：
            if 条件1:
                满足条件1执行的语句
            elif 条件2:
                不满足条件1,但满足条件2执行的语句
            else:
                以上条件都不满足
    调试Debug
        让程序中断,逐语句执行,审查程序执行过程以及
        变量的取值( 找错误的过程 )
        步骤：
            1. (在可能出错的行)加断点
            2. 开始调试Debug
            3. (待断点命中后)按下F8(执行下一句)
            .....
            4. 关闭程序ctrl + shift + f4
    练习:exercise04~
    修改名称的快捷键：shift + F6
"""
number = int(input("请输入数字："))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("零")