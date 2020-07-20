"""
练习2：
通过input输入一个目录（目录中有很多文件可能有文件夹），
删除这个目录中所有大小小于10字节的普通文件
"""
import os
path_input = input("请输入一个目录：　")
print(os.listdir(path_input))
list_file = os.listdir(path_input)
for f in list_file:
    if os.path.isfile(path_input+'/'+f) and os.path.getsize(path_input+'/'+f) <10:
        os.remove(path_input+'/'+f)

print(os.listdir(path_input))

