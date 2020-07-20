"""
1. 玩家攻击敌人,敌人受伤(播放动画)
2. 玩家(攻击力)攻击敌人(血量),
敌人受伤(播放动画,血量减少)
3. 敌人(攻击力)还能攻击玩家(血量),
玩家受伤(碎屏,血量减少)
"""


class Player:
    def __init__(self, atk=0, blood=100):
        self.atk = atk
        self.blood = blood

    def attack(self,enemy):
        print("玩家攻击")
        enemy.damage(self)


    def damage(self, enemy):
        print("碎屏,血量减少")
        self.blood = 0 if self.blood < 0 else self.blood - enemy.atk
        print(f"玩家血量{self.blood}")


class Enemy:
    def __init__(self, atk=0, blood=100):
        self.atk = atk
        self.blood = blood

    def attack(self,player):
        print("怪物攻击")
        player.damage(self)

    def damage(self, player):
        print("播放动画")
        self.blood = 0 if self.blood < 0 else self.blood - player.atk
        print(f"怪物血量{self.blood}")


player_01 = Player(10, 100)
enemy01 = Enemy(20, 200)
player_01.attack(enemy01)
print()
enemy01.attack(player_01)
# print(enemy01.blood)
