class Meeting():

    def __init__(self, hour, minute, duration) -> None:
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self) -> str:
        return (f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)')