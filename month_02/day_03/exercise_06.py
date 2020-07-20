with open("file.txt","wb+") as f:
    f.write("你好，天\n".encode())
    f.write("你好，地\n".encode())
    f.flush()
    f.seek(0,0)
    data = f.read()
    print(data)