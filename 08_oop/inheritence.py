"""
Inheritance means one class can reuse attributes
and methods from another class.
"""

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"€{amount} deposited. New balance: €{self.balance}")

class SavingsAccount(BankAccount):

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest added: €{interest}")


account = SavingsAccount("Prashant", 1000)

account.deposit(500)
account.add_interest()