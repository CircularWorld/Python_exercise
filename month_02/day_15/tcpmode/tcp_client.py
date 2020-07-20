from socket import *

IP ='0.0.0.0'
PORT = 8888
ADDR = (IP,PORT)


sock = socket()
sock.connect(ADDR)

while True:
    msg = input(">>")
    if not msg:
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()