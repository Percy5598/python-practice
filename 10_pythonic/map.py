"""
map() lets you apply the same function to every item in an iterable.
"""

numbers = [1, 2, 3, 4]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)


numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))

def square(x):
    return x ** 2
numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))

# Use of map in ML
predictions = [0.2, 0.7, 0.4, 0.9]
binary = list(map(lambda x: 1 if x >= 0.5 else 0, predictions))
print(binary)