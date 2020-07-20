month = int(input('请输入月份：'))
if month > 12 or month < 1:
    print('输入有误')
else:
    if month == 4 or month == 6 or month == 9 or month == 11:
        print('有３０天')
    elif month == 2:
        print('有28天')
    else:
        print('有31天')
