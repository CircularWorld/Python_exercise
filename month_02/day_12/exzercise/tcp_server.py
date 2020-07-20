'''
客户端端收发信息
'''
from  socket import *
from multiprocessing import  *
#TCP套接字
tcp_socket  = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen()


def connect():
    while True:
        print("等待链接...")
        global tcp_socket
        connfd,addr = tcp_socket.accept()
        print('地址:',addr)
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            print(addr[1],data.decode())
            msg = 'Thanks'
            connfd.send(msg.encode())
        connfd.close()

#进程创建
p  = Process(target=connect)
p.start()
connect()
p.join()

tcp_socket.close()