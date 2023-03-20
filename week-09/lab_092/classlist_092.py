class Student():

    def __init__(self, name, idnum, modules=None) -> None:
        self.name = name
        self.id = idnum

        if modules == None:
            self.modules = []
        else:
            self.modules = modules

    def average(self) -> float:
        sum = 0
        for i in self.modules:
            sum += i[1]
        
        return (sum / len(self.modules))
    
    def modlist(self) -> str:
        return (", ".join(sorted([i[0] for i in self.modules])))
    
    def __str__(self) -> str:
        return (f'Name: {self.name}\nID: {self.id}\nModules: {self.modlist()}\nAverage mark: {self.average():.0f}')
    
class Classlist():

    def __init__(self) -> None:
        self.clist = {}

    def add(self, obj) -> None:
        self.clist[obj.id] = obj

    def __str__(self) -> str:
        return "\n".join([str(i[1]) for i in sorted(self.clist.items(), key=lambda x: x[1].average(), reverse=True)])