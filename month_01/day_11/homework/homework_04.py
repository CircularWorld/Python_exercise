"""
    -- (1)小明使用手机打电话
            识别对象
                小明　手机
            分配职责
                打电话　通话
            建立交互
                人　调用　手机
            　       １　直接创建对象掉用
                    ２　在构造函数中创建
                    ３　通过参数传递对象

    -- (2)小明一次请多个保洁打扫卫生
          效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
          区别:保洁与保洁列表
    -- (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
          区别:敌人与敌人列表
    -- (4)
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
        提示：张无忌与赵敏是数据不同
             行为相同
"""
# -- (1)
# 小明使用手机打电话
# class People:
#     def __init__(self,name,brand):
#         self.name =name
#         self.mobile = Mobile(brand)
#     def use(self):
#         print("使用")
#         self.mobile.call()
#
# class Mobile:
#     def __init__(self,brand):
#         self.brand = brand
#     def call(self):
#         print("打电话")
#
# xm = People("小明","MX")
# xm.use()

# -- (2)
# 小明一次请多个保洁打扫卫生
# 效果: 调用一次小明通知方法, 可以有多个保洁在打扫卫生.
# 区别: 保洁与保洁列表
# class Xm:
#     def action(self,cleaner):
#         print("请保洁",end = '')
#         cleaner.clean_room()
#
# class Cleaner:
#     count = 0
#     def __init__(self):
#         Cleaner.count+=1
#
#     def clean_room(self):
#         print(f"阿姨打扫房间")
# xm = Xm()
# list_clean =[]
# for __ in range(5):
#     list_clean.append(Cleaner())　
# for i in range(len(list_clean)):
#     xm.action(list_clean[i])
"""
    -- (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
          区别:敌人与敌人列表
"""
# class Creature:
#     def __init__(self,name,hp,atk):
#         self.name  = name
#         self.hp  = hp
#         self.atk  = atk
#
# class Player(Creature):
#     def __init__(self,name,hp,atk):
#         super().__init__(name,hp,atk)
#     def attack(self,*targt):
#         print("玩家群体攻击")
#         for enemy in targt:
#             enemy.damage(self.atk)
#
# class Enemy(Creature):
#     def __init__(self,name,hp,atk):
#         super().__init__(name,hp,atk)
#     def damage(self,atk):
#         self.hp -= atk
#         print(f"{self.name}怪物减血")
#         if self.hp <=0:
#             print("怪物si亡动画")
#
# play01 = Player("亚瑟王",1000,20)
#
# list_enemys = [
#     Enemy("哥布林1",100,10),
#     Enemy("哥布林2",100,10),
#     Enemy("哥布林3",100,10),
#     Enemy("哥布林4",100,10),
#     Enemy("哥布林5",100,10),
# ]
#
# play01.attack(*list_enemys)

"""
    -- (4)
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
        提示：张无忌与赵敏是数据不同
             行为相同
"""
class People:
    def __init__(self,name, kunfu, salary):
        self.name = name
        self.kunfu = kunfu
        self.salary = salary

    def teach(self,zm):
        print(f"{self.name}教{zm.name}{self.kunfu}")
    def work(self):
        print(f"{self.name}工作挣了{self.salary}")


zwj = People("张无忌","九阳神功",5000)
zm = People("赵敏","寒冰神掌",10000)
zwj.teach(zm)
zwj.work()
zm.teach(zwj)
zm.work()