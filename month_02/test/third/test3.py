"""
3.输入一个正数n，输出所有和为n 连续正数序列。（20分）
    例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。
"""

#
# def get_sequence(n):
#     if n <3:
#         return
#     list_sequence = []
#     for i in range(1, n):
#         res = 0
#         start = i
#         while i<(n+1)//2: #当大于(n+1)//2 时结束
#             if res < n:
#                 res += i
#                 i += 1
#             elif res == n:
#                 end = i-1
#                 list_sequence.append((start, end))
#                 break
#             else:
#                 break
#     return list_sequence
#
#
# print(get_sequence(3))


def find_continuous_seq(n):
    if n<3:
        return
    small = 1
    big = 2
    sum = small+big
    while small < (n+1)//2:
        if sum == n:
            print_continuous_seq(small,big)
        while sum>n:
            #如果序列累加的和比n大  将small向前移动
            sum -= small
            small += 1
            if sum == n:
                print_continuous_seq(small,big)
        big += 1
        sum += big

def print_continuous_seq(small,big):
    for i in range(small,big+1):
        print(i,end=' ')
    print()

find_continuous_seq(15)
