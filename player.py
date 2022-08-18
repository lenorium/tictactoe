import random
from grid import Grid
from levels import Levels


class Player:
    def __init__(self, level, symbol):
        self.level = Levels(level)
        self.symbol = symbol

    def make_move(self, grid: Grid):
        if self.level != Levels.USER:
            print(f'Making move level "{self.level.value}"')

        match self.level:
            case Levels.USER:
                i, j = self.__input_coord(grid)
            case Levels.EASY:
                i, j = self.__random_coord(grid)
            case Levels.MEDIUM:
                cell = self.__highest_priority_coord(grid, True)
                if cell is None:
                    cell = self.__highest_priority_coord(grid, False)
                if cell is not None:
                    i, j = cell.row, cell.col
                else:
                    i, j = self.__random_coord(grid)

        grid.update(i, j, self.symbol)

    def __input_coord(self, grid: Grid):
        while True:
            coord = input('Enter the coordinates:')
            try:
                i, j = [int(c) - 1 for c in coord.split()]
            except ValueError:
                print('You should enter numbers!')
                continue

            if not grid.is_valid_coord(i, j):
                continue
            return (i, j)

    def __random_coord(self, grid):
        empty_coordinates = grid.get_empty_cells_coordinates()
        i, j = random.choice(empty_coordinates)
        return (i, j)

    def __highest_priority_coord(self, grid, self_win):
        if grid.is_empty():
            return None

        count = grid.size - 1

        row = next(filter(lambda line: self.__is_win_line(line, count, self_win), grid.state), None)
        if row is not None:
            return self.__get_win_cell(row, self_win)

        by_column = list(zip(*grid.state))
        column = next(filter(lambda line: self.__is_win_line(line, count, self_win), by_column), None)
        if column is not None:
            return self.__get_win_cell(column, self_win)

        diagonal = [grid.state[i][i] for i in range(grid.size)]
        if self.__is_win_line(diagonal, count, self_win):
            return self.__get_win_cell(diagonal, self_win)

        diagonal = [grid.state[i][grid.size - 1 - i] for i in range(grid.size)]
        if self.__is_win_line(diagonal, count, self_win):
            return self.__get_win_cell(diagonal, self_win)

        return None

    def __is_win_line(self, line, count, self_win):
        if self_win:
            return sum(c.equals(self.symbol) for c in line) == count and not self.__is_used_by_opponent(line)
        else:
            return sum(c.is_used and c.symbol != self.symbol for c in line) == count \
                   and not any(c.symbol == self.symbol for c in line)

    def __get_win_cell(self, win_line, self_win):
        if self_win:
            return next(filter(lambda c: not c.equals(self.symbol), win_line), None)
        else:
            return next(filter(lambda c: not c.is_used, win_line), None)

    def __is_used_by_opponent(self, line):
        return any(self.__cell_is_used_by_opponent(cell) for cell in line)

    def __cell_is_used_by_opponent(self, cell):
        return cell.is_used and cell.symbol != self.symbol

    def is_winner(self, grid):
        return any(all(s.equals(self.symbol) for s in line) for line in grid.state) \
               or any(all(grid.state[j][i].equals(self.symbol)
                          for j in range(grid.size)) for i in range(grid.size)) \
               or all(grid.state[i][i].equals(self.symbol) for i in range(grid.size)) \
               or all(grid.state[i][grid.size - 1 - i].equals(self.symbol) for i in range(grid.size))
