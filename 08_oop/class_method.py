"""
A @classmethod works with the class itself, 
rather than one particular object.

Same as "self" is used to represent the instance 
of the class, "cls" represents the class itself.  
"""
class BankAccount:
    bank_name = "Nordic Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_account(self):
        print(self.owner, self.balance)

    @classmethod
    def show_bank_name(cls):
        print(cls.bank_name)


account = BankAccount("Prashant", 1000)

account.show_account()
BankAccount.show_bank_name()

"""
Suppose we extract the account information 
from a string, we can use a class method to
create an instance of the class from that string. 
""" 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_string(cls, data):
        owner, balance = data.split(",")
        return cls(owner, float(balance))

account = BankAccount.from_string("Prashant,1500")

print(account.owner)
print(account.balance)