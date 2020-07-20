from common.iterable_tools import ItarableHelp


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9007, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# def find_all(func):
#     for emp in list_employee:
#         # if emp.money >= 15000:
#         if func(emp):
#             yield emp

def condition01(emp):
    return emp.money >= 15000


def condition02(emp):
    return emp.name == "魏鑫珑"


for item in ItarableHelp.find_all(list_employee, condition01):
    print(item.__dict__)



for item in ItarableHelp.find_all(list_employee, condition02):
    print(item.__dict__)




