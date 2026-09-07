"""
Normal Loop

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


names = ["prashant", "john", "maria"]

upper_names = []

for name in names:
    upper_names.append(name.upper())

"""
numbers = [1, 2, 3, 4, 5]

# For every number in numbers, put number ** 2 into the new list.
squares = [number ** 2 for number in numbers]
print(squares)

names = ["prashant", "john", "maria"]
upper_names = [name.upper() for name in names]
print(upper_names)

# Even numbers
even_numbers = [number for number in numbers if number % 2 == 0]