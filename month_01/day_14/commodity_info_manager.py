"""
    参照student_info_manager.py完成商品管理系统
    1. 实现添加商品信息功能
        View -- 录入商品信息
        Controller -- 添加商品信息
    画出内存图
"""

class CommodityModel:
    def __init__(self, cid = 0, name = "", price=0):
        self.cid = cid
        self.name = name
        self.price = price

class CommodityView:
    """
        商品视图：负责处理界面逻辑
    """
    def __init__(self):
        self.__control = CommodityControl()

    def __display_menu(self):
        print("1:添加商品信息")
        print("2:显示商品信息")
        print("3:删除商品信息")
        print("4:修改商品信息")


    def __select_menu(self):
        item = input("请输入选项：")
        if item =="1":
            self.__input_Commodity()
        elif item =='2':
            self.__show_commodity()
        elif item =='3':
            self.__del_commodity()
        elif item =="4":
            self.__modify_commodity()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_Commodity(self):
        cod = CommodityModel()
        cod.__name = input("请输入商品名字：")
        cod.__price = input("请输入商品价格：")
        self.__control.add_commodity(cod)


    def __show_commodity(self):
        for commodity in self.__control.list_commodity:
            print(f'{commodity.__name}的价格是{commodity.__price},编号{commodity.cid}')

    def __del_commodity(self):
        cid = input_cid()
        self.__control.remove_commodity(cid)
        pass

    def __modify_commodity(self):
        cid = input_cid()
        self.__control.get_commodity(cid).__name = input("请输入商品名字：")
        self.__control.get_commodity(cid).__price = input("请输入商品价格：")


def input_cid():
    cid = int(input("请输入要修改的商品编号："))
    return cid

class CommodityControl:
    def __init__(self):
        self.__list_commodity = []
        self.__start_cid = 1001

    @property
    def list_commodity(self):
        return self.__list_commodity

    @list_commodity.setter
    def list_commodity(self):
        return self.__list_commodity


    def add_commodity(self,com):
        com.cid = self.__start_cid
        self.__start_cid+=1
        self.__list_commodity.append(com)

    def remove_commodity(self,del_cid):
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == del_cid:
                del self.list_commodity[i]
                return True
        return False


    def show_Commodity_info(self):
        for item in self.__list_commodity:
            print(f"{item.__dict__}")

    def get_commodity(self, cid):
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == cid:
                return self.list_commodity[i]



view = CommodityView()
view.main()