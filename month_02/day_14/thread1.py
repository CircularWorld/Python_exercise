import threading
from multiprocessing import Process
import time
import os

a = 1
def music():
    for i in range(3):
        time.sleep(1)
        print(os.getpid(),"music")
    global a
    print(a)
    a+=1

t = threading.Thread(target=music)

t.start()
for i in range(3):
    time.sleep(1)
    print(os.getpid(),"音乐")

t.join()
print('s',a)
