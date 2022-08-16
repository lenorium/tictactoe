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
        return [[i, j] for i in range(self.size)
                for j in range(self.size) if not self.state[i][j].is_used()]

    def is_in_range(self, i, j):
        return 0 <= i or i < self.size and 0 <= j or j < self.size

    def is_occupied(self, i, j):
        return self.state[i][j].is_used()
