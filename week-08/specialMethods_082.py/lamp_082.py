class Lamp():

    def __init__(self, on=False) -> None:
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False
    
    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def __str__(self) -> str:
        return str(self.on)