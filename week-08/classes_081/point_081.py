class Point():

    def set_attributes(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print_attributes(self):
        print(f'x: {self.x}0\ny: {self.y}0')

    def reflect(self):
        self.x -= (self.x * 2)
        self.y -= (self.y * 2)