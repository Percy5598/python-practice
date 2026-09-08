"""
reduce() repeatedly combines items to produce one
final value.

reduce(function, iterable)

map:     [1,2,3,4] → [2,4,6,8]
filter:  [1,2,3,4] → [2,4]
reduce:  [1,2,3,4] → 10
"""
numbers = [1, 2, 3, 4]
total = 1 + 2 + 3 + 4

from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print(total)


