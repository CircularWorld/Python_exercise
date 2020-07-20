'''
11.在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
   提示：使用字典存储数据
'''
dict_color = {"R": "红色", "G": "绿色", "B": "蓝色", "A": "透明度"}
color_in = input("请输入颜色(RGBA)：")
if color_in in dict_color:
    print(f"{dict_color[color_in]}存在")
else:
    print("不存在")