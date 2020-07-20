"""
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    天才：140以上（包含）
    超常：120-139之间（包含）
    聪慧：110-119之间（包含）
    正常：90-109之间（包含）
    迟钝：80-89之间（包含）
    低能：80以下
    根据心理年龄与实际年龄，打印智商等级。
"""
def calculate_talent(ma,ca):
    """
    计算个人天分
    :param ma:心理年龄
    :param ca: 实际年龄
    :return: 天分
    """
    iq = ma / ca * 100
    if iq >= 140:
        return "天才"
    if iq >= 120:
        return "超常"
    if iq >= 110:
        return "聪慧"
    if iq >= 90:
        return "正常"
    if iq >= 80:
        return "迟钝"
    else:
        return "低能"

ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
int(calculate_talent(ma,ca))
# if iq >= 140:
#     print("天才")
# elif 120 <= iq <= 139: # el就是在表达小于140,所以在判断iq <=139属于重复判断
#     print("超常")
# elif 110 <= iq <= 119:
#     print("聪慧")
# elif 90 <= iq <= 109:
#     print("正常")
# elif 80 <= iq <= 89:
#     print("迟钝")
# else:
#     print("低能")

