"""
    １　识别对象
    ２　分配职责
    ３　建立职责
小明请保洁打扫对象
"""
#1
class Student:
    def __init__(self,name):
        self.name = name

    def let(self):
        work = Worker()
        print("请")
        work.clea()

class Worker:
    def __init__(self):
        pass
    def clea(self):
        print("打扫")

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.work = Worker()
#
#
#     def let(self):
#         print("请")
#         self.work.clea()
#
# class Worker:
#     def __init__(self):
#         pass
#
#     def clea(self):
#         print("打扫")
#3
class Student:
    def __init__(self, name):
        self.name = name

    def let(self,work):
        print("请")
        work.clean()

class Worker:
    def __init__(self):
        pass

    def clea(self):
        print("打扫")
#
# lx = Student("小明")
# work  = Worker()
# lx.let(work)


