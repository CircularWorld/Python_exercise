from socket import *
# 文件 时间
import time



# TCP
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0', 8887))
tcp_socket.listen(5)

# 等待连接
while True:
    print("等待连接...")
    connfd, addr = tcp_socket.accept()
    print(addr)

    while True:
        data = connfd.recv(1024)
        if not data:
            break
    sql = time.localtime()
    # print(sql)
    f = open(f"{sql.tm_year}-{sql.tm_mon}-{sql.tm_mday}.jpg", 'wb')

    f.write(data)
    connfd.send('上传成功'.encode())
    f.flush()
    f.close()
    connfd.close()

tcp_socket.close()
