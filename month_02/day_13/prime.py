import time
from multiprocessing import Process

"""
练习1 ： 编写一个程序
* 使用单进程 求100000以内质数之和  记录所用时间
* 使用4个进程，将100000拆分为4份，分别求每部分中质数之和 记录时间
* 使用10个进程，将100000拆分为10份，分别求每部分中质数之和 记录时间
"""


def times(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("执行时间", end - start)
        return res

    return wrapper


class Prime(Process):
    def __init__(self, begin=0, end=0):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        sum_prime = []
        for i in range(self.begin, self.end):
            if isPrime(i):
                sum_prime.append(i)
        print(sum(sum_prime))


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True


@times
def process4():
    jobs = []
    for num in range(1, 100001, 25000):
        p = Prime(num, num + 25000)
        jobs.append(p)
        p.start()

    for item in jobs:
        item.join()


process4()  # 执行时间: 15.002186059951782
