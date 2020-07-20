'''
八大行星：
"水星""金星""地球""huo星""木星""土星""天王星""海王星"
创建列表存储4个行星：“水星” "金星" "huo星" "木星"
插入"地球"、追加"土星" "天王星" "海王星"
打印距离太阳最近、最远的行星(第一个和最后一个元素)
打印太阳到地球之间的行星(前两个行星)
删除"海王星",删除第四个行星
倒序打印所有行星(一行一个)
'''
from builtins import print

list_planets = ['水星', '金星', '火星', '木星']
# 插入"地球"、追加"土星" "天王星" "海王星"
list_planets.insert(2, '地球')
print(list_planets)
list_planets[len(list_planets):]=['土星','天王星','海王星']
# list_planets.append('土星')
# list_planets.append('天王星')
# list_planets.append('海王星')
print(list_planets)
# 打印距离太阳最近、最远的行星(第一个和最后一个元素)
print(list_planets[0])
print(list_planets[-1])
# 打印太阳到地球之间的行星(前两个行星)
for plant in list_planets[:2]:
    print(plant)
# 删除"海王星",删除第四个行星
# 倒序打印所有行星(一行一个)
list_planets.remove('海王星')
print(list_planets)
del list_planets[3]
print(list_planets)
# 倒序打印所有行星(一行一个)
for i in range(len(list_planets) -1,-1,-1):
    print(list_planets[i])

