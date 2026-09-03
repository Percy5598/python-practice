# Class is a blueprint for creating objects.
# It defines a set of attributes and methods of objects.
class Student:

    # Initializing the attributes of the class
    def __init__(self, name, age):
    # Self is a reference to the current instance of the class    
        self.name = name
        self.age = age

    # Methods are the functions inside the class
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Lets do some realistic examples of the class
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Balance: €{self.balance}")

account_1 = BankAccount("Prashant", 1000)
account_2 = BankAccount("Alice", 1500)
account_3 = BankAccount("Bob", 2000)
account_4 = BankAccount("Charlie", 2500) 

account_1.show_balance()
  

account_1.deposit(500)
account_1.show_balance()

account_1.withdraw(200)
account_1.show_balance() 

# OOPS is used to create libraries in scikit-learn


