"""
1. 打印下列类的对象
xx车的速度是xx
编号xx的商品名称是xx,单价xx
xx鼠标单价xx,宽xx,颜色xx
2. 拷贝下列类的对象,
修改拷贝前对象实例变量,
打印拷贝后对象.
"""


class Car:
    def __init__(self, bread="", speed=0):
        self.bread = bread
        self.speed = speed

    def __str__(self):
        return f"{self.bread}车的速度是{self.speed}"

    def __repr__(self):
        return f'Car("{self.bread}",{self.speed})'

class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"编号{self.cid}的商品名称是{self.name},单价{self.price}"

    def __repr__(self) -> str:
        return super().__repr__()


class Mouse:
    def __init__(self, brand, unit_price, weight, colour):
        self.brand = brand
        self.unit_price = unit_price
        self.weight = weight
        self.colour = colour

    def __str__(self):
        return f"{self.brand}鼠标单价{self.unit_price},宽{self.weight},颜色{self.colour}"


    def __repr__(self):
        return f'Mouse("{self.brand}",{}{}{})'
    """
        1. 打印下列类的对象
        xx车的速度是xx
        编号xx的商品名称是xx,单价xx
        xx鼠标单价xx,宽xx,颜色xx
        2. 拷贝下列类的对象,
        修改拷贝前对象实例变量,
        打印拷贝后对象.
        """
car = Car("QQ",100)
car_01 = eval(car.__repr__())
car_01.speed = 120
car_01.bread = "路虎"
car.speed = 200
print(car)
print(car_01)

mouse = Mouse("Philips",50,0.2,"白色")
print(mouse)
    # f"{self.brand}鼠标单价{self.unit_price},宽{self.weight},颜色{self.weight}"