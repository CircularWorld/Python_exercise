"""
自定义进程类
"""

from multiprocessing import Process
import time


# 自定义类
class MyProcess(Process):
    def __init__(self, val):
        self.val = val
        super().__init__()  # 加载父类属性


    def fun1(self):
        print('步骤1:假设很复杂', self.val)

    def fun2(self):
        print('步骤2:假设也很复杂', self.val)

    def sum_prime(self):
        prime = []
        for num in range(1,self.val+1):
            if self.isPrime(num):
                prime.append(num)
        print(sum(prime))

    @staticmethod
    def isPrime(num):
        if num <=1:
            return False
        for item in range(2,num//2):
            if num % item ==0 and num > 1:
                return False

        return True

    # 重写run,将其作为一个新进程的执行内容
    def run(self):
        t1 = time.localtime()
        self.sum_prime()
        self.sum_prime()
        self.sum_prime()
        self.sum_prime()

process = MyProcess(4)

process.start()  # 启动进程 执行 run

process.join()

# process.sum_prime()
