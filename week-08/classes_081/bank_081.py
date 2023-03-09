class BankAccount():

    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def print_attributes(self):
        print(f'Name: {self.name}\nAccount number: {self.number}\nBalance: {self.balance}.00')

    def deposit(self, num):
        self.balance += num