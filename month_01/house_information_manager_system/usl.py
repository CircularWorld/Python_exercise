from bll import HouseManagerController
from common.iterable_tools import IterableHelper


class HouseView:
    def __init__(self):
        self.__control = HouseManagerController()

    def __display_menu(self):
        print("1:显示所有房源信息")
        print("2:显示总价格最大房子")
        print("3:显示总面积最小房子")
        print("4:显示房型数量")
        print("5:删除房子信息")
        print("6:对房子价格升序")

    def __select_menu(self):
        select = input_select("选项")
        if select == 1:
            self.__show_house_informaitin()
        elif select == 2:
            # house = self.__control.get_house_max_total_price()
            # house = IterableHelper.get_max(self.__control.get_house_list(),lambda house: house.total_price)
            house = max(self.__control.get_house_list(), key=lambda house: house.total_price)
            print(house.__dict__)
        elif select == 3:
            # house = self.__control.get_house_min_area()
            # house = min(self.__control.get_house_list(), key=lambda house: house.area)
            house = min(self.__control.get_house_list(), key=lambda house: house.id)
            print(house.__dict__)
        elif select ==4:
            print(self.__control.count_house_type())
            pass
        elif select == 5:
            id = input_select("房源编号")
            # if self.__control.del_house_by_id(id):
            if IterableHelper.del_single_by_info(self.__control.__list_houses, lambda house: house.id == id):
                print("删除成功")
            else:
                print("删除失败，没找到此房源")
        elif select == 6:
            self.__control.ascending_ording()
            for house in sorted(self.__control.__list_houses,key= lambda house:house.total_price):
                print(house.__dict__)


    def __show_house_informaitin(self):
        for house in self.__control.get_house_list():
            print(house.__dict__)

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()


def input_select(message):
    while True:
        try:
            num = int(input(f"请输入{message}:"))
            return num
        except:
            print("输入有误")
