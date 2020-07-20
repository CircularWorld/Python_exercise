from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)

while True:
    msg= input(">>")
    udp_socket.sendto(msg.encode(),("0.0.0.0",8888))
    # data = udp_socket.recv(1024)
    data ,addr = udp_socket.recvfrom(1024)
    print(addr,data.decode())
