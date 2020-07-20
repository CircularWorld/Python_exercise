try:
    f = open("file.txt", "ab")
except FileNotFoundError:
    print("没有文件进行创建")
    f = open("file.txt", "w")
    # raise Exception("文件不存在")


f.close()
