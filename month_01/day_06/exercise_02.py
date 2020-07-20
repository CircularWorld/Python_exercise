'''
将下列英文语句按照单词进行翻转.
To have a government that is of people by people for people

people for people by people of is that government a have To
"""
'''

words = 'To have a government that is of people by people for people'
list_words = str.split(" ")
words = ' '.join(list_words[::-1])
print(words)
