"""
练习1：使用input输入一个单词，打印出这个单词的解释
，如果没有这个单词则打印"没有找到该单词"
* 每个单词占一行
* 单词与解释之间有空格
* 单词按照从小到大排列
"""
f= open("dict.txt","r")
list_data = f.readlines()
# print(list_data[1:4])
dict_data=dict()
for item in list_data:
    data_temp = []
    w = item.split(" ",2)
    print(w)
    for i in range(1,len(w)):
        if not w[i]:
            data_temp.append(w[i])
    str_temp = " ".join(data_temp)
    print(str_temp)
    dict_data[w[0]] = str_temp

# print(dict_data)
f.close()