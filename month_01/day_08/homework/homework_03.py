"""
3. 参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
"""
def social_insurance(salary_before_tax):
    """
    计算社保缴纳费用
    :param salary_before_tax: 个人工资
    :return: 社保费用
    """
    return salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3

salary_before_tax = float(input("请输入税前工资："))
print(f"社保费用:{social_insurance(salary_before_tax)}元")
