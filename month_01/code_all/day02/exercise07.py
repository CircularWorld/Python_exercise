"""
    在终端中录入一个疫情确诊人数,再录入一个治愈人数,
    打印治愈比例
    格式：治愈比例为xx%
"""
def cure_rate(definite_num,cure_num):
    return  cure_num / definite_num * 100

definite_num = int(input("请输入确诊人数："))
cure_num = int(input("请输入治愈人数："))
cure_rate_result = cure_rate(definite_num,cure_num)
print(f"治愈比例为：{cure_rate_result}%")
