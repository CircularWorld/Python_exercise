"""

"""
import re

filename = 'studentinfo.txt'


def menu():
    print('''|============功能菜单＝＝＝＝＝＝＝＝
|    1 录入学生信息　　　　　　　　　｜　　
|    2 查找学生信息　　　　　　　　　｜　　
|    3 删除学生信息　　　　　　　　　｜　　
|    4 修改学生信息　　　　　　　　　｜　　
|    5 排序　　　　　　　　　　　　　｜
|    6 统计学生总人数　　　　　　　　｜　　　
|    7 显示所有学生信息　　　　　　　｜　　　　
|    0 退出系统　　　　　　　　　　　｜
|＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
|   说明：通过数字键选择菜单　　　　
－－－－－－－－－－－－－－－－－－－
''')


def main():
    ctrl = True
    dict_func = {"1": insert, '2': search, '3': delete, '4': modify, '5': sort, '6': total, '7': show}
    while ctrl:
        menu()
        option = input('请输入你的选择：')
        option_str = re.sub('\D', '', option)
        if option_str in ['0', "1", '2', '3', '4', '5', '6', '7']:
            if option_str == '0':
                ctrl = False
            else:
                dict_func[option_str]()


def insert():
    list_student = []
    mark = True
    while mark:
        id = input("请输入ID(如 1001) :")
        if not id :
            break
        name = input("请输入名字 :")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩 :"))
            python = int(input("请输入python成绩 :"))
            c_language = int(input("请输入Ｃ语言成绩 :"))
        except:
            print("输入无效，不是整型数值．．．．重新录入信息")
            continue
        student = {'id':id,'name':name,'englist':english,"python":python,"c_language":c_language}
        list_student.append(student)
        inputMark = input("是否继续添加？（y/n）: ")
        inputMark = re.sub("\W",'',inputMark)
        if inputMark == 'n':
            mark = False
            save(list_student)


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    with open(filename,'r'):

        pass

def save(list_student):
    with open(filename,"a") as f:
        for info in list_student:
            f.write(str(info)+'\n')

main()
