"""
Composition means building one class using objects
of another class.
"""
class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

        # BankAccount HAS a TransactionHistory
        self.history = TransactionHistory()

    def deposit(self, amount):
        self.balance += amount
        self.history.add_transaction(f"Deposited €{amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.history.add_transaction(f"Withdrew €{amount}")

account = BankAccount("Prashant", 1000)

account.deposit(500)
account.withdraw(200)

account.history.show_transactions()
