class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money
    def __lt__(self, other):
        return True if self.money < other.money else False

list_employee = [
EmployeeModel(1001, 9003, "林玉玲", 13000),
EmployeeModel(1002, 9003, "王荆轲", 16000),
EmployeeModel(1003, 9003, "刘岳浩", 11000),
EmployeeModel(1004, 9003, "冯舜禹", 17000),
EmployeeModel(1005, 9003, "曹海欧", 15000),
EmployeeModel(1006, 9003, "魏鑫珑", 12000),
]

# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# 2. 定义函数,在list_employee中查找员工编号为1005的员工

def find_money_gt_2w():
    for item in list_employee:
        if item.money >=15000:
            yield item

def find_eid_employee(eid):
    for item in list_employee:
        if item.eid == eid:
            return item

def print_employee(result):
    for employee in result:
        print(employee.__dict__)

# result = find_money_gt_2w()
# print_employee(result)
#
# result_02 = find_eid_employee(1005)
# print(result_02.__dict__)

# 3. 定义函数,在list_employee中查找所有员工的姓名
# 4. 定义函数,在list_employee中查找薪资最高的员工

def find_all_employees_name():
    for item in list_employee:
        yield item.name

def find_max_money_employee():
    max_employee = list_employee[0]
    for item in list_employee:
        if max_employee > item:
            max_employee = item
    return max_employee

names = find_all_employees_name()
for name in names:
    print(name)

print(find_max_money_employee().__dict__)