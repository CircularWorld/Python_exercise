from socket import *
from threading import Thread
from signal import *

IP ='0.0.0.0'
PORT = 8888
ADDR = (IP,PORT)

class MyThread(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                self.connfd.close()
            else:
                print(data.decode())
                self.connfd.send(b"Thanks")


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen()
    print("listen Port",PORT)
    while True:
        try:
            connfd,addr = sock.accept()
            print(addr)
        except KeyboardInterrupt:
            sock.close()
            return
        t = MyThread(connfd)
        t.setDaemon(True)
        t.start()

main()

