"""
创建图形管理器
1. 记录多种图形（圆形、矩形....）
2. 提供计算总面积的方法.
满足：
开闭原则
测试：
创建图形管理器，存储多个图形对象。
通过图形管理器，调用计算总面积方法.
"""


class GraphicManager:
    def __init__(self):
        self.__list_geometrys = []

    def add_graphic(self, geometry):
        if isinstance(geometry,Geometry):
            self.__list_geometrys.append(geometry)
            return self.__list_geometrys

    def calculate_total_area(self):
        total_area = 0
        for geometry in self.__list_geometrys:
            total_area += geometry.calculate_area()
        return total_area

class Geometry:
    def calculate_area(self):
        pass


class Circle(Geometry):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # super().calculate_area()
        def calculate_area(self):
            return 3.14 * self.radius ** 2


class Rectanle(Geometry):
    def __init__(self, length, width):
        self.lenth = length
        self.width = width

    def calculate_area(self):
        return self.lenth * self.width


manager = GraphicManager()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectanle(5, 6))
print(manager.calculate_total_area())
