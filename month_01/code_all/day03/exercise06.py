"""
    输入课程阶段数,显示课程名称
    1 显示 Python语言核心编程
    2 显示 Python高级软件技术
    3 显示 Web 全栈
    4 显示 网络爬虫
    5 显示 数据分析、人工智能
"""
def num_to_course(number):
    """
    根据数字计算课程
    :param number:和课程相对应的数字
    :return: 返回课程
    """
    dict_course = {1:"Python语言核心编程",
                   2:"Python高级软件技术",
                   3:"Web全栈",
                   4:"网络爬虫",
                   5:"数据分析、人工智能"
                  }
    return dict_course[number]

print(num_to_course(3))


# if number == "1":
#     print("Python语言核心编程")
# if number == "2":
#     print("Python高级软件技术")
# if number == "3":
#     print("Web全栈")
# if number == "4":
#     print("网络爬虫")
# if number == "5":
#     print("数据分析、人工智能")
