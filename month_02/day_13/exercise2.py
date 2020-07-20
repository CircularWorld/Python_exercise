"""
进程池 父进程退出 池自动销毁
"""

from multiprocessing import Pool

from time import ctime, sleep


def worker(msg, sec):
    print(ctime(), '---', msg)
    sleep(sec)
    print(msg, "---end")


pool = Pool(2)

for i in range(10):
    msg = 'Tedu-%d' % i
    pool.apply_async(func=worker, args=(msg, 2))

pool.close()
pool.join()
