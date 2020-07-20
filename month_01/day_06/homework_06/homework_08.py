'''
8.列表推导式练习：
  计算1970年到2050年之间所有闰年
'''
list_leap_year = [year for year in range(1970, 2050) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]
print(list_leap_year)
