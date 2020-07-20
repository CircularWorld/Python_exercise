"""
练习3： 在一个文件 my.log 中不间断的写入如下内容

 1. 2020-01-01  14:15:16
 2. 2020-01-01  14:15:18
 3. 2020-01-01  14:15:20
 4. 2020-01-01  14:15:22
 5. 2020-01-01  14:15:24
 6. 2020-01-01  14:17:29
 7. 2020-01-01  14:17:31

 每个时间占一行，每隔2秒写入一行
 当程序终止以后，下次启动，要求序号能够衔接继续写
 写的内容每写入一行就要在文件中显示

 提示 ： import time
        sleep()
"""
import time

f = open("my.log", "ab+", buffering=1)
f.seek(0, 0)
list_data = f.readlines()
# print(list_data)
if len(list_data):
    # count = list_data[-1].split(' ')[0]
    # print(count)
    count = len(list_data)
else:
    count = 0
while True:
    # f.seek(0, 2)
    count += 1
    f.write((str(count) + '. ' + str(time.ctime()) + '\n').encode())
    time.sleep(2)
