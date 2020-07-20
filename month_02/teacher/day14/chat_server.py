"""
author: Levi
email: lvze@tedu.cn
time: 2020-7-14
env: Python3.6
socket and Process exercise
"""
from socket import *

# 服务器使用地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)

# 存储用户 {name:address ...}
user = {}

# 处理进入聊天室
def do_login(sock,name,address):
    if name in user:
        sock.sendto(b"FAIL",address)
        return
    else:
        sock.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
        # 存储用户
        user[name] = address
        print(user)

# 处理聊天
def do_chat(sock,name,content):
    msg = "%s : %s"%(name,content)
    for i in user:
        # 刨除本人
        if i != name:
            sock.sendto(msg.encode(),user[i])

# 处理退出
def do_exit(sock,name):
    del user[name]  # 移除此人
    # 通知其他人
    msg = "%s 退出聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])

# 启动函数
def main():
    sock = socket(AF_INET,SOCK_DGRAM)  # UDP套接字
    sock.bind(ADDR)

    # 循环接收来自客户端请求
    while True:
        # 接收请求 (所有用户的所有请求)
        data,addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ',2) # 对请求内容进行解析
        # 根据请求调用不同该函数处理
        if tmp[0] == 'L':
            # tmp ==> [L,name]
            do_login(sock,tmp[1],addr) # 处理用户进入聊天具体事件
        elif tmp[0] == 'C':
            # tmp==>[C,name,xxxxxxx]
            do_chat(sock,tmp[1],tmp[2])
        elif tmp[0] == 'E':
            # tmp==>[E,name]
            do_exit(sock,tmp[1])

if __name__ == '__main__':
    main()





