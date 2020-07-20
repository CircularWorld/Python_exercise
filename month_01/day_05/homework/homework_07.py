'''
7. 判断一个字符串是否是回文
    例如：上海自来水来自海上
         山西运煤车煤运西山
    思路：正序与倒序相同
    提示：反向切片[::-1]
'''
words = input('请输入一句话判断是否为回文：')
if words:
    words_reverse = words[::-1]
    if words == words_reverse:
        print("回文")
    else:
        print("不是回文")
else:
    print('不能输入空')