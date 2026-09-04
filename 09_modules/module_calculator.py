"""
Mental Model
Run directly:

calculator.py
     ↓
__name__ = "__main__"
     ↓
run the main code

Import:

main.py
   ↓
import calculator
   ↓
calculator.py
   ↓
__name__ = "calculator"
   ↓
don't run the main code

Absolute:
from ml.preprocessing import clean_data
     ↑
start from known package/project location


Relative:
from .preprocessing import clean_data
     ↑
start from where I currently am
"""

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b    

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b 



def main():
    print("Application started")
    print(add(10, 20))
    print(subtract(10,20)) 
    print(multiply(10,20)) 
    print(divide(10,20)) 
      
if __name__ == "__main__":
    main()

