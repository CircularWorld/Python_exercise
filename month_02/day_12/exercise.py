'''
multiprocessing
'''
# from multiprocessing import *
import multiprocessing
import time

a = [[1],2,4]
def func1():
    print('func1...begin')
    global a
    a[0][0] = 9
    time.sleep(3)
    print("func1--end")


p = multiprocessing.Process(target=func1)
p.daemon = True

p.start()

print(p.name)
print(p.pid)
print(p.is_alive())
time.sleep(2)

# p.join()
# print(a)
