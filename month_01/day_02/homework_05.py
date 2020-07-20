'''
5. 温度转换器：
    摄氏度 = （华氏度 - 32） 除以 1.8
    Celsius<->Fahrenheit
    在终端中录入摄氏度，计算华氏度
'''
print('摄氏度＜－＞华氏度')
while  True:
    Fahrenheit = input('请输入华氏度(按Q 退出)：')
    if Fahrenheit == 'q' and Fahrenheit == 'Q':
        break
    Fahrenheit = float(Fahrenheit)
    Celsius = (Fahrenheit - 32) / 1.8
    print('%.2f华氏度　＝　%.2f摄氏度' % (Fahrenheit, Celsius))


