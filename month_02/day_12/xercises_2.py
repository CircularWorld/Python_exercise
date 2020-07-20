import multiprocessing
import time
def func(t,name):
    time.sleep(t)
    print("name:",name)

# p = multiprocessing.Process(target=func,args=(2,"王也"))
p = multiprocessing.Process(target=func,args=(3,),kwargs={'name':"王也"})

p.start()

p.join(1)
print("--------------")