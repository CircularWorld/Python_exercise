"""
      2. 编写一个函数，参数传入一个设备端口名称
         返回值是这个端口描述中所对应的 address
         信息

         思路： 根据端口名确定段落
               再从段落中匹配目标

         提示： 段与段之间有空行
               每段第一个单词是端口名称
               端口名称可能很复杂
"""
import re


def get_device_address(device):
    list_paras = get_split_data()
    for para in list_paras:
        # data = re.findall("^.+\S\s?", para)
        data = re.match("\S+", para).group()#非空字符
        # print(type(data))
        if device in str(data):
            # print(str(data))
            s = str(para)
            address = re.search(r"\w{4}\.\w{4}\.\w{4}", s).group()
            return address
    return False


def get_txt_string():
    """
    获取文本字符串
    :return: 返回文本字符串
    """
    f = open("log.txt", "r")
    data = f.read()
    f.close()
    return data


def get_split_data():
    """
    分割段落
    :return: 返回段落列表
    """
    data = get_txt_string()
    return re.split(r"\n\n", data)


# print(get_device_address("BVI1"))

def main():
    device = input("请输入设备名称：")
    address = get_device_address(device)
    if address:
        print("设备地址为:", address)
    else:
        print("设备不存在")


if __name__ == '__main__':
    main()
