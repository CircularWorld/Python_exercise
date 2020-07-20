'''
9.将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
  注意：列表中包含非字符串数据
'''
list_words = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
list_words = [str(list_words[i]) for i in range(len(list_words))]
# print(list_words)
words = ''.join(list_words)
print(words)
