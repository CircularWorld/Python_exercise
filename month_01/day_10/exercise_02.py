class Wife:
    count = 0
    @classmethod
    def print_wife_number(cls):
        print(cls.count)
    def __init__(self, name=None):
        self.name =name
        Wife.count+=1

wife_01 = Wife("双飞燕")

wife_02 = Wife("Ａｌｉｓｔ")

Wife.print_wife_number()