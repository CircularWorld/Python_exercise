from bll import GameControl


class Game2048View:
    def __init__(self):
        self.__control = GameControl()

    def print_map(self):
        for item in self.__control.map:
            for value in item:
                print(value, end=" | ")
            print()
        # print(self.__control.map)

    def select_direction(self):
        direction = input("请输入方向wasd:")
        if direction == 'w':
            self.__control.move_up()
        elif direction == 's':
            self.__control.move_down()
        elif direction == 'a':
            self.__control.move_left()
        elif direction == 'd':
            self.__control.move_right()

    def main(self):
        while True:
            self.print_map()
            self.select_direction()
