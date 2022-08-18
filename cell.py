class Cell:
    def __init__(self, row, col):
        self.__symbol = ' '
        self.__is_used = False
        self.__row = row
        self.__col = col

    def __str__(self):
        return f'{self.__symbol}'

    def __repr__(self):
        return f'{self.__symbol} ({self.row} , {self.col})'

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol
        self.__is_used = True

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    @property
    def is_used(self):
        return self.__is_used

    def equals(self, symbol):
        return self.__symbol == symbol

