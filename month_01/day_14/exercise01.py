"""
3. 参照student_info_manager.py完成员工管理系统.
    class EmployeeModel:
        def __init__(self, eid=0, did=0, name="", money=0.0):
            self.eid = eid # 员工编号
            self.did = did # 部门编号
            self.name = name # 姓名
            self.money = money # 薪资
    (选做)完成修改功能
"""


# 4.将employee_info_manager.py分解为四个模块
class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0, sid=0):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name  # 姓名
        self.money = money  # 薪资
        self.sid = sid


# 入口
class EmployeeView(object):
    def __init__(self):
        self.__employee_controller = EmployeeController()

    def __display_memu(self):
        print("1) 添加员工信息")
        print("2) 查看员工信息")
        print("3) 删除员工信息")
        print("4) 修改员工信息")

    def __selet_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_employee()
        elif item == "2":
            self.__show_employee()
        elif item == "3":
            self.__delete_employee()

    def main(self):
        while True:
            self.__display_memu()
            self.__selet_menu()

    def __input_employee(self):
        employee = EmployeeModel(1,1,1,1)
        # employee.eid = int(input("请输入员工编号："))
        # employee.did = int(input("请输入部门编号："))
        # employee.name = input("请输入员工姓名：")
        # employee.money = float(input("请输入员工薪资："))
        self.__employee_controller.add_employee(employee)

    def __show_employee(self):
        for employee in self.__employee_controller.list_employee:
            print(f"{employee.name}的部门编号是：{employee.did},员工编号是：{employee.eid},薪资是：{employee.money}.")

    def __delete_employee(self):
        remove_eid = int(input("请输入你要删除的员工编号"))
        if self.__employee_controller.remove_employee(remove_eid):
            print("删除成功")
        else:
            print("删除失败")


class EmployeeController:
    def __init__(self):
        self.__start_sid = 1001
        self.__list_employee = []

    @property
    def list_employee(self):
        return self.__list_employee

    def add_employee(self, employee):
        employee.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_employee.append(employee)

    def remove_employee(self, remove_eid):
        for employee in self.__list_employee:
            if employee.eid == remove_eid:
                self.__list_employee.remove(employee)
                return True
        return False


employee = EmployeeView()
employee.main()
