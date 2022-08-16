from grid import Grid
from player import Player
from game import Game

X_SYMBOL = 'X'
O_SYMBOL = 'O'
GRID_SIZE = 3

if __name__ == '__main__':
    error = 'Bad parameters!'

    game_levels = {'user', 'easy'}
    while True:
        try:
            command, *user_levels = input('Input command:').lower().strip().split()
        except ValueError:
            print(error)
            continue

        if command == 'exit':
            break

        if command == 'start':
            if len(user_levels) != 2 or any(level not in game_levels for level in user_levels):
                print(error)
                continue

            grid = Grid(GRID_SIZE)

            player1 = Player(user_levels[0], X_SYMBOL)
            player2 = Player(user_levels[1], O_SYMBOL)

            game = Game(grid, player1, player2)
            game.run()

        else:
            print(error)
