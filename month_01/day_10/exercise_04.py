class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("hp data error")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value in range(1, 31):
            self.__atk = value
        else:
            raise Exception("atk data error")

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        if value in range(21):
            self.__defence = value
        else:
            raise Exception("defence data error")


enemy_01 = Enemy("哥布林", 60, 12, 5)
print(enemy_01.__dict__)
enemy_02 = Enemy("大哥布林", 120, 20, 10)
enemy_03 = Enemy("哥布林王", 100, 30, 20)
