"""
    common/
        iterable_tools.py
    可迭代对象工具
# 1. 教学意义：深刻掌握函数式编程思想
# 　　分、隔、做
# 2. 实用价值：在开发过程中不断壮大自定义高阶函数
# 功能更强大
# 3. 利于面试：精通函数式编程
# 常常遇到xx功能发现实现方式大部分逻辑相同只是核心xx不同
# 我就将共性提取到xx类中放到单独的模块中.
# 在各种项目中直接导入使用.
# 思想来源于微软Linq技术

"""


class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func):
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        for emp in iterable:
            if func(emp):
                return emp

    @staticmethod
    def select(iterable, func):
        for emp in iterable:
            yield func(emp)

    @staticmethod
    def del_all(iterable, func):
        count = 0
        for r in range(len(iterable) - 1, -1, -1):
            if func(iterable[r]):
                del iterable[r]
                count += 1
        return count

    @staticmethod
    def del_single(iterable, func):
        for r in range(len(iterable) - 1, 0, -1):
            if func(iterable[r]):
                return iterable

    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for emp in iterable:
            if func(max_value) < func(emp):
                max_value = emp
        return max_value

    @staticmethod
    def get_min(iterable, func):
        max_value = iterable[0]
        for emp in iterable:
            if func(max_value) > func(emp):
                max_value = emp
        return max_value

    @staticmethod
    def ascending_order(iterable, func):
        for r in range(len(iterable)-1):
            for c in range(r+1,len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r],iterable[c] = iterable[c],iterable[r]

    @staticmethod
    def print_me():
        print("love")

