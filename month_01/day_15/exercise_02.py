"""
定义函数,获取成绩
如果成绩输入有误,循环录入,直到正确为止.
"""

def get_score():
    while True:
        try:
            score = float(input("请输入成绩:"))
            return score
        except:
            print("出错了")




print(get_score()) # 有效的成绩