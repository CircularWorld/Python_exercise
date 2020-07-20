'''
线程 同步互斥
'''

from threading import Thread, Lock

a = b = 0


def value():
    while True:
        with lock:
            if a != b:
                print(a, '---', b)


t = Thread(target=value)
lock = Lock()
t.start()
while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

t.join()
