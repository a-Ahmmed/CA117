class Element():

    def set_attributes(self, number, name, symbol, boilingPoint):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.bp = boilingPoint

    def print_attributes(self):
        print(f'Number: {self.number}\nName: {self.name}\nSymbol: {self.symbol}\nBoiling point: {self.bp} K')