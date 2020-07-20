'''
输入课程阶段数,显示课程名称
1 显示 Python语言核心编程
2 显示 Python高级软件技术
3 显示 Web 全栈
4 显示 网络爬虫
5 显示 数据分析、人工智能
'''

stage = int(input('请输入阶段数：'))
if stage == 1:
    print('Python语言核心编程')
elif stage == 2:
    print('Python高级软件技术')
elif stage == 3:
    print('Web 全栈')
elif stage == 4:
    print('网络爬虫')
elif stage == 5:
    print('数据分析、人工智能')
else:
    print('输入有误！')
