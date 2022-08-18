from grid import Grid
from player import Player
from game import Game
from levels import Levels

X_SYMBOL = 'X'
O_SYMBOL = 'O'
GRID_SIZE = 3

if __name__ == '__main__':
    error = 'Bad parameters!'

    while True:
        try:
            command, *levels = input('Input command:').lower().strip().split()
        except ValueError:
            print(error)
            continue

        if command == 'exit':
            break

        if command == 'start':
            if len(levels) != 2 or any(not Levels.is_level(level) for level in levels):
                print(error)
                continue

            grid = Grid(GRID_SIZE)

            player1 = Player(levels[0], X_SYMBOL)
            player2 = Player(levels[1], O_SYMBOL)

            game = Game(grid, player1, player2)
            game.run()

        else:
            print(error)
