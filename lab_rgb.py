from random import randint


class Cell:
    def __init__(self, value, group):
        self.__value = value
        self.__group = group

    def get_value(self):
        return self.__value

    def get_group(self):
        return self.__group

    def set_value(self, value):
        self.__value = value

    def set_group(self, group):
        self.__group = group

    def is_wall(self):
        if self.__value == 0:
            return True
        else:
            return False


class Labyrinth:
    def __init__(self, size):
        if size % 2 == 0:
            self.__size = size + 1
        else:
            self.__size = size
        self.__data = []
        self.__generated = False

    def generate_labyrinth(self):
        group_counter = 1
        for line in range(self.__size):
            tmp = []
            if line % 2 == 1:
                for colum in range(self.__size):
                    if colum % 2 == 1:
                        tmp.append(Cell((randint(50, 250), randint(50, 250), randint(50, 250)), group_counter))
                        group_counter = group_counter + 1
                    else:
                        tmp.append(Cell((0, 0, 0), 0))
            else:
                for colum in range(self.__size):
                    tmp.append(Cell((0, 0, 0), 0))
            self.__data.append(tmp)

        while group_counter > 2:
            direction = randint(1, 4)

            # 1 left
            # 2 right
            # 3 up
            # 4 down

            if direction == 1:
                x = randint(3, self.__size - 2)
                y = randint(1, self.__size - 2)

                if x % 2 == 0:
                    x = x + 1
                if y % 2 == 0:
                    y = y + 1

                position_cell_one = [x, y]
                position_cell_two = [x - 2, y]
                position_wall = [x - 1, y]
            elif direction == 2:
                x = randint(1, self.__size - 4)
                y = randint(1, self.__size - 2)

                if x % 2 == 0:
                    x = x + 1
                if y % 2 == 0:
                    y = y + 1

                position_cell_one = [x, y]
                position_cell_two = [x + 2, y]
                position_wall = [x + 1, y]
            elif direction == 3:
                x = randint(1, self.__size - 2)
                y = randint(3, self.__size - 2)

                if x % 2 == 0:
                    x = x + 1
                if y % 2 == 0:
                    y = y + 1

                position_cell_one = [x, y]
                position_cell_two = [x, y - 2]
                position_wall = [x, y - 1]
            else:
                x = randint(1, self.__size - 2)
                y = randint(1, self.__size - 4)

                if x % 2 == 0:
                    x = x + 1
                if y % 2 == 0:
                    y = y + 1

                position_cell_one = [x, y]
                position_cell_two = [x, y + 2]
                position_wall = [x, y + 1]

            if not self.__data[position_cell_one[0]][position_cell_one[1]].get_group() == self.__data[position_cell_two[0]][position_cell_two[1]].get_group():
                tmp_group = self.__data[position_cell_one[0]][position_cell_one[1]].get_group()
                tmp_value = self.__data[position_cell_one[0]][position_cell_one[1]].get_value()
                tmp_group2 = self.__data[position_cell_two[0]][position_cell_two[1]].get_group()
                tmp_value2 = self.__data[position_cell_two[0]][position_cell_two[1]].get_value()
                for line in range(self.__size - 1):
                    for colum in range(self.__size - 1):
                        if tmp_group2 == self.__data[line][colum].get_group():
                            self.__data[line][colum].set_group(tmp_group)
                            self.__data[line][colum].set_value(tmp_value)
                self.__data[position_cell_two[0]][position_cell_two[1]].set_group(tmp_group)
                self.__data[position_cell_two[0]][position_cell_two[1]].set_value(tmp_value)
                self.__data[position_wall[0]][position_wall[1]].set_group(tmp_group)
                self.__data[position_wall[0]][position_wall[1]].set_value(tmp_value)
                group_counter = group_counter - 1

    def generate_exit(self):
        self.__data[self.__size - 1][self.__size - 2] = Cell(255, -1)

    def generate_enter(self):
        self.__data[0][1] = Cell(255, -1)

    def get_data(self):
        tmp = []
        for line in range(self.__size):
            tmp_line = []
            for colum in range(self.__size):
                tmp_line.append(self.__data[line][colum].get_value())
            tmp.append(tmp_line)
        return tmp
