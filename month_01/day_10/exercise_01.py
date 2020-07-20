'''
创建狗类
数据：品种、爱称、年龄、体重
行为：吃、叫
实例化两个对象并调用其方法
'''
class Dog:
    """
    variety, 品种、
    pet_name,爱称、
    age,年龄、
    weight体重
    eat(self)吃、
    woof(self)叫
    """
    def __init__(self, variety, pet_name, age, weight):
        self.variety = variety
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

    def eat(self):
        print(self.pet_name,"肉肉")

    def woof(self):
        print(self.pet_name,"汪汪汪")

dog_01 = Dog("土狗","憨批","91","12")
dog_01.eat()
dog_01.woof()

