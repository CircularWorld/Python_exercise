from socket import *
# 服务端地址
ADDR = ('127.0.0.1',8888)
udp_socket = socket(AF_INET,SOCK_DGRAM)
# 绑定本机
# udp_socket.bind(("0.0.0.0",7777))
while True:
    word = input("请输入单词： ")
    udp_socket.sendto(word.encode(),ADDR)
    if not word:
        break
    data,addr = udp_socket.recvfrom(1024)
    print(data.decode())

udp_socket.close()