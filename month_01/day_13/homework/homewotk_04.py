"""
4. 小明使用手机打电话
   要求:增加座机,卫星电话时不影响小明.
   写出案例中体现的面向对象三大特征和六大原则.
"""
# 面向对象三大特征
'''
１封装 　创建Xiaoming　Mobile类　Satellite_phone类　
２继承　　创建Ｄevice类　进行　抽象（找成员的共性）　分离（小明和手机等通信工具），方法统一（方便多种设备代码修改管理），
３多态　　彰显子类个性，（不同，变化，具体）　
        编码时Xiaoming调用device 
        子类重写父类，
        向Xiaoming类添加Mobile和Satellite_phone对象
        
'''
# 面向对象六大设计原则.
"""
１开闭原则：对扩展开放对修改关闭　增加新的device  Xiaoming不用改变　
２类的单一原则　Xiaoming　调用所有设备，　Mobile实现电话通话　Satellite_phone实现网络通话
３依赖倒置　　　Xiaoming　依赖使用　抽象的device 　而不是ｄｅｖｉｃｅ的子类
４组合复用原则　（Xiaoming 通过　device 调用手机，不必小明直接调用手机网络通信需要修改添加）Xiaoming　和设备　通信
５里氏替换　　　Mobile重写时先调用父类方法，子拥有父类所有功能，并可直接替换父类（在父类的基础上添加功能）
６迪米特法则　　（由Ｄｅｖｉｃｅ父类　建立小明和子类的关系）　Ｄｅｖｉｃｅ父类　隔离Xiaoming　和　Mobile　Satellite_phone　的变化
"""


class Xiaoming:
    def call_phone(self, device):
        print("小明")
        device.message()


class Device:

    def message(self):
        pass


class Mobile(Device):

    def message(self):
        super().message()
        print("手机音频")


class Satellite_phone(Device):
    def message(self):
        super().message()
        print("网络电话")


xm = Xiaoming()
mb = Mobile()
ph = Satellite_phone()

xm.call_phone(mb)
xm.call_phone(ph)
