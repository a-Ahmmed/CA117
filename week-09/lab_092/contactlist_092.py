class Contact():

    def __init__(self, name, phone, email) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return (f'{self.name} {self.phone} {self.email}')
    
class Contactlist():

    def __init__(self) -> None:
        self.d = {}

    def add(self, obj) -> None:
        self.d[obj.name] = obj

    def remove(self, query) -> None:
        if query in self.d:
            self.d.__delitem__(query)

    def get(self, query) -> None:
        if query in self.d:
            return self.d[query]
        else:
            return None

    def __str__(self) -> str:
        clist, length = f'Contact list\n------------\n', len(self.d) - 1
        for i, key in enumerate(sorted(self.d)):
            if i != length:
                clist += str(self.d[key]) + '\n'
            else:
                clist += str(self.d[key])

        return clist