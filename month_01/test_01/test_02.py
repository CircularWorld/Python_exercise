'''
2.需求：在终端中获取月份和年份，打印相应的天数.
    1 3 5 7 8 10 12 有 31天
    2平年有28天，闰年有29天
4  6  9  11 有 30天
步骤：在终端中录入年份和月份,根据逻辑判断 ,显示天数
'''
month = int(input('请输入月份：'))
year = int(input("请输入年份："))
if month in range(1,13):
    if month in (4, 6, 9, 11):
        print(f"{year}年{month:02}月有３0天")
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f'{year}是闰年，二月有２９天')
        else:
            print(f'{year}是平年，二月有２８天')
    else:
        print(f"{year}年{month:02}月有３1天")
else:
    print("输入有误")
