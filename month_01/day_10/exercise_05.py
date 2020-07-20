class Mouse:
    def __init__(self, brand, price, weight, color):
        self.brand = brand
        self.price = price
        self.weight = weight
        self.color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if len(value) < 6:
            self.__brand = value
        else:
            raise Exception("brand input error ")

    @property
    #  price = property(读取函数)
    #  (1) 创建属性对象property()
    #  (2) 将下面的函数作为参数property(读取函数)
    #  (3) 将属性对象交给变量名关联price
    def price(self):
        return self.__price

    # price.setter(设置函数)
    # (1) 调用属性的setter函数
    # (2) 将下面的函数作为参数setter(设置函数)
    @price.setter
    def price(self, value):
        if 0 <= value <= 10000:
            self.__price = value
        elif value < 0:
            self.__price = 0
        elif value > 10000:
            self.__price = 10000
        else:
            raise Exception("price input error")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 100 <= value <= 1000:
            self.__weight = value
        else:
            raise Exception("weight input error")


mouse01 = Mouse("phip",1000,800,"白色")
print(mouse01.__dict__)
