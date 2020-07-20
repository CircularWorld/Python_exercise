class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Bicycle(Car):
    def __init__(self,brand,speed,battery_capacity,power):
        super().__init__(brand,speed)
        self.battery_capacity = battery_capacity
        self.power = power

bic_01 = Bicycle("凤凰",30,20000,2)
print(bic_01.brand)
print(bic_01.speed)
print(bic_01.battery_capacity)
print(bic_01.power)
