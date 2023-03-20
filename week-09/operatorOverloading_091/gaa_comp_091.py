class Score():

    def __init__(self, goals=0, points=0) -> None:
        self.goals = goals
        self.points = points
    
    def total_points(self) -> int:
        return (self.goals * 3) + self.points

    def __str__(self) -> str:
        return (f'{self.goals} goal(s) and {self.points} point(s)')
    
    def __eq__(self, other) -> bool:
        return self.total_points() == other.total_points()
    
    def __gt__(self, other) -> bool:
        return self.total_points() > other.total_points()
    
    def __ge__(self, other) -> bool:
        return self.total_points() >= other.total_points()
    
    def __lt__(self, other) -> bool:
        return self.total_points() < other.total_points()
    
    def __le__(self, other) -> bool:
        return self.total_points() <= other.total_points()