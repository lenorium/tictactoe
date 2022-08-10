"""
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
"""
import random

X_SYMBOL = 'X'
O_SYMBOL = 'O'
EMPTY_CELL = ' '


class Game:
    def __init__(self, grid):
        self.grid = grid

    def is_finished(self):
        winner = self.get_winner()
        if winner is not None:
            print(f'{winner} wins')
            return True

        filled_cells = [s for line in self.grid.state for s in line if s != EMPTY_CELL]
        if len(filled_cells) == self.grid.total_size:
            print('Draw')
            return True

        return False

    def get_winner(self):
        players = {X_SYMBOL, O_SYMBOL}
        for symbol in players:
            if any(all(s == symbol for s in line) for line in self.grid.state) \
                    or any(all(self.grid.state[j][i] == symbol
                               for j in range(self.grid.size)) for i in range(self.grid.size)) \
                    or all(self.grid.state[i][i] == symbol for i in range(self.grid.size)) \
                    or all(self.grid.state[i][self.grid.size - 1 - i] == symbol for i in range(self.grid.size)):
                return symbol
        return None


class Grid:
    side = 3
    total_size = side ** 2

    def __init__(self):
        init_state = [EMPTY_CELL] * self.total_size
        self.state = [init_state[i: i + self.side] for i in range(0, self.total_size, self.side)]

    def print(self):
        print('---------')
        [print('|', *line, '|') for line in self.state]
        print('---------')


class Player:
    def __init__(self, level, symbol):
        self.level = level
        self.symbol = symbol
        self.is_human = level == 'user'

    def make_move(self, grid: Grid):
        if self.is_human:
            while True:
                coord = input('Enter the coordinates:')
                try:
                    i, j = [int(c) - 1 for c in coord.split()]
                except ValueError:
                    print('You should enter numbers!')
                    continue

                if 0 > i or i > grid.side - 1 or 0 > j or j > grid.side - 1:
                    print(f'Coordinates should be from 1 to {grid.side}!')
                    continue

                if grid.state[i][j] != EMPTY_CELL:
                    print('This cell is occupied! Choose another one!')
                    continue
                break
        else:
            print(f'Making move level "{self.level}"')
            empty_coordinates = [[i, j] for i in range(grid.side)
                                 for j in range(grid.side) if grid.state[i][j] == EMPTY_CELL]
            i, j = random.choice(empty_coordinates)

        grid.state[i][j] = self.symbol


def play():
    grid = Grid()
    grid.print()

    game = Game(grid)

    player1 = Player('user', X_SYMBOL)
    player2 = Player('easy', O_SYMBOL)

    current_player = None
    while not game.is_finished():
        current_player = player2 if current_player == player1 else player1
        current_player.make_move(grid)
        grid.print()


if __name__ == '__main__':
    play()
