# 3. 直接使用IterableHelper类现有功能,完成下列需求
#     -- 在技能列表中查找名称是"一阳指"的技能对象
#     -- 在技能列表中查找攻击比例atk_rate大于1的所有技能对象
#     -- 在技能列表中所有技能名称name和消耗法力cost_sp
from common.iterable_tools import IterableHelper


class Skill:
    def __init__(self, name="", atk_rate=0.0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration


list_skills = [
    Skill("横扫千军", 1, 50, 5),
    Skill("九阳神功", 3, 150, 6),
    Skill("降龙十八掌", 3, 150, 5),
    Skill("一阳指", 1.2, 0, 2),
    Skill("乾坤大挪移", 3.2, 30, 2),
    Skill("打狗棍", 1.3, 0, 6),
]
if __name__ == '__main__':
    employee = IterableHelper.find_single(list_skills, lambda emp: emp.name == "一阳指")
    print(employee.__dict__)

    for item in IterableHelper.find_all(list_skills, lambda emp: emp.atk_rate > 1):
       print(item.__dict__)

    for item in IterableHelper.select(list_skills,lambda emp:(emp.name,emp.cost_sp)):
        print(item)