"""练习1： 大文件拆分
将一个文件拆分为两个部分，每个部分分别是文件的一半
即源文件的上下半部分，分别拆到一个新文件里

要求使用两个进程同时进行

提示： 按照文件的字节数计算文件大小
os.path.getsize()"""
import multiprocessing
import os

f = open("new.jpg", "rb")

img_size = os.path.getsize("new.jpg")
img_up = f.read(int(img_size / 2))
img_down = f.read()


def write_file_up():
    print("up..begin")
    f = open("new.jpg", "rb")
    f2 = open("up.jpg", 'wb')
    up_size = img_size // 2
    while up_size >= 1024:
        f2.write(f.read(1024))
        up_size -= 1024
    else:
        f2.write(f.read(up_size))
    f.close()
    f2.close()
    print("up..end")


def write_file_down():
    print("down..begin")
    f = open("new.jpg", "rb")
    f3 = open("down.jpg", 'wb')
    f.seek(img_size // 2, 0)
    while True:
        data = f.read(1024)
        if not data:
            break
        f3.write(data)
    f.close()
    f3.close()
    print("down..end")


p1 = multiprocessing.Process(target=write_file_up)
# p2 = multiprocessing.Process(target=write_file_down)

p1.start()
write_file_down()

p1.join()

