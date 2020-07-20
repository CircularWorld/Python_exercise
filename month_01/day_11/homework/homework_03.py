"""
3. 通过属性限制数据范围,体会属性的继承
    父类：车(品牌，速度)
                 0-280
    创建子类：电动车(电池容量,充电功率)
                  0 - 50000  200 - 250
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 280:
            self.__speed = value
        elif value < 0:
            self.__speed = 0
        elif value > 280:
            self.__speed = 280
        else:
            raise Exception("speed data error")


class Bicycle(Car):
    def __init__(self, brand, speed, battery_capacity, power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.power = power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if 0 <= value <= 50000:
            self.__battery_capacity = value
        elif value < 0:
            self.__battery_capacity = 0
        elif value > 50000:
            self.__battery_capacity = 50000
        else:
            raise Exception("battery data error")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if 200 <= value<=250:
            self.__power= value
        elif value <200:
            self.__power = 200
        elif value > 250:
            self.__power = 250
        else:
            raise Exception("power data error")
    # 200 - 250
    # 父类：车(品牌，速度)
    #              0-280
    # 创建子类：电动车(电池容量,充电功率)
    #               0 - 50000  200 - 250

bic_01 = Bicycle("凤凰", 2, 60000, 260)
print(bic_01.__dict__)
print(bic_01.brand)
print(bic_01.speed)
print(bic_01.battery_capacity)
print(bic_01.power)
