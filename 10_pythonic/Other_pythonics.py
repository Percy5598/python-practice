# Iterators gives values at a time
"""
iter()
  ↓
iterator
  ↓
next() → 10
next() → 20
next() → 30
"""
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Mutable vs immutable
"""
Can be changed after creation
list
dict
set

Cannot be changed after creation
int
float
str
tuple
bool
None
"""

# Shallow copy vs deep copy
"""
=               → same object
.copy()         → shallow copy
deepcopy()      → independent nested copy
"""
original = [[1, 2], [3, 4]]

copy = original
copy = original.copy()

import copy
deep_copy = copy.deepcopy(original)

# Variable Scope
"""
L → Local
E → Enclosing
G → Global
B → Built-in
"""
x = "global"
def test():
    x = "local"
    print(x)
test()

# Closure
"""
A closure occurs when an inner function remembers values
from its outer function.

"""

def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = multiplier(2)
print(double(5))

# dataclass
"""
A dataclass makes classes that mainly store data much 
easier to write.
"""
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    score: float

student = Student("Alice", 25, 91.5)
print(student)   

# __slots__
""" 
It restricts which attributes instances can have and
can reduce memory overhead in certain situations. 
"""
class Student:
    __slots__ = ["name", "age"]

# match / case 
"""
Instead of
if status == "success":
    ...
elif status == "error":
    ...
elif status == "pending":
    ...
"""
status = "error"
match status:
    case "success":
        print("Success")
    case "error":
        print("Error")
    case "pending":
        print("Pending")

# Type Hints    
def calculate(scores: list[float]) -> float:
    return sum(scores) / len(scores)    

# Decorators
"""
A decorator lets you modify or extend a function's
behavior without changing the function itself.
Decorators appear frequently in:
FastAPI
Flask
testing
authentication
logging
Python frameworks
"""
def logger(func):
    def wrapper():
        print("Function starting")
        func()
        print("Function finished")

    return wrapper

@logger
def hello():
    print("Hello")

hello()