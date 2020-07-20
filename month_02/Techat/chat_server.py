"""
author: jiayuhao
email: jiayuhaowork@163.com
time: 2020-7-14
env: Python3.6
socket and Process exercise

1.建立udp网络套接字
2.循环接收来自客户端的请求
3.根据请求调用不同的函数去解决

"""
from socket import *
from multiprocessing import Process

# 服务器使用地址
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

# 存储用户 {name:address, ...}
user = {}


def do_login(sock, name, address):
    if name in user or '管理' in name:
        sock.sendto(b"FAIL", address)
        return
    else:
        sock.sendto(b'OK', address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for i in user:
            sock.sendto(msg.encode(), user[i])
        # 存储用户
        user[name] = address
        print(user)


def do_chat(sock, name, content):
    # 将信息发送给所有用户
    msg = "%s : %s" % (name, content)
    # print(msg)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])


def do_exit(sock, name):
    del user[name]
    msg = '%s 退出了聊天室' % name
    for i in user:
        sock.sendto(msg.encode(), user[i])


def handle(sock):
    # 循环接受所有客户端请求
    while True:
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ', 2)  # 对请求内容进行解析 从左向右切割

        # 根据请求调用不同函数处理
        # print(data)
        if tmp[0] == 'L':
            # tmp==>[L,name]
            do_login(sock, tmp[1], addr)  # 处理用户进入聊天具体事件
        elif tmp[0] == 'C':
            do_chat(sock, tmp[1], tmp[2])  # 发送信息给所有人 某:msg
        elif tmp[0] == 'E':
            do_exit(sock, tmp[1])


# 搭建启动函数
def main():
    # udp 套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    # 创建一个进程分担功能
    p = Process(target=handle, args=(sock,))
    p.daemon = True
    p.start()
    # 父进程发送管理员消息
    while True:
        content = input("管理员消息:")
        # 服务端退出
        if content == 'quit':
            break
        # 进程间通信
        data = 'C 管理员消息 ' + content
        sock.sendto(data.encode(), ADDR)


if __name__ == '__main__':
    main()
