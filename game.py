from player import Player


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

        if self.grid.is_full():
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
