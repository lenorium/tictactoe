class Cell:
    def __init__(self):
        self.symbol = ' '
        self.is_used = False

    def __str__(self):
        return f'{self.symbol}'

    def fill(self, symbol):
        self.symbol = symbol
        self.is_used = True

    def is_filled(self):
        return self.is_used
