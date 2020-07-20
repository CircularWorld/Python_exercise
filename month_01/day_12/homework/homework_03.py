"""
    (1). 创建父子类,添加实例变量
            创建父类:人(姓名,年龄)
            创建子类:学生(成绩)
    (2). 创建父子对象,直接打印.
            格式: 我是xx,今年xx.
                 我是xx,今年xx,成绩是xx.
    (3). 通过eval + __repr__拷贝对象,
         修改拷贝前对象的实例变量,
         打印拷贝后对象的实例变量.
"""
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'我是{self.name},今年{self.age}'

class Student(People):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score

    def __str__(self):
        return f'我是{self.name},今年{self.age},成绩是{self.score}'

    def __repr__(self):
        return f'Student("{self.name}",{self.age},{self.score})'
p1 = People("夏明",10)
stu1 = Student("夏雨",30,99)
stu1.name = "刘星"
print(p1)
print(stu1)
stu2 = eval(stu1.__repr__())
print(stu2)