"""
文件的复制
下载一个图片
从主目录复制到当前目录
"""

f_01 = open("/home/tarena/JYH/beautiful.jpg","rb")
f_02 = open("beautiful.jpg","rb")
# for line in f_01:
#     f_02.write(line)

while  True:
    data = f_01.read(1024)
    if not data:
        break
    f_02.write(data)

# while True:
#     line = f_01.readline()
#     f_02.write(line)
#     if not line:
#         break

# list_01 = f_01.readlines()
# for line in list_01:
#     print(line)
# f_02.writelines(list_01)


f_01.close()
f_02.close()
