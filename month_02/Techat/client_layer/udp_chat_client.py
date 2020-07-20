from socket import *
from multiprocessing import Pool
ADDR = ("0.0.0.0", 8888)
udp_socket = socket(AF_INET,SOCK_DGRAM)

FLAG = 0 # 0登录 1用户发信息
name = ''

def login():
    while True:
        # 登录
        global name
        name = input("请输入您的名称:")
        package = str((name,0,''))
        udp_socket.sendto(package.encode(), ADDR)
        msg = udp_socket.recv(1024)
        # print(msg.decode())
        if not msg:
            print("名称重复,请重新输入")
            continue
        else:
            print(msg.decode())
            break

def sendmsg():
    while True:
        data = input(name+"我说:")
        package = str((name,data))
        udp_socket.sendto(package.encode(), ("0.0.0.0", 8888))

def recivemsg():
    while True:
        msg = udp_socket.recv(1024)
        print(msg.decode())

def main():
    login()

    pool = Pool(4)

    pool.apply_async(func=sendmsg)
    pool.apply_async(func=recivemsg)

    pool.close()
    pool.join()


main()




