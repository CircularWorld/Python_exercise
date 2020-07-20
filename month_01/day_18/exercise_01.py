"""
练习1需求:
在员工列表中,查找删除薪资15000以内的所有员工
在员工列表中,查找删除部门编号是9005的所有员工

步骤
$1. 定义函数,完成需求.
x2. 将变化点定义为函数
将通用代码定义为函数
x3. 通用函数使用参数隔离变化点
$4. 在IterableHelper类中创建通用函数
$5. 在当前模块中调用通用函数(lambda)
"""
from iterable_tools import IterableHelper


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
    EmployeeModel(1004, 9004, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

# IterableHelper.del_all(list_employee, lambda emp: emp.money < 15000)

# for employee in list_employee:
#     print(employee.__dict__)
# count = IterableHelper.del_all(list_employee, lambda emp: emp.did == 9005)

# for employee in list_employee:
#     print(employee.__dict__)



# max_employe = IterableHelper.get_max(list_employee, lambda emp: emp.money)
# print(max_employe.__dict__)
# print(IterableHelper.get_max(list_employee, lambda emp: emp.eid).__dict__)

# IterableHelper.ascending_order(list_employee, lambda emp: emp.money)
IterableHelper.ascending_order(list_employee, lambda emp: emp.eid)
for employee in list_employee:
    print(employee.__dict__)

sorted(list_employee,key= lambda emp:True)

