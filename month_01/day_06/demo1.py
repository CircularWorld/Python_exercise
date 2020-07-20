# str = '我是话十大黄金时代和'
#
# print(str[len(str)-1:-1:-1])

# list02= ["全聚德", "大董"]
# print(list02)
# list02[::-1] = ["全", "大"]
# print(list02)

# x = 1;y = 3
# x,y = y,x
# print(x,y)

# tuple_01 = (1,)
# print(type(tuple_01))
# list_01 = [1,2,3]
# tuple_02 = tuple(list_01)
# print(tuple_02)
# str_01 = 'asdasd'
# a,*b = 'asdasd'
# print(type(a),type(b),a,b)
dict_01 = {'TS':100,'wk':900}
print(type(dict_01),dict_01)
tuple_01 = ('我爱',['1',2],('你爱','bs'))
dict_02 = dict(tuple_01)
print(dict_02)
for key,value in dict_02.items():
    print('key ＝',key)
    print('value=',value)



