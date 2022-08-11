from cell import Cell


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.state = [[Cell() for i in range(size)] for j in range(size)]

    def print(self):
        print('---------')
        [print('|', *line, '|') for line in self.state]
        print('---------')

    def get_empty_cells_coordinates(self):
        return [[i, j] for i in range(self.size) for j in range(self.size) if not self.state[i][j].is_filled()]
