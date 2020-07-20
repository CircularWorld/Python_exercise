"""
    在终端中获取月份，打印相应的天数.
    1 3 5 7 8 10 12 有 31天
    2有28天
    4  6  9  11 有 30天
    输入的月份有误
"""
dict_month_days = {"1": 31, "2": 28, "3": 31, "4": 30,
                   "5": 31, "6": 30, "7": 31, "8": 31,
                   "9": 30, "10": 31, "11": 30,
                   "12": 31}
year = int(input("请输入年份:"))
month = input("请输入月份:")
dict_month_days["2"] = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
if month in dict_month_days:
    print(f"{year}年{month}月有{dict_month_days[month]}天")
else:
    print("输入的月份有误")

# # 月份输入正确
# if month == 2:
#     print("28天")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("30天")
# else:  # 1 3 5 7 8 10 12
#     print("31天")

