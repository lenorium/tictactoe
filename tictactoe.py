from grid import Grid
from player import Player
from game import Game

X_SYMBOL = 'X'
O_SYMBOL = 'O'
GRID_SIZE = 3

if __name__ == '__main__':
    # grid = Grid(GRID_SIZE)
    #
    # player1 = Player('user', X_SYMBOL)
    # player2 = Player('easy', O_SYMBOL)
    #
    # game = Game(grid, player1, player2)
    # game.run()

    error = 'Bad parameters!'
    while True:
        try:
            command, *user_levels = input('Input command:').lower().strip().split()
        except ValueError:
            print(error)
            continue

        if command == 'exit':
            break

        game_levels = {'user', 'easy'}
        if command == 'start':
            if len(user_levels) != 2 or any(level not in game_levels for level in user_levels):
                print(error)
                continue

            level1, level2 = user_levels

            grid = Grid(GRID_SIZE)

            player1 = Player(level1, X_SYMBOL)
            player2 = Player(level2, O_SYMBOL)

            game = Game(grid, player1, player2)
            game.run()

        else:
            break

