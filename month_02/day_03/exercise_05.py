with open("file.txt","w") as f:
    while True:
        data = input(">>")
        if not data:
            break
        # f.write(data+'\n')
        f.write(data)
        # f.flush()
