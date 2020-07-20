"""
逻辑
打印
"""

from threading import Lock, Thread, Event
import string

e = Event()
lock1 = Lock()
lock2 = Lock()

def show_num():
    flg = True
    num = 1
    for num in range(1,52,2):
            lock1.acquire()
            print(num,end ='')
            print(num+1,end ='')
            lock2.release()

def show_chat():
    for vla in string.ascii_uppercase:
            lock2.acquire()
            print(vla, end='')
            lock1.release()

def print_char():
    for i in range(65,91):
        print(chr(i))



print_char()

# t = Thread(target=show_num)
# t2 = Thread(target=show_chat)
#
# lock2.acquire()
# t.start()
# t2.start()
#
# t.join()
# t2.join()
