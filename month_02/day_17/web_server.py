"""
Web 服务程序
用户有一组网页，希望使用我们提供的类快速搭建一个服务，实现
自己网页的展示浏览

IO 多路复用和 http训练
"""

from socket import *
from select import select
import re


class WebServer:
    def __init__(self, host='0.0.0.0', port=8000, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.__rlist = []
        self.__wlist = []
        self.__xlist = []
        self.create_sock()
        self.bind()

    def create_sock(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)
        # self.sock.listen()

    def send_response(self, info, connfd):
        if info == '/':
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        try:
            f = open(filename, 'rb')
        except:
            response = "HTTP/1.1 404 FALSE\r\n"
            response += "Content-Type text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry...<h1>"
            response = response.encode()
        else:
            data = f.read()
            response = "HTTP/1.1 200 OK\r\n"
            response +="Content-Type text/html\r\n"
            response +="Content-length:%d\r\n" % len(data)
            response +="\r\n"
            response  = response.encode() +data
        finally:
            connfd.send(response)


    def handle(self, connfd):
        data = connfd.recv(1024 * 10)  # 客户端发送请求
        if  data:
            pattern = "[A-Z]+\s+(?P<info>/\S*)"
            info = re.match(pattern, data.decode())
            print("info: ", info.group("info"))
            self.send_response(info.group('info'), connfd)
        else:
            self.__rlist.remove(connfd)
            connfd.close()

    def start(self):
        self.sock.listen(5)
        print("Listen port :", self.port)
        self.__rlist.append(self.sock)
        while True:
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = self.sock.accept()
                    print("客户端: ", addr)
                    connfd.setblocking(False)
                    self.__rlist.append(connfd)
                else:
                    self.handle(r)  # 处理请求


if __name__ == '__main__':
    web = WebServer(host='0.0.0.0', port=8005, html="./static")
    web.start()
