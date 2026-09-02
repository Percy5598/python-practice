# Lambda functions
square = lambda x: x ** 2
print(square(5))

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using lambda to sort dictionaries by value 
students = [
    {"name": "Anna", "score": 85},
    {"name": "Mika", "score": 92},
    {"name": "Sara", "score": 78},
    {"name": "John", "score": 95}
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)

# map() and filter() with lambda functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using map() to double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# Using filter() to get numbers greater than 5
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)

from functools import reduce
# Using reduce() to calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)
