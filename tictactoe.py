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
TOTAL = GRID_SIZE ** 2


def create_grid():
    # так делать не надо, потому что он создает вложенный список,
    # где элементами являются не несколько разных списков,
    # а один и тот же, просто ссылки повторяются
    # типа: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # но id() каждого из этих трех внутренних списков один и тот же
    #  ---> return [[EMPTY_CELL] * GRID_SIZE] * GRID_SIZE
    initial_state = [EMPTY_CELL] * TOTAL
    return [initial_state[i: i + GRID_SIZE] for i in range(0, TOTAL, GRID_SIZE)]


def print_grid(grid: list):
    print('---------')
    [print('|', *line, '|') for line in grid]
    print('---------')


def is_finished(grid: list):
    winner = get_winner(grid)
    if winner is not None:
        print(f'{winner} wins')
        return True

    filled_cells = [s for line in grid for s in line if s != EMPTY_CELL]
    if len(filled_cells) == TOTAL:
        print('Draw')
        return True

    return False


def get_winner(grid: list):
    players = {X_SYMBOL, O_SYMBOL}
    for symbol in players:
        if any(all(s == symbol for s in line) for line in grid) \
                or any(all(grid[j][i] == symbol for j in range(GRID_SIZE)) for i in range(GRID_SIZE))\
                or all(grid[i][i] == symbol for i in range(GRID_SIZE)) \
                or all(grid[i][GRID_SIZE - 1 - i] == symbol for i in range(GRID_SIZE)):
            return symbol
    return None


def make_move(grid: list, is_human: bool):
    if is_human:
        while True:
            coord = input('Enter the coordinates:')
            try:
                i, j = [int(c) - 1 for c in coord.split()]
            except ValueError:
                print('You should enter numbers!')
                continue

            if 0 > i or i > GRID_SIZE - 1 or 0 > j or j > GRID_SIZE - 1:
                print(f'Coordinates should be from 1 to {GRID_SIZE}!')
                continue

            if grid[i][j] != EMPTY_CELL:
                print('This cell is occupied! Choose another one!')
                continue
            break
    else:
        print('Making move level "easy"')
        empty_coordinates = [[i, j] for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == EMPTY_CELL]
        i, j = random.choice(empty_coordinates)

    grid[i][j] = X_SYMBOL if is_human else O_SYMBOL


if __name__ == '__main__':
    game_grid = create_grid()
    print_grid(game_grid)
    is_human = True

    while True:
        make_move(game_grid, is_human)
        print_grid(game_grid)
        if is_finished(game_grid):
            break
        is_human = not is_human
