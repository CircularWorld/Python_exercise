"""
拷贝一个文件夹
将一个文件夹拷贝一份
*假设文件夹只有普通文件
*将每个文件的拷贝作为一个拷贝事件
*使用进程池完成事件

前提,获取当前目录

创建文件夹 os.mkdir("name")
"""

from multiprocessing import Pool
from multiprocessing import Queue

import os
q = Queue()

# 获取文件夹大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return total_size

def copyfile(name, old, new):
    # print(f"{new}/{name}")
    # print(f"{old}/{name}")
    # fr = open(old+'/'+name, 'rb')
    # fw = open(new+'/'+name, 'wb')

    fr = open(f"{old}/{name}", 'rb')
    fw = open(f"{new}/{name}", 'wb')
    while True:
        data = fr.read(1024)
        q.put(data)
        if not data:
            break
        n = fw.write(q.get())
        q.put(n)
    fr.close()
    fw.close()


def main():
    old = input("要拷贝的目录:")
    total_size = get_size(old)
    new = old + '--备份'
    try:
        os.mkdir(new)
    except Exception as e:
        print(e)

    pool = Pool()

    for file in os.listdir(old):
        pool.apply_async(func=copyfile, args=(file, old, new))
    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get()
    print("拷贝了%.2f%" % (copy_size/total_size*100))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
