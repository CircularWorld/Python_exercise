'''
6. 计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
    字符串列表：words =["qtx","看一看","想啊想","练练"]
    结果:2
'''
words =["qtx","看一看","想啊想","练练"]
count =0
for temp in words:
    if len(temp)>2 and temp[0] == temp[-1]:
        count+=1
        # print(temp)
print(count)