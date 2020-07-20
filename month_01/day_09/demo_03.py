"""
＊号元祖形参
    形参只有一个
    只支持位置
"""
def func01(*args):
    print(args)

list01 = [1,23,4]
func01()
func01(list01)

def func02(*args,p1 =1,p2 =3):
    print(args)
    print(p1)
    print(p2)

func02()