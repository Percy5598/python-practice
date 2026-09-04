"""
An abstract class defines what a class must be able to do,
without necessarily defining how it does it.
"""
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Savings: withdrew €{amount}")

class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Current: withdrew €{amount}")


savings = SavingsAccount("Prashant", 1000)
current = CurrentAccount("Anna", 2000)

savings.withdraw(100)
current.withdraw(100)