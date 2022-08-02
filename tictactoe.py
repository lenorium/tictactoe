"""
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)
"""

X_SYMBOL = 'X'
O_SYMBOL = 'O'
GRID_SIZE = 3


def create_grid():  # , allowed_symbols: set
    initial_state = input('Enter the cells:')
    initial_state = initial_state.replace('_', ' ')
    initial_state = list(initial_state)
    return [initial_state[i: i + GRID_SIZE] for i in range(0, len(initial_state), GRID_SIZE)]


def print_grid(grid: list):
    print('---------')
    [print('|', *line, '|') for line in grid]
    print('---------')


def is_finished(grid: list):
    winner = get_winner(grid)
    if winner is not None:
        print(f'{winner} wins')
        return True
    filled_cells = [s for line in grid for s in line if s == O_SYMBOL or s == X_SYMBOL]
    if len(filled_cells) == len(grid):
        print('Draw')
        return True
    else:
        print('Game not finished')
        return False


def get_winner(grid: list):
    players = {X_SYMBOL, O_SYMBOL}
    for symbol in players:
        if any(all(s == symbol for s in line) for line in grid for s in line) \
                or all(grid[i][i] == symbol for i in range(GRID_SIZE)) \
                or all(grid[i][GRID_SIZE - 1 - i] == symbol for i in range(GRID_SIZE)):
            return symbol
    return None


def get_coordinates(grid: list):
    while True:
        coord = input('Enter the coordinates:')
        try:
            i, j = coord.split()
            i, j = int(i) - 1, int(j) - 1
        except ValueError:
            print('You should enter numbers!')
            continue
        if 0 > i or i > 2 or 0 > j or j > 2:
            print('Coordinates should be from 1 to 3!')
            continue
        if grid[i][j] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        return i, j


def make_move(grid: list):
    i, j = get_coordinates(grid)
    x_symbols = [s for line in grid for s in line if s == X_SYMBOL]
    o_symbols = [s for line in grid for s in line if s == O_SYMBOL]
    grid[i][j] = X_SYMBOL if len(x_symbols) <= len(o_symbols) else O_SYMBOL


if __name__ == '__main__':
    game_grid = create_grid()
    print_grid(game_grid)
    while True:
        make_move(game_grid)
        print_grid(game_grid)
        if is_finished(game_grid):
            break
