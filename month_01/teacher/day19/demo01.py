"""
    Python核心1
        Python 简介
            执行过程
                源代码 -编译-> 字节码 -解释-> 机器码
                 .py         .pyc          01
                         (只有导入的模块)
                |-----第一次-----|

                main.py  -- 入口(代码简单,导入其他功能模块)
                usl.py   -- 界面(处理界面逻辑View)
                bll.py   -- 业务(业务逻辑Controller)
                model.py -- 模型(封装Model)
            快捷键:百度搜索Pycharm快捷
        Python自动化内存管理
            引用计数:每个对象记录被变量绑定(引用)的数量,
                    当为0时被销毁。
                缺点:循环引用 - 两个垃圾数据互相引用
                时机:时刻
            标记清除:"全盘"扫描内存,检查(标记)不再使用的数据.
                缺点:效率太低
                时机:内存告急
            分代回收:将内存分为小中大三代
                    每次创建新数据都在0代分配空间
                    当标记清除后,将前一代有用的数据升级到下一代.
                    前一代所有数据清空
            内存优化:
                尽少产生垃圾/自定义对象池/控制内存管理系统
                对象池:每当创建对象时,在池中判断是否存在相同对象,
                      如果有直接返回地址
                      如果没有再分配空间创建对象
                      例如,字符串池/整数池/小数池.....
                      价值:提高内存利用率


"""
# 循环引用
list01 = []
list02 = []
list01.append(list02)
list02.append(list01)
del list01, list02

# 产生垃圾的常用代码:
a = "数据1"
a = "数据2"  # 当变量a又指向"数据2"时,"数据1"成为垃圾.

b = "数据3"
del b  # 因为变量b被销毁,所以"数据3"成为垃圾

# 根据某些逻辑,循环拼接字符串.(频繁修改字符串)
str_result = ""
for number in range(10):
    # 两个不可变对象,相加后会产生新对象
    str_result = str_result + str(number)
print(str_result)

# 解决:使用可变对象代替不可变对象
list_result = []
for number in range(10):
    list_result.append(str(number))
str_result = "".join(list_result)
print(str_result)

data01 = "悟空"
data02 = "悟空"
print(id(data01))
print(id(data02))