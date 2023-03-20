class Meeting():

    def __init__(self, hour, minute, duration) -> None:
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self) -> str:
        return (f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)')

class Schedule():

    def __init__(self) -> None:
        self.l = []

    def add(self, obj) -> None:
        self.l.append(obj)

    def __str__(self) -> str:
        slist = f'Schedule\n--------\n'
        for obj in sorted(self.l, key=lambda x: (x.hour * 60 + x.minute)):
            slist += (str(obj) + '\n')
        
        slist += f'Meetings today: {len(self.l)}'
        return slist