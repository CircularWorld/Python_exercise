f = open("dict.txt","r")
word = input("please input: ")

for line in f:
    w = line.split(" ",3)
    print(w)
    if w[0] > word:
        print("未找到")
    elif word == w[0]:
        print(w[-1].strip())
        break
    else:
        print("未找到")#zzzz