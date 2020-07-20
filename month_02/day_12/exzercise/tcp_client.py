from socket import  *

tcp_socket = socket(AF_INET,SOCK_STREAM)

tcp_socket.connect(('0.0.0.0',8888))
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

    msg = tcp_socket.recv(1024)
    print("返回:",msg.decode())

tcp_socket.close()