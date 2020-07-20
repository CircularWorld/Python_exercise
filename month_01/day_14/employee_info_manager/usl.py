from bll import EmployeeControl
from model import EmployeeModel


class EmployeeView:

    def __init__(self):
        self.__control = EmployeeControl()

    def __display_menu(self):
        print("1:添加员工信息")
        print("2:查看员工信息")
        print("3:删除员工信息")
        print("4:修改员工信息")

    def __select_menu(self):
        select = input("请输入你的选择:")
        if select == '1':
            self.__input_employee_info()

        elif select == '2':
            self.__show_employee_info()

        elif select == '3':
            self.__del_employee()
            pass
        elif select == '4':
            self.__modify_employee()
            pass

    def __input_employee_info(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工姓名:")
        employee.money = int(input("请输入员工工资:"))
        employee.did = int(input("请输入员部门编号:"))
        self.__control.add_employee(employee)

    def __show_employee_info(self):
        for employee in self.__control.list_employees:
            print(f"{employee.name}的员工编号为:{employee.eid},员工工资:{employee.money}元,部门编号：{employee.did}")

    def __del_employee(self):
        eid = int(input("请输入要删除员工的员工编号:"))
        if self.__control.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee = EmployeeModel()
        employee.eid = int(input("请输入需要修改的员工编号："))
        employee.name = input("请输入需要修改的员工姓名：")
        employee.did = int(input("请输入需要修改的部门编号："))
        employee.money = int(input("请输入需要修改的员工薪资："))
        if self.__control.change_employee(employee):
            print("修改成功")
        else:
            print("修改失败")
        pass

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
