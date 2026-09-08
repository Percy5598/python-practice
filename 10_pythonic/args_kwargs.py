"""
unpacking
* means take the elements inside this iterable and put them here individually"
"""
numbers = [1, 2, 3, 4]
print(*numbers) 

numbers = [10, 20, 30]
a, b, c = numbers
print(a)
print(b)
print(c)

# Collect remaining values
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Dictionary unpacking with **

model_config = {
    "learning_rate": 0.01,
    "epochs": 100
}

config = {
    **model_config,
    "batch_size": 32
}

print(config)