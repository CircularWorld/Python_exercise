# 给你一个长度为n的数组，
# 其中 只有一个 数字出现大于n/2次，
# 问如何快速找到这个数字（20分）

listnum = [1,4,5,5,5,5,5,7,7]

# def get_num(listnum):
#
#     dictnum = dict()
#
#     for num in listnum:
#         if num in dictnum:
#             dictnum[num]+=1
#             if dictnum[num] > len(listnum)/2:
#                 return num
#         else:
#             dictnum[num]=1

def get_num(listnum):
    # return sorted(listnum)[len(listnum)//2]
    return sorted(listnum)



print(get_num(listnum))