"""
    业务逻辑层
"""
from dal import HouseDao


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()


    @property
    def list_house(self):
        return self.__list_houses

    # @list_house.setter
    # def list_house(self, value):
    #     self.__list_houses = value

    def get_house_informaitin(self):
        for house in self.__list_houses:
            yield house

    def get_house_list(self):
        return self.__list_houses

    def del_house_by_id(self, id):
        for i, house in enumerate(self.__list_houses):
            if house.id == id:
                del self.__list_houses[i]
                return True
        return False

    def get_house_max_total_price(self):
        max_house = self.__list_houses[0]
        for item in self.__list_houses:
            if max_house.total_price < item.total_price:
                max_house = item
        return max_house

    def get_house_min_area(self):
        min_house = self.__list_houses[0]
        for item in self.__list_houses:
            if min_house.area > item.area:
                min_house = item
        return min_house

    def count_house_type(self):
        dict_house_type = {}  # type:dict
        for house in self.__list_houses:
            if house.house_type not in dict_house_type:
                dict_house_type[house.house_type] = 1
            else:
                dict_house_type[house.house_type]+=1
        return dict_house_type

    def ascending_ording(self):
        self.__list_houses = sorted(self.__list_houses,key= lambda house:house.total_price)