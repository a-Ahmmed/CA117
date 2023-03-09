class BankAccount():

    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, funds):
        self.balance += funds

    def withdraw(self, funds):
        if (self.balance - funds) >= 0:
            self.balance -= funds

    def __str__(self) -> str:
        return (f'Your current balance is {self.balance:.2f} euro')