"""
字节串类型演示
"""
#定义一个字节串数据
b1 = b"hello world" #英文字符
b2 = "弄好".encode() #utf8字符定义为字符串
b3 = "弄好,hello".encode()
print(type(b1))
print(b1)

print(type(b2))
print(b2)

print(type(b3))
print(b3)
print(b3.decode())
b3.decode().encode().decode().encode()
print(b'\xe5\xbc\x84\xe5\xa5\xfd'.decode())

