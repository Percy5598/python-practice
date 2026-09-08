"""
filter() is used when you want to keep only the items
that satisfy a condition.
map() vs filter() 
map changes every item
filter keep some item
"""


numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)

print(list(result))


numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# For ML
predictions = [
    {"name": "A", "probability": 0.91},
    {"name": "B", "probability": 0.32},
    {"name": "C", "probability": 0.84},
    {"name": "D", "probability": 0.41}
]

high_confidence = list(
    filter(lambda x: x["probability"] >= 0.5, predictions)
)

print(high_confidence)