class Grandfather:
    def play(self):
        print("AAA")


class Father(Grandfather):
    pass


class Son(Father):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'名字"{self.name}",{self.age})'

    def __repr__(self):
        return f'Son("{self.name}",{self.age})'

son = Son("小明",8)
son_01 = eval(son.__repr__())
# son_01.name = "小红"
print(son_01)
while True:
    eval(input("命令："))

