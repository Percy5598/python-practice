"""
Generators are important because they let Python 
produce values one at a time instead of storing 
everything in memory at once.
yield 1 → pause
          ↓
       ask again
          ↓
yield 2 → pause
          ↓
       ask again
          ↓
yield 3
"""
# The entire list is created in memory.
def get_numbers():
    return [1, 2, 3, 4, 5]

# Generators uses yield  
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()
print(numbers)

