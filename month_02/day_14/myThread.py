'''
自定义线程类
'''
from threading import Thread
import time
class MyThread(Thread):
    def __init__(self, song=None):
        self.song = song
        super().__init__()
    def run(self):
        for i in range(3):
            print("se",self.song)
            time.sleep(1)

t =MyThread("小幸运")
t.start()
t.join()