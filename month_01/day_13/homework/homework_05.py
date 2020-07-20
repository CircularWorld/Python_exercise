"""
    玩家攻击敌人(掉装备),还可能死亡(播放死亡动画)
    敌人攻击玩家(碎屏),还可能死亡(游戏结束)
    要求：增加其他角色参与战斗,玩家和敌人类代码不变.
"""

# 战斗系统　单位　玩家１　　敌人１
class CombatSystem:
    def action(self,attacker,victim):
        if isinstance(attacker,Target) and isinstance(victim,Target):
            attacker.attack()
            victim.damage()
        else:
            raise Exception(f"targets have  lose attacker={attacker}  attacker = {victim}")

class Target:
    def __init__(self, atk=0, hp=0):
        self.atk = atk
        self.hp = hp
    def attack(self):
        pass
    def damage(self):
        pass

class Player(Target):
    def attack(self):
        print("玩家发动攻击")
        pass

    def damage(self,):
        super().damage()
        print("玩家受伤碎屏")


class Enemy(Target):
    def attack(self):
        print("敌人发动攻击")
        pass

    def damage(self):
        super().damage()
        print("敌人掉装备")
    pass

def remain_HP(victim,attacker):
    victim.hp -= attacker.atk


c_system = CombatSystem()
play_01 = Player(5,100)
enemy_01 = Enemy(10,200)
c_system.action("s","s")
c_system.action(play_01,enemy_01)
c_system.action(enemy_01,play_01)
