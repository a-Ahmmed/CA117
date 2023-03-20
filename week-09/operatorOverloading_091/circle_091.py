class Point():
    
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def midpoint(self, other) -> object:
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)
    
    def __str__(self) -> str:
        return (f'({self.x:.1f}, {self.y:.1f})')

class Circle():

    def __init__(self, obj=None, radius=1) -> None:
        if obj == None:
            self.centre = Point()
        else:
            self.centre = obj
            
        self.radius = radius

    def __str__(self) -> str:
        return (f'Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})\nRadius: {self.radius}')