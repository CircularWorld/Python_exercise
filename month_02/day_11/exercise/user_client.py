from socket import *

tcp_socket = socket()
tcp_socket.connect(("127.0.0.1",8888))

while True:
    msg  = input("我:")
    if not msg:
        break
    tcp_socket.send(msg.encode())

    data = tcp_socket.recv(1024)
    print("小美:",data.decode())

tcp_socket.close()

