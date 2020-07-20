from socket import *

f=  open("landscape.jpg", 'rb')


# with open('new.jpg','wb') as f:
#     f.write(img)
tcp_socket = socket()

tcp_socket.connect(("127.0.0.1", 8887))
while True:
    data = f.read(1024)
    if not data:
        break
    tcp_socket.send(data)

data = tcp_socket.recv(1024)
print(data.decode())

tcp_socket.close()
