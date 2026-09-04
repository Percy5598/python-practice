"""
Dunder means double underscore.
__init__   → initialize an object
__str__    → define how an object is displayed as text
__len__    → define what len(object) means
__eq__     → define how == works
__add__    → define how + works
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account: €{self.balance}"

account = BankAccount("Prashant", 1000)
print(account)


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __len__(self):
        return len(self.transactions)

account = BankAccount("Prashant")
account.add_transaction("Deposit €500")
account.add_transaction("Withdraw €100")
account.add_transaction("Deposit €200")
print(len(account))
