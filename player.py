import random
from grid import Grid


class Player:
    def __init__(self, level, symbol):
        self.level = level
        self.symbol = symbol
        self.is_human = level == 'user'

    def input_coordinates(self, grid: Grid):
        while True:
            coord = input('Enter the coordinates:')
            try:
                i, j = [int(c) - 1 for c in coord.split()]
            except ValueError:
                print('You should enter numbers!')
                continue

            if not grid.is_in_range(i, j):
                print(f'Coordinates should be from 1 to {grid.size}!')
                continue

            if grid.is_occupied(i, j):
                print('This cell is occupied! Choose another one!')
                continue
            return (i, j)

    def make_move(self, grid: Grid):
        if self.is_human:
            i, j = self.input_coordinates(grid)
        else:
            print(f'Making move level "{self.level}"')
            empty_coordinates = grid.get_empty_cells_coordinates()
            i, j = random.choice(empty_coordinates)
        grid.state[i][j].symbol = self.symbol

    def is_winner(self, grid):
        return any(all(s.equals(self.symbol) for s in line) for line in grid.state) \
               or any(all(grid.state[j][i].equals(self.symbol)
                          for j in range(grid.size)) for i in range(grid.size)) \
               or all(grid.state[i][i].equals(self.symbol) for i in range(grid.size)) \
               or all(grid.state[i][grid.size - 1 - i].equals(self.symbol) for i in range(grid.size))
