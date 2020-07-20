class GameControl:

    def __init__(self):
        self.__map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]
        self.list_merge = []

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, value):
        self.__map = value

    def zero_to_end(self):
        """
            零元素向后移动
            思想：从后向前判断，如果是0则删除,在末尾追加.
        """
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(0)

    def merge(self):
        """
            合并数据
              核心思想：零元素后移，判断是否相邻相同。如果是则合并.
        """
        self.zero_to_end()
        for i in range(len(self.list_merge) - 1):
            if self.list_merge[i] == self.list_merge[i + 1]:
                self.list_merge[i] += self.list_merge[i + 1]
                del self.list_merge[i + 1]
                self.list_merge.append(0)

    def move_left(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        :return:
        """
        for line in self.map:
            self.list_merge = line
            self.merge()

    # 4. 向右移动 move_right
    def move_right(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        :return:
        """
        for line in self.map:
            # 从右向左获取数据形成新列表
            self.list_merge = line[::-1]
            # 处理数据
            self.merge()
            # 将处理后的数据再从右向左还给map
            line[::-1] = self.list_merge

    # 5. 向上移动 move_up   转置  move_left　转置
    def square_matrix_transposition(self):
        """
            方阵转置（列转换为行）
        :param map: 需要转置的方阵
        :return:
        """
        for c in range(1, len(self.map)):  # 1 2 3
            for r in range(c, len(self.map)):
                self.map[r][c - 1], self.map[c - 1][r] = self.map[c - 1][r], self.map[r][c - 1]

    def move_up(self):
        """
            向上移动
            思想：  转置  move_left　转置　
        """
        self.square_matrix_transposition()
        self.move_left()
        self.square_matrix_transposition()

    # 6. 向下移动
    def move_down(self):
        """
            向下移动
            思想: 转置  move_right　转置
        :return:
        """
        self.square_matrix_transposition()
        self.move_right()
        self.square_matrix_transposition()
