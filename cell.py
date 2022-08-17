class Cell:
    def __init__(self):
        self.__symbol = ' '
        self.__is_used = False

    def __str__(self):
        return f'{self.__symbol}'

    def set_symbol(self, symbol):
        self.__symbol = symbol
        self.__is_used = True

    def get_symbol(self):
        return self.__symbol

    def is_used(self):
        return self.__is_used

    def equals(self, symbol):
        return self.__symbol == symbol

    symbol = property(get_symbol, set_symbol)
