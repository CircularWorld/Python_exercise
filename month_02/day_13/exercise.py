import multiprocessing
from time import sleep
import os
import sys,os

def th1():
    sleep(1)
    print("吃饭")
    print(os.getppid(),"---",os.getpid())

def th2():
    # sys.exit("不睡了")
    sleep(2)
    print("睡觉")
    print(os.getppid(),"---",os.getpid())

def th3():
    sys.exit("不打了")
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"---",os.getpid())

things = [th1,th2,th3]
jobs=[]
for th in things:
    p = multiprocessing.Process(target=th)
    p.start()
    jobs.append(p)
for item in jobs:
    item.join()