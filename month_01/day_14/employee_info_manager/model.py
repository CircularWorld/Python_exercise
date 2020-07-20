class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name  # 姓名
        self.money = money  # 薪资