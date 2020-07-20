"""
    第一次送给女友的生日礼物
    理论知识：
        1. 注释：给人看的,计算机不看。
        2. 导入：使用别人的代码
               from 文件 import 内容
        3. 函数-功能
            写法1：
                制作功能
                    def 函数名称():
                        函数体

                使用功能
                    函数名称()
            写法2：
                参数:使用功能时给制作功能时传递的信息
                制作功能
                    def 函数名称(参数1,参数2,参数3):
                        函数体

                使用功能
                    函数名称(数据1,数据2,数据3)
            写法3：
                制作功能
                    def 函数名称(参数1,参数2,参数3):
                        函数体

                使用功能
                    函数名称(数据1,参数3 = 数据3)
"""
from pyecharts.charts import WordCloud
# 准备和女友说的话
from greetings import words

# 创建词云图
wc = WordCloud()
# 使用词云图的添加功能(需要呈现的内容和图片)
wc.add("", words, word_size_range=[12, 12], mask_image="heart.jpg")
wc.render()