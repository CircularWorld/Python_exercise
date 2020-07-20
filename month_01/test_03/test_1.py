"""
创建函数，生成指定行数的杨辉三角。
杨辉三角：
每行端点与结尾的数为1，每个数是它左上方和右上方的数的和
输入：6
输出：
     [
                [1],
               [1, 1],
              [1, 2, 1],
             [1, 3, 3, 1],
           [1, 4, 6, 4, 1],
         [1, 5, 10, 10, 5, 1]
     ]
     杨辉三角的两个腰边的数都是 1，其它位置的数都是上顶上两个数之和。这就是我们用C语言写杨辉三角的关键之一
     print("|","Ursula".center(20),"|")
"""

def get_yanghui_triangle(row_num):


    for r in range(row_num):
        list_temp = []
        for c in range(r+1):
            if r>1  and c > 0 and c <len(list_triangle[r-1]):
                num  = list_triangle[r-1][c-1] + list_triangle[r-1][c]
                list_temp.append(num)
            else:
                list_temp.append(1)
        list_triangle.append(list_temp)


def print_yanghui_triangle():
    for item in list_triangle:
        print(item)
        # print("|", "Ursula".center(20), "|")

list_triangle = []
get_yanghui_triangle(7)
print_yanghui_triangle()
# print(list_triangle)

