import random
from grid import Grid


class Player:
    def __init__(self, level, symbol):
        self.level = level
        self.symbol = symbol
        self.is_human = level == 'user'

    def input_coordinates(self, grid: Grid):
        if self.is_human:
            while True:
                coord = input('Enter the coordinates:')
                try:
                    i, j = [int(c) - 1 for c in coord.split()]
                except ValueError:
                    print('You should enter numbers!')
                    continue

                if 0 > i or i > grid.size - 1 or 0 > j or j > grid.size - 1:
                    print(f'Coordinates should be from 1 to {grid.size}!')
                    continue

                if grid.state[i][j].is_filled():
                    print('This cell is occupied! Choose another one!')
                    continue
                break
        else:
            print(f'Making move level "{self.level}"')
            empty_coordinates = grid.get_empty_cells_coordinates()
            i, j = random.choice(empty_coordinates)

        return (i, j)

    def make_move(self, grid: Grid):
        i, j = self.input_coordinates(grid)
        grid.state[i][j].fill(self.symbol)

    def is_winner(self, grid):
        return any(all(s.symbol == self.symbol for s in line) for line in grid.state) \
               or any(all(grid.state[j][i].symbol == self.symbol
                          for j in range(grid.size)) for i in range(grid.size)) \
               or all(grid.state[i][i].symbol == self.symbol for i in range(grid.size)) \
               or all(grid.state[i][grid.size - 1 - i].symbol == self.symbol for i in range(grid.size))
