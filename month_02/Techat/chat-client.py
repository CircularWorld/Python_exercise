"""
发送请求,得到结果
通信协议
    L 登录    name
    C 发信息   msg
    E 退出
"""
from socket import *
from multiprocessing import Process
import sys

# ADDR = ('127.0.0.1', 8000)
ADDR = ('124.70.156.125', 8000)


# 请求进入聊天室 OK FAIL
def login(sock):
    while True:
        name = input("Name:")
        msg = 'L ' + name  # 根据通信协议整理发送信息
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result.decode() == 'OK':
            print("你已进入聊天室")
            return name
        else:
            print("您的名字太受欢迎,换一个吧")


def send_msg(sock, name):
    while True:
        try:
            msg = input("我:")
        except KeyboardInterrupt:
            msg = 'exit'
        if msg == 'exit':
            data = "E " + name
            sock.sendto(data.encode(), ADDR)
            sys.exit("您已退出聊天室")
        data = 'C %s %s' % (name, msg)
        sock.sendto(data.encode(), ADDR)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(2048)
        print('\n'+data.decode()+"\n我:",end = '')


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("192.168.137.154",5826))
    # sock.sendto(b"test", ADDR)
    name = login(sock)
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True
    p.start()
    send_msg(sock, name)
    # p.join()


if __name__ == '__main__':
    main()
