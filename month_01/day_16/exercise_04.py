"""
自定MyRange类
实现range(5)效果
"""


# class MyRangeIterator:
#     def __init__(self,data):
#         self.num = data
#         self.index = -1
#
#     def __next__(self):
#         self.index +=1
#         if self.index < self.num:
#             return self.index
#         else:
#             raise StopIteration


class MyRange:
    def __init__(self, end=0):
        self.end = end
        self.num = 0

    def __iter__(self):
        # return MyRangeIterator(self.num)
        while self.num < self.end:
            yield self.num
            self.num += 1


for item in MyRange(5):  # 0~4
    print(item)
