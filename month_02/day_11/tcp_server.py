from socket import *

# 创建tcp套接字   参数默认为tcp协议
tcp_socket = socket(AF_INET, SOCK_STREAM)
#绑定
tcp_socket.bind(('0.0.0.0', 8888))

# 设置监听 将套接字设置为监听套接字，确定监听队列大小
tcp_socket.listen(5)
while True:
    # 等待处理客户端链接 阻塞函数
    print("Waiting for connect ...")
    connfd, addr = tcp_socket.accept()
    print("Connect from,", addr)  # 打印客户端地址
    data = True
    # 等待接收 阻塞函数
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Recv:", data.decode())
        msg = '服务器返回'
        n = connfd.send(msg.encode())
    #关闭
    connfd.close()#客户端退出,对应的客户套接字无用了
tcp_socket.close()