with open("file.txt","rb+") as f:
    data = f.read(10)
    print(data)
    f.write(b"hello")