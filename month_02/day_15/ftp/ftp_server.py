'''
ftp 文件服务 服务器:
多线程 并发模型训练
'''
from socket import *
from threading import Thread
import os, time

IP = '0.0.0.0'
PORT = 8888
ADDR = (IP, PORT)

FTP = "/home/tarena/JYH/FTP/"


class FtpServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        # 判断文件库是否为空
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
            list_str = '\n'.join(file_list)
            self.connfd.send(list_str.encode())
            # self.connfd.send(b"##")

    def do_download(self, file):
        # if not os.path.exists(FTP + file):
        #     self.connfd.send(b"FAIL")
        # else:
        #     self.connfd.send(b"OK")
        try:
            f = open(FTP + file,'rb')
        except:
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.connfd.send(b"##")
                    break
                self.connfd.send(data)
            f.close()

    def do_pushfile(self,file):
        # try:
        #     f = open(FTP + file, 'rb')
        # except:
        f = open(FTP + file, 'wb')
        self.connfd.send(b"OK")
        time.sleep(0.1)
        # else:
        #     self.connfd.send(b"FAIL")
        #     return
        print("正在下载...")
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                time.sleep(0.1)
                break
            f.write(data)
        print("下载完成")
        f.close()


    def run(self):
        while True:
            data = self.connfd.recv(1024).decode().split(" ", 2)
            print(data)

            if data[0] == "LIST":
                # 查看文件列表
                self.do_list()
                # self.connfd.send(b"list")
            elif data[0] == "RETR":
                print(data)
                self.do_download(data[1])
                # print("客户下载")
            elif data[0] == "STOR":
                print(data)
                self.do_pushfile(data[1])
            elif data[0] == "EXIT":
                self.connfd.close()
            else:
                self.connfd.send("无法识别请重新输入".encode())
        self.connfd.close()


def main():
    sock = socket()
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(ADDR)
    sock.listen()
    print("listen Port:", PORT)
    while True:
        try:
            connfd, addr = sock.accept()
            print(addr)
        except KeyboardInterrupt:
            return
        t = FtpServer(connfd)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
