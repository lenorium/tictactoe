from cell import Cell


class Grid:
    def __init__(self, size: int):
        self.__size = size
        self.__state = [[Cell(i, j) for j in range(size)] for i in range(size)]

    @property
    def state(self):
        return self.__state

    @property
    def size(self):
        return self.__size

    def update(self, row, col, symbol):
        if self.is_valid_coord(row, col):
            self.__state[row][col].symbol = symbol

    def print(self):
        print('---------')
        [print('|', *line, '|') for line in self.__state]
        print('---------')

    def get_empty_cells_coordinates(self):
        return [[i, j] for i in range(self.__size)
                for j in range(self.__size) if not self.__state[i][j].is_used]

    def is_empty(self):
        return all(not s.is_used for line in self.__state for s in line)

    def is_full(self):
        return all(s.is_used for line in self.__state for s in line)

    def is_in_range(self, row, col):
        return 0 <= row or row < self.size and 0 <= col or col < self.__size

    def is_occupied(self, row, col):
        return self.__state[row][col].is_used

    def is_valid_coord(self, row, col):
        if (row is None or col is None) or not self.is_in_range(row, col):
            print(f'Coordinates should be from 1 to {self.__size}!')
            return False
        if self.is_occupied(row, col):
            print('This cell is occupied! Choose another one!')
            return False
        return True

