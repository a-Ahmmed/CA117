class Point():

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def distance(self, p2):
        dist = ((p2.x - self.x) * (p2.x - self.x) + (p2.y - self.y) * (p2.y - self.y)) ** 0.5
        return dist
    
    def __str__(self) -> str:
        return (f'({self.x:.1f}, {self.y:.1f})')