from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)

udp_socket.bind(("0.0.0.0",8888))

# udp_socket.accept()
while True:
    data,addr = udp_socket.recvfrom(1024)
    print(addr[1],data.decode())
    udp_socket.sendto("谢谢:".encode(),addr)
