"""
    Python核心3
        函数参数
            实际参数:对应
                位置实参:按顺序
                关键字实参:按名字
            形式参数:
                位置形参:必填
                默认形参:可选
                星号元组形参:合 - 位置实参
                命名关键字形参:约束只能是关键字实参
                双星号字典形参:合 - 关键字实参
"""


# 位置形参:必填
def func01(p1, p2, p3):
    pass


# 位置实参:按顺序对应
func01(1, 2, 3)
list01 = ["a", "b", "c"]
func01(*list01)  # 拆

# 关键字实参:按名称对应
func01(p1=1, p2=2, p3=3)
dict01 = {"p1": "a", "p2": "b", "p3": "c"}
func01(**dict01)  # 拆


# 默认形参:可选
def func02(p1=0, p2="", p3=0.0):
    pass


func02()
func02(1, "b")
func02(p2="b")
func02(1, p3=3.0)


# 星号元组形参:合 - 位置实参
def func03(*args):
    print(args)  # (1, 2, 3, 4, 5)


func03(1, 2, 3, 4, 5)


# 命名关键字形参:约束只能是关键字实参
def func04(*args, a, b):
    pass


# sorted(__iterable,*,key,everse)
def func05(a, *, b=0):
    pass

func04(1, a=2, b=3)
# a属于主要必填数据,b属于特定环境下的修饰
func05(1, b=2)

# 双星号字典形参:合 - 关键字实参
def func06(**kwargs):
    pass
