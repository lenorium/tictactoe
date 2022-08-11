from grid import Grid
from player import Player
from game import Game

X_SYMBOL = 'X'
O_SYMBOL = 'O'
GRID_SIZE = 3

if __name__ == '__main__':
    grid = Grid(GRID_SIZE)

    player1 = Player('user', X_SYMBOL)
    player2 = Player('easy', O_SYMBOL)

    game = Game(grid, player1, player2)
    game.run()
