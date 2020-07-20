"""
    函数参数
        实际参数
            １．位置参数　实参按照位置与形参对应
            2．关键字实参：实参按照名称与形参对应
"""


def func01(p1, p2, p3):
    """
    我是函数
    :param p1: 第一个参数
    :param p2:
    :param p3:
    :return:
    """
    print(p1)
    print(p2)
    print(p3)


func01(1, 2, 3)
# ctrl+p 查看参数
# ctrl+q　查看文档
# func01(1,2)
# TypeError: func() missing 1 required positional argument: 'p3'
# func01(1,2,3,4)
# TypeError: func() takes 3 positional arguments but 4 were given

func01(p1=1, p2=2, p3=3)

