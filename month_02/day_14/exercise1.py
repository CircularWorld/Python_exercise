'''
练习1： 模拟售票系统
现有500 张票 记为 T1--T500 放在一个列表
有10个窗口一起买票 记为 w1 -- w10 ,每张票卖出需要0.1秒
创建10个线程 模拟10个窗口，票的售出顺序必须是1--500
每张票卖出时 打印 w2----T203

编程创建10个 线程模拟这个过程
'''
from threading import Thread

from time import sleep

ticket = ["T%d" % i for i in range(1, 501)]
# print(list_ticket)


def sell(window):
    while ticket:
        print(window+'----'+ticket.pop(0))
        sleep(0.1)




jobs = []
for i in range(1, 11):
    w = "w%d" % i
    t = Thread(target=sell, args=(w,))
    t.start()
    jobs.append(t)

for i in jobs:
    i.join()