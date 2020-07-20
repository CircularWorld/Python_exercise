'''
根据年龄，输出对应的人生阶段。
        年龄       ⼈⽣阶段
        0-6 岁      童年
        7-17 岁     少年
        18-40 岁    ⻘年
        41-65 岁    中年
        65 岁之后    ⽼年
    步骤:
        终端中获取年龄
        显示人生阶段
'''
age = int(input('请输入年龄：'))
if  age < 1:
    print('请输入大于０的整数')
else:
    if age <=6:
        print('童年')
    elif age <=17:
        print('少年')
    elif age <=40:
        print('青年')
    elif age <=65:
        print('中年')
    else:
        print('老年')