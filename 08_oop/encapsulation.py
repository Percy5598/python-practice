"""
Encapsulation means keeping an object's internal data
controlled and deciding how that data can be accessed
or changed. Python uses _ or __ to indicate that a
variable or method is intended to be private.    
"""
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account_1= BankAccount(1000)

account_1.deposit(500)

print(account_1.get_balance())        