"""
We do not need:
from math_tools.calculator import add
from math_tools.calculator import multiply
from math_tools.statistics import mean
from math_tools.statistics import maximum
"""

from math_tools import add, multiply, mean, maximum

print(add(10, 20))
print(multiply(5, 4))

numbers = [10, 20, 30, 40, 50]

print(mean(numbers))
print(maximum(numbers))