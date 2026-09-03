"""
Different objects can use the same method name,
but behave differently.
"""

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn €{amount}")

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        self.balance -= amount + 2
        print(f"Withdrawn €{amount} + €2 fee")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn €{amount} with no fee")

savings = SavingsAccount("Prashant", 1000)
current = CurrentAccount("Anna", 1000)

savings.withdraw(100)
current.withdraw(100)

accounts = [
    SavingsAccount("Prashant", 1000),
    CurrentAccount("Anna", 1000),
    SavingsAccount("Mika", 2000)
]

for account in accounts:
    account.withdraw(100)