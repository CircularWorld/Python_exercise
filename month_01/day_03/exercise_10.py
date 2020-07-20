'''

'''
while 1:
     print('奇数') if int(input('请输入一个整数：'))%2 else print('偶数')

while 1:
    year = int(input('输入年份:'))
    if year:
        print('闰年') if year%4==0 and year%100 or year%400 ==0 else print('平年')