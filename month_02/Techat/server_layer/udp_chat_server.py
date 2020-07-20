from socket import *
from multiprocessing import Process, Pool, Queue  # 进程池 进程通信
import re

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(("0.0.0.0", 8888))

user_list = []


def isExists(name):
    global user_list
    print("isExists===",user_list)
    for user in user_list:
        # print(user_list)
        if name in user:
            return True
        else:
            return False


def userlogin():
    global user_list
    data, addr = udp_socket.recvfrom(1024)
    print(data.decode(),addr)
    name = re.findall(r"^\W+(\w+).+", data.decode())
    # 判断名字是否存在,不存在就加入,退出就删除
    if not isExists(name[0]):
        udp_socket.sendto(f"{name[0]}加入直播间".encode(), addr)
        user_list.append((name[0],addr))
        print(user_list)
        print(f"{name[0]}加入直播间")
    else:
        udp_socket.sendto("".encode(), addr)


def main():
    list_process = []
    while len(list_process)<10:
        p = Process(target=userlogin)
        list_process.append(p)
        p.start()

    for proc in list_process:
        proc.join()



if __name__ == '__main__':
    main()
