# 定义函数,根据年月日计算星期数
# 结果：星期一
# 星期二
# ....
# 星期日
# 步骤:定义函数(函数名称/参数/返回值)
# 拼接年月日 --> 字符串 2020-6-17 %Y-%m-%d
# 字符串 --> 时间元组
# 时间元组 --> 星期
# 星期 --> 星期一
# 语法:时间元组 = time.strptime(时间字符串,格式)
import time
year = 2020
month = 6
day = 17
tuple_time = time.strptime(f"{year}/{month}/{day}","%Y/%m/%d")
dict_time = {0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日"}
print(dict_time[tuple_time[6]])