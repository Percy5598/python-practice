"""
OOP Mini Project - Bank Management System
"""

from abc import ABC, abstractmethod


# Composition: BankAccount HAS-A TransactionHistory
class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        if not self.transactions:
            print("No transactions.")
            return

        for transaction in self.transactions:
            print(transaction)


# Abstract base class
class BankAccount(ABC):

    bank_name = "Nordic Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.history = TransactionHistory()

    # Instance method
    def deposit(self, amount):

        if self.is_valid_amount(amount):
            self._balance += amount

            self.history.add_transaction(
                f"Deposited €{amount}"
            )

            print(f"Deposited €{amount}")

        else:
            print("Deposit amount must be positive.")

    # Abstract method
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Property
    @property
    def balance(self):
        return self._balance

    # Dunder method
    def __str__(self):
        return (
            f"Account owner: {self.owner}, "
            f"Balance: €{self._balance}"
        )

    # Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @classmethod
    def create_account_from_string(cls, account_string, interest_rate=0.05):
        owner, balance = account_string.split(",")

        return cls(
            owner.strip(),
            float(balance.strip()),
            interest_rate
        )

# Inheritance
class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    # Polymorphism: SavingsAccount has its own withdraw()
    def withdraw(self, amount):

        if self.is_valid_amount(amount) and amount <= self._balance:

            self._balance -= amount

            self.history.add_transaction(
                f"Withdrew €{amount}"
            )

            print(f"Withdrew €{amount}")

        else:
            print("Invalid withdrawal amount.")

    def add_interest(self):

        interest = self._balance * self.interest_rate
        self._balance += interest

        self.history.add_transaction(
            f"Interest added: €{interest:.2f}"
        )

        print(f"Applied interest: €{interest:.2f}")


# Inheritance
class CurrentAccount(BankAccount):

    WITHDRAWAL_FEE = 2

    # Polymorphism: CurrentAccount has its own withdraw()
    def withdraw(self, amount):

        total = amount + self.WITHDRAWAL_FEE

        if self.is_valid_amount(amount) and total <= self._balance:

            self._balance -= total

            self.history.add_transaction(
                f"Withdrew €{amount} + €{self.WITHDRAWAL_FEE} fee"
            )

            print(
                f"Withdrew €{amount} "
                f"(€{self.WITHDRAWAL_FEE} fee)"
            )

        else:
            print("Invalid withdrawal amount.")

# Testing

print("----- Creating Accounts -----")

savings = SavingsAccount("Prashant", 1000, 0.05)
current = CurrentAccount("Anna", 2000)

print(savings)
print(current)


print("\n----- Deposits -----")

savings.deposit(500)
current.deposit(500)


print("\n----- Withdrawals -----")

savings.withdraw(200)
current.withdraw(100)


print("\n----- Interest -----")

savings.add_interest()


print("\n----- Balances -----")

print(f"{savings.owner}: €{savings.balance:.2f}")
print(f"{current.owner}: €{current.balance:.2f}")


print("\n----- Transaction History: Savings -----")

savings.history.show_transactions()


print("\n----- Transaction History: Current -----")

current.history.show_transactions()


print("\n----- Static Method -----")

print(BankAccount.is_valid_amount(100))
print(BankAccount.is_valid_amount(-100))


print("\n----- Class Method -----")

account = SavingsAccount.create_account_from_string(
    "Mika,1500"
)

print(account)


print("\n----- Polymorphism -----")

accounts = [
    SavingsAccount("John", 1000, 0.03),
    CurrentAccount("Maria", 1000),
]

for account in accounts:
    account.withdraw(100)