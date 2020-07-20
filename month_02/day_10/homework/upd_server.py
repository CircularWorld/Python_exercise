"""
作业 ： 1. 写一个程序，使用udp。
          要求，从客户端可以循环的输入单词，服务端查询到单词，讲
          单词的解释发送给客户端，让客户端打印

          单词通过数据表words查询

          思路： 客户端输入一个单词，发送一次，然后等接收，打印
                服务端，接收单词，查询单词 讲解释发送给客户端
"""
from socket import *
import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8'
                     )
# 创建游标 (游标对象负责调用执行sql 语句，操作数据，得到结果)
cur = db.cursor()

# 套接字创建
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定Ip
udp_socket.bind(('0.0.0.0', 8888))
# 获取信息
while True:
    data,addr = udp_socket.recvfrom(1024)
    print("接受的单词为：",data.decode())
    if not data:
        break
    try:
        sql = 'select mean from words where word = %s;'
        if not sql:
            mean = '单词不存在'
        cur.execute(sql,data.decode())
        mean = cur.fetchone()
        udp_socket.sendto(mean[0].encode(),addr)
    except Exception as e:
        print(e)
        db.rollback()



udp_socket.close()
