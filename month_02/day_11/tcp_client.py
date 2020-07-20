from socket import *

# tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket = socket()

tcp_socket.connect(("127.0.0.1",8888))
while True:
    msg  = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

    data = tcp_socket.recv(1024)
    print("From server: ",data.decode())

tcp_socket.close()