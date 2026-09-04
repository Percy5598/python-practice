import module_calculator
from module_calculator import subtract

result = module_calculator.add(10, 5)
result_1 = subtract(10, 5)
print(result)
print(result_1)


from math_tools.calculator import add, multiply

print(add(10, 20))
print(multiply(10, 20))

# This works beacuse of ___init__.py
from math_tools import add
print(add(30, 20))