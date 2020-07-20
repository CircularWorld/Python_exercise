'''
9, 根据下列信息提取变量
   使用占位符拼接字符串·
    湖北确诊67802人,治愈63326人,治愈率0.93
	70秒是1分钟零10秒
'''
confirm_num = 67802
cure_num =63326
cure_rate = cure_num/confirm_num
print("""湖北确诊%d人,治愈%d人,治愈率%.2f""" % (confirm_num,cure_num,cure_rate))

time = int(input('请输入时间s：'))

print('%d秒是%.2d分钟零%.2d秒' % (time,time//60,time%60))