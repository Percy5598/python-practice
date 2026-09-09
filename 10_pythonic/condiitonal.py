"""
any() returns True if at least one item is truthy.
all() returns True if every item is truthy.

any(condition for item in collection)
all(condition for item in collection)
"""
numbers = [1, 3, 5, 8, 9]
result = any(x % 2 == 0 for x in numbers)
print(result)

numbers = [2, 4, 6, 8]
result = all(x % 2 == 0 for x in numbers)
print(result)
