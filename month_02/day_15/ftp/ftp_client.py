from socket import *
from time import sleep
IP = '0.0.0.0'
PORT = 8888
ADDR=(IP,PORT)

class FtpClient:
    def __init__(self,sock):
        self.sock = sock
        # super.__init__()
    def do_list(self):
        self.sock.send(b"LIST")
        restult = self.sock.recv(128).decode()
        print("restult ==",restult)
        if restult =="OK":
            #接收文件列表  考虑粘包
                file = self.sock.recv(1024*1024).decode()
                print(file)
        else:
            print("文件库为空")


    def do_download(self,file):
        msg = f"RETR {file}"
        self.sock.send(msg.encode())
        result = self.sock.recv(128)
        if result == b'OK':
            f = open(file,"wb")
            while True:
                data = self.sock.recv(1024)
                if data ==b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

    def do_push_file(self,file):
        try:
            f = open(file,'rb')
        except:
            print("文件不存在")
            return
        else:
            msg = f"STOR {file}"
            self.sock.send(msg.encode())
            result = self.sock.recv(128)
            if result == b"OK":
                while True:
                    data = f.read(1024)
                    if not data:
                        sleep(0.1)
                        self.sock.send(b"##")
                        break
                    self.sock.send(data)
                f.close()
            else:
                print("文件存在")









def main():
    sock = socket()
    sock.connect(ADDR)
    ftp = FtpClient(sock)
    while True:
        print("=========命令选项========")
        print("          list          ")
        print("          get file      ")
        print("          put file      ")
        print("          exit          ")
        print("=========命令选项========")

        msg = input(">>")
        if msg == "list":
            ftp.do_list()
        elif msg[:3] == 'get':
            filename = msg.split(" ")[-1]
            print(filename)
            ftp.do_download(filename)
        elif msg[:3] == 'put':
            filename = msg.split(" ")[-1]
            print(filename)
            ftp.do_push_file(filename)
        elif msg[:3] == 'exit':
            ftp.do_exit()
            break


main()
