from threading import Thread
from time import sleep

def func(sec, name):
    print("有参线程")
    sleep(sec)
    print("%s 线程end" % name)


jobs = []
for i in range(5):
    t = Thread(target=func, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.setDaemon(True)
    t.start()
    print(t.getName())

# 列表推导式
# [x.join() for x in jobs]
