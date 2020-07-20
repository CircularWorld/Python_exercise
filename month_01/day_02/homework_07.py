"""
7. 根据工资计算个人社保缴纳费用
    步骤：在终端中录入缴纳基数,根据公式计算,显示缴纳费用
    公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%

"""
print('个人社保缴纳费用')
wage = float(input('您的工资为：'))
social_security = wage * 0.08 + wage * 0.02 + 3 + wage * 0.002 + wage * 0.12

print('社保缴纳金额为： %.2f' % social_security)
