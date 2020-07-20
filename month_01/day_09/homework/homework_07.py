'''
7. 以万物皆对象的思想，洞察你身边的客观事物,挑选2个创建类和对象.
    目标:使用计算机描述生活
    体会:现实事物  -抽象->  类  -具体-> 对象
'''
class Human:
    def __init__(self,name,sex,profession):
        self.name = name
        self.sex = sex
        self.profession = profession
    def action(self,behavior):
        print(self.name,behavior)

class Company:
    def __init__(self,name,company_id,business):
        self.name = name
        self.company_id = company_id
        self.business = business
    def income(self,money):
        print(self.name,self.business,"收入",money)

people1 = Human("岳云鹏","男","相声家")
people1.action("参加极限挑战")

tedu = Company("达内","12398127","教育")
tedu.income("99999999999")

