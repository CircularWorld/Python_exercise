from  multiprocessing import Queue

q = Queue(3)

def request():
    name = 'lilei'
    pwd = "123"
    q.put(name)
    q.put(pwd)

def handle():
    name = q.get()
    pwd = q.get()
    print(name)
    print(pwd)

def main():
    request()
    handle()

main()