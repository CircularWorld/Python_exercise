class Skill:
    def __init__(self, name="", atk_rate=0, cost_sp=0, duration=0):
        self.name = name
        self.atk_rate = atk_rate
        self.cost_sp = cost_sp
        self.duration = duration


"""
3. 在技能列表中完成下列操作
    -- 定义函数,查找攻击比例atk_rate大于1的所有技能
    -- 定义函数,查找消耗法力cost_sp为零并且持续时间duration大于5的所有技能
    -- 定义函数,查找名称为"九阳神功"的单个技能对象
    -- 定义函数,查找消耗法力最大的单个技能对象
    -- 定义函数,根据持续时间,对技能列表升序排列
    -- 定义函数,判断技能列表中是否存在名称相同的技能对象
              有true没有false(要求:自定义算法实现)
"""
list_skills = [
    Skill("寒冰掌",1.2,30,5),
    Skill("九阳神功",0.9,30,5),
    Skill("铁砂掌",1000,0,6),
]



def find_atk_rate_gt_1_skill():
    for skill in list_skills:
        if skill.atk_rate > 1:
            yield skill

def find_skills_cost_sp_eq_0_and_duration_gt_5():
    for skill in list_skills:
        if skill.cost_sp ==0 and skill.duration >5:
            yield skill

def find_skill_by_name(name):
    for skill in list_skills:
        if skill.name == name:
            return skill

def find_max_skill_cost_sp():
    c_sp_max_skill = list_skills[0]
    for skill in list_skills:
        if c_sp_max_skill.cost_sp < skill.cost_sp:
            c_sp_max_skill = skill
    return c_sp_max_skill

def sort_skill_increase_by_duration():
    for r in range(len(list_skills)-1):
        for c in range(r+1,len(list_skills)):
            if list_skills[r].duration > list_skills[c].duration:
                list_skills[r] ,list_skills[c] = list_skills[c] ,list_skills[r]


def find_skill_same_name():
    for r in range(len(list_skills)-1):
        for c in range(r+1,len(list_skills)):
            if list_skills[r].name == list_skills[c].name:
                return True
    return False

def print_skills(skills):
    for skill in skills:
        print(skill.__dict__)

skills = find_atk_rate_gt_1_skill()
# print_skills(skills)


print_skills(find_skills_cost_sp_eq_0_and_duration_gt_5())



