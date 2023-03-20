class Score():

    def __init__(self, goals=0, points=0) -> None:
        self.goals = goals
        self.points = points
    
    def __str__(self) -> str:
        return (f'{self.goals} goal(s) and {self.points} point(s)')