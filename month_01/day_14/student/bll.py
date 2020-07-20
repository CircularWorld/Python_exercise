class StudentController:
    """
        学生控制器
            负责处理业务逻辑
    """

    def __init__(self):
        self.__list_students = []
        self.__start_sid = 1001

    # 只读属性
    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu):
        stu.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_students.append(stu)
