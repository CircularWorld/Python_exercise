"""
文件写操作
"""
f = open("file.txt", "w")

# n = f.write("无尽之海\n")
# print("写入了%d个字符" % n)
#
# n = f.write("黑暗深渊")
# # print("写入了%d个字符" % n)
# n = f.write(b"hello word\n")
# print("写入了%d个字节" % n)
# n = f.write(b"hello Kitty\n")
# print("写入了%d个字节" % n)
list_word = ["天之道\n","损有余而补不足"]
f.writelines(list_word)
f.close()
