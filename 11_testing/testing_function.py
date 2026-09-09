# Assert: checks if something is true
x = 10
assert x == 10
assert x == 20

# Testing a function
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(10, 20) == 30
assert add(-1, 1) == 0

def calculate_accuracy(correct, total):
    return correct / total

assert calculate_accuracy(80, 100) == 0.8
assert calculate_accuracy(50, 100) == 0.5
assert calculate_accuracy(100, 100) == 1.0

# Gives the message
assert add(2, 3) == 10, "Addition is incorrect"