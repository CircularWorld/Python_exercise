class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃")

class Dog(Animal):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        # super().__init__(name)

class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)

dog_01 = Dog("泰德","red")
print(dog_01.name,dog_01.color)
bird_01 = Bird("红日")
anim = Animal("bird")

# dog_01.eat()
# bird_01.eat()
# anim.eat()
# print(isinstance(dog_01, Dog))
# print(isinstance(dog_01, Bird))
# print(isinstance(dog_01, Animal))
# print(issubclass(Dog, Animal))
# print(issubclass(Dog, Dog))
# print(issubclass(Dog, Bird))
# print(type(dog_01) == Dog)
# print(type(dog_01) == Animal)
# print(type(dog_01) == Bird)
