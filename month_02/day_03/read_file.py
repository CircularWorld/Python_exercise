f = open("file.txt", "r")
# while True:
#     data = f.read(1024)
#     print(data,end = '')
#     if not data:
#         break
# data  = f.readline(10)
# print("读一行：",data)
# data  = f.readline()
# print(data)
# list_data = f.readlines(30)
# print(list_data)
# print(len(list_data))
for line in f:
    print(line,end = "")

f.close()
# print(type(data))

