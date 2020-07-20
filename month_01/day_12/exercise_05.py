class Grenade:
    def bomb(self,thing):
        thing.shock()


class Thing:
    def shock(self):
        pass

class People(Thing):
    def shock(self):
        print("碎屏")

class House(Thing):
    def shock(self):
        print("房子倒了")

grenade = Grenade()
man = People()
house = House()
grenade.bomb(man)
grenade.bomb(house)