"""
Instance method  → self → works with an object
Class method     → cls  → works with the class
Static method    → no self / cls → independent utility
"""
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.is_valid_amount(amount):
            self.balance -= amount
            print(f"Withdrew €{amount}")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


account = BankAccount("Prashant", 1000)

account.withdraw(200)

print(BankAccount.is_valid_amount(500))
print(BankAccount.is_valid_amount(-100))


class BankAccount:

    bank_name = "Nordic Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Instance method
    def withdraw(self, amount):
        self.balance -= amount

    # Class method
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    # Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

"""
 withdraw()
    ↓
Needs a specific account
    ↓
self


get_bank_name()
    ↓
Needs the class information
    ↓
cls


is_valid_amount()
    ↓
Doesn't need account or class information
    ↓
no self / no cls

"""
