"""
面相对象
    小明吃炸鸡，红烧肉（口感味道各有风味），
       面向对象：考虑问题从对象的角度出发
            识别对象   分配职责   建立交互
        三个特征：
            封装：分而治之,变则疏之      [分]
            继承：抽象、统一、隔离变化   [隔]
            多态：体现子类个性(变化)    [做]
        六个原则：
            开闭原则：能够增加新功能,不修改客户端代码.
            单一职责：小而精,有且只有一个改变的原因
            依赖倒置：使用抽象(爸爸),不适用具体(儿子)
            组合复用：优先使用组合关系,不是继承关系.
                继承：统一变化(交通工具约束火车汽车在

"""
class XiaoMing:
    def __init__(self):
        pass
    def eat(self,food):
        print("我开动了")
        food.taste()
        pass

class Food:
    def __init__(self, name=''):
        self.name = name

    def taste(self):
        pass

class SoyMilk(Food):
    def __init__(self, name=''):
        super().__init__(name)

    def taste(self):
        super().taste()
        print(f"{self.name}好浓好甜")

class RoastDuck(Food):
    def __init__(self, name=''):
        super().__init__(name)

    def taste(self):
        super().taste()
        print(f"{self.name}香气四溢，肥而不腻")

mil  =SoyMilk("豆浆")
kaya  =RoastDuck("烤鸭")

xiaoming  =XiaoMing()
xiaoming.eat(mil)
xiaoming.eat(kaya)