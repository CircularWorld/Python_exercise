class Mobile:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
    def tell(self,name):
        print(self.brand,name)

mob_01 = Mobile("魅族","3200","银白")
mob_01.tell("不知火舞")
mob_02 = Mobile("华为","4200","漆黑")
mob_02.tell("草稚京")