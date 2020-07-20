"""
5.  使用面向对象思想,描述下列情景.
    张无忌使用乾坤大挪移(眩晕+伤害)攻击
    张无忌使用九阳神功(伤害+击飞)攻击
    还可能使用其他技能攻击
    要求：增加其他技能，人的代码不变。
"""


class Zwj:
    def use(self, skill):
        print("张无忌使用", end="")
        skill.effect()


class Skill:
    def effect(self):
        pass


class Qkdny(Skill):
    def effect(self):
        print("乾坤大挪移(眩晕+伤害)攻击")

class Jysg(Skill):
    def effect(self):
        print("九阳神功(伤害+击飞)攻击")

zwj = Zwj()

skill1 = Jysg()
skill2 = Qkdny()
zwj.use(skill1)
zwj.use(skill2)




