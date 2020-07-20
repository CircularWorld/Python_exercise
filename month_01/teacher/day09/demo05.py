"""
    函数参数 - 总结
        实际参数：对应
            1.位置实参：顺序
                函数名(数据1,数据2,数据3)
                3. 序列实参：拆
                    函数名(*序列)
            2.关键字实参：名字
                函数名(参数名2=数据2)
                4. 字典实参：拆
                    函数名(**字典)

        形式参数：约束
            1. 默认形参：可选
                def 函数名(参数名1 = 数据1,参数名2=数据2)
            2. 位置形参：必填
                def 函数名(参数名1,参数名2,参数名3)
            3. 命名关键字形参：必须是关键字实参
                def 函数名(*,参数名1,参数名2)
                def 函数名(*args,参数名1,参数名2)
            4. 不定长形参：长度无限
                4.1 星号元组形参：合并位置实参
                    def 函数名(*args)
                4.2 双星号字典形参：合并关键字实参
                    def 函数名(**kwargs)

"""

def func01(p1=0, p2=1, p3=2):
    print(p1)
    print(p2)
    print(p3)


func01(p1="a", p2="b", p3="c")


def func02(*,p1,p2):
    print(p1)
    print(p2)

func02(p1 =1,p2 = 2)