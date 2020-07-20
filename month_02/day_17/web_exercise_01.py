from socket import *

s = socket()
s.bind(("0.0.0.0", 9997))
s.listen()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
f = open("index.html", "r")
info = f.read()
f.close()

while True:
    c, addr = s.accept()
    print("Connect from", addr)
    data = c.recv(4096)
    print(data.decode().split("\r\n")[0])
    # html = "HTTP/1.1 200 OK\r\n"
    # html+= "Content-Type:text/html\r\n\n"
    # html+=info
    html= """HTTP/1.1 200 OK
    Content-Type:text/html
    
    %s
    """ % info

    c.send(html.encode())
    c.close()

s.close()
