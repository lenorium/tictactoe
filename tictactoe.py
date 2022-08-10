"""
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
"""
import random

X_SYMBOL = 'X'
O_SYMBOL = 'O'
EMPTY_CELL = ' '
GRID_SIZE = 3


class Cell:
    def __init__(self):
        self.symbol = EMPTY_CELL
        self.is_used = False

    def __str__(self):
        return f'{self.symbol}'

    def fill(self, symbol):
        self.symbol = symbol
        self.is_used = True

    def is_filled(self):
        return self.is_used


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


class Game:
    def __init__(self, grid, player1, player2):
        self.grid = grid
        self.player1 = player1
        self.player2 = player2

    def is_finished(self):
        winner = self.get_winner()
        if winner is not None:
            print(f'{winner.symbol} wins')
            return True

        empty_cells = self.grid.get_empty_cells_coordinates()
        if len(empty_cells) == 0:
            print('Draw')
            return True

        return False

    def get_winner(self) -> Player:
        return next(filter(lambda p: p.is_winner(self.grid), (self.player1, self.player2)), None)

    def run(self):
        self.grid.print()
        current_player = None
        while not self.is_finished():
            current_player = self.player2 if current_player == self.player1 else self.player1
            current_player.make_move(self.grid)
            self.grid.print()


if __name__ == '__main__':
    grid = Grid(GRID_SIZE)

    player1 = Player('user', X_SYMBOL)
    player2 = Player('easy', O_SYMBOL)

    game = Game(grid, player1, player2)
    game.run()
