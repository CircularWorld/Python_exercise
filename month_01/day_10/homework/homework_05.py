"""
5.创建技能类(技能名称,攻击比率,消耗法力,持续时间)
  保证数据范         0 - 2  0 - 80  0 - 120
"""
class Skill:
    def __init__(self,name,atk_rate,mana_cost,duration):
        self.name = name
        self.atk_rate = atk_rate
        self.mana_cost = mana_cost
        self.duration = duration

    @property
    def atk_rate(self):
        return self.__atk_rate

    @atk_rate.setter
    def atk_rate(self, value):
        if 0<= value<=2:
            self.__atk_rate = value
        elif value<0:
            self.__atk_rate = 0
        elif value>2:
            self.__atk_rate = 2
        else:
            raise Exception("atk_rate data error")
    @property
    def mana_cost(self):
        return self.__mana_cost

    @mana_cost.setter
    def mana_cost(self, value):
        if 0 <= value <= 80:
            self.__mana_cost = value
        elif value < 0:
            self.__mana_cost = 0
        elif value > 80:
            self.__mana_cost = 80
        else:
            raise Exception("mana_cost data error")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 120:
            self.__duration = value
        elif value < 0:
            self.__duration = 0
        elif value > 80:
            self.__duration = 80
        else:
            raise Exception("duration data error")

def print_skill_info(skill):
    print(f"{skill.name}攻击频率{skill.atk_rate}消耗法力{skill.mana_cost}持续时间{skill.duration}s")
skill_01 = Skill("火球术",1.5,40,2)
skill_02 = Skill("寒冰箭",1.2,30,4)
print(skill_01.__dict__)
print_skill_info(skill_01)
print_skill_info(skill_02)
