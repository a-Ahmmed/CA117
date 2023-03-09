class Student():

    def __init__(self, sid, name, modlist=None) -> None:
        self.sid = sid
        self.name = name

        if modlist == None:
            self.modlist = []
        else:
            self.modlist = modlist
    
    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)
    
    def del_module(self, module):
        if module in self.modlist:
            self.modlist.append(module)

    def __str__(self) -> str:
        return (f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(sorted(self.modlist))}')