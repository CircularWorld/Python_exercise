from typing import List

from model import EmployeeModel


class EmployeeControl:
    """
    逻辑控制
    """

    def __init__(self):
        self.__list_employees = []  # type: List[EmployeeModel]
        self.__start_eid: int = 1001

    @property
    def list_employees(self):
        return self.__list_employees

    @list_employees.setter
    def list_employees(self, value):
        self.__list_employees = value

    def add_employee(self, employee: EmployeeModel):
        employee.eid = self.__start_eid
        self.__list_employees.append(employee)
        self.__start_eid += 1

    def remove_employee(self, eid):
        for employee in self.list_employees:
            if eid == employee.eid:
                self.list_employees.remove(employee)
                return True
        return False

    def change_employee(self, employee : EmployeeModel):
        for item in self.list_employees:
            if employee.eid == item.eid:
                item.name = employee.name
                item.money = employee.money
                item.did = employee.did
                return True
        return False
